import pandas
#import random
data = pandas.read_csv("data.csv")
print(data)
#print(data.score)
#print(data[data.name == "X"]) 
#X = (data[data.name == "X"])
#print(X.score) 
#choice = random.choice(data.score)
#choice2 = (data[data.score == choice])
#print(choice2.name.values)

import numpy as np

#with open("data.csv") as file_name:
    #array = np.loadtxt(file_name, delimiter=",")

#print(array)

#import csv

#with open("data.csv") as file_name:
    #file_read = csv.reader(file_name)

#array = list(file_read)
 
#print(array)
#df = pandas.DataFrame(np.random.randn(100, 5), columns = list("abcde"))
#rows = np.random.choice(data.index.values, 1, replace=False)
#sampled_df = data.ix[rows]

#data = pandas.read_csv("data.csv")
#choice = np.random.choice(data.score, replace=False)
#secret = (data[data.score == choice])
#moviename = secret.name.values 
#scorevalue = secret.score.values
#scorevalue2 = str(scorevalue)[1:-1]
#print(scorevalue2)
#data = data.drop(data[data['score']==(choice)].index,inplace=True)
#
print(data)
#print(data[data['score']==(choice.values)].index.values)