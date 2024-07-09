import numpy 


with numpy.load('bloodmnist_64.npz') as data:
    print(data["train_images"])

    

