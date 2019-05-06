#!/usr/bin/python2
import sys
import numpy as np


# In[4]:


def divider_of_evalues(file, factor, column_of_evalue=1):
        f = open(file)
        for line in f:
            list_of_columns = line.rstrip().split()
            list_of_columns[column_of_evalue] = float(list_of_columns[column_of_evalue]) / factor
            print(list_of_columns)


# In[5]:


if __name__ == "__main__":
    
    input_file = sys.argv[1]
    dividing_factor = float(sys.argv[2])
    column_of_evalue = 1
    if len(sys.argv) > 3:
        column_of_evalue = int(sys.argv[3]) - 1
        print("The last thing to pecify is the column in which there is the e-value, in human form not python one.")
    divider_of_evalues(input_file, dividing_factor) 

