
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

x = np.linspace(-9.0,9.0,200)

x0,x1,y0,y1 = set_boundaries(x,[0.0,0.4])
plt.xlim(x0,x1)
plt.ylim(y0,y1)

# some sizing to make the plot look nice
charsize = 12   # points
labelsize=10
major_ticklength = 0.6*labelsize
major_tickwidth = 0.9   # points
minor_ticklength = 0.3*labelsize
minor_tickwidth = 0.7   # points
plt.tight_layout(pad=1.2)

plt.tick_params(axis='both',\
    length=major_ticklength, width=major_tickwidth,which='major',labelsize=labelsize)
plt.tick_params(axis='both',\
    length=minor_ticklength,width=minor_tickwidth,which='minor',labelsize=8)

plt.ylabel(r'$p(x;\mu,\sigma)$',fontsize=charsize)
plt.xlabel(r'$x$',fontsize=charsize)
plt.title(r'$\mu = 0.0$',fontsize=charsize)

for sigma,clr,lns in zip([1.0,2.0,3.0],['0.5','0.3','0.1'],['-','--',':']):
    rv = norm(loc=mu,scale=sigma)
    y = rv.pdf(x)
    plt.plot(x,y,\
        linestyle=lns,linewidth=2.0,solid_capstyle='round',\
        solid_joinstyle='miter',color=clr)

plt.legend((r'$\sigma=1.0$',r'$\sigma=2.0$',r'$\sigma=3.0$'),loc='best',fontsize=labelsize)
plt.savefig('Normal_mu0.pdf',format='pdf')
plt.clf()

x = np.linspace(-4.0,6.0,200)
x0,x1,y0,y1 = set_boundaries(x,[0.0,0.4])
plt.xlim(x0,x1)
plt.ylim(y0,y1)
plt.tight_layout(pad=1.2)

plt.tick_params(axis='both',\
    length=major_ticklength, width=major_tickwidth,which='major',labelsize=10)
plt.tick_params(axis='both',\
    length=minor_ticklength,width=minor_tickwidth,which='minor',labelsize=8)

plt.ylabel(r'$p(x;\mu,\sigma)$',fontsize=charsize)
plt.xlabel(r'$x$',fontsize=charsize)
plt.title(r'$\sigma = 1.0$',fontsize=charsize)

for mu,clr,lns in zip([0.0,2.0,4.0],['0.5','0.3','0.1'],['-','--',':']):
    rv = norm(loc=mu,scale=1.0)
    y = rv.pdf(x)
    plt.plot(x,y,\
        linestyle=lns,linewidth=2.0,solid_capstyle='round',\
        solid_joinstyle='miter',color=clr)

plt.legend((r'$\mu=0.0$',r'$\mu=2.0$',r'$\mu=4.0$'),loc='best',fontsize=labelsize)
plt.savefig('Normal_sigma1.pdf',format='pdf')

