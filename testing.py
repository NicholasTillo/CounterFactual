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

Model = deeplearningmodel.modelReader()
data, labels = Model.loadData("link")
Model.createModel("Data\default_of_credit_card_clients.csv")

# print("Actual One: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2, 3913, 3102, 689, 0, 0, 0, 0, 689, 0, 0, 0, 0]]))))
# print("Coutnerfactual 1: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]]))))

# print("Coutnerfactual 1:" + str(Model.predict([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]])))
# print("Coutnerfactual 2:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2.2, 2, -1.1, -1.1, -2, -2.4200000000000004, 4304.3, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0.0, 0, 0])))
# print("Coutnerfactual 3:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2, 2.2, -1, -1, -2, -2.2, 3913, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0, 0, 0])))

#print(len([90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]))
#print("Actual One: " + str(Model.predict(np.array([[90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]]))))
# print("Actual One: " + str(Model.predict(np.array([[450000,2,1,1,40,-2,-2,-2,-2,-2,-2,5512,19420,1473,560,0,0,19428,1473,560,0,0,1128]]))))
#print("Actual One: " + str(Model.predict(np.array([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]]))))
print("Actual One: " + str(Model.predict(np.array([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]]))))

#print("Actual One: " + str(Model.predict(data)))
##result = Model.predict([[50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]])
##for i,j in zip(result, labels):
 #   print("Predicted: "+ str(i[0]) + ", Actual: " +str(j[0]) )
