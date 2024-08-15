import numpy as np
import random
import deeplearningmodelGoodCopy
from itertools import combinations
import seaborn as sns
import matplotlib.pyplot as plt
import os

#Import in a second. 
class Individual:
    def __init__(self, paramList,runner):
        self.runner = runner
        self.numMutate = 0
        self.param = paramList
        self.fitness = 0
        self.elite = self.runner.behaviour(self)
        self.classifyVal = 0

    def __str__(self):
        return str(self.param)
    def __lt__(self, other):
        return self.fitness < other.fitness
    def getList(self):
        return self.param
    def getFitness(self):
        return self.fitness
    def getClassifier(self):
        return self.classifyVal
    def getTimesMutated(self):
        return self.numMutate
    
    
    def mutate(self):
        #change a bit of the individual, rarely. 
        for i in range(len(self.param)):
            num = random.random()
            if num < self.runner.mutationrate:
                self.numMutate += 1

                value = self.runner.featureSpaceLists[i]
                #print(value)
                #print(type(value))
                if type(value) == list:
                    #If this feature space is defined to be descrite and ordered, chose an option above or below and apply it.
                    randIndex = value.index(self.param[i])

                    
                    if random.random() < 0.5 and (randIndex + 1 < len(value)):
                        #If we are able to go up, 
                        self.param[i] = value[randIndex + 1]
                    elif(randIndex > 0):
                        #If we are able to go down, 
                        self.param[i] = value[randIndex - 1]


                elif type(value) == set:
                    #If this feature space is defined to be descrit, chose an option randomly.
                    randIndex = (random.random() * len(value))
                    self.param[i] = value[randIndex]

                elif type(value) == str:
                    #If the range is a specific data type. 
                    if value == "int":
                        #When reaching an integer, mutate by an amount up to 10% of the standard deviation. 

                        with open("statFile.txt",'r') as statFile:
                            #Find the mean and standard deivation
                            mean, std = statFile.readlines()[i].split(",")
                            number = int(float(std) * (random.random()*0.1))
                            if number == 0:
                                if random.random() < 0.5:
                                    number = 1
                            

                            if num < (self.runner.mutationrate/2):
                                #Chose wether to increase or decrease the number. 
                                self.param[i] += number 
                            else:
                                self.param[i] -= number

                    if value == "float":
                        #When reaching an float, mutate by an amount up to 10% of the standard deviation. 

                        with open("statFile.txt",'r') as statFile:
                            #Find the mean and standard deivation
                            mean, std = statFile.readlines()[i].split(",")
                            number = (float(std) * (random.random()*0.1))
                            if number == 0:
                                if random.random() < 0.5:
                                    number = 1
                            

                            if num < (self.runner.mutationrate/2):
                                #Chose wether to increase or decrease the number. 
                                self.param[i] += number 
                            else:
                                self.param[i] -= number

                        
        return 
    
    def determineBehaviour(self):
        #Determine and set the behaviour of the individual
        self.elite = self.runner.behaviour(self)
        return
    
    def determineFitness(self):
        #Determine and set the fitness of the individual
        self.fitness = self.runner.Fitness(self)
        return
    
    def classify(self, classifier):
        #Attempt to classify the individual using the runners classifier. 
        try:
            value = classifier.predict(np.array([self.param]))
            self.classifyVal = value
            return True
        except:
            return False
        


    


