# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 17:52:17 2022

@author: Aswathi
"""
import pandas as pd
import matplotlib.pyplot as plt



df =pd.read_csv(r'Dataset.csv')


def lineplot():
    f= plt.figure()
    f.set_figwidth(9)
    f.set_figheight(4)
    
    plt.plot(df.Brand,df.TopSpeed,label="Top Speed(Km/h)")
    plt.plot(df.Brand,df.FastCharge,label="Fast Charging(Km/h)")
    plt.legend()
    plt.show()




def barplot():
    f=plt.figure()
    f.set_figwidth(9)
    f.set_figheight(4)
    f=plt.bar(df.Brand,df.TopSpeed)
    plt.show()

   


def histogramplot():
    df =pd.read_csv(r'Dataset_2.csv')
    f=plt.figure()
    f.set_figwidth(12)
    f.set_figheight(4)
    f=plt.hist(df.Brand)
    plt.xticks(rotation=45) #To avoid overlapping in axis
    plt.show()
    
lineploting()  
barplot() 
histogramplot()    
