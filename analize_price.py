import pandas as pd
import matplotlib.pyplot as plt
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
path = os.path.join(__location__, "auto_ru_yamaha.csv")


titanic = pd.read_csv(path)

#print(titanic)

glides = titanic[lambda x: x["model"] == "YZF_R6"]

print(glides.groupby(["year"]).count()["price"])
print(glides.groupby(["year"]).mean())
ax1 = glides.groupby(["year"]).mean().plot()

#ax2 = glides.groupby(["year"]).count()["price"].plot.bar(rot=0)

#plt.xlim(1990, 2025)
plt.title("Yamaha YZF-R6")

plt.show()
