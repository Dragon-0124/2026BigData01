import seaborn as sns

ex = sns.load_dataset('exercise')

# print(ex.info())
# print(ex.head(10))

# print(ex['kind'].value_counts())
# print(ex['time'].value_counts())
# print(ex['diet'].value_counts())

# print(len(ex[ex['diet'] == 'low fat']))
# print(ex[ex['diet'] == 'low fat'])

running_df = ex[ex['kind'] == 'running']
sns.catplot(running_df, x = 'time', y = 'pulse', hue = 'diet', kind = 'point') # x축은 시간, y는 심박수, hue는 기준, kind는 그래프의 유형