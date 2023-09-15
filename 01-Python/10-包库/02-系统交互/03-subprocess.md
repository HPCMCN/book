> class **Popen**(*args, bufsize=- 1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=None, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, group=None, extra_groups=None, user=None, umask=- 1, encoding=None, errors=None, text=None, pipesize=- 1, process_group=None)

* args: list/str, 运行的命令

* stdin/stdout/stderr: 标准输入/输出/异常, 可选值: 

  ```
  PIPE: 将输入或者输出return到run的返回值中
  None: 仅执行命令, 不进行其他操作
  STDOUT: 将其他标准输入重定向到其他类型, 类似 sh scripts.sh >> /dev/null 2>&1
  DEVNULL: 将输出重定向到 /dev/null中
  ```

* input: 标准输入

* capture_output: bool, 内部是stdout=PIPE, stderr=PIPE

* shell: bool, 主要针对window系统, False表示优先扫描当前文件下的`cmd.exe`, True表示扫描`%SystemRoot%\System32\cmd.exe`

* cwd: str, 定义运行命令时的workon目录

* timeount: second, 命令行执行超时限制

* check: bool, 非零退出码则会爆出: CalledProcessError异常.

* encoding: str, 标准输入/输出/异常输出的编码方式

* errors: object, 根据encoding编码方式, 如果存在指定异常, 则将被拦截, 类似: `stdout.decode(encoding, errors)`

* text:

* env: dict, 环境变量

* universal_newlines:

* other_popen_kwargs