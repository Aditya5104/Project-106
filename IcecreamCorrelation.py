import numpy as np
import csv
import plotly.express as px

def getDataSource(dataPath):
    icecreamsales=[]
    Temerature=[]

    with open (dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            icecreamsales.append(float(row["Ice-cream"]))
            Temerature.append(float(row["Temperature"]))

    return{"x":Temerature,"y":icecreamsales}    

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation of tempreture and icecream sale is ", correlation[0,1])

def setup():
    dataPath="Icecream.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)

setup()    