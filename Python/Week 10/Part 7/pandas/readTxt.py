import pandas as pd # import pandas
tf = pd.read_csv('DataFiles/text/films.txt')

# print(tf.head(5))

# print(tf.tail(5))

# read headers / filed names
# print(tf.columns)

# ['ID', 'Title', 'Yr', 'Rating', 'Duration', 'Genre']

# print(tf['Title'])

# print(tf.iloc[1])
# print(tf.head(5))
# print(tf.iloc[0])
# print(tf.iloc[2,4])
# print(tf.iloc[2:5])

# for index, row in tf.iterrows():
#     print(index,row[["Title","Genre"]])

# use loc to find a specific data base on-text or numeric 
# print(tf.loc[tf["Title"] == "Batman v Superman"])

"search using panda"
# findMovie = input("Enter thee title of the Movie you want to find: ")
# print(tf.loc[tf["Title"] == findMovie])

"Describe file"
# print(tf.describe)

"sort the values"
# print(tf.head(20).sort_values('Yr'))
# print(tf.sort_values(['Yr'], ascending=[3]))


"Drop / remove"
# print(tf.drop(["field data"], axis=0)