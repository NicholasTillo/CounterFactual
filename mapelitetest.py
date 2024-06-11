import numpy as np
import random

#Import in a second. 
class Individual:
    def __init__(self, paramList) -> None:
        self.param = paramList
        self.fitness = Fitness(paramList)
        self.elite = behaviour(paramList)
    def __str__(self):
        return self.param
    

#The userinput is the inputted 
userInput = []
#Get whether if the conditions are actionable or not.
actionable = []

population = []
resolution = 32
iteration = 1000

xDimension = "NumActionableChanges"
yDimension = "NumInactionableChanges"

#Create empty grid. 
x = np.empty(shape=(resolution,resolution))


testind1 = Individual([1,2,3,4])
testind1 = Individual([1,2,3,3])

mutationRate = 0.05
def CountActionChanges(ind):
    count = 0
    for i,j in ind, userInput:
        if i is not j:
            count += 1
    return count

def CountInActionChanges(ind):
    count = 0
    for i,j,k in ind, userInput, actionable:
        #If it has been changed, and its not actionable.
        #Condition is not actionable. 
        
        if i is not j and k:
            count += 1
    return count



def XSection(Condiiton, indList):
    if xDimension == "NumActionableChanges":
        return CountActionChanges(indList)
    pass

    
def YSection(Condition,indList):
    if yDimension == "NumInactionableChanges":
        return CountInActionChanges(indList)
    pass


def Fitness(pIndividual):
    #4 Way maximization function
    #Validity, Proximity, Scarcisty, Plausibility. 
    
    pass



def behaviour(indList):
    #Determine which section to
    #Returns a tuple of the location of the cell this individual is at.   
    x = XSection(xDimension,indList)
    y = YSection(yDimension,indList)
    location = (x,y)
    return location



def Mutate(ind):
    #INitlatize New Individual

    pass



def Compete(ind1,ind2):
    fit1 = ind1.fitness
    fit2 = ind2.fitness

    if fit1 < fit2:
        return ind2
    else:
        return ind1


for i in iteration:
    #Select Parent
    #Genetic Variation
    #Development & valuation
    #Determine Niche
    #Compete With Niece, replacement on victory. 
    pass


#Visualize


