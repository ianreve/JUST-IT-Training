import pandas as pd # import pandas
movies = pd.read_csv('DataFiles/text/films.txt')

"using and / &"
# print(movies.loc[(movies['Rating']=='PG') & (movies['Genre']=='Action')])

"Using OR / |"
# print(movies.loc[(movies['Rating']=='PG') | (movies['Genre']=='Action')])

"search using str.contains"
# print(movies.loc[movies['Genre'].str.contains('Comedy')])


# print(movies.loc[movies['Genre'] == 'Action','Genre'])

"Change value of a collumn"
# movies.loc[movies['Duration'] > 105, ["Genre"]] = 'YES'
# print(movies)

movies.loc[movies["Duration"] > 105, ["Too long?"]] = "Over 1 hour 45"

print(movies)
