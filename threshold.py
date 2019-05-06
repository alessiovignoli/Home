#!/usr/bin/python

#testing the threshold within negative and positive results hits
#compuing and comparing the hits of blast with the threshold, and separating them with being positive and negative;
#on the first line of the matrix, we have the separation within true negative e false negative, then on the second line false positive and true 

import sys
import numpy as np

def conf_mat(filename,th,sp=-2,cp=-1):  #score position, class position, to call the function even if variable is in a different position
    cm = [[0.0,0.0],[0.0,0.0]]        #confusion matrix, position [0][0] is KUNITZ, position [1][1] is NOT KUNITZ, position [0][1] kunitz predicted as non kunitz FALSE POSITIVE, [1][0] predicted as kunitz, but not really are kunitz, so FALSE NEGATIVE.
    f = open(filename)
    for line in f:
        v = line.rstrip().split() #first column is the identifier, separating by space, and stripping the last element of the line
        if int(v[cp])==1: i=0     #KUNITZ DOMAIN, but we want that in the first row, so inverting the index
        if int(v[cp])==0: i=1     #NON KUNITZ DOMAIN, we wnat that in the second row
        if float(v[sp])<th:
            j=0                        #POSITIVE, first column, predicted as positive
        else:
            j=1                   #negative, second column, predicted as negative
                                 #now adding element in the matrix: 
        cm[i][j]= cm[i][j]+1 
    return cm


def print_performance(cm):
    tp=cm[0][0] 
    tn=cm[1][1]
    fp=cm[0][1]
    fn=cm[1][0]
    acc=(tp+tn)/(tp+fn+tn+fp) 
    mc=((tp*tn)-(fp*fn))/(np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)))
    tpr=(tp)/(tp+fn)
    fpr=(fp)/(fp+tn)
    

#TPR(truepositiverate)=TP/TP+FN(totalpositive)
#FPR(falsepositiverate)=FP/FP+TN(totalnegative)
#according on the definition of the matrix, the positive are the second row of my matrix so p, and the negative are the sum of the first row so n. 
    
    print str(fpr)+"\t"+str(tpr)
    #print('Q2', acc, 'MCC', mc)
#computing the accuracy of the prediction, to set a good threshold (you could run it several times to check the threshold, and in case choose the optimal one)

#getting random nymbers from numpy --> numpy.random

if __name__ == "__main__":
    filename = sys.argv[1]
    th = float(sys.argv[2])
    sp=-2     #scoreposition
    if len(sys.argv)>3: sp=int(sys.argv[3])-1
    cm= conf_mat(filename,th)
    #print cm 
    print_performance(cm)
