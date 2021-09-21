import numpy as np
import csv
import plotly.express as px

def getDataSource(dataPath):
    MarksInPercentage=[]
    DaysPresent=[]

    with open (dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            MarksInPercentage.append(float(row["MarksInPercentage"]))
            DaysPresent.append(float(row["DaysPresent"]))

    return{"x":DaysPresent,"y":MarksInPercentage}    

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation of Marks and days present", correlation[0,1])

def setup():
    dataPath="Marks.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setup()  