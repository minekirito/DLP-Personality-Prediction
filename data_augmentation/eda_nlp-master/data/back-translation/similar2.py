from nltk.text import TextCollection

text1 = 'I like the movie so much '
text2 = 'That is a good movie '
text3 = 'This is a great one '
text4 = 'That is a really bad movie '
text5 = 'This is a terrible movie'

# 构建TextCollection对象
tc = TextCollection([text1, text2, text3,text4, text5])
new_text = 'That one is a good movie. This is so good!'
word = 'That'
tf_idf_val = tc.tf_idf(word, new_text)
print('{}的TF-IDF值为：{}'.format(word, tf_idf_val))
#结果：That的TF-IDF值为：0.02181644599700369
