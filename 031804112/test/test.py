import jieba
import sys
from collections import Counter
import numpy as np


class EmptyFileError(Exception):
    def __init__(self):
        print("要比较的文本为空文本")


def get_stopwords():
    # 加载停用词，用于去掉不需要的无意义的一些词
    stop_words = []
    try:
        with open('stopword.txt', 'r', encoding='utf-8') as stop:
            words = stop.readlines()
            for word in words:
                stop_words.append(word.strip())
    except FileNotFoundError:
        print("找不到stopword.txt，请把它放到main所在文件夹下")
    # 停用词去重
    stop_words = set(stop_words)
    stop.close()
    return stop_words


def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            # 读取整个txt为一个字符串
            content = f.read()
    except FileNotFoundError:
        print("找不到要对比的文件")
    if (len(content) == 0):
        raise (EmptyFileError)

    # 去掉换行符和空格
    content = content.replace('\n', ' ').replace(' ', '')
    f.close()
    return content


def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    f.close()


def text2vector(text, stopwords):
    # 分词，去停用词（停用词含常用标点）
    words = jieba.cut(text)
    words = [word for word in words if word not in stopwords]
    word_counts = Counter(words)
    return word_counts


def cos_similarity(v1, v2):
    # 计算余弦相似度
    numerator = np.inner(v1, v2)
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denominator != 0:
        return numerator / denominator
    else:
        return 0

def simi(original,compare,result):
    original=original
    compare=compare
    result=result
    # 读取文件
    ori_text = read_file(original)
    comp_text = read_file(compare)

    # 停用词
    stopword = get_stopwords()

    # 文本向量化
    ori_counter = text2vector(ori_text, stopword)
    comp_counter = text2vector(comp_text, stopword)

    total_words = set(list(ori_counter.keys()) + list(comp_counter.keys()))
    ori_vector = np.zeros(len(total_words))
    comp_vector = np.zeros(len(total_words))

    for idx, word in enumerate(total_words):
        ori_vector[idx] = ori_counter.get(word, 0)
        comp_vector[idx] = comp_counter.get(word, 0)

    # 计算相似度
    sim = cos_similarity(ori_vector, comp_vector)
    sim1 = "%.2f" % sim
    sim2 = str(sim1)

    # 写入文件
    write_file(result, sim2)
    print(original,compare,sim2)