
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson
from pylab import rcParams
rcParams['figure.figsize'] = 3,3

def set_boundaries(x,y,margin=0.05):
    width = max(x)-min(x)
    height = max(y)-min(y)
    hpad = margin*width
    vpad = margin*height
    x0 = min(x)-hpad
    x1 = max(x)+hpad
    y0 = min(y)-vpad
    y1 = max(y)+vpad
    return x0,x1,y0,y1

mu = 2.3
x = np.arange(poisson.ppf(0.01,mu),poisson.ppf(0.99,mu))
y = poisson.pmf(x,mu)

x0,x1,y0,y1 = set_boundaries(x,[0.0,0.4])
plt.xlim(x0,x1)
plt.ylim(y0,y1)

# some sizing to make the plot look nice
charsize = 10   # points
major_ticklength = 0.6*charsize
major_tickwidth = 0.9   # points
minor_ticklength = 0.3*charsize
minor_tickwidth = 0.7   # points
plt.ylabel(r'$\mathcal{P}_\lambda(m)$',fontsize=charsize)
plt.xlabel(r'$m$',fontsize=charsize)
plt.tight_layout()

plt.tick_params(axis='both',\
    length=major_ticklength, width=major_tickwidth,which='major',labelsize=10)
plt.tick_params(axis='both',\
    length=minor_ticklength,width=minor_tickwidth,which='minor',labelsize=8)

plt.plot(x,y,color='0.6',linestyle='-',linewidth=2.0,drawstyle='steps-mid')

mu = 1.2
x = np.arange(poisson.ppf(0.01,mu),poisson.ppf(0.999,mu))
y = poisson.pmf(x,mu)

plt.plot(x,y,color='k',linestyle='-',linewidth=2.0,drawstyle='steps-mid')
plt.legend((r'$\lambda=2.3$',r'$\lambda=1.2$'),loc='best',fontsize=charsize)
plt.savefig('Poisson.pdf',format='pdf')
