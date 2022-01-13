# 限流

DRF中限流模块有三种:

* AnonRateThrottle: 根据ip
* UserRateThrottle: 根据用户id, 未登录用户根据ip
* ScopedRateThrottle: 类似UserRateThrottle, 但是可以指定限流字段

注意:

限流throttle_classes, 是可以配置多个的, 但是要注意的是, 如果中间有一个被拒绝访问, 那么不会直接跳出, 会执行全部后, 去限制时间的最大值

例如:

```python
"DEFAULT_THROTTLE_RATES": {
        "login_min": "3/m",  # 每分钟允许3次登录
        "login_day": "20/d",  # 每天允许20次登录
    }

class LoginMinRateThrottle(UserRateThrottle):
    scope = "login_min"


class LoginDayRateThrottle(UserRateThrottle):
    scope = "login_day"
# 此时绑定两个限制器后, 连续在1分钟内访问3次后, 提示限制登录, 然后继续访问(在提示限制登录时间内)超过20次后就会出现今天无法访问, 已经超过20次
```

如果想修改此方法, 让限制时间内的访问次数不记录在限制次数中, 需要修改APIView, 可以做Mixin, 让view继承即可

```python
class ManyThrottleMixin(object):

    def check_throttles(self, request):
        """
        Check if request should be throttled.
        Raises an appropriate exception if the request is throttled.
        """
        duration = None
        for throttle in self.get_throttles():
            if not throttle.allow_request(request, self):
                duration = throttle.wait()
                break

        if duration:
            self.throttled(request, duration)
```

