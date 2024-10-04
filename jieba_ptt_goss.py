import jieba
import os

# 將要讀取的文章檔案，存成list
source_file_path = r'./ptt_goss'
file_list = os.listdir(source_file_path)
# print(file_list)

all_article_string = ''
for each_article in file_list:
    article_path = source_file_path  + '/' + each_article
    # print(article_path)
    with open(article_path, 'r', encoding = 'utf-8') as f:
        tmp_article_string = f.read().split('---split---')[0].split('\n')[1:]
    # print(tmp_article_string)
    for article_line in tmp_article_string:
        all_article_string += article_line + '\n'
# print(all_article_string) 

# 載入自定義辭典
jieba.load_userdict('./mydict.txt')

# 使用預設模式分詞
s_list = jieba.cut(all_article_string)
word_count = {}
for i in s_list:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
for key, value in word_count.items():
    print(f"{key}:{value}\n")
