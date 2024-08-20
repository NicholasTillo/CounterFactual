# CounterFactual MapElite
Quality Diversity Coutnerfactual Generation Proof Of Concept

## Usage Description

##Data Preprocessing
The data must be in the form of:
| Feature Title 1 | Feature Title 2   | Feature Title 3 | Labeles |
| :-----: | :---: | :---: | :---: |
| Feature Value 1 | Feature value 2   | Feature value 3   | Corresponding Label |
| Feature Value 1 | Feature value 2   | Feature value 3   | Corresponding Label |
| Feature Value 1 | Feature value 2   | Feature value 3   | Corresponding Label |
| Feature Value 1 | Feature value 2   | Feature value 3   | Corresponding Label |

### Launching for the first time:
1. Install all the required depenancies
2. Launch the gui.py program.
3. Under the section asking if there is a premade save file, select "No"
4. For each of the sections, input the correct data.
   
| "Get the Directory"  |  "What do you want the "x or y" axis to represent   | "Feature Space List"    | Descriptor List | Actioanable List | Grid Tuple | Original Data Inputted | Number of Iterations | Optional Name |
| :-----: | :---: | :---: | :----: | :---: | :---: | :---: | :---: | :----: |
| Either a relative or absolute path to the csv that contains the preprocessed data | Choosing what each axis represents for the map elite algorithm. Basically, what do the cells represent? All options are as follows: Put the feature number to make that feature the axis.  "NumActionableChanges" , "NumInactionableChanges", "NumTotalChanges", "NumTimesMutated" | A list of lists that describe the possible domains for each of the features, can input types to describe infinite domains, (int, float)   | A list of 0's or 1's for each feature that describes if that value is Qualitative or Quantitative, 0 for Quantitative, 1 for qualitative. | A list of 0's and 1's for each feature that describes if that feature is actionable or non-actionable, 0 for non-actionable 1 for actioanble | A tuple, (must be 2 length) describing the "resolution" of the map elite grid, (x,y) | The original data value, what is the original data list that counterfactuals should be generated to solve. | Integer value desciribing the number of iterations | An optional value that will change the finalized output files to be of that name, for easier documentation |  
5. Once data is inputted, select the finalzie button
6. Wait for the 

### Launching with a premade save file:
1. Launch the gui.py program.
2. Under the section asking if you have a premade save file, select "Yes"


### Launching with a custom classifier
1. Launch the gui.py program.
2. If you have a save file describing the details of the running, select "Yes"
3. If not, select "No"

Prof. Ting Hu
Nicholas Tillo
