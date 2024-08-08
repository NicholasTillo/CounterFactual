import numpy 


with numpy.load('Data\dermamnist_64.npz') as data:
    for i in data:
        print(i)
    print(data["train_images"])
    print(data["train_labels"])
    for i in data["train_images"]:
        print(i)
    

    

