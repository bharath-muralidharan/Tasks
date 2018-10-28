import numpy as np
import matplotlib.pyplot as plt


#Random poisson samples histogram
for i in range(3):
    poisson_array = np.random.poisson(lam = 5,size = 1000)
    np.savetxt("Data_points/Poisson/"+str(i+1)+"Data.csv",poisson_array,delimiter=',')
    plt.ylabel('Probability')
    plt.xlabel('X')
    plt.title('Random poisson sample histogram '+str(i+1))
    plt.hist(poisson_array,density=True)
    plt.savefig('Graphs/Poisson/poisson_graph'+str(i+1)+'.png')
    plt.show()
    plt.close()
