#!/usr/bin/env python3
"""裁剪视频截图：去除企鹅logo、水印、字幕"""
from PIL import Image
from pathlib import Path

SCREENSHOTS = Path("/Users/mik/strange LLM/output/screenshots")

# 裁剪参数 (原始1280x720): left=60, top=35, right=1220, bottom=635
# 即 crop=1160x600+60+35
CROP_BOX = (60, 35, 1220, 635)

# 页码 → 源截图文件名映射
MAPPING = {
    7:   "video1_t0030_跟我一起进入梦境.jpg",
    14:  "video1_t0100_那如果把角色区分一下.jpg",
    15:  "video1_t0205_给这些特殊的善寒文信息起了个新词叫memory.jpg",
    17:  "video1_t0459_其实呢就是个约定罢了.jpg",
    19:  "video1_t0435_我们聚焦于agent和大模型的对话过程来看.jpg",
    21:  "video1_t0524_也就是一套约定而已.jpg",
    23:  "video1_t0844_但想了想还是给它起个新名字吧.jpg",
    25:  "video1_t0930_就是有点拉垮.jpg",
    27:  "video5_t0140_那这样的开源模型有多少呢.jpg",
    28:  "video5_t0344_你观察出什么规律了.jpg",
    31:  "video3_t0025_最大的不同就是可以接入社交媒体.jpg",
    33:  "video3_t0200_看到这里的token数是对应的上的.jpg",
    35:  "video3_t0255_把今日的AI新闻整理成PDF发给我.jpg",
    37:  "video3_t0345_markdown文件看起来还行.jpg",
    50:  "video2_t0500_但是如果换个视角.jpg",
    52:  "video5_t0024_这颜色已经深得吓人了.jpg",
    54:  "video4_t0024_比如最著名的开源操作系统LINUX.jpg",
    57:  "video2_t0829_却可能数不清六根手指.jpg",
    61:  "video2_t0729_如果你发出了这样的疑问.jpg",
    64:  "video2_t0959_刚刚分析了AI这些年带来的割裂感.jpg",
    72:  "video6_t0022_不然我就从这跳下去.jpg",
    74:  "video6_t0115_那就变成了我们熟悉的向量.jpg",
    75:  "video6_t0139_这里面呢就有一些点是看起来合理的视频.jpg",
    77:  "video6_t0129_这个点就在这儿.jpg",
    79:  "video6_t0050_以及还有哪些场景.jpg",
    81:  "video6_t0430_现在的AI视频模型已经有相当多的.jpg",
    90:  "video2_t1200_他不就是采样出的一个样本而已吗.jpg",
    116: "video2_t0300_我到现在还能清楚的记得.jpg",
}

for page, src_name in MAPPING.items():
    src = SCREENSHOTS / src_name
    dst = SCREENSHOTS / f"v6_page{page:03d}.jpg"
    if not src.exists():
        print(f"MISSING: {src_name}")
        continue
    img = Image.open(src)
    cropped = img.crop(CROP_BOX)
    cropped.save(dst, "JPEG", quality=90)
    print(f"OK: page {page:3d} -> {dst.name} ({cropped.size[0]}x{cropped.size[1]})")

print(f"\nDone: {len(MAPPING)} screenshots processed")
