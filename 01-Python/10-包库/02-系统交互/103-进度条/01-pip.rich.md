```python
import time
import threading

from pip._vendor.rich.progress import (
    BarColumn,
    Progress,
    MofNCompleteColumn,
    TextColumn,
    TimeRemainingColumn,
)

columns = (
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    MofNCompleteColumn(),
    TextColumn("ETA"),
    TimeRemainingColumn(),
)
progress = Progress(*columns, refresh_per_second=30, transient=True)
# refresh_per_second: 刷新率, 1秒刷新 30 次.
# transient: 进度条在任务执行完成之后, 是否还在screen中存在

total = 5
task_id = progress.add_task(" " * (getattr(threading.local(), "indentation", 0) + 2) + "【111】", total=total)
progress.start()
for _ in range(total):
    progress.update(task_id, advance=1)
    # progress.update(task_id, completed=i + 1)
    # advance: 进度条每次增加的进度步长
    # completed: 直接将进度条重置到某个位置

    time.sleep(0.3)
progress.stop()

```

