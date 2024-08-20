import PyQt5
import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core

import deeplearningmodelGoodCopy
import mapelitetestGoodCopy
import sys
from ast import literal_eval


class MainWindow(wid.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.setFixedSize(core.QSize(400, 600))
        # Set the central widget of the Window.

        
        button = wid.QPushButton("Finalize!")
        button.clicked.connect(self.single_run)

        button1 = wid.QPushButton("Run For All Features!")
        button1.clicked.connect(self.all_features)


        label1 = wid.QLabel("Get the Directory")
        label1.setAlignment(core.Qt.AlignHCenter)
        label2 = wid.QLabel("What do you want the x axis to represent")
        label2.setAlignment(core.Qt.AlignHCenter)
        label3 = wid.QLabel("What do you want the y axis to represent")
        label3.setAlignment(core.Qt.AlignHCenter)

        label4 = wid.QLabel("Feature Space List")
        label4.setAlignment(core.Qt.AlignHCenter)
        label5 = wid.QLabel("Descirptor List")
        label5.setAlignment(core.Qt.AlignHCenter)
        label6 = wid.QLabel("Actionable List")
        label6.setAlignment(core.Qt.AlignHCenter)
        label7 = wid.QLabel("Grid Tuple")
        label7.setAlignment(core.Qt.AlignHCenter)

        label8 = wid.QLabel("Original Data Inputted")
        label8.setAlignment(core.Qt.AlignHCenter)


        entry1 = wid.QLineEdit("DirectoryData")
        entry1.setAlignment(core.Qt.AlignHCenter)

        entry2 = wid.QLineEdit("1")
        entry2.setAlignment(core.Qt.AlignHCenter)

        entry3 = wid.QLineEdit("0")
        entry3.setAlignment(core.Qt.AlignHCenter)

        entry4 = wid.QLineEdit("[[1,2,3],[1,2,3],[1,2,3]]")
        entry4.setAlignment(core.Qt.AlignHCenter)

        entry5 = wid.QLineEdit("[0,0,1]")
        entry5.setAlignment(core.Qt.AlignHCenter)

        entry6 = wid.QLineEdit("[0,0,1]")
        entry6.setAlignment(core.Qt.AlignHCenter)

        entry7 = wid.QLineEdit("[3,3]")
        entry7.setAlignment(core.Qt.AlignHCenter)

        entry8 = wid.QLineEdit("[1,2,3,700]")
        entry8.setAlignment(core.Qt.AlignHCenter)



        labelOutput = wid.QLabel("OUTPUT")
        labelOutput.setAlignment(core.Qt.AlignHCenter)

        layout = wid.QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button1)
        layout.addWidget(label1)
        layout.addWidget(entry1)
        layout.addWidget(label2)
        layout.addWidget(entry2)
        layout.addWidget(label3)
        layout.addWidget(entry3)
        layout.addWidget(label4)
        layout.addWidget(entry4)
        layout.addWidget(label5)
        layout.addWidget(entry5)
        layout.addWidget(label6)
        layout.addWidget(entry6)
        layout.addWidget(label7)
        layout.addWidget(entry7)
        layout.addWidget(label8)
        layout.addWidget(entry8)
        layout.addWidget(labelOutput)
        

        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

        self.entryone = entry1
        self.entrytwo = entry2
        self.entrythree = entry3
        self.entryfour = entry4
        self.entryfive = entry5        
        self.entrysix = entry6
        self.entryseven = entry7
        self.entryeight = entry8


        
    def single_run(self):
        print(self.entryone.text())


    def manualchange(self):
        pass


    def all_features(self):

        userInput = [float(i) for i in self.entryeight.text().replace("[","").replace("]","").split(",")]
        DescriptorList = [int(i) for i in self.entryfive.text().replace("[","").replace("]","").split(",")]
        featureSpaceLists = self.manualchange(self.entryfour.text())

        print(featureSpaceLists)
        print(type(featureSpaceLists))

        #Get whether if the conditions are actionable or not.
        actionable = [int(i) for i in self.entrysix.text().replace("[","").replace("]","").split(",")]
        iteration = 100


        whatx = self.entrytwo.text()
        whaty = self.entrythree.text()
        if whatx.isdigit():
            whatx = int(whatx)
        
        if whaty.isdigit():
            whaty = int(whaty)

        #Create empty grid. 
        gridstats = self.entryseven.text().replace("[","").replace("]","").split(",")
        gridstats[0] = int(gridstats[0])
        gridstats[1] = int(gridstats[1])
        
        gridstats.extend([whatx,whaty])
        #Create some test individuals. 

        mutationRate = 0.05
        Model = deeplearningmodelGoodCopy.modelReader(len(userInput))
        Model.createModel("Data\default_of_credit_card_clients.csv")
        runner = mapelitetestGoodCopy.MapEliteRunner(mutationRate,  gridstats,  "Data\default_of_credit_card_clients.csv", Model, userInput,  DescriptorList,  featureSpaceLists,actionable)
        result = runner.run(iteration)
        # runner.runAllCombinations()
        self.make_shortcut_file(userInput,DescriptorList, featureSpaceLists,actionable,gridstats,iteration)
    
        self.subsite = OutputWindow(result)
        self.subsite.show()

        



    def make_shortcut_file(self, uI, dL, fSL, actionable, gS,iteration):
        with open("shortcut.txt","w") as shortcutFile:
            shortcutFile.write(uI+"\n"+dL+"\n"+fSL+"\n"+actionable+"\n"+gS+"\n"+iteration)
        



        

