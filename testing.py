import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import deeplearningmodel

# Create a sample 2D numpy array
# data = np.random.rand(10, 10)

# Create the heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(data, annot=True, cmap='viridis')
# plt.title('Heatmap of 2D Numpy Array')
# plt.show()

#print(len([20000,2,2,1,24,2,2,-1,-1,-2,-2,3913,3102,689,0,0,0,0,689,0,0,0,0]))
#print(len([False,False,False,True, True, False,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]))

# Model = deeplearningmodel.modelReader()
# data, labels = Model.loadData("link")
# Model.createModel("Data\default_of_credit_card_clients.csv")

# print("Actual One: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2, 3913, 3102, 689, 0, 0, 0, 0, 689, 0, 0, 0, 0]]))))
# print("Coutnerfactual 1: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]]))))

# print("Coutnerfactual 1:" + str(Model.predict([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]])))
# print("Coutnerfactual 2:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2.2, 2, -1.1, -1.1, -2, -2.4200000000000004, 4304.3, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0.0, 0, 0])))
# print("Coutnerfactual 3:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2, 2.2, -1, -1, -2, -2.2, 3913, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0, 0, 0])))

#print(len([90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]))
#print("Actual One: " + str(Model.predict(np.array([[90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]]))))
# print("Actual One: " + str(Model.predict(np.array([[450000,2,1,1,40,-2,-2,-2,-2,-2,-2,5512,19420,1473,560,0,0,19428,1473,560,0,0,1128]]))))
#print("Actual One: " + str(Model.predict(np.array([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]]))))
#print("Actual One: " + str(Model.predict(np.array([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]]))))

#print("Actual One: " + str(Model.predict(data)))
##result = Model.predict([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]])
##for i,j in zip(result, labels):
 #   print("Predicted: "+ str(i[0]) + ", Actual: " +str(j[0]) )
# 
# # print(len([50000.36982232727, 5595.900087337819, 5260.311762193608, 1, 46, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 47929, 48905, 49764, 37608.11958899026, 32428, 15313, 5363.133481308545, 5440.513345646703, 5219.36159778346, 5265.217255061664, 5246.38568121507, 5215.391474809184]  ))
# data, labels = Model.loadData("Data\default_of_credit_card_clients.csv")
# counter = 0
# for i,j in zip(data,labels):
#      counter += 1
     
#      prediction = Model.predict(np.array([i]))
#      print(str(counter) +","+str(prediction)+","+ str(j))
#      #print(i)



# featureSpaceLists= [int,
#                     [1,2],
#                     [1,2,3,4],
#                     [1,2,3],
#                     int,
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     [-1,1,2,3,4,5,6,7,8,9],
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int,
#                     int]
# DescriptorList = ["Quantitative","Qualitative","Qualitative","Qualitative","Quantitative","Qualitative","Qualitative","Qualitative",
#                   "Qualitative","Qualitative","Qualitative","Quantitative","Quantitative","Quantitative","Quantitative","Quantitative",
#                   "Quantitative","Quantitative","Quantitative","Quantitative","Quantitative","Quantitative","Quantitative"]
# print(featureSpaceLists[0])/
# print(type(featureSpaceLists[0]))
# result = []
# for i in DescriptorList:
#     if i == "Quantitative":
#         result.append(0)
#     else: 
#         result.append(1)
    
# print(result)

# print("Actual One: " + str(Model.predict(np.array([[50000,1,1,2,26,-1,0,0,0,0,0,15448,16392,18096,18425,18619,19060,1500,2000,1500,1200,900,1000]]))))
# import TwoYearRec.deeplearningmodeltwoyear as rec

# model = rec.modelReader()
# model.createModel("l")
# with open("TwoYearRec\compass_data_mace.csv","r") as file:
#     file.readline()
#     for i in file:
#         result = list()
#         counter = 0
#         for k in (i[:-1]).split(","):
#             if counter == 0 or counter == 1:
#                 counter += 1
#                 continue
#             result.append(float(k))
#             counter += 1
#         result = np.array([result])
#         print(result)
#         print(model.predict(result))
#         break


# with open("statFile.txt",'r') as statFile:
#             #Find the mean and standard deivation
#             mean, std = statFile.readlines()[3].split(",")
#             print(mean)
#             print(std)
            

# with open("statFile.txt",'r') as statFile:
#             #Find the mean and standard deivation
#             mean, std = statFile.readlines()[3].split(",")
#             print(mean)
#             print(std)

# arr = [[1,1,1,1,1],
#        [1,1,4,5,6],
#        [1,1,7,8,9]]
# arr2 = np.array(arr)
# print(arr2.shape)

number = 3
result = [[0]*number]
print(result)


import os
cwd = os.getcwd()
path = os.path.join(cwd, "Output")           
os.makedirs(path)
print(cwd)