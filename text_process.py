# -*- coding: utf-8 -*-
"""创建于2020.03.02"""
import re


infile_path ="./test_file.txt" #请添加文件，暂只支持文件文件，文件后辍最好为txt
old_str = "Python Software" #在该处请添加要被替换字符串,支持模糊匹配，匹配规则参照python正则表达式
new_str = "python software" #在该处请添加要潜换成的新的字符串


def main():
    """主程序"""
    tf_list = read_file(infile_path)
    new_tf_list = []
    for tf_line in tf_list:
        new_tf_line = re.sub(old_str, new_str, tf_line) #进行文本替换操作
        new_tf_list.append(new_tf_line)
    write_file(new_tf_list)


def read_file(filename):
    """读取文件到列表"""
    try:
        file_handle = open(filename, "r")
        textlist = file_handle.read().splitlines()
        file_handle.close()
        return textlist
    except IOError as e:
        print("Read file error: "+ str(e))
        sys.exit()

def write_file(text_list):
    """写入列表到文件"""
    outfile_part = infile_path.rsplit(".",1)
    outfile_path = outfile_part[-2] + "_out." + outfile_part[-1]
    try:
        file_handle = open(outfile_path, "w")
        for text_line in text_list:
            file_handle.write(text_line + '\n')
        file_handle.close()
    except IOError as e:
        print("Read file error: "+ str(e))
        sys.exit()


if __name__ == "__main__":
    main()
