import seaborn as sns

mpg = sns.load_dataset('mpg')


print(mpg[mpg['horsepower'].isnull()])
mpg['horsepower'] = mpg['horsepower'].fillna(
    mpg.groupby('cylinders')['horsepower'].transform('median')
)
print(mpg.info())
print(mpg[mpg['horsepower'].isnull()])