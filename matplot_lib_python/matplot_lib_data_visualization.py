#matpolt to create low level graphs 
import matplotlib.pyplot as plt
import numpy as np
x_axis= [1,2,3,4,5]
y_axis = np.array([6,3,7,5,1])
# plt.plot(x_axis,y_axis)
# plt.show()
plt.title("Stock Market")
# plt.xlabel("average buying price")
# plt.ylabel("average selling price")
# plt.plot(x_axis,y_axis,marker="o",color="r",linestyle="-")
# plt.grid()
# plt.subplot(1,4,2)
# plt.barh(x_axis,y_axis,color="g")
# plt.show()
ly_labels = ["apple","tesla","google","microsoft","amazon"]
plt.pie(y_axis,labels=ly_labels,autopct="%1.1f%%")
plt.legend(loc="lower left")
# plt.show()
# plt.hist(y_axis,bins=5)
# plt.show()


#assignment #explode shadow change colors in pie chart 
#create hist graph 