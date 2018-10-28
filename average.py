import numpy as np
import matplotlib.pyplot as plt
import random

mu = 5
sigma = 1
# To repeat experiment 100 times
for i in range(100):
    n = np.random.normal(mu,sigma,size = 1000)
    n_random_100 = random.sample(list(n),100)
    p = np.random.poisson(mu,size = 1000)
    p_random_100 = random.sample(list(n),100)
    x = []
    for j  in range(100):
        x.append((p_random_100[j]+n_random_100[j])/2)    
    np.savetxt("Data_points/Average/"+str(i+1)+'Data.csv',x,delimiter=',')
    plt.hist(x,density=True)
    plt.ylabel('Probability')
    plt.xlabel('X')
    plt.title('Average points histogram '+str(i+1))
    plt.savefig('Graphs/Average/Average_graph'+str(i+1)+'.png')
    plt.show()
    plt.close()
