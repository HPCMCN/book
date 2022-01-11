# -*- coding:utf-8 -*-
# author: HPCM
# time: 2022/1/11 21:23
# file: checker.py
import re
import subprocess

key_rules = [
    r"((.*secret.*)\s*=\s*(['\"]?.*['\"]?))",
    r"((.*key.*)\s*=\s*['\"]?(.*)['\"]?)",
    r"((.*ak.*)\s*=\s*['\"]?(.*)['\"]?)",
    r"((.*sk.*)\s*=\s*['\"]?(.*)['\"]?)",
]

value_rules = [r"[a-zA-Z0-9*]{2,}\.(?:com|net|cn|org|us|xyz|top|wang|pub|xin|site|cc|co|info|club|win)"]
result = subprocess.Popen("git config --global core.quotepath false && git diff --cached --name-only --cached", shell=True, stdout=subprocess.PIPE)
for file in result.stdout.read().decode().splitlines():
    if not file:
        continue
    with open(file) as f:
        content = f.read()
    for vr in value_rules:
        for res in re.findall(vr, content, flags=re.I):
            print(f"检测到网址: {res}")
            if "***" not in res:
                print(f"{file}: {res}")
                exit("本次提交存在网站信息, 请处理后重新提交!")
    for kr in key_rules:
        for res in re.findall(kr, content, flags=re.I):
            print(f"检测到私钥: {res[1]}={res[2]}")
            if "***" not in res[2]:
                msg = f"存在隐私数据泄露风险: {res}\n" + \
                      f"\t{res[1]} = {res[2]}"
                if not input("是否自动替换(Y/N):")[0].upper() == "Y":
                    exit("请手动调整!")
                replace_content = res[0].replace(res[2], f"{res[2][:2]}***{res[2][-2:]}")
                if replace_content == res[1]:
                    exit("替换失败!")
                content = re.sub(res[0], replace_content, content, flags=re.S)

    with open(file, "w+") as f:
        f.write(content)

if not input("是否确认提交代码(Y/N):")[0].upper() == "Y":
    exit("已终止提交代码!")



