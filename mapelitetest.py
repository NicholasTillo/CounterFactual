import numpy as np
import random


#Import in a second. 
class Individual:
    def __init__(self, paramList,runner) -> None:
        self,runner = runner
        self.param = paramList
        self.fitness = self.runner.Fitness(paramList)
        self.elite = self.runner.behaviour(paramList)
    def __str__(self):
        return self.param

    


class Grid:
    
    def __init__(self, resolution, XDimen, YDimen) -> None:
        self.grid =  np.empty(shape=(resolution,resolution))
        self.xDim = XDimen
        self.yDimen = YDimen
        self.resolution = resolution
    
    def initGrid(self):
        self.grid.fill(1)

    def getRand(self,num):
        #Pick random sections of the map, if they are filled, return them.
        result = None
        while type(result) is not Individual:
            int1 = int(random.random()*self.resolution)
            int2 = int(random.random()*self.resolution)
            result = self.grid[int1][int2]
        return result



class MapEliteRunner:
    def __init__(self,mutationRate,map) -> None:
        self.mutationrate = mutationRate
        self.map = map
        self.numElites = 0
        pass


    #Put a elite into the correct space. 
    def addElite(self,ind):
        #Check who wins the competition, and put whoever wins on top of that map.
        pass


    #Get 2 random parnets, used for reproduction. 
    def getParents(self):
        par1 = self.map.getRand()
        par2 = self.map.getRand()
        while par2 == par1:
            par2 = self.map.getRand()


        return par1, par2

    #Create a child, used for reproduction. 
    def generateChild():
        #Take half from parent 1 and half from parent 2
        pass
        
    #Two Functions for defining the behaviour of an individual  
    def CountActionChanges(ind):
        count = 0
        for i,j,k in zip(ind, userInput, actionable):
            if i is not j and k:
                count += 1
        return count


    def CountInActionChanges(ind):
        count = 0
        for i,j,k in zip(ind, userInput, actionable):
            #If it has been changed, and its not actionable.
            #Condition is not actionable. 
            if i is not j and not k:
                count += 1
        return count
    

    #Helper function used by the behavour functions
    def Section(self, Condition, indList):
        if Condition == "NumActionableChanges":
            return self.CountActionChanges(indList)
        elif Condition == "NumInactionableChanges":
            return self.CountInActionChanges(indList)
        pass



    def Compete(ind1,ind2):
        #Check which of 2 individuals are more fit for survival. 
        if ind1.fitness < ind2.fitness:
            return ind2
        else:
            return ind1
        

    def Fitness(pIndividual):
        #4 Way maximization function
        #Validity, Proximity, Scarcisty, Plausibility. 
        pass


    def behaviour(self, indList):
        #Determine which section to
        #Returns a tuple of the location of the cell this individual is at.   
        x = self.Section(xDimension,indList)
        y = self.Section(yDimension,indList)
        location = (x,y)
        return location
    
    def Mutate(ind):
        #change a bit of the individual, rarely. 

        pass


#The userinput is the inputted 
userInput = [1,20000,2,2,1,24,2,2,-1,-1,-2,-2,3913,3102,689,0,0,0,0,689,0,0,0,0,1]
#Get whether if the conditions are actionable or not.
actionable = [False,False,False,True, True, False,]

resolution = 32
iteration = 1000

xDimension = "NumActionableChanges"
yDimension = "NumInactionableChanges"

#Create empty grid. 
x = Grid(resolution, xDimension, yDimension)
x.initGrid()

#Create some test individuals. 
testind1 = Individual(userInput)

mutationRate = 0.05

runner = MapEliteRunner(mutationRate,x)



for i in iteration:
    #Select Parent
    #Genetic Variation
    #Development & valuation
    #Determine Niche
    #Compete With Niece, replacement on victory. 
    pass


#Visualize


