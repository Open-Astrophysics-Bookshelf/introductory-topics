import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
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


mu = 0.0
sigma = 1.0

rv = norm(loc=mu,scale=sigma)
x = np.linspace(-5.0,5.0,200)
y = rv.pdf(x)

x0,x1,y0,y1 = set_boundaries(x,y)
plt.xlim(x0,x1)
plt.ylim(y0,y1)

# some sizing to make the plot look nice
charsize = 10   # points
major_ticklength = 0.6*charsize
major_tickwidth = 0.9   # points
minor_ticklength = 0.3*charsize
minor_tickwidth = 0.7   # points
plt.tight_layout()

plt.tick_params(axis='both',\
    length=major_ticklength, width=major_tickwidth,which='major',labelsize=10)
plt.tick_params(axis='both',\
    length=minor_ticklength,width=minor_tickwidth,which='minor',labelsize=8)

plt.ylabel(r'$p(x)$',fontsize=charsize)
plt.xlabel(r'$x/\sigma$',fontsize=charsize)

plt.plot(x,y,linestyle='-',linewidth=2.0,solid_capstyle='round',\
    solid_joinstyle='miter',color='k')

plt.fill_between(x, 0.0, y, where=(np.abs(x)<2.0), facecolor='0.4',edgecolor='none')
plt.fill_between(x, 0.0, y, where=(np.abs(x)<1.0), facecolor='0.6',edgecolor='none')

plt.savefig('sigma.pdf',format='pdf')
