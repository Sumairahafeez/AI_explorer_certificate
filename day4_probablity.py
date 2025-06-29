
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
mew, sigma = 0, 1
x = np.linspace(-5, 5, 100)
y = 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mew)**2/(2*sigma**2))

plt.plot(x, y)
plt.title('Normal Distribution')
plt.show()
# Bernoulli distribution 
# it describes the probability of success or failure in a single trial
p = 0.5  # probability of success
plt.bar([0, 1], [1 - p, p], tick_label=['Failure', 'Success'])
plt.title('Bernoulli Distribution')
plt.show()
def Bayes_theorem(prior, likelihood, evidence):
    """
    Calculate the posterior probability using Bayes' theorem.
    
    Parameters:
    prior (float): The prior probability of the hypothesis.
    likelihood (float): The likelihood of the evidence given the hypothesis.
    evidence (float): The total probability of the evidence.
    
    Returns:
    float: The posterior probability of the hypothesis given the evidence.
    """
    return (prior * likelihood) / evidence
