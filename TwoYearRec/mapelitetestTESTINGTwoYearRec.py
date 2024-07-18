import numpy as np
import random
import deeplearningmodeltwoyear
import seaborn as sns
import matplotlib.pyplot as plt


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

                elif type(value) == type:
                    #If the range is a specific data type. 
                    if value == int:
                        #When reaching an integer, mutate by an amount up to 10% of the standard deviation. 

                        with open("statFileTwoYear.txt",'r') as statFile:
                            #Find the mean and standard deivation
                            mean, std = statFile.readlines()[i].split(",")
                            number = int(float(std) * (random.random()*0.1))
                            if num < (self.runner.mutationrate/2) and self.param[i] < number:
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
        self.grid =  np.empty(shape=(resolutionx,resolutiony), dtype=Individual)

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
    
    def getFitnessGrid(self):
        #Returns a 2D grid of the corresponing fitness's of the individuals that inhabit that elite. 
        #Used in the display
        clone =  np.empty(shape=(self.resolutionx,self.resolutiony), dtype=float)
        clone.fill(0)
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
               if self.grid[i][j] is not None:
                    clone[i][j] = self.grid[i][j].getFitness()

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
    def __init__(self,mutationRate,map, classifier,originalList, descriptorList, featureSpaceList) -> None:
        #Self Explanitory
        self.mutationrate = mutationRate

        #Stores the grid object that stores individuals. 
        self.map = map

        #Current number of elites 
        self.numElites = 0
        #Classifier Object
        self.classifier = classifier
        #Original List, that we are generating the counterfactuals for
        self.originalList = originalList
        #Original classification for the original list, to see if we are wasting our time. 
        self.originalClassifier = classifier.predict(np.array([originalList]))
        #A list that describes if each feature is qualitative or quantitivatie. 
        self.descriptorList = descriptorList
        #2D array that describes the feature spaces for each feature. 
        self.featureSpaceLists = featureSpaceList
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
            if (i != j) and (not k):
                count += 1
        return count
    
    def CountTotalChanges(self,ind):
        count = 0
        for i,j in zip(ind, userInput):
            if (i != j):
                count += 1
        return count
    
    def CountLoanChanges(self,ind):
        count = 0
        for i,j in zip(ind[5:], userInput[5:]):
            if (i != j):
                count += 1
        return count
    def CountNonLoanChanges(self,ind):
        count = 0
        for i,j in zip(ind[:5], userInput[:5]):
            if (i != j):
                count += 1
        return count

    def CountNumTimesMutated(self,ind):
        return ind.getTimesMutated()

    #Helper function used by the behavour functions
    def Section(self, Condition, ind):
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
        #I

        
        indList = ind.getList()
        resultList = []

        for i in range(len(indList)):
            subtraction = 0
            if self.descriptorList[i] == "Quantitative": 
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
            elif self.descriptorList[i] == "Qualitative":
                #Do Dice Distnace, 
                # if standardizedIndList[i] == standardizedOrgList[i]:
                if indList[i] ==  self.originalList[i]:

                    #If they are the same, there is no distnace, 
                    subtraction = 0
                else:
                    #If they are not the same. 
                    subtraction = 1
                    #sparsity += 1

            resultList.append(subtraction)         
        
        #print(resultList)
        proximityval = (1 - (sum(resultList) / len(indList) ))
        #print(resultList)

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
        x = self.Section(self.map.xDim,ind)
        y = self.Section(self.map.yDim,ind)
        location = (x,y)
        return location
    


    def showPlot(self):
        plot = sns.heatmap(self.map.getFitnessGrid(), annot=True, cmap='viridis')
        plt.title('Heatmap of 2D Numpy Array')
        plt.show()
        plot = plot.get_figure()
        plot.savefig("figure.png")
        return

    def showAllCFs(self):
        allInst = self.map.getGrid()
        with open("outputfile.txt", 'w') as output:
            output.write(",X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,Y\n" )
            output.write("ID,LIMIT_BAL,SEX,EDUCATION,MARRIAGE,AGE,PAY_0,PAY_2,PAY_3,PAY_4,PAY_5,PAY_6,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6,default payment next month\n")

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

        return self.map.getGrid()




#The userinput is the inputted FOR THE LOAN APPLICATION SETTING. 

userInput = [2.0,2.0,2.0,0.0,1.0]
userInputClone = [2.0,2.0,2.0,0.0,1.0]
DescriptorList = ["Qualitative","Qualitative","Qualitative","Quantitative","Quantitative"]


featureSpaceLists= [
                    [1,2,3],
                    [1,2],
                    [1,2],
                    int,
                    [1,2]
                    ]
#Get whether if the conditions are actionable or not.
actionable = [False,False,False,True, True]

resolutionx = 5
resolutiony = 5

iteration = 10000

xDimension = "NumActionableChanges"
yDimension = "NumTimesMutated"

#Create empty grid. 
x = Grid(resolutionx, resolutiony, xDimension, yDimension)
x.initGrid()

#Create some test individuals. 
Model = deeplearningmodeltwoyear.modelReader()
Model.createModel("TwoYearRec\compass_data_mace.csv")
mutationRate = 0.05

runner = MapEliteRunner(mutationRate,  x,  Model,  userInput,  DescriptorList,  featureSpaceLists)
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
    runner.checkElite(child)


#Visualize
print(runner)

runner.showPlot()
print("Total Number Of Elites: " + str(runner.map.updateNumElite()))
runner.showAllCFs()