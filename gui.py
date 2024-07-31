import PyQt5
import PyQt5.QtWidgets as wid
import PyQt5.QtCore as core

import deeplearningmodelGoodCopy
import mapelitetestGoodCopy
import sys



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

        entry8 = wid.QLineEdit("[1,2,3]")
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

    def all_features(self):

        userInput = [float(i) for i in self.entryeight.text().replace("[","").replace("]","").split(",")]
        DescriptorList = [int(i) for i in self.entryfive.text().replace("[","").replace("]","").split(",")]
        featureSpaceLists = self.entryfour.text().replace("[","").replace("]","").split(",")
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
        runner.run(iteration)
        # runner.runAllCombinations()





    def make_shortcut_file(self):
        pass

        


class ChosenLoadFile(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(400, 300))

        label1 = wid.QLabel("Get the Directory Of The Premade File")
        label1.setAlignment(core.Qt.AlignHCenter)

        entry1 = wid.QLineEdit("X")
        entry1.setAlignment(core.Qt.AlignHCenter)

        button = wid.QPushButton("Finalize!")
        button.clicked.connect(self.button_done)

        layout = wid.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(entry1)
        layout.addWidget(button)

        window = wid.QWidget()
        window.setLayout(layout)

        self.setCentralWidget(window)


    def button_done(self,Param):
        print("do Calculations")
        pass


    
class DialogWindow(wid.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setFixedSize(core.QSize(400, 300))
        
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
    



application = wid.QApplication(sys.argv)

window = DialogWindow()
window.show() 
application.exec()