#!/usr/bin/env python3
"""裁剪视频截图v2：根据页面主题正确映射"""
from PIL import Image
from pathlib import Path
import glob

SCREENSHOTS = Path("/Users/mik/strange LLM/output/screenshots")

CROP_BOX = (60, 35, 1220, 635)

# 正确的 spec页码 → 源截图 映射（根据页面标题和截图字幕内容匹配）
MAPPING = {
    # 第一幕
    "7":   "video1_t0030_跟我一起进入梦境.jpg",              # 清空大脑，从零开始
    "12":  "video1_t0100_那如果把角色区分一下.jpg",           # 三块补丁，三个新名词
    "13":  "video1_t0205_给这些特殊的善寒文信息起了个新词叫memory.jpg",  # 第一层建筑逻辑
    "15":  "video1_t0459_其实呢就是个约定罢了.jpg",           # "其实呢就是个约定罢了"
    "17":  "video1_t0435_我们聚焦于agent和大模型的对话过程来看.jpg",  # 一个新名词诞生了(Agent)
    "20":  "video1_t0524_也就是一套约定而已.jpg",             # "也就是一套约定而已"(MCP)
    "21":  "video1_t0844_但想了想还是给它起个新名字吧.jpg",     # "新瓶装旧酒的名词诈骗"(Skill)
    "23":  "video1_t0930_就是有点拉垮.jpg",                  # 从塔顶往下看
    "25":  "video5_t0140_那这样的开源模型有多少呢.jpg",        # 3000个模型
    "26":  "video5_t0344_你观察出什么规律了.jpg",              # 3000+→109→35

    # 第二幕
    "29":  "video3_t0025_最大的不同就是可以接入社交媒体.jpg",    # 真实测试：OpenClawdbot
    "31":  "video3_t0200_看到这里的token数是对应的上的.jpg",    # 0.1美元
    "33":  "video3_t0255_把今日的AI新闻整理成PDF发给我.jpg",    # AI新闻整理成PDF
    "35":  "video3_t0345_markdown文件看起来还行.jpg",          # 发现时间没找对

    # 第三幕
    "50":  "video2_t0500_但是如果换个视角.jpg",               # 2024年
    "52":  "video5_t0024_这颜色已经深得吓人了.jpg",            # 3000个模型
    "54":  "video4_t0024_比如最著名的开源操作系统LINUX.jpg",    # "开源"变了
    "57":  "video2_t0829_却可能数不清六根手指.jpg",            # 越难的越好
    "61":  "video2_t0729_如果你发出了这样的疑问.jpg",           # 不是你不会用AI
    "64":  "video2_t0959_刚刚分析了AI这些年带来的割裂感.jpg",   # 错误在进化

    # 第四幕
    "69":  "video6_t0022_不然我就从这跳下去.jpg",             # 互动时间：排难度
    "72":  "video6_t0139_这里面呢就有一些点是看起来合理的视频.jpg",  # 噪音海洋找绿洲
    "74":  "video6_t0115_那就变成了我们熟悉的向量.jpg",        # 解空间概念
    "75":  "video6_t0129_这个点就在这儿.jpg",                 # 足球场找沙子
    "76":  "video6_t0050_以及还有哪些场景.jpg",               # 回到那四个视频
    "78":  "video6_t0430_现在的AI视频模型已经有相当多的.jpg",   # 辨伪指南

    # 第五幕+
    "90":  "video2_t1200_他不就是采样出的一个样本而已吗.jpg",   # 采样样本
    "116": "video2_t0300_我到现在还能清楚的记得.jpg",          # 回到第一个画面
}

# 删除旧的v6文件
for old in SCREENSHOTS.glob("v6_page*.jpg"):
    old.unlink()
    print(f"DEL: {old.name}")

# 裁剪并保存
for page, src_name in MAPPING.items():
    src = SCREENSHOTS / src_name
    dst = SCREENSHOTS / f"v6_page{page}.jpg"
    if not src.exists():
        print(f"MISSING: {src_name}")
        continue
    img = Image.open(src)
    cropped = img.crop(CROP_BOX)
    cropped.save(dst, "JPEG", quality=90)
    print(f"OK: page {page:>4s} -> {dst.name} ({cropped.size[0]}x{cropped.size[1]})")

print(f"\nDone: {len(MAPPING)} screenshots processed")
