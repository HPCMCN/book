# ruamel.yaml

官网: https://yaml.readthedocs.io/en/latest/install.html#optional-requirements

## 1. 安装

```shell
pip install ruamel.yaml
```

## 2. 基本用法

* 序列化

  ```python
  with open("2.txt", encoding="utf8") as f:
      configs = yaml.load(f, Loader=yaml.RoundTripLoader)
  ```

* 反序列化

  ```python
  print(yaml.dump(configs, Dumper=yaml.RoundTripDumper, allow_unicode=True))
  ```

  

  

