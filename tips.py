import numpy as np
import matplotlib.pyplot as plt
import math

# part 0 - loading in the array
data = np.array([22.7, 16.3, 13.6, 16.8, 29.9, 15.9, 14.0, 15.0, 14.1, 18.1, 
                 22.8, 27.6, 16.4, 16.1, 19.0, 13.5, 18.9, 20.2, 19.7, 18.2, 
                 15.4, 15.7, 19.0, 11.5, 18.4, 16.0, 16.9, 12.0, 40.1, 19.2]) 

# part 1 - plotting the histogram for tips
plt.subplot(1, 2, 1)
plt.hist(data)
plt.title("Random sample of 30 observed tips")
plt.xlabel("number of tips")
plt.ylabel("tip ammount")

# part 2 - 95% confidence interval
conf95 = [(np.mean(data) - (1.96 * (np.std(data)/math.sqrt(30)))), (np.mean(data) + (1.96 * (np.std(data)/math.sqrt(30))))]
print("Mean is:", np.mean(data))
print("95% confidence interval is:", conf95)

# part 3 - generating samples
bst_samples = np.asarray([np.random.choice(data, 30, replace = True) for _ in range(1000)]) # generated 1000 samples
bst_means = np.around(np.mean(bst_samples, axis = 1), decimals = 3) # calculating mean with triple decimal precision

# part 4 - histogram for boostram samples
plt.subplot(1, 2, 2)
plt.hist(bst_means)
plt.title("Bootstrap sample means")
plt.xlabel("Mean")
plt.ylabel("Number of sample with mean")
plt.gcf().set_size_inches(15, 10.5)
plt.show()

# part 5 - bootstrap sample 95% confidence interval
conf95_bst = [(np.mean(bst_means) - (1.96 * (np.std(bst_means)/math.sqrt(30)))), (np.mean(data) + (1.96 * (np.std(bst_means)/math.sqrt(30))))]
print("95% confidence interval for the bootstrap samples is:", conf95_bst)