class SettingsScreen(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(800,600))

        label1 = wid.QLabel("Get the Directory Of The Premade File. The data is stored as: \n UserInput, DescriptorList, FeatureSpaceList,actionableList,GridStatus, iterations, \n all seperated by new lines. ")
        label1.setAlignment(core.Qt.AlignHCenter)

        entry1 = wid.QLineEdit("X")
        entry1.setAlignment(core.Qt.AlignHCenter)
        self.entry = entry1

        buttonSave = wid.QPushButton("Save")
        buttonSave.clicked.connect(self.saveSettings)   

        layout = wid.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(entry1)
        layout.addWidget(buttonSave)


        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)

        def saveSettings(self):
            with open("settings.txt","w") as settingsFile:
                pass

class ChosenLoadFile(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(800,600))

        label1 = wid.QLabel("Get the Directory Of The Premade File. The data is stored as: \n UserInput, DescriptorList, FeatureSpaceList,actionableList,GridStatus, iterations, \n all seperated by new lines. ")
        label1.setAlignment(core.Qt.AlignHCenter)

        entry1 = wid.QLineEdit("X")
        entry1.setAlignment(core.Qt.AlignHCenter)
        self.entry = entry1

        button = wid.QPushButton("Finalize!")
        button.clicked.connect(self.button_done)

        buttonOpen = wid.QPushButton("Open File")
        buttonOpen.clicked.connect(self.openShortcut)   

        layout = wid.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(entry1)
        layout.addWidget(button)
        layout.addWidget(buttonOpen)


        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)


    def button_done(self,Param):
        print("do Calculations")
        pass
    def manualchange(self):
        pass
    def openShortcut(self):
        #try:
            path = self.entry.text()
            with open(path,"r") as shorcutFile:
                
                userInput = literal_eval(shorcutFile.readline())
                DescriptorList = literal_eval(shorcutFile.readline())
                featureSpaceLists = literal_eval(shorcutFile.readline())

                actionable = literal_eval(shorcutFile.readline())
                gridstats = literal_eval(shorcutFile.readline())
                iteration = int(shorcutFile.readline())

                datalink = shorcutFile.readline()

                #Create empty grid. 
                
                #Create some test individuals. 

                mutationRate = 0.05
                Model = deeplearningmodelGoodCopy.modelReader(len(userInput))
                Model.createModel(datalink)

                runner = mapelitetestGoodCopy.MapEliteRunner(mutationRate,  gridstats,  "Data\default_of_credit_card_clients.csv", Model, userInput,  DescriptorList,  featureSpaceLists,actionable)
                result = runner.run(iteration, "3x128, dropout", showGrid=False)


                self.subsite = OutputWindow(result)
                self.subsite.show()
        #except:
            print("Error Has Occured, Try New Path")



    
class DialogWindow(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(800,600))
        
        label1 = wid.QLabel("Do You Have A File To Load Data From?")
        label1.setAlignment(core.Qt.AlignHCenter)


        buttonyes = wid.QPushButton("Yes!")
        buttonyes.clicked.connect(self.yes_clicked)
        buttonno = wid.QPushButton("No!")
        buttonno.clicked.connect(self.no_clicked)

        layout = wid.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(buttonyes)
        layout.addWidget(buttonno)

        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)


    def yes_clicked(self,param):
        self.subwindow = ChosenLoadFile()
        self.subwindow.show()
    def no_clicked(self,param):
        self.subwindow = MainWindow()
        self.subwindow.show()
    


class OutputWindow(wid.QMainWindow):
    def __init__(self, dataoutput):
        super().__init__()
        self.data = dataoutput
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(800,600))
        self.selected = 1


        layout = wid.QGridLayout()

        submitbutton = wid.QPushButton("Learn More")
        submitbutton.clicked.connect(self.ClickedInfo)

        labelx = wid.QLabel("Do You Have A File To Load Data From?")
        labely = wid.QLabel("Do You Have A File To Load Data From?")


        


        self.buttons = {}

        counterx = 0

        for i in self.data:
            countery = 0

            for j in i:
                tempButton = wid.QRadioButton(self)
                if j == None:
                    text = "None"
                    tempButton.setText(text)
                else:
                    tempButton.setText(str(j.fitness[0]))
                tempButton.toggled.connect(lambda _, p=j: self.select(p))
                layout.addWidget(tempButton, countery,counterx)
                countery += 1
            counterx += 1
        
        layout.addWidget(labelx,countery,counterx + 1)
        layout.addWidget(labely,countery,counterx + 2)
        layout.addWidget(submitbutton,countery,counterx + 2)



        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)
        


    def select(self,param):
        print(self.buttons)
        print(param)

        self.selected = param
        
        print("trigger")
        print(self.selected)

    

    def ClickedInfo(self,param):
        print(self.selected)

        self.subwindow = SingleInfoScreen(self.selected)
        self.subwindow.show()


    

class SingleInfoScreen(wid.QMainWindow):
    def __init__(self,singleCF):
        self.data = singleCF

        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(800,600))

        label1 = wid.QLabel(str(singleCF))
        label1.setAlignment(core.Qt.AlignHCenter)
        layout = wid.QVBoxLayout()
        layout.addWidget(label1)
        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)


    
application = wid.QApplication(sys.argv)

window = DialogWindow()
window.show() 
application.exec()