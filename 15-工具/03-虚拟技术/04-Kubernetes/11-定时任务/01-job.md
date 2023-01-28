# 1. Job

## 1.1 简介

定时任务

## 1.2 使用

* yaml

  ```yaml
  apiVersion: batch/v1
  kind: Job
  metadata:
    name: echo
  spec:
    suspend: false # 1.21+
    ttlSecondsAfterFinished: 100    # job结束后, 多久进行自动清理. 0表示立即清理
    backoffLimit: 4                 # job失败重试次数
    completions: 1                  # 将会启动多个Pod进行执行(job执行总数), 默认等于parallelism
    parallelism: 1                  # 并行任务执行数量(job并发数量)
    template:
      spec:
        containers:
        - command:
          - echo
          - Hello, Job
          image: busybox
          name: echo
        restartPolicy: Never
  
  ```

  