# -*- coding:utf-8 -*-
# author: HPCM
# time: 2022/1/12 22:00
# file: gs.py
import os

blacks = [
    "SUMMARY.md",
]


def generate_summary(path="."):
    tsm = []
    for p in os.listdir(path):
        sm = {}
        if p.startswith(".") or p in blacks:
            continue
        sp = os.path.join(path, p)
        if os.path.isdir(sp):
            gs = generate_summary(sp)
            if gs:
                sm["value"] = os.path.join(sp, "README.md")
                sm["name"] = p
                sm["son"] = gs
        elif p.endswith(".md") and p.upper() != "README.MD":
            sm["name"] = os.path.splitext(p)[0]
            sm["value"] = sp
            sm["son"] = []
        if sm:
            tsm.append(sm)
    return tsm


def write_summary(tsm, idt=0):
    smc = ""
    for ms in sorted(tsm, key=lambda x: "-" in x["name"] and int(x["name"].split("-")[0]) or 0):
        smc += " " * idt * 2 + f"* [{ms['name']}]({ms['value']})\n"
        if ms["son"]:
            smc += write_summary(ms["son"], idt + 1)
    return smc


content = write_summary(generate_summary())
with open("SUMMARY.md", "w+", encoding="utf-8") as fp:
    fp.write("# Book\n" + content.replace("\\", "/"))
