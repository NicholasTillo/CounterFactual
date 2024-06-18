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
Model.createModel("Data\default_of_credit_card_clients.csv")

# print("Actual One: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2, 3913, 3102, 689, 0, 0, 0, 0, 689, 0, 0, 0, 0]]))))
# print("Coutnerfactual 1: " + str(Model.predict(np.array([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]]))))

# print("Coutnerfactual 1:" + str(Model.predict([[20000, 2, 2, 1, 24, 2, 2, -1, -1, -2, -2.2, 3913, 3412.2, 689, 0, 0, 0.0, 0.0, 689, 0, 0, 0, 0]])))
# print("Coutnerfactual 2:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2.2, 2, -1.1, -1.1, -2, -2.4200000000000004, 4304.3, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0.0, 0, 0])))
# print("Coutnerfactual 3:" + str(Model.predict([22000.0, 2, 2.2, 1.1, 24, 2, 2.2, -1, -1, -2, -2.2, 3913, 3412.2, 757.9, 0, 0.0, 0.0, 0.0, 689, 0, 0, 0, 0])))

# print(len([90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]))
print("Actual One: " + str(Model.predict(np.array([[90000,2,2,2,34,0,0,0,0,0,0,29239,14027,13559,14331,14948,15549,1518,1500,1000,1000,1000,5000]]))))
print("Actual One: " + str(Model.predict(np.array([[500000,1,1,2,29,0,0,0,0,0,0,367965,412023,445007,542653,483003,473944,55000,40000,38000,20239,13750,13770]]))))

