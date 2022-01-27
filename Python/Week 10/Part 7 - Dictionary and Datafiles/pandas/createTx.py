from matplotlib.pyplot import axis
import pandas as pd
from pyparsing import traceParseAction # import pandas
wf = pd.read_csv('DataFiles/csv/weatherdata.csv')

# wf.to_csv('DataFiles/text/Teswfilms.csv')

"Create csv and existing data from films.txt"
# wf.loc[wf["Title"]=="The Legend of Tarzan"].to_csv("DataFiles/text/Teswfilms.csv")

# wf = pd.read_csv('DataFiles/text/films.txt')

# print(wf.columns)
# ['Reading Timestamp', 'Ambient Temp', 'Ground Temp', 'Humidity',
#        'Wind Speed', 'Rainfall']
# wf['Total Temps'] = wf.iloc[:,1:3].sum(axis=1)
# print(wf.head(5))

# wf.loc[wf["Total Temps"]==wf.iloc[:,1:3].sum(axis=1)].to_csv("DataFiles/csv/TotalTemps.csv")
wf["Total Temps"] = wf.iloc[:,1:3].sum(axis=1)

wf.to_csv("DataFiles/csv/TotalTemps.csv",index=False)