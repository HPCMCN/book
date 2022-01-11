#!/c/Python/Python37 python.exe
# -*- coding:utf-8 -*-
# author: HPCM
# time: 2022/1/11 21:23
# file: checker.py
import re
import subprocess

key_rules = [
    r"(([\w0-9-_]*secret[\w0-9-_]*)\s*=\s*(['\"]?.*['\"]?))",
    r"(([\w0-9-_]*key[\w0-9-_]*)\s*=\s*['\"]?(.*)['\"]?)",
    r"(([\w0-9-_]*ak[\w0-9-_]*)\s*=\s*['\"]?(.*)['\"]?)",
    r"(([\w0-9-_]*sk[\w0-9-_]*)\s*=\s*['\"]?(.*)['\"]?)",
]

value_rules = [r"[a-zA-Z0-9*]{2,}\.(?:com|net|cn|org|us|xyz|top|wang|pub|xin|site|cc|co|info|club|win)"]
result = subprocess.Popen("git config --global core.quotepath false && git diff --cached --name-only --cached", shell=True, stdout=subprocess.PIPE)
for file in result.stdout.read().decode().splitlines():
    if not file:
        continue
    with open(file, encoding="utf-8") as f:
        content = f.read()
    for vr in value_rules:
        for res in re.findall(vr, content, flags=re.I):
            print(f"[{file}]checked value: {res}")
            if len(res) > 3 and "***" not in res:
                print(f"{file}: {res}")
                exit("There is value information in this submission. Please process and resubmit!")
    for kr in key_rules:
        for res in re.findall(kr, content, flags=re.I):
            print(f"[{file}]checked key: {res[1]}={res[2]}")
            if len(res[2]) > 3 and "***" not in res[2]:
                msg = f"There is a risk of privacy data disclosure: {res}\n" + \
                      f"\t{res[1]} = {res[2]}"
                exit(msg)
                # if not input("是否自动替换(Y/N):")[0].upper() == "Y":
                #     exit("请手动调整!")
                # replace_content = res[0].replace(res[2], f"{res[2][:2]}***{res[2][-2:]}")
                # if replace_content == res[1]:
                #     exit("替换失败!")
                # content = re.sub(res[0], replace_content, content, flags=re.S)

    # with open(file, "w+") as f:
    #     f.write(content)

# if not input("是否确认提交代码(Y/N):")[0].upper() == "Y":
#     exit("已终止提交代码!")



