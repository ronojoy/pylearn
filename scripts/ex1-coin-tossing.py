import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt

# N throws of a coin with parameter theta0
N, theta0 = 10, 0.5

# data contains the outcome of the trial
data = stats.bernoulli.rvs(p = theta0, size = N)
theta = np.linspace(0, 1, 128)

nthrow = [0, 1, 2, 3, 4, 5, 8, 16, 32, N]

for k, n in enumerate(nthrow):
   
   # number of heads
   heads = data[:n].sum()
   # posterior probability with conjugate prior
   p = stats.beta.pdf(theta, 1 + heads, 1 + n - heads)

   # plot the posterior
   sx = plt.subplot(len(nthrow) / 2, 2, k + 1)
   plt.setp(sx.get_yticklabels(), visible=False)
   plt.plot(theta, p, label="tosses %d \n heads %d " % (n, heads))
   plt.fill_between(theta, 0, p, color="#348ABD", alpha=0.4)
   plt.vlines(theta0, 0, 4, color="k", linestyles="--", lw=1)
   leg = plt.legend()
   leg.get_frame().set_alpha(0.4)
   plt.autoscale(tight=True)

plt.tight_layout()
