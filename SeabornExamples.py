# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 16:45:03 2017

@author: Dih Negretto
"""

""" Exemplo de utilização do Seaborn """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

    
print("1 - Classic plot")
print("2 - Histogram")
print("3 - KDE (Kernel Density Estimation)")
print("4 - Histogram and KDE")
print("5 - 2D KDE Plot")
print("6 - Joint Plot")
print("7 - Pair Plots usando o Iris Dataset")
print("8 - Faceted Histograms usando Tips Dataset")
print("9 - Factor Plots usando Tips Dataset")
print("10 - Joint Distributions usando Tips Dataset")
print("11 - Bar Plots usando Planets Dataset")
print("12 - Bar Plots usando Planets Dataset (outro exemplo)")
    
opcao = input("Escolha uma opcao: ")

data = np.random.multivariate_normal([0,0], [[5,2],[2,2]], size=2000)
data = pd.DataFrame(data, columns=["x","y"]) 
    
if opcao == "1":  
    # Create some data
    rng = np.random.RandomState(0)
    x = np.linspace(0, 10, 500)
    y = np.cumsum(rng.randn(500, 6), 0)
    # Plot básico com Matplot         
    #plt.plot(x,y)
    #plt.legend("ABCDEF", ncol=2, loc="upper-left")
       
    # Plot básico com Seaborn     
    sns.set()
    plt.plot(x,y)
    plt.legend("ABCDEF", ncol=2, loc="upper left")
        
elif opcao == "2":    
    for col in "xy":
        plt.hist(data[col], normed=True, alpha=0.5)

elif opcao == "3":
    for col in "xy":
        sns.kdeplot(data[col], shade=True)
        
elif opcao == "4":
    sns.distplot(data["x"])
    sns.distplot(data["y"])        

elif opcao == "5":
    sns.kdeplot(data)    
        
elif opcao == "6":
      with sns.axes_style("white"):
          #sns.jointplot("x","y", data, kind="kde")
          sns.jointplot("x","y", data, kind="hex")

elif opcao == "7":
    iris = sns.load_dataset("iris")
    print(iris.head())
    sns.pairplot(iris, hue="species", size=2.5)

elif opcao == "8":
    tips = sns.load_dataset("tips")
    print(tips.head())
    tips["tip_pct"] = 100 * tips["tip"] / tips["total_bill"]
    grid = sns.FacetGrid(tips, row="sex", col="time", margin_titles=True)
    grid.map(plt.hist, "tip_pct", bins=np.linspace(0,40,15))

elif opcao == "9":
    tips = sns.load_dataset("tips")
    print(tips.head())
    with sns.axes_style(style="ticks"):
        g = sns.factorplot("day", "total_bill", "sex", data=tips, kind="box")
        g.set_axis_labels("Day", "Total Bill")

elif opcao == "10":
    tips = sns.load_dataset("tips")
    with sns.axes_style("white"):
        #sns.jointplot("total_bill", "tip", data=tips, kind="hex")
        sns.jointplot("total_bill", "tip", data=tips, kind="reg")

elif opcao == "11":
    planets = sns.load_dataset("planets")
    print(planets.head())
    with sns.axes_style("white"):
        g = sns.factorplot("year", data=planets, aspect=2, kind="count",
                           color="steelblue")
        g.set_xticklabels(step=5)
        
elif opcao == "12":
    planets = sns.load_dataset("planets")
    with sns.axes_style("white"):
        g = sns.factorplot("year", data=planets, aspect=4.0, kind="count",
                           hue="method", order=range(2001,2015))
        g.set_ylabels("Number of Planets Discovered")
    
    
    
    
    