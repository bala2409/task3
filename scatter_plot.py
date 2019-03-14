import matplotlib.pyplot as plt

x=[8,4,13,10,7]
y=[2,50,6,9,5]
x2=[2,2,34,5,65,12]
y2=[3,12,44,53,44,11]

plt.scatter(x,y,label="scatter1",color='r',marker='x',s=10)
plt.scatter(x2,y2,label="Scatter2",color='b',marker='o',s=100)
plt.legend()
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Scatter Plot")
plt.show()
