import numpy as np
import random
import deeplearningmodel
import seaborn as sns
import matplotlib.pyplot as plt

#Import in a second. 
class Individual:
    def __init__(self, paramList,runner) -> None:
        self.runner = runner
        self.param = paramList
        self.fitness = 0
        self.elite = self.runner.behaviour(self)
        self.classifyVal = 0

    def __str__(self):
        return str(self.param)
    
    def getList(self):
        return self.param
    def getFitness(self):
        return self.fitness
    def getClassifier(self):
        return self.classifyVal
    
    def mutate(self):
        #change a bit of the individual, rarely. 
        for i in range(len(self.param)):
            num = random.random()
            if num < self.runner.mutationrate:
                self.param[i] += self.param[i] * (random.random()*0.4)

                #print("mutate")
        return 
    
    def determineBehaviour(self):
        self.elite = self.runner.behaviour(self)
        return
    def determineFitness(self):
        self.fitness = self.runner.Fitness(self)
        return
    
    def classify(self, classifier):
        # print("HERE")
        try:
            # print("Type of Param: " + str(type(np.array(self.param))))
            # print("Shape: " + str(np.array([self.param]).shape))

            value = classifier.predict(np.array([self.param]))
            self.classifyVal = value
            #print("Classified Fine")
            return True
        except:
            #print("Classify Failed")
            return False
        


    


class Grid:
    
    def __init__(self, resolution, XDimen, YDimen) -> None:
        self.grid =  np.empty(shape=(resolution,resolution), dtype=Individual)
        #What do the dimensions mean?
        self.xDim = XDimen
        self.yDimen = YDimen
        #How many elites per dimension. 
        self.resolution = resolution
        self.inside = {}

    def __str__(self) -> str:
        return str(self.grid)
    def initGrid(self):
        #self.grid.fill(1)
        pass

    def getRand(self):
        #Pick random section of the map, if they are filled, return them.
        result = list(self.inside.keys())[int(random.random() * len(self.inside.keys()))]
        
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
            return self.grid[location]
        except:
            return False
        
    def getGrid(self):
        return self.grid
    
    def getFitnessGrid(self):
        clone =  np.empty(shape=(self.resolution,self.resolution), dtype=float)
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
               if self.grid[i][j] is not None:
                    clone[i][j] = self.grid[i][j].getFitness()

        return clone
    
    def updateNumElite(self):
        count = 0
        for i in self.grid:
            for j in i:
                if j is not None:
                    count += 1

        #print("Current Count is: " + str(count))
        return count
    def remove(self, ind):
        # print(self.inside)
        del self.inside[ind]
        # print(self.inside)
        return



