### __We reinforced our learning of get requesting an API by developing the jokes program with command line argument with a first and a last name.__

### _Jupiter notebooks_
1.	You have to run ‘jupyter notebook’ at the prompt to open a http browser to reflect the current workspace
2.	Click new and python 3
3.	Everything is in a cell and there are two modes – edit(green) and control(blue) mode
4.	Pressing B creates a new cell in control mode
5.	Pressing A creates a new cell in control mode above the original cell.
6.	Markdown removes the prefix In
7.	M for markdown
8.	And y for code cell
9.	Press ctrl + shift +P to see all the commands 
10.	Pressing shift + enter would run the python code
11.	Pressing d twice in control mode deletes the cell.
12.	Kernel > Restart & run all
13.	Please note that the cell should be in a chronological order.
14.	Do not use the jupyter notebook inside the vs code
15.	Panda is a library that is usually used with jupyter
![Please refer to this site for additional Jupyter commands and shortcuts] (https://www.cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf/)
    1. 	3 key data structure
        1. Series – one dimensional data structure
        2. Data frame – 2-dimensional data structure
        3. Panel – 3-dimensional data structure

## __Series__
1. Import pandas as pd or can be left blank, we would have to use s0 =panda.
2. import pandas as pd

### Example

    names = ("First", "Second", "Third")

    a = (1,2,3)

    b = [4,5,6]

    c = {"Seventh":7,'Eigth':8,"Ninth":9}

    s0 = pd.Series(a) # index defaults to 0,1,2,...

    s1 = pd.Series(a, index=names)

    s2 = pd.Series(b, names)  # index= is implied 

    if second argument is present. 

    s3 = pd.Series(b, names, dtype='float32')  # 

    ### Here we can also set datatype

    s4 = pd.Series(b, names)

    s5 = pd.Series(c) #

3.	Iteration is possible in series.
4.	Matplotlib inline used in creating graphs
5.	Series is very much like dictionary
6.	We can use get to check the existence. Returns none if null>

### __Data frames__ 
1. are series of series
2.	each series becomes a row
3.	Indexes and columns
4.	The initial series if it contains character automatically converts into column heading
5.	Df.index reflects the ranges a of 
6.	Df.set_index(‘one’)
7.	Df[“three”] = def[‘one’]*df[‘two’]  creates a new column
8.	Del df[‘one’] Df-- display
9.	Df.pop 
10.	Df2[‘two’] = df[‘two’] * df[‘two’].mean()
11.	Df2 = pd.dataframe()  creation of new dataframe

#### __Quandle is a library for financial data__
#### Commands
1. Conda install quandl
2. Conda update jupyter
3. ZACKS/SERV – is a service that handles major published financial data.
4. Qopts is creating a dictionary which contains the list of items
5.  Panda data frames allows the use of ‘.’ Instead of []
6. [Matplotlib](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html)
7. [Descriptive](https://www.math.ubc.ca/~pwalls/math-python/scipy/matplotlib/)
