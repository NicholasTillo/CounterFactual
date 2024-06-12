import numpy as np
from keras import Sequential
import tensorflow as tf
import csv


class modelReader:
    def __init__(self) -> None:
        pass


    def createModel(self,datalink):
        #Everything in this file kinda. 
        pass
    def predict(self,data):
        pass


#MODEL IS NOT COMPLETE. 

with open("Data\default_of_credit_card_clients.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    fields2 = next(csvreader)

    rows = []
    labels = []
    for row in csvreader:
        rows.append(row[1:-1])
        labels.append([row[-1]])

    rowNP = np.array(rows, dtype=float)
    labels = np.array(labels,  dtype=float)


# Generating some  data
data = rowNP  # 30000,23
labels = labels  # 30000,1


#Standarize data. 
data = np.transpose(data)
for i in data:
    mean = np.mean(i)
    std = np.std(i)
    for num in range(len(i)):
        i[num] = (i[num] - mean) / std
data = np.transpose(data)

#Split into eval and training data
split = -5000
dataEVAL = data[split:]
labelEVAL = labels[split:]

data = data[:split]
labels = labels[:split]



# Creating a Sequential model
model = Sequential()

# Adding layers to the model
model.add(tf.keras.layers.Input(shape=(23,)))
model.add(tf.keras.layers.Dense(128, activation='relu'))  
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(128, activation='relu'))  
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # Output layer with 1 neuron and sigmoid activation for binary classification

# Compiling the model
model.compile(optimizer='adam', loss= tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

# Training the model
model.fit(data, labels, epochs=20, batch_size=16, validation_split=0.2)

results = model.evaluate(dataEVAL,labelEVAL)

print(results)
#
"""
x1 = [230000,2,1,2,27,-1,-1,-1,-1,-1,-1,16646,17265,13266,15339,14307,36923,17270,13281,15339,14307,37292,0]
x2 = [190000,2,1,2,27,-1,-1,-1,-1,-1,-1,16646,17265,13266,15339,14307,36923,17270,13281,15339,14307,37292,0]
x3 =  [70000,2,2,2,26,2,0,0,2,2,2,41087,42445,45020,44006,46905,46012,2007,3582,0,3601,0,1820]
list = []
list.extend([x1,x2,x3])
guess_data3 = np.array(list,dtype=int)"""

predict3 = model.predict(data)
#See the sums of each of the classified ones. 
nose = []
yes = []
#compare the label to the generated one. 
for i in zip(predict3,labels):
    if i[1][0] == 0:
        nose.append(i[0][0])
    else:
        yes.append(i[0][0])


print("Average score for 0 labels slash nose:")
print(sum(nose)/len(nose))
print("Average score for 1 labels of Yes")
print(sum(yes)/len(yes))



