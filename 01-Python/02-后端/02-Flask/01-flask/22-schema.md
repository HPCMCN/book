# Schema

用于接口反序列化工具



* 安装

  ```shell
  pip install marshmallow
  ```

* 使用

  ```python
  # schema.py
  from marshmallow import Schema, fields, EXCLUDE, validate
  
  class CronSchema(Schema):
      job_days = fields.List(fields.Integer, required=True, validate=validate.Length(min=1))
      job_time = fields.Time(format="%H:%M:%S")
  
  
  class CronRuleSchema(Schema):
      limit = fields.Integer(required=True)
  
  
  class CronJob2Schema(Schema):
      uuids = fields.List(fields.String)
      vmgroupid = fields.Integer()
      job_name = fields.String(required=True)
      job_desc = fields.String()
      status = fields.Boolean(default=True)
      run_now = fields.Boolean(default=False)
      cron = fields.Function(deserialize=lambda x: CronSchema().load(x, unknown=EXCLUDE))
      rules = fields.Function(deserialize=lambda x: CronRuleSchema().load(x, unknown=EXCLUDE))
  
      class Meta:
          unknown = EXCLUDE
          
  # 使用
  data = CronJob2Schema().load(request.json)
  data["uuid"]
  ```

  

