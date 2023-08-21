from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter

kkma = Kkma()

# print(kkma.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(kkma.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(kkma.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))

okt = Okt()

# print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
# print(okt.normalize(u'안녕하세욬ㅋㅋㅋㅋㅋ'))

text = "안녕하세요. 파이썬입니다. 저는 파이썬을 배우고 있습니다. 파이쏜은 넘나 잼있습니다."

# for word, tag in kkma.pos(text):
#     print(word, tag)
word_list=[]

for word, tag in okt.pos(text):
    # if tag in 'Noun':
    if tag in ['Noun', 'Adjective']:
        word_list.append(word)
        # print(word, tag)

# print(word_list)

print(Counter(word_list))