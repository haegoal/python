from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

okt = Okt()

text = "안녕하세요. 파이썬입니다. 저는 파이썬을 배우고 있습니다. 파이쏜은 넘나 잼있습니다."

word_list=[]

for word, tag in okt.pos(text):
    if tag in ['Noun', 'Adjective']:
        word_list.append(word)


word_list_count = Counter(word_list)

wc = WordCloud(font_path='malgun')

result = wc.generate_from_frequencies(word_list_count)

#matplotlib 로 이미지 출력하기
plt.axis('off') # x,y축은 필요없음으로 생략
plt.imshow(result)
plt.show()
#워드클라우드 파일저장
wc.to_file('wordcloud_result.png')
