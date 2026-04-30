import pandas as pd

df = pd.DataFrame( { '국' : [1, 6, 7], '영' : [2, 4, 8], '수' : [3, 5, 9], '화' : [10, 3, 11]}, index=[1, 2, 3] )
print(df)


print(df.sample(frac=0.33)) # Randomly select fraction of rows.
print(df.sample(1)) # Randomly select n rows.
print(df.nlargest(1,'국')) # Select and order top n entries.
print(df.nsmallest(1,'국')) # Select and order bottom n entries.
print(df.head(2)) # Select first n rows
print(df.tail(2)) # Select last n rows