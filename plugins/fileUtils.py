#!/usr/bin/env python
# encoding: utf-8

import os.path
import yaml


def string_encoding(data: bytes):
    # 简单的判断文件编码类型
    # 说明：UTF兼容ISO8859-1和ASCII，GB18030兼容GBK，GBK兼容GB2312，GB2312兼容ASCII
    CODES = ['UTF-8', 'GB18030', 'BIG5']
    # UTF-8 BOM前缀字节
    UTF_8_BOM = b'\xef\xbb\xbf'

    # 遍历编码类型
    for code in CODES:
        try:
            data.decode(encoding=code)
            if 'UTF-8' == code and data.startswith(UTF_8_BOM):
                return 'UTF-8-SIG'
            return code
        except UnicodeDecodeError:
            continue
    return 'unknown'


def file_encoding(file_path: str):
    # 获取文件编码类型
    if not os.path.exists(file_path):
        return "utf-8"
    with open(file_path, 'rb') as f:
        return string_encoding(f.read())


def file_is_exist(file_path):
    # 判断文件是否存在
    return os.path.exists(file_path)


def loadYaml(yaml_path):
    if file_is_exist(yaml_path):
        with open(yaml_path, mode='r', encoding=file_encoding(yaml_path)) as file:
            safe_load = yaml.safe_load(file)
            return safe_load
    return None
