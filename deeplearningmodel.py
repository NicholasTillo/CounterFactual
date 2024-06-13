import numpy as np
from keras import Sequential
from keras import models
import tensorflow as tf
import csv


class modelReader:
    def __init__(self) -> None:
        self.model=None
        pass

        
    def checkSave():
        try:
            open("my_model.keras","r")
            return True
        except:
            return False
    def createSave(self,model):
        try:
            model.save('my_model.keras')
            return True
        except:
            return False
    def loadSave(self):
        self.model = models.load_model('my_model.keras')
        return True
    
    
    def createModel(self,datalink):
        #Everything in this file kinda. 
        # Generating some  data
        if self.checkSave():
            self.model = self.loadSave()
            return
        data,labels = self.loadData(datalink)  # 30000,23 | 30000,1

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
        self.model = model

        self.evaluate(dataEVAL,labelEVAL,data,labels)

        return


    def evaluate(self, dataEVAL,labelEVAL,data,labels):

        results = self.model.evaluate(dataEVAL,labelEVAL)
        print(results)
        predict3 = self.model.predict(data)
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

        pass

    def predict(self,data):
        prediction = self.model.predict(data)
        return prediction

    def loadData(self,datalink):
        datalink = "Data\default_of_credit_card_clients.csv"
        with open(datalink) as csvfile:
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
        return rowNP, labels


#MODEL IS NOT COMPLETE. 