class Grid:
    
    def __init__(self, resolutionx, resolutiony, XDimen, YDimen) -> None:
        #Numpy array object storage
        self.grid =  np.empty(shape=(resolutiony,resolutionx), dtype=Individual)

        #Description of what the dimensions mean, Should be an ENUM. 
        self.xDim = XDimen
        self.yDim = YDimen
        #How many elites per dimension. 
        self.resolutionx = resolutionx
        self.resolutiony = resolutiony

        #Hashmap used for faster lookup 
        self.inside = {}

    def __str__(self) -> str:
        return str(self.grid)
    def get_dimensions(self):
        return self.xDim, self.yDim
    def getResolution(self):
        return self.resolutionx, self.resolutiony
    def initGrid(self):
        #Does Nothing
        #self.grid.fill(1)
        pass

    def getRand(self,number):
        #Pick random section of the map, if they are filled, return them.

        if number == 1:
            return list(self.inside.keys())[int(random.random() * len(self.inside.keys()))]
        
        result = set()
        if number <= 4:
            while len(result) != number:
                result.add(list(self.inside.keys())[int(random.random() * len(self.inside.keys()))])
        else:
            while len(result) != 4:
                result.add(list(self.inside.keys())[int(random.random() * len(self.inside.keys()))])

        final = list(result)
        final.sort()
        return final[0],final[1]
        
    

    def set(self, location, item):
        #Set 1 section of the grid, update the hashmap accordingy. 
        try:
            if None in location:
                return False
            self.grid[location] = item
            self.inside[item] = location
            return True
        except:
            return False 
        
    def get(self, location):
        #Recive the individual at a specific location. 
        #I think requires a tuple. 
        try:
            return self.grid[location]
        except:
            return False
        
    def getGrid(self):
        #Returns the whole grid object. 
        return self.grid
    
    def getFitnessGrid(self, relative = False):
        #Returns a 2D grid of the corresponing fitness's of the individuals that inhabit that elite. 
        #Used in the display
        if relative == True:
            lowest = 100
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i][j] is not None:
                            temp = self.grid[i][j].getFitness()
                            if temp < lowest:
                                lowest = temp

                        
            clone =  np.empty(shape=(self.resolutiony,self.resolutionx), dtype=float)
            clone.fill(0)
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i][j] is not None:
                            clone[i][j] = (self.grid[i][j].getFitness() - lowest) * 100

        else:
            clone =  np.empty(shape=(self.resolutiony,self.resolutionx), dtype=float)
            clone.fill(0)
            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i][j] is not None:
                            clone[i][j] = (self.grid[i][j].getFitness())
        
        return clone
    
    def updateNumElite(self):
        #Update the number of elites that are currently in the grid. 
        #Very pricy, 
        #Should cut this down. 
        count = 0
        for i in self.grid:
            for j in i:
                if j is not None:
                    count += 1

        return count
    

    def remove(self, ind):
        #Remove an individual from the internal hashmap
        del self.inside[ind]
        return



