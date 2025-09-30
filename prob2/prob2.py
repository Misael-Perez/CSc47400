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

Food_AND_Dairy= pd.concat([data94_98,data07_08])
print(Food_AND_Dairy)
#Something useful I learned. outside of data camp is melt command. We need to make a gender/sex column make it easier to plot.
Food_AND_Dairy=Food_AND_Dairy.melt(id_vars=["Food","Timeline"], value_vars=["Men's Mean","Women's Mean"],var_name="Gender/Sex",value_name="Mean")
Food_AND_Dairy["Gender/Sex"]=Food_AND_Dairy["Gender/Sex"].str.replace("'s Mean","")
Improved_table= Food_AND_Dairy.pivot_table(index=["Food","Gender/Sex"],columns="Timeline", values="Mean").reset_index()

print(Improved_table)
Improved_table["Change"]= ((Improved_table["2007-08"] - Improved_table["1994-98"]) / Improved_table["1994-98"]) * 100
print(Improved_table)
Improved_table["Food"]=Improved_table["Food"].str.strip()

#Only fruits and Dairy products
Products= Improved_table[Improved_table["Food"].isin(Fruit_Types + Dairy_Products)]
#Now to order the product into groups
Order= Fruit_Types + [""] + Dairy_Products



Men= Products[Products["Gender/Sex"]=="Men"]
Men=Men.set_index("Food").reindex(Order).reset_index()

Women= Products[Products["Gender/Sex"]=="Women"]
Women=Women.set_index("Food").reindex(Order).reset_index()
print(Men)
print(Women)
#Bar graph for the men
plt.figure(figsize=(15,10))
plt.subplots_adjust(bottom=0.20)
plt.bar(Men["Food"],Men["Change"],width=0.6)
plt.title("Percent Increase or Decrease")
plt.ylabel("Change")
plt.xticks(rotation=45,ha="right")
plt.show()

#Bar graph for the Women
plt.figure(figsize=(15,10))
plt.subplots_adjust(bottom=0.20)
plt.bar(Women["Food"],Women["Change"],width=0.6)
plt.title("Percent Increase or Decrease")
plt.ylabel("Change")
plt.xticks(rotation=45,ha="right")
plt.show()