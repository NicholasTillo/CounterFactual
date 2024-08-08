import numpy as np
from keras import Sequential
from keras import models
import tensorflow as tf
import csv


class modelReader:
    def __init__(self) -> None:
        self.model=None

        pass

        
    def checkSave(self):
        try:
            open("my_medical_model.keras","r")
            return True
        except:
            return False
        

    def createSave(self,model):
        try:
            print("ATTEMPTINGSAVE")
            model.save('my_medical_model.keras')
            print("Save Good")

            return True
        except:
            print("SAVE FAILED")
            return False
        

    def loadSave(self):
        print("Trying to Load Model")
        self.model = models.load_model('my_medical_model.keras')
        print("Loaded Model")
        return True
    
    
    def createModel(self,datalink):
        #Everything in this file kinda. 
        # Generating some  data
        if self.checkSave():
            self.loadSave()
            return "Recived from File"
        
        training_data = []
        training_labels = [] 

        testing_images = []
        testing_labels = []
        with np.load('Data\dermamnist_64.npz') as data:
            training_data = data["train_images"]
            training_labels = data["train_labels"]
            testing_data = data["test_images"]
            testing_labels = data["test_labels"]


        #data,labels = self.loadData(datalink)  # 30000,23 | 30000,1

        #Standarize data. 
        
        # data = np.transpose(data)
        # with open("statFile.txt",'w') as statFile:
        #     for i in data:
        #         mean = np.mean(i)
        #         std = np.std(i)
        #         for num in range(len(i)):
        #             i[num] = (i[num] - mean) / std
                    
        #         statFile.write(str(mean) +","+str(std)+ "\n")

        # data = np.transpose(data)
        

        #Split into eval and training data

        # Creating a Sequential model
        model = Sequential()

        # Adding layers to the model
        model.add(tf.keras.layers.Input(shape=(64,64,3,)))
        model.add(tf.keras.layers.Activation("relu"))
        model.add(tf.keras.layers.SeparableConv2D(64, 3, padding="same"))
        model.add(tf.keras. layers.BatchNormalization())
        model.add(tf.keras.layers.Dropout(0.2))
    
    
        model.add(tf.keras.layers.Activation("relu"))
        model.add(tf.keras.layers.SeparableConv2D(128, 3, padding="same"))
        model.add(tf.keras. layers.BatchNormalization())

        model.add(tf.keras.layers.MaxPooling2D((4,4), strides=4, padding="valid")) 

        model.add(tf.keras.layers.MaxPooling2D((4,4), strides=4, padding="valid")) 

        model.add(tf.keras.layers.GlobalAveragePooling2D())
        model.add(tf.keras.layers.Dense(1, activation=None))

        # Compiling the model
        model.compile(optimizer='adam', loss= tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

        # Training the model
        model.fit(training_data, training_labels, epochs=25, batch_size=8, validation_split=0.1)
        self.model = model


        self.createSave(model)
        self.evaluate(testing_data,testing_labels,training_data,training_labels)

        return "Recived from File"

    def standarize(self, data):
        with open("statMedicalFile.txt",'r') as statFile:
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
        datalink = "Data\dermamnist_64.npz"
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

reader = modelReader()
reader.createModel("Data\dermamnist_64.npz")