class MapEliteRunner:
    def __init__(self,mutationRate,gridData, data, model,originalList, descriptorList, featureSpaceList,actionablelist, tuningVal = None) -> None:
        #Self Explanitory
        self.mutationrate = mutationRate

        #Stores the grid object that stores individuals. 
        x = Grid(gridData[0], gridData[1], gridData[2], gridData[3])
        x.initGrid()
        self.map = x

        #Current number of elites 
        self.numElites = 0
        #Classifier Object
        self.datalink = data

        self.classifier = model
        #Original List, that we are generating the counterfactuals for
        self.originalList = originalList
        #Original classification for the original list, to see if we are wasting our time. 
        self.originalClassifier = self.classifier.predict(np.array([originalList]))
        #A list that describes if each feature is qualitative or quantitivatie. 
        self.descriptorList = descriptorList
        #2D array that describes the feature spaces for each feature. 
        self.featureSpaceLists = featureSpaceList
        self.actionableList = actionablelist

        if not tuningVal:
            self.tuningValue = 1
        else:
            self.tuningValue = tuningVal

        self.xlabel = None
        self.ylabel = None


        testind1 = Individual(originalList.copy(), self)
        testind1.determineBehaviour()
        testind1.classify(self.classifier)
        testind1.determineFitness() 
        self.checkElite(testind1)

        
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
            par1 = self.map.getRand(1)
            return par1
        
        par1, par2 = self.map.getRand(numPar)

        return par1, par2

    #Create a child, used for reproduction. 
    def generateChild(self):
        #Take half from parent 1 and half from parent 2
        newList = []

        if self.numElites == 1:
            par1 = self.getParents(1)
            newList = par1.getList()
        else:
            par1, par2 = self.getParents(self.numElites)
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
        for i,j,k in zip(ind, self.originalList, self.actionableList):
            if (i != j) and (k == 1):
                count += 1
        return count


    def CountInActionChanges(self, ind):
        count = 0
        for i,j,k in zip(ind, self.originalList, self.actionableList):
            #If it has been changed, and its not actionable.
            #Condition is not actionable. 
            if (i != j) and (not k == 1):
                count += 1
        return count
    
    def CountTotalChanges(self,ind):
        count = 0
        for i,j in zip(ind, self.originalList):
            if (i != j):
                count += 1
        return count
    
    def CountLoanChanges(self,ind):
        count = 0
        for i,j in zip(ind[5:], self.originalList[5:]):
            if (i != j):
                count += 1
        return count
    
    def CountNonLoanChanges(self,ind):
        count = 0
        for i,j in zip(ind[:5], self.originalList[:5]):
            if (i != j):
                count += 1
        return count

    def CountNumTimesMutated(self,ind):
        return ind.getTimesMutated()
    
    def DiscreteAxis(self,num,ind,xory):
        #Divide the range (Assumed by mean + 4x SD, (Similar to assuming normal distribution)) by number of squares
        #CURRENTLY BROKEN, IT ONYL EVER RETURNS 0, 
        #ITS NOT GOOD, 
        #IT MIGHT BE TOO BIG TO DO 2* STD, 
        #MIGHT CHANGE TO 1, BUT NOT SURE>
        numX, numY = self.map.getResolution() 
        if xory == "x":
            usedNum = numX
        elif xory == "y":
            usedNum = numY
        rangenum = 0


        #This is the value that dictates how many times the original value the range would be, 
        #For example, with a tolerance_number of 2, the coutnerfactuals would generate from 0 - 2* the original value. 
        tolerance_number = 2

        if self.descriptorList[num] == 0: 
            #Initilaize Empty Lists. 
            featurelist = []


            with open("statFile.txt") as stats:
                mean, std = stats.readlines()[num].split(",")
                rangenum = float(mean) + float(std) * self.tuningValue

            boxsize = int(rangenum) / usedNum

            #Iterate through all the numbers, and find which smallest one encapsulates in input (ind[num])
            #Also make sure to 
            current = (self.originalList[num] - (rangenum/2))
            value = None

            for i in range(usedNum):

                next = current + boxsize
                if type(self.originalList[num]) == int:
                    featurelist.append(str(int(current)) + " - " + str(int(next)))
                elif type(self.originalList[num]) == float:
                    featurelist.append("{:.3f}".format(float(current)) + " - " + "{:.3f}".format(float(next)))


                if ind[num] <= next and value == None:
                    value = i
                current = next

            #Choose  which label to set it as. 
            if xory == "x":
                self.xlabel = featurelist
            else:
                self.ylabel = featurelist
        
            return value
        
        elif self.descriptorList[num] == 1:

            #Update Labels
            if xory == "x":
                self.xlabel = list(self.featureSpaceLists[num])
            else:
                self.ylabel = list(self.featureSpaceLists[num])


            #Find Whwere it supposed to be, and num of things in feature space. 
            location = self.featureSpaceLists[num].index(ind[num])
            number2 = len(self.featureSpaceLists[num])
            result = [0]*(usedNum)
            
            for i in range(number2):
                result[i % usedNum] += 1
            current = 0
            

            for i in range(location+1):
                if result[current] > 0:
                    result[current] -= 1
                elif result[current] == 0:
                    current += 1
                    result[current] -= 1

            return current
        








    #Helper function used by the behavour functions
    def Section(self, Condition, ind, xy):
        if type(Condition) == int:
            return self.DiscreteAxis(Condition, ind.getList(), xy)
        elif callable(Condition):
            return function(ind)
        
        
        numX, numY = self.map.getResolution()
        if xy == "x":
            self.xlabel = range(0,numX)
        elif xy == "y":
            self.ylabel = range(0,numY)
        if Condition == "NumActionableChanges":
            return self.CountActionChanges(ind.getList())
        elif Condition == "NumInactionableChanges":
            return self.CountInActionChanges(ind.getList())
        elif Condition == "NumTotalChanges":
            return self.CountTotalChanges(ind.getList())
        elif Condition == "NumLoanChanges":
            return self.CountLoanChanges(ind.getList())
        elif Condition == "NumNonLoanChanges":
            return self.CountNonLoanChanges(ind.getList())
        elif Condition == "NumTimesMutated":
            return self.CountNumTimesMutated(ind)
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

        sparsity = 0
        #Validity, 
        validityval = ind.getClassifier()

        #Proximity, getting Distnace: using Gower distance Function
        #For each measure, 
        #If its qualitative, then use the Dice Distance, 
        #If its numeric, use manhatten distnace. 
        
        indList = ind.getList()
        resultList = []

        for i in range(len(indList)):
            subtraction = 0
            if self.descriptorList[i] == 0: 
                #Do Range Normalized Manhattan Distance. 
                if indList[i] == self.originalList[i]:
                    subtraction = 0
                elif indList[i] == 0 or self.originalList[i] == 0:
                    ## FIX THIS
                    sparsity += 1
                    subtraction = 1
                elif indList[i] > self.originalList[i]:
                    sparsity += 1
                    subtraction = (np.abs((indList[i] - self.originalList[i]))/indList[i])
                elif indList[i] < self.originalList[i]:
                    sparsity += 1
                    subtraction = (np.abs((indList[i] - self.originalList[i]))/self.originalList[i])
                

                #print(np.abs((standardizedIndList[i] - standardizedOrgList[i])) / standardizedOrgList[i])
            elif self.descriptorList[i] == 1:
                # Do Dice Distnace, 
                # if standardizedIndList[i] == standardizedOrgList[i]:
                if indList[i] ==  self.originalList[i]:

                    #If they are the same, there is no distnace, 
                    subtraction = 0
                else:
                    #If they are not the same. 
                    subtraction = 1
                    #sparsity += 1

            resultList.append(subtraction)         

        proximityval = (1 - (sum(resultList) / len(indList) ))

        #Plausibility
        #plausibiltiy  = 0
        #Loop through the data, and find the cloest k neighbours. 

        #Should describe a realisitc data instance, 
        #Find the closest k neighbours within the datast. 

        #Sparsity
        #sparsity =  - (sparsity/len(indList))
        #sparsity = 0
        #Should vary from x* in only a few features.  

        result = (1-validityval) + (proximityval) #+ plausibiltiy + sparsity

        return result


    def behaviour(self, ind):
        #Determine which section to
        #Returns a tuple of the location of the cell this individual is at.  
        x = self.Section(self.map.xDim,ind,"x")
        y = self.Section(self.map.yDim,ind,"y")
        location = (y,x)
        return location
    

    def showPlot(self, where=None ,showGrid=True):
        plt.subplots(figsize=(10,10))

        plot = sns.heatmap(self.map.getFitnessGrid(relative=False), annot=True, fmt=".3f", cmap='viridis',xticklabels = self.xlabel, yticklabels = self.ylabel)
        plot.figure.tight_layout()
        x,y = self.map.get_dimensions()
        plot.set(
            title="Heatmap",
            xlabel=x,
            ylabel=y,
        )
        plot.set()
        plt.title('Heatmap of 2D Numpy Array')
        if showGrid:
            plt.show()
        plot = plot.get_figure()
        plot.savefig("Output/figure"+str(where)+".png")
        plot.clf()
        return 

    def showAllCFs(self, where):
        allInst = self.map.getGrid()

        with open("Output/outputfile"+str(where)+".txt", 'w') as output:
            with open(self.datalink) as data:
                raw = data.readline()
                output.write(raw)

            output.write("Original Input: "+ str(self.originalList) + "Original Label: "+ str(self.originalClassifier) +"\n")

            counti = 0
            for i in allInst:
                countj = 0
                for j in i:
                    if j == None:
                        output.write("Counterfactual at location: " + str(counti) + "," + str(countj)+ ": "+ str(j) +"\n")
                    else:
                        output.write("Counterfactual at location: " + str(counti) + "," + str(countj)+ ": "+ str(j) + " Fitness: "+ str(j.fitness) +" Classifier Val: " +str(j.getClassifier()) +"\n")
                    countj+=1
                counti+=1

        return allInst


    def run(self,iterations,where, showGrid = True):

        cwd = os.getcwd()
        path = os.path.join(cwd, "Output")
        if not os.path.exists(path):
            os.makedirs(path)

        for i in range(iterations):
            if i % 100 == 0:
                print("Iteration: "+str(i))
            #print("Iteration: "+str(i))
            #Select Parent
            #Genetic Variation
            #Development & evaluation
            #Determine Niche
            child = self.generateChild()
            #Compete With Niece, replacement on victory. 
            self.checkElite(child)

        #Visualize
        
        self.showPlot(showGrid = showGrid, where = where)
        print("Total Number Of Elites: " + str(self.map.updateNumElite()))
        resultFig =  self.showAllCFs(where)
        return resultFig



    def runAllCombinations(self,iterations):

        perm = combinations(range(len(self.originalList)),2)
        currentResolution = self.map.getResolution()
        for i in (perm):
            self.map = Grid(currentResolution[0],currentResolution[1],i[0],i[1])
            testind1 = Individual(self.originalList.copy(), self)

            testind1.determineBehaviour()
            testind1.classify(self.classifier)
            testind1.determineFitness() 
            self.checkElite(testind1)

            self.run(iterations, i,False)






