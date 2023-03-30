import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ol = soup.select_one(".list_movieranking")

li_list = ol.find_all('li')
# print(li_list)

movie = []

for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1]
    mvdate = li.select_one('.txt_info > .txt_num').text

    movie.append([rank, name, see, grade, num, mvdate])
    # print(rank, name, see, grade, num, mvdate)

print(movie)

import pandas as pd

# df = pd.DataFrame(movie, columns=['순위', '영화명', '관람가', '평점', '예매율', '개봉일'])

# df.to_csv('movie_info.csv', index=False, encoding='cp949')

df = pd.read_csv('movie_info.csv', encoding='cp949')

# print(df.info())

# print(df[df['평점']>8])

import matplotlib.pyplot as plt
# matplotlib.rcParams['font.family'] = 'Malgun Gothic'

# 23.01.04 >> %y.%m.%d
df['개봉일'] = pd.to_datetime(df['개봉일'], format='%y.%m.%d')
# print(df.info())
print(df)
df_weekly = df.resample('W', on='개봉일').mean()
df_weekly = df_weekly.fillna(0)
print(df_weekly)
plt.plot(df_weekly.index, df_weekly['예매율'])
plt.show()