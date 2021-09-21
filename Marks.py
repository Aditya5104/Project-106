import pandas as pd
import plotly.express as px


df=pd.read_csv("Marks.csv")
fig=px.scatter(df,x="DaysPresent",y="MarksInPercentage")
fig.show()