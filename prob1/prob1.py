import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import FileLink,display
#checking the sheet names first

file= pd.ExcelFile("Appendix B (shares).xls")
print(file.sheet_names)

File=pd.read_excel("Appendix B (shares).xls", sheet_name=["94-98 FAH","03-04 FAH","05-06 FAH","07-08 FAH"], header=76,nrows=64, usecols="A,H,K")

data94_98= File["94-98 FAH"]
data94_98.columns=["Food","Men's Mean","Women's Mean"]
print(data94_98)
data03_04= File["03-04 FAH"]
data03_04.columns=["Food","Men's Mean","Women's Mean"]
data05_06= File["05-06 FAH"]
data05_06.columns=["Food","Men's Mean","Women's Mean"]
data07_08= File["07-08 FAH"]
data07_08.columns=["Food","Men's Mean","Women's Mean"]

Fruit_Types=["Apples as fruit","Bananas","Berries","Grapes","Melons","Oranges, Total","Other citrus fruit","Stone fruit","Tropical fruit"]

Dairy_Products=["Fluid milk total","Butter","Cheese","Yogurt","Dairy, Other"]
#It is time to combine all of them into one big table. We need to add a column that will tell us what time period it is from.
data94_98["Timeline"]="1994-98"
data03_04["Timeline"]="2003-04"
data05_06["Timeline"]="2005-06"
data07_08["Timeline"]="2007-08"

#Time to combine

Food_AND_Dairy= pd.concat([data94_98,data03_04,data05_06,data07_08])
print(Food_AND_Dairy)
#Something useful I learned. outside of data camp is melt command. We need to make a gender/sex column make it easier to plot.
Food_AND_Dairy=Food_AND_Dairy.melt(id_vars=["Food","Timeline"], value_vars=["Men's Mean","Women's Mean"],var_name="Gender/Sex",value_name="Mean")
Food_AND_Dairy["Gender/Sex"]=Food_AND_Dairy["Gender/Sex"].str.replace("'s Mean","")
print(Food_AND_Dairy)
#Finally it is CLEAN
LineStyle=["-","--","-.",":"]
Marker=["o","s","D","v"]



MEN_only= Food_AND_Dairy[Food_AND_Dairy["Gender/Sex"]=="Men"]

MEN_only["Food"]=MEN_only["Food"].str.strip()
plt.figure(figsize=(12,6))
for i,fruit in enumerate(Fruit_Types):
    data= MEN_only[MEN_only["Food"]==fruit]
    style=LineStyle[i % len(LineStyle)]
    marker=Marker[i % len(Marker)]
    plt.plot(data["Timeline"],data["Mean"], marker=marker, linestyle=style,label=fruit)

plt.subplots_adjust(bottom=0.20)
plt.title("Men Fruits")
plt.xlabel("Timeline")
plt.ylabel("Means")
plt.figtext(0.5, 0.02, "*Figure 1: It seems like the only fruit that is getting less brought/eaten is Other citrus fruit. Other than that, the stone fruit look like the favorite of the population in recent years. \n Source: https://www.ers.usda.gov/publications/pub-details?pubid=81817",wrap=True, ha="center", fontsize=10)
plt.legend()
plt.show()


plt.figure(figsize=(12,6))
for i,dairy in enumerate(Dairy_Products):
    data= MEN_only[MEN_only["Food"]==dairy]
    style=LineStyle[i % len(LineStyle)]
    marker=Marker[i % len(Marker)]
    plt.plot(data["Timeline"],data["Mean"], marker=marker, linestyle=style,label=dairy)

plt.subplots_adjust(bottom=0.20)
plt.title("Men Dairy")
plt.xlabel("Timeline")
plt.ylabel("Means")
plt.figtext(0.5, 0.02, "*Figure 2: With the dairy products, cheese is being eaten less over the years. Yogurt is pretty popular and has stayed popular over the years.. \n Source: https://www.ers.usda.gov/publications/pub-details?pubid=81817",wrap=True, ha="center", fontsize=10)
plt.legend()
plt.show()


Women_only= Food_AND_Dairy[Food_AND_Dairy["Gender/Sex"]=="Women"]
#Women Fruit
Women_only["Food"]=Women_only["Food"].str.strip()
plt.figure(figsize=(12,6))
for i,fruit in enumerate(Fruit_Types):
    data= Women_only[Women_only["Food"]==fruit]
    style=LineStyle[i % len(LineStyle)]
    marker=Marker[i % len(Marker)]
    plt.plot(data["Timeline"],data["Mean"], marker=marker, linestyle=style,label=fruit)

plt.subplots_adjust(bottom=0.20)
plt.title("Women Fruits")
plt.xlabel("Timeline")
plt.ylabel("Means")
plt.figtext(0.5, 0.02, "*Figure 3: Just like the men, the stone fruit is being eaten along with the bananas. The Other citrus fruit seem to be the only one getting less popular. But at the 2007-08, it seems to be raising and grow even more in popularity in the coming years. \n Source: https://www.ers.usda.gov/publications/pub-details?pubid=81817",wrap=True, ha="center", fontsize=10)
plt.legend()
plt.show()

#Dairy products now
plt.figure(figsize=(12,6))
for i,dairy in enumerate(Dairy_Products):
    data= Women_only[Women_only["Food"]==dairy]
    style=LineStyle[i % len(LineStyle)]
    marker=Marker[i % len(Marker)]
    plt.plot(data["Timeline"],data["Mean"], marker=marker, linestyle=style,label=dairy)

plt.subplots_adjust(bottom=0.20)
plt.title("Women Dairy")
plt.xlabel("Timeline")
plt.ylabel("Means")
plt.figtext(0.5, 0.02, "*Figure 4: With the dairy products over the years. Yogurt is pretty popular and . \n Source: https://www.ers.usda.gov/publications/pub-details?pubid=81817",wrap=True, ha="center", fontsize=10)
plt.legend()
plt.show()