def main():
    #The us`erinput is the inputted FOR THE LOAN APPLICATION SETTING. 

    userInput = [30000,2,2,2,22,0,0,0,0,0,0,28387,29612,30326,28004,26446,6411,1686,1400,560,3000,1765,0]
    DescriptorList = [0,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]

    featureSpaceLists= [int,
                        [1,2],
                        [1,2,3,4],
                        [1,2,3],
                        int,
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        [-1,0,1,2,3,4,5,6,7,8,9],
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int,
                        int]
    #Get whether if the conditions are actionable or not.
    actionable = [0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    resolutionx = 4
    resolutiony = 20

    iteration = 5000

    #CAn have them just be a number, and itll show ones with 
    xDimension = 2
    yDimension = 0

    #Create empty grid. 
    gridstats = (resolutionx, resolutiony, xDimension, yDimension)

    #Create some test individuals. 

    mutationRate = 0.1
    Model = deeplearningmodelGoodCopy.modelReader(23)
    Model.createModel("Data\default_of_credit_card_clients.csv")
    runner = MapEliteRunner(mutationRate,  gridstats,  "Data\default_of_credit_card_clients.csv", Model, userInput,  DescriptorList,  featureSpaceLists,actionable)
    #runner.run(iteration,"WithOutRelative")
    runner.runAllCombinations(iteration)
    # runner.runAllCombinations()



def main2():
    userInput = [2.0,2.0,2.0,0.0,1.0]
    DescriptorList = [1,1,1,0,1]


    featureSpaceLists= [[1,2,3],[1,2],[1,2],int,[1,2]]
    #Get whether if the conditions are actionable or not.
    actionable = [0,0,0,1,1]

    resolutionx = 5
    resolutiony = 5

    iteration = 1000


    xDimension = 3
    yDimension = 0

    #Create empty grid. 

    gridstats = (resolutionx, resolutiony, xDimension, yDimension)
   

    #Create some test individuals. 
    Model = deeplearningmodelGoodCopy.modelReader(5)
    Model.createModel("TwoYearRec\compass_data_mace.csv")
    mutationRate = 0.5

    runner = MapEliteRunner(mutationRate,  gridstats,  "TwoYearRec\compass_data_mace.csv", Model, userInput,  DescriptorList,  featureSpaceLists, actionable)
    # runner.runAllCombinations(iteration)
    runner.run(iteration,"Name")
