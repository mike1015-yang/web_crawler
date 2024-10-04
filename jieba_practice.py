import jieba

# 載入自定義辭典
jieba.load_userdict('./mydict.txt')

s = '你好，我叫小賀，今天去國立中央大學上課，感覺非常開心'

s1_list = jieba.cut(s, cut_all = True)
s2_list = jieba.cut(s, cut_all = False)
s3_list = jieba.cut(s)
s4_list = jieba.cut_for_search(s)

print(f"全模式: {' | '.join(s1_list)}")
print("精確模式: ", ' | '.join(s2_list))
print("預設模式: ", ' | '.join(s3_list))
print("搜尋引擎模式: ", ' | '.join(s4_list))