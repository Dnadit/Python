import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/일별평균대기오염도_2022.csv", encoding="cp949")

print(df.info())

print(df.columns)

name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)

sub_df = df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30) & (df['오존농도(ppm)'] >= 0.001)]
print(sub_df)

sub_df = df.loc[df['미세먼지농도(㎍/㎥)'] >= 30][['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']]
print(sub_df)

sub_df_5 = df[df['미세먼지농도(㎍/㎥)'] > 30][['측정일시', '측정소명', '미세먼지농도(㎍/㎥)']]
print(sub_df_5)

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

print(df.head(20))

# 지역별 미세먼지와 초미세먼지 농도 평균 계산
df_area = df.groupby('측정소명').mean(numeric_only=True).head(10)

# 그래프 그리기
plt.bar(df_area.index, df_area['미세먼지농도(㎍/㎥)'], label='PM10')
plt.bar(df_area.index, df_area['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Area')
plt.ylabel('Concentration')
plt.title('Air Pollution by Area')
plt.show()

# 그래프 그리기
plt.boxplot([df['미세먼지농도(㎍/㎥)'], df['초미세먼지농도(㎍/㎥)']])
plt.xticks([1,2],['PM10', 'PM2.5'])
plt.ylabel('Concentration')
plt.title('Air Pollution Boxplot')
plt.show()

import pandas as pd

# 데이터 파일 경로
data_path = './data/일별평균대기오염도_2022.csv'

# CSV 파일 읽기
df = pd.read_csv(data_path, encoding='cp949')

# 필요한 필드 추출
df = df[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

# 결측치 처리
df = df.dropna()

# 측정일시 컬럼의 데이터 타입을 datetime으로 변경
df['측정일시'] = pd.to_datetime(df['측정일시'], format='%Y%m%d')

# 이상치를 모아서 result.csv 파일로 저장
q1 = df['미세먼지농도(㎍/㎥)'].quantile(0.25)
q3 = df['미세먼지농도(㎍/㎥)'].quantile(0.75)
iqr = q3 - q1
outlier_df = df[(df['미세먼지농도(㎍/㎥)'] < q1 - 1.5 * iqr) | (df['미세먼지농도(㎍/㎥)'] > q3 + 1.5 * iqr)]
outlier_df.to_csv('result.csv', index=False, encoding='utf-8-sig')


