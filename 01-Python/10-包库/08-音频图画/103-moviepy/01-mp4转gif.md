* 安装

  ```shell
  pip install moviepy
  ```



* 使用

  ```python
  from moviepy.editor import *
  
  mp4_path = r"C:\Users\xxx\Desktop\xxx 2023-09-20 15-05-19.mp4"
  au = VideoFileClip(mp4_path, audio=False)
  clip = (
      au.set_duration(au.duration / 1.8)  # 视频加速 1.8
          .resize(0.2)                    # 调整分辨率 0.2
  )
  clip.write_gif(r"C:\Users\xxx\Desktop\1.gif", fps=8)
  ```

  

