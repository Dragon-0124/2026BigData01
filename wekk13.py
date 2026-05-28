import seaborn as sns

health = sns.load_dataset('healthexp')
# print(health.head())
# print(health.tail(7))
# print(health.info())
# print(health.describe())
# print(health['Country'].unique()) # ['Germany', 'France', 'Great Britain', 'Japan', 'USA', 'Canada'] - Length: 6, dtype: str
# print(health['Country'].nunique())  # 6
print(health['Country'].value_counts()) # Japan -51 / USA - 51 / Germany - 50 / Canada - 44 / Great Britain - 43 / France - 35