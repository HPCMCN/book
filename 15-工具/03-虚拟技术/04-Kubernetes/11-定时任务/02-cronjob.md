# 1. crontjob

## 1.1 简介

## 1.2 使用

* yaml

  ```yaml
  apiVersion: batch/v1beta1
  kind: CronJob
  metadata:
    name: hello
  spec:
    suspend: true                        # 是否暂停
    schedule: '*/1 * * * *'              # 定时配置
    successfulJobsHistoryLimit: 3        # 保留成功任务个数
    concurrencyPolicy: Allow             # 并发策略: Allow/允许并发, Forbid/不允许并发, Replace/不允许并发, 但是后面执行时, 会强杀前面任务
    failedJobsHistoryLimit: 1            # 保留失败任务个数
    jobTemplate:
      metadata:
      spec:
        template:
          metadata:
            labels:
              run: hello
          spec:
            containers:
            - args:
              - /bin/sh
              - -c
              - date; echo Hello from the Kubernetes cluster
              image: busybox
              name: hello
            restartPolicy: OnFailure
  ```

  