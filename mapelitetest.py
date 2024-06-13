import numpy as np
import random
import deeplearningmodel


#Import in a second. 
class Individual:
    def __init__(self, paramList,runner) -> None:
        self.runner = runner
        self.param = paramList
        self.fitness = self.runner.Fitness(paramList)
        self.elite = self.runner.behaviour(paramList)
    def __str__(self):
        return str(self.param)
    
    def getList(self):
        return self.param

    


class Grid:
    
    def __init__(self, resolution, XDimen, YDimen) -> None:
        self.grid =  np.empty(shape=(resolution,resolution), dtype=Individual)
        #What do the dimensions mean?
        self.xDim = XDimen
        self.yDimen = YDimen
        #How many elites per dimension. 
        self.resolution = resolution
        self.inside = {}

    
    def initGrid(self):
        #self.grid.fill(1)
        pass

    def getRand(self):
        #Pick random sections of the map, if they are filled, return them.
        print(list(self.inside.values()))
        result = list(self.inside.keys())[int(random.random() * len(self.inside.keys()))]

        # while type(result) is not Individual:
        #     int1 = int(random.random()*self.resolution)
        #     int2 = int(random.random()*self.resolution)
        #     result = self.grid[int1][int2]

        
        return result
    

    def set(self, location, item):
        try:
            self.grid[location] = item
            self.inside[item] = location
            return True
        except:
            return False
        
    def get(self, location):
        try:
            print(location)
            return self.grid[location]
        except:
            return False


class MapEliteRunner:
    def __init__(self,mutationRate,map, classifier) -> None:
        self.mutationrate = mutationRate
        self.map = map
        self.numElites = 0
        self.classifier = classifier
        pass



    def __str__(self) -> str:
        return str(self.map)
    #Put a elite into the correct space. 
    def checkElite(self,ind):
        #Check who wins the competition, and put whoever wins on top of that map.
        elite = self.map.get(ind.elite)
        winner = self.Compete(elite,ind)
        result = self.map.set(ind.elite, winner)

        self.numElites += 1
        return result


    #Get 2 random parnets, used for reproduction. 
    def getParents(self, numPar):

        if numPar == 1:
            par1 = self.map.getRand()
            return par1
        

        par1 = self.map.getRand()
        par2 = self.map.getRand()
        while par2 == par1:
            par2 = self.map.getRand()

        return par1, par2

    #Create a child, used for reproduction. 
    def generateChild(self):
        #Take half from parent 1 and half from parent 2
        newList = []

        if self.numElites == 1:
            par1 = self.getParents(1)
            newList = par1.getList()
        else:
            par1, par2 = self.getParents(2)
            for i in zip(par1.getList(), par2.getList()):
                if random.random < 0.5:
                    newList.append(i[0])
                else:
                    newList.append(i[1])
        baby = Individual(newList, self)

        return baby
        
    #Two Functions for defining the behaviour of an individual  
    def CountActionChanges(self,ind):
        count = 0
        for i,j,k in zip(ind, userInput, actionable):
            if i is not j and k:
                count += 1
        return count


    def CountInActionChanges(self, ind):
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



    def Compete(self, ind1,ind2):
        #Check which of 2 individuals are more fit for survival. 
        if type(ind1) is not Individual:
            return ind2
        elif type(ind2) is not Individual:
            return ind1
        elif ind1.fitness < ind2.fitness: 
            return ind2
        else:
            return ind1
        

    def Fitness(self, indList):
        #4 Way maximization function
        #Validity, Proximity, Scarcisty, Plausibility. 
        result = 0
        #Validity, 
        
        return result


    def behaviour(self, indList):
        #Determine which section to
        #Returns a tuple of the location of the cell this individual is at.   
        x = self.Section(xDimension,indList)
        y = self.Section(yDimension,indList)
        location = (x,y)
        return location
    
    def Mutate(self, ind):
        #change a bit of the individual, rarely. 
        for i in ind.getList():
            if random.random() < mutationRate:
                i += i * 0.1
                print("mutate")
        pass


#The userinput is the inputted 
userInput = [20000,2,2,1,24,2,2,-1,-1,-2,-2,3913,3102,689,0,0,0,0,689,0,0,0,0]
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
Model = deeplearningmodel.modelReader()
Model.createModel("Data\default_of_credit_card_clients.csv")
mutationRate = 0.05

runner = MapEliteRunner(mutationRate,x,Model)
testind1 = Individual(userInput, runner)


runner.checkElite(testind1)
for i in range(iteration):
    #Select Parent
    #Genetic Variation
    #Development & evaluation
    #Determine Niche
    child = runner.generateChild()
    
    #Compete With Niece, replacement on victory. 
    runner.checkElite(child)
    pass


#Visualize
print(runner)

