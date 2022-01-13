# 1. 需求说明

## 1.1 需求拆解

1. 进行简单的账号密码认证
2. 账号密码认证进行发放token, 携带token进行认证则进行跳转
3. 未防止浏览器自动弹窗行为, 对401的response的headers中的`WWW-Authenticate`进行修改, 不然不能触发JS的登录弹窗行为
4. 从header和json中同时获取token进行认证
5. token失效时间为7天, 当用户修改密码时, token立即失效

## 1.2 接口信息

```json
POST	/api/login
```

### 请求参数

| 参数     | 说明      | 类型 | 是否必选 |
| -------- | --------- | ---- | -------- |
| username | 用户账号  | str  | 是       |
| password | 用户密码  | str  | 是       |
| token    | 认证token | str  | 是       |

### 响应参数

| 参数  | 说明 | 类型      | 是否必选 |
| ----- | ---- | --------- | -------- |
| token | str  | 认证token | 是       |

### 请求示例

```shell
curl --location --request POST 'http://10.111.0.10:8001/api/login' \
--header 'Authorization: Basic dGVz***MA==' \
--header 'Content-Type: application/json' \
--data-raw '{
    "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYzMDk4MjA0OSwiZXhwIjoyMjUzMDYyMDQ5fQ.eyJpZCI6MCwiaHAiOiI5NjFlNiJ9.me4Yc6lpdE2Ztnz7aRKJ6RBAZw3DHApLssDEemvJhs1iNNWnINtBMjDek2gBiG9W2nG6fXhQuZotxI2sFyT3oA"
}'
```

# 2. 代码实现

## 2.1 基于Flask-HttpAuth

### User模型

```python
from werkzeug import security

from appliction import app


class Users(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(256), unique=True, nullable=False)
    _password = db.Column("password", db.String(256), nullable=False)
    name = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    email = db.Column(db.String(64))
    login_time = db.Column(db.DateTime)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = security.generate_password_hash(password)

    def check_password(self, password):
        return security.check_password_hash(self._password, password)
```

### 认证中间件

```python
import itsdangerous
from flask import g, request, abort
from flask_httpauth import HTTPBasicAuth


def generate_auth_token(user):
    """生成token"""
    expires = 7 * 24 * 60 * 60
    s = itsdangerous.TimedJSONWebSignatureSerializer(constants.SECRET_KEY, expires_in=expires)
    return s.dumps({
        "id": user.id,
        "hp": sha256(user.password.encode()).hexdigest()[:5]
    })


def verify_auth_token(token):
    """校验token"""
    try:
        if not token:
            return None
        from common import curd_manager

        logger.info("verify token: {}".format(token))

        s = itsdangerous.TimedJSONWebSignatureSerializer(constants.SECRET_KEY)
        data = s.loads(token)
        logger.info(data)
        g.user = curd_manager.OUsers.select_obj(idt=data["id"])
        if sha256(g.user.password.encode()).hexdigest()[:5] != data["hp"]:
            logger.error("用户修改密码, token失效!")
            raise itsdangerous.SignatureExpired("用户修改密码, token失效!")
        return g.user
    except itsdangerous.SignatureExpired:
        return None
    except itsdangerous.BadData:
        return None


@auth.verify_password
def verify_password(token_or_username, password):
    """身份认证, 优先校验token"""
    g.user = verify_auth_token(token_or_username or request.headers.get("Token") or request.json.get("token"))
    g.token = None
    if g.user:
        g.token = True
        return True
    g.user = curd_manager.OUsers.select_obj(params={"username": token_or_username})
    if g.user and g.user.check_password(password):
        return True
    return False
```

### 登录接口

```python
@bp_api.route("/login", methods=["POST"])
@decorator.auth.login_required
def login():
    from common import decorator

    if g.token:
        return redirect("/")
    curd_manager.OUsers.update(idt=g.user.id, kwargs={"login_time": datetime.now()})
    return rsp_api.json_rsp({"token": decorator.generate_auth_token(g.user)})
```

