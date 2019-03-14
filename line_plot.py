import matplotlib.pyplot as plt

x=[8,4,13,10,7]
y=[2,50,6,9,5]

plt.plot(x,y,color='b',label='line')
plt.legend()
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Line Plot")
plt.show()
