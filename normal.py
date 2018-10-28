import numpy as np
import matplotlib.pyplot as plt


mu = 5#mean
sigma = 1#std deviation
for i in range(3):
        normal_array = np.random.normal(mu,sigma,size=1000)
        np.savetxt("Data_points/Normal/"+str(i+1)+'Data.csv',normal_array,delimiter=',')
        plt.ylabel('Probability')
        plt.xlabel('X')
        plt.title('Random normal samples histogram '+str(i+1))
        plt.hist(normal_array,density = True)
        plt.savefig('Graphs/Normal/normal_graph'+str(i+1)+'.png')
        plt.show()
        plt.close()
