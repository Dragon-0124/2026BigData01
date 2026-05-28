import seaborn as sns
import matplotlib.pyplot as plt

# (데이터 측정)년도, (대상)국가, (1인단 연간 의효비)지출액, (평균)기대 수명
health = sns.load_dataset('healthexp')

# 가장 최근 년도인 2020년의 데이터를 필터링 후 추출
health_2020 = health[health['Year']==2020]

# print(health_2020)
# print(health_2020.sort_values('Life_Expectancy', ascending=False))
# print(health_2020.sort_values(by=['Life_Expectancy'], ascending=False))
# print(health_2020.sort_values(ascending=False , by=['Life_Expectancy']))
# print(health_2020.sort_values(ascending=False , 'Life_Expectancy')) # by=['']기준이 가장 처음에 위치하지 않거나 기준이 여러가지 일 때 사용하지 않으면 오류 발생


# 전체 데이터 셋에서 의료비 지출이 5000달러 이상인 데이터만 추출
# high_spending = health[health['Spending_USD']>=5000]

# print(high_spending)
# print(high_spending['Country'].unique()) # 조건에 맞는 국가 확인

# # 국가 별 평균 의료지 지출 및 평균 기대수명 산출
# country_mean = health.groupby('Country')[['Spending_USD' , 'Life_Expectancy']].mean()
# print(country_mean)

# 국가 별로 데이터가 몇개씩 있는지 확인
# print(Health['Country'].value_counts())

# 년도 별 평균 의료비 지출과 평균 기대수명 구하기
# year_mean = health.groupby('Year')[['Spending_USD' , 'Life_Expectancy']].mean()
# print(year_mean)

# 국가별 기대수명 분포 확인
# sns.catplot(data=health, x='Year', y='Life_Expectancy', col="Country", kind='box', col_wrap=3)
# plt.show()

# 가장 최근(2020년) 국가별 의료비 지출 비교
# sns.catplot(data=health_2020, x='Country', y='Spending_USD', kind='bar', palette=sns.color_palette('muted'))
# plt.show()

# 국가 별 의료비 및 기대수명의 상관관계 (산점도)
# sns.relplot(data=health, x='Spending_USD' , y='Life_Expectancy', col='Country', col_wrap=3, kind='scatter', hue='Year', palette='Set1')
# plt.show()


# print(health.sort_values('Year',ascending=False))
# 2가지 기준으로 정렬(년도별 , 기대수명 내림차순)
# print(health.sort_values(['Year','Life_Expectancy'],ascending=[False, False]))

# 2가지 기준으로 정렬(년도별 , 기대수명 내림차순)후 상위 10개 데이터 출력
# print(health.sort_values(['Year','Life_Expectancy'],ascending=[False, False]).head(10))