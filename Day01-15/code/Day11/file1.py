"""
从文本文件中读取数据

Version: 0.1
Author: 尹诗流
Date: 2020-07-26
"""

import time


def main():
    # 一次性读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取，通过time.sleep()逐行打印
    with open('致橡树.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表list中
    with open('致橡树.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
