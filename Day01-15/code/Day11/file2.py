"""
读取圆周率文件判断其中是否包含自己的生日

Version: 0.1
Author: 尹诗流
Date: 2020-07-26
"""
import pprint

birth = input('请输入你的生日(四位数字): ')
with open('pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        pprint.pprint(pi_string)
        print('Bingo!!!')
