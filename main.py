#MapPlot.py
#Name: Colton Janes
#Date: 04/20/2025
#Assignment: Lab10

#Decision Set: https://corgis-edu.github.io/corgis/python/cancer/
#Help reference: https://www.w3schools.com/python/pandas/pandas_plotting.asp

import cancer
import pandas as pd
import matplotlib.pyplot as plt

cancer_reports = cancer.get_cancer_reports()

#states = []
bCancer_deaths = [] #breast cancer deaths, rate per 100,000 population
cCancer_deaths = [] #colorectal cancer deaths, rate per 100,000 population
lCancer_deaths = [] #lung cancer deaths, rate per 100,000 population

for report in cancer_reports:
    #state = cancer_deaths["State"]
    breastC_deaths = report["Types"]["Breast"]["Total"]
    colorectalC_deaths = report["Types"]["Colorectal"]["Total"]
    lungC_deaths = report["Types"]["Lung"]["Total"]
    
    #states.append(state)
    bCancer_deaths.append(breastC_deaths)
    cCancer_deaths.append(colorectalC_deaths)
    lCancer_deaths.append(lungC_deaths)

df = pd.DataFrame({
    "Breast": bCancer_deaths,
    "Colorectal": cCancer_deaths,
    "Lung": lCancer_deaths
})

avg_deaths = df.mean() #I need average deaths per cancer type, listed in above df

plot_df = pd.DataFrame({
    "Cancer Type": avg_deaths.index,
    "Avg Deaths per 100k": avg_deaths.values
})

ax = plot_df.plot(kind="bar", x="Cancer Type", y="Avg Deaths per 100k", legend=False)
ax.set_ylabel("Avg Deaths per 100,000")
ax.set_xlabel("Cancer Types")
ax.set_title("Average Cancer Death Rate by Type (US States, 2007-2013)")
ax.set_xticklabels(plot_df["Cancer Type"], rotation=0)  #x labels were vertical and cut off before; making horizontal

plt.savefig("AVG Cancer Death Rate by Type in US - 2007-2013")