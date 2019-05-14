#!/usr/bin/env python3
# coding: utf-8
import urllib.request
from . import thunder_subs


def search(fp):
    """
    格式化其中一个结果如下：
        {
            'scid': '86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9',
            'sname': '神秘博士2011圣诞篇The.Doctor.The.Widow.And.The.Wardrobe.ass',
            'language': '简体',
            'rate': '4',
            'surl': 'http://subtitle.v.geilijiasu.com/86/AE/86AE53FC9D5A2E41E5E9CAB7C1A3794A1B7206B9.ass',
            'svote': 545,
            'roffset': 4114797192
        }

    每项中需要注意的数据有：
        scid: 猜测为字幕文件的scid
        sname: 字幕文件的原始文件名
        language: 字幕语言
        surl: 字幕下载地址
    """
    # 获取一个本地电影文件名为cid的hash值
    cid = thunder_subs.cid_hash_file(fp)

    info_list = thunder_subs.get_sub_info_list(cid, 1000)
    return info_list


def get_url(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return data