class MapEliteRunner:
    def __init__(self,mutationRate,map, classifier,originalList) -> None:
        self.mutationrate = mutationRate
        self.map = map
        self.numElites = 0
        self.classifier = classifier
        self.originalList = originalList
        pass


    def __str__(self) -> str:
        return str(self.map)
    

    #Put a elite into the correct space. 
    def checkElite(self,ind):
        #Check who wins the competition, and put whoever wins on top of that map.
        elite = self.map.get(ind.elite)
        winner = self.Compete(elite,ind)
        result = self.map.set(ind.elite, winner)

        self.numElites = self.map.updateNumElite()
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
                if random.random() < 0.5:
                    newList.append(i[0])
                else:
                    newList.append(i[1])

        baby = Individual(newList, self)
        baby.mutate()
        baby.determineBehaviour()
        baby.classify(self.classifier)
        baby.determineFitness()

        return baby
        
    #Two Functions for defining the behaviour of an individual  
    def CountActionChanges(self,ind):
        count = 0
        for i,j,k in zip(ind, userInput, actionable):
            #print("i: " + str(i))
            #print("j: " + str(j))
            #print("k: " + str(k))

            if (i != j) and (k):
                count += 1
        return count


    def CountInActionChanges(self, ind):
        count = 0
        for i,j,k in zip(ind, userInput, actionable):
            #If it has been changed, and its not actionable.
            #Condition is not actionable. 

            #print("i: " + str(i))
            #print("j: " + str(j))
            #print("k: " + str(k))
            if (i != j) and (not k):
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
        
        elif ind1.getFitness() < ind2.getFitness(): 
            #Remove Ind1 from the map and inside. 
            self.map.remove(ind1)
            return ind2
        
        else:
            return ind1
        

    def Fitness(self, ind):
        #4 Way maximization function
        #Validity, Proximity, Scarcisty, Plausibility. 
        result = 0
        #Validity, 
        validityval = ind.getClassifier()
        #Proximity, 
        indList = ind.getList()
        resultList = []

        standardizedIndList = self.classifier.standarize(indList)
        standardizedOrgList = self.classifier.standarize(self.originalList)

        for i in range(len(indList)):
            resultList.append(np.abs((standardizedIndList[i] - standardizedOrgList[i])))
        proximityval = sum(resultList)
        #print(proximityval)

        result = (1-validityval) - proximityval/10


        return result


    def behaviour(self, ind):
        #Determine which section to
        #Returns a tuple of the location of the cell this individual is at.  
        indList = ind.getList() 
        x = self.Section(xDimension,indList)
        y = self.Section(yDimension,indList)
        location = (x,y)
        return location
    


    def showPlot(self):
        sns.heatmap(self.map.getFitnessGrid(), annot=True, cmap='viridis')
        plt.title('Heatmap of 2D Numpy Array')
        plt.show()
        return

    def showAllCFs(self):
        allInst = self.map.getGrid()
        with open("outputfile.txt", 'w') as output:
            output.write("Original Input: "+ str(self.originalList) + "\n")

            counti = 0

            for i in allInst:
                countj = 0
                for j in i:
                    if j == None:
                        output.write("Counterfactual at location: " + str(counti) + "," + str(countj)+ ": "+ str(j) +"\n")
                    else:
                        output.write("Counterfactual at location: " + str(counti) + "," + str(countj)+ ": "+ str(j) + " Fitness: "+ str(j.fitness) +"\n")

                    
                    countj+=1
                counti+=1

        return self.map.getGrid()




#The userinput is the inputted 
userInput = [50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]
userInputClone = [50000,1,2,1,46,0,0,0,0,0,0,47929,48905,49764,36535,32428,15313,2078,1800,1430,1000,1000,1000]


#Get whether if the conditions are actionable or not.
actionable = [False,False,False,True, True, False,True,True,True,True,
              True,True,True,True,True,True,True,True,True,True,True,
              True,True]

resolution = 8
iteration = 100000

xDimension = "NumActionableChanges"
yDimension = "NumInactionableChanges"

#Create empty grid. 
x = Grid(resolution, xDimension, yDimension)
x.initGrid()

#Create some test individuals. 
Model = deeplearningmodel.modelReader()
Model.createModel("Data\default_of_credit_card_clients.csv")
mutationRate = 0.05

runner = MapEliteRunner(mutationRate,x,Model,userInput)
testind1 = Individual(userInputClone, runner)

testind1.determineBehaviour()
testind1.classify(runner.classifier)
#print("HERE")

testind1.determineFitness()
#print(testind1.getFitness())
runner.checkElite(testind1)

maxClass = 0.5

for i in range(iteration):
    if i % 100 == 0:
        print("Iteration: "+str(i))
    #print("Iteration: "+str(i))
    #Select Parent
    #Genetic Variation
    #Development & evaluation
    #Determine Niche
    child = runner.generateChild()
    #Compete With Niece, replacement on victory. 
    if child.classifyVal < maxClass:
        runner.checkElite(child)
    else:
        runner.checkElite(child)
    pass


#Visualize
print(runner)
runner.showPlot()
print("Total Number Of Elites: " + str(runner.map.updateNumElite()))
runner.showAllCFs()