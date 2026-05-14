import seaborn as sns

ex = sns.load_dataset('exercise')

ex1 = ex[
    (ex['diet'] == 'low fat')&
    (ex['time'] == '30 min')&
    (ex['kind'] == 'running')
]

print(ex1)

mean_ex = ex1['pulse'].mean()
print(mean_ex)