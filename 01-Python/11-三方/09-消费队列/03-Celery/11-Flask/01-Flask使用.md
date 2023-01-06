```python
# celerys/main.py
import os
import sys
import logging

from celery import Celery

APPS_NAME = "apps"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
APPS_DIR = os.path.join(BASE_DIR, APPS_NAME)
sys.path.insert(0, APPS_DIR)
sys.path.insert(0, BASE_DIR)
print(BASE_DIR, APPS_DIR)

from application import Application
from config import constants

application = Application()
application.start()
app = Celery("transform")

app.config_from_object("celerys.config")
app.conf.update(application.app.config)
app.autodiscover_tasks()
```

```python
# celery/config.py
broker_url = "redis://127.***.1/14"
result_backend = "redis://127.***.1/15"
imports = [
    "celerys.tasks.salt_tasks",
    "celerys.tasks.init_web",
    "celerys.tasks.sender",
]
```

```shell
# celery/__init__.py
import os
import sys

from celery import Celery

APPS_NAME = "apps"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
APPS_DIR = os.path.join(BASE_DIR, APPS_NAME)
sys.path.insert(0, APPS_DIR)
sys.path.insert(0, BASE_DIR)
print(BASE_DIR, APPS_DIR)
```

```shell
# celery/tasks/init_web.py
import logging
from hashlib import md5
from datetime import datetime

import apscheduler.schedulers

from common import curd_manager
from celerys.main import app, application

logger = logging.getLogger("celery")

@app.task(name="初始化定时器")
def init_cron():
    """初始化定时系统
    """
    with application.app.app_context():
        try:
            application.aps.start()
            logger.info("定时器启动成功!")
        except apscheduler.schedulers.SchedulerAlreadyRunningError:
            logger.warning("已启动!")

```

