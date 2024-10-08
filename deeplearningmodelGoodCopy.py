import numpy as np
from keras import Sequential
from keras import models
import tensorflow as tf
import csv
from os import remove, path


class modelReader:
    def __init__(self, features, Model = None) -> None:
        self.model = Model
        self.numFeatures = features
        pass

        
    def checkSave(self):
        try:
            open("my_model.keras","r")
            return True
        except:
            return False
        

    def createSave(self,model):
        try:
            print("ATTEMPTINGSAVE")
            model.save('my_model.keras')
            print("Save Good")

            return True
        except:
            print("SAVE FAILED")
            return False
        

    def loadSave(self):
        print("Trying to Load Model")
        self.model = models.load_model('my_model.keras')
        print("Loaded Model")
        return True
    
    
    def createModel(self,datalink):
        #Everything in this file kinda. 
        # Generating some  data
        if self.model != None:
            print("Model Already Created!")
            return None
        
        if self.checkSave():
            self.loadSave()
            
            #Test if its the correct shape
            data,labels = self.loadData(datalink) 
            try:
                self.predict(data[0])
                return "Recived from File"
            except:
                #Delete Original Files, then continue on making as normal
                if path.exists("my_model.keras"):
                    remove("my_model.keras")
                if path.exists("statFile.txt"):
                    remove("statFile.txt")
                pass

        else:
            data,labels = self.loadData(datalink) 

        # Standarize data. 
        data = np.transpose(data)
        with open("statFile.txt",'w') as statFile:
            for i in data:
                mean = np.mean(i)
                std = np.std(i)
                for num in range(len(i)):
                    i[num] = (i[num] - mean) / std
                    
                statFile.write(str(mean) +","+str(std)+ "\n")

        data = np.transpose(data)
        

        #Split into eval and training data

        split = -(int(len(data) * 0.2))
        dataEVAL = data[split:]
        labelEVAL = labels[split:]

        data = data[:split]
        labels = labels[:split]

        # Creating a Sequential model
        model = Sequential()

        # Adding layers to the model
        model.add(tf.keras.layers.Input(shape=(self.numFeatures,)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))  
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(128, activation='relu'))  
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

        #3x64 No Dropout
        # model.add(tf.keras.layers.Input(shape=(self.numFeatures,)))
        # model.add(tf.keras.layers.Dense(64, activation='relu'))  
        # model.add(tf.keras.layers.Dense(64, activation='relu'))
        # model.add(tf.keras.layers.Dense(64, activation='relu'))  
        # model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # Output layer with 1 neuron and sigmoid activation for binary classification

        #5x64 No Dropout
        # model.add(tf.keras.layers.Input(shape=(self.numFeatures,)))
        # model.add(tf.keras.layers.Dense(64, activation='relu'))  
        # model.add(tf.keras.layers.Dense(64, activation='relu'))
        # model.add(tf.keras.layers.Dense(64, activation='relu'))
        # model.add(tf.keras.layers.Dense(64, activation='relu'))  
        # model.add(tf.keras.layers.Dense(64, activation='relu'))  
        # model.add(tf.keras.layers.Dense(1, activation='sigmoid')) 


        #1x512
        # model.add(tf.keras.layers.Input(shape=(self.numFeatures,)))
        # model.add(tf.keras.layers.Dense(512, activation='relu'))  
        # model.add(tf.keras.layers.Dense(1, activation='sigmoid')) 

        #3x256
        # model.add(tf.keras.layers.Input(shape=(self.numFeatures,)))
        # model.add(tf.keras.layers.Dense(256, activation='relu'))  
        # model.add(tf.keras.layers.Dense(256, activation='relu'))
        # model.add(tf.keras.layers.Dense(256, activation='relu'))  
        # model.add(tf.keras.layers.Dense(1, activation='sigmoid')) 


        # Compiling the model
        model.compile(optimizer='adam', loss= tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

        # Training the model
        model.fit(data, labels, epochs=25, batch_size=8, validation_split=0.1)
        self.model = model

        self.createSave(model)
        self.evaluate(dataEVAL,labelEVAL,data,labels)

        return "Model Loaded Success from File"

    def standarize(self, data):
        with open("statFile.txt",'r') as statFile:
            mean, std = statFile.readline().split(",")
            
            mean = float(mean)
            std = float(std)
            if type(data[0]) == np.array or type(data[0]) == list:
                data = np.transpose(data)
                for i in data:
                    for num in range(len(i)):
                        i[num] = (i[num] - mean) / std
                data = np.transpose(data)
            else:
                data = np.transpose(data)
                for num in range(len(data)):
                    data[num] = (data[num] - mean) / std
                data = np.transpose(data)
        
        return data
        
        

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
        #I THINK I HAVE TO STANDARIZE THE DATA. PROBABLY HAVE TO UNSTANDARIZE THE RESULTS. 
        #data = self.standarize(data)
        prediction = self.model.predict(data, verbose = 0)
        return prediction

    def loadData(self,datalink):
        with open(datalink) as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)

            rows = []
            labels = []
            for row in csvreader:
                rows.append(row[:-1])
                labels.append([row[-1]])

        rowNP = np.array(rows, dtype=float)
        labels = np.array(labels,  dtype=float)
        return rowNP, labels

#MODEL IS NOT COMPLETE. 






