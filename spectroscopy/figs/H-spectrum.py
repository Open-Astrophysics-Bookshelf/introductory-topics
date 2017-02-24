import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

def wavelength(n,m):
    lam0 = (1+sc.m_e/sc.m_p)/sc.Rydberg * 1.0e9 # nm
    if n > m: n,m = m,n
    return lam0/(1/n**2 - 1/m**2)

width = 4
height = 1.2

plt.style.use('text-sans')
plt.rc('xtick',**{'direction':'out'})

Nlines = 5
greek = [r'$\alpha$',r'$\beta$',r'$\gamma$',r'$\delta$',r'$\epsilon$']

Lyman = [ wavelength(1,m) for m in range(2,2+Nlines) ]
Balmer = [ wavelength(2,m) for m in range(3,3+Nlines) ]
Paschen = [ wavelength(3,m) for m in range(4,4+Nlines) ]

plt.figure(figsize=(width,height))
plt.gca().get_yaxis().set_visible(False)
ymin,ymax = plt.ylim(0,1)
plt.xlim(20,1400)
plt.vlines(Lyman,ymin,ymax,color='0.5',linestyle='--')
plt.annotate(s=r'Lyman ($m\to 1$)',fontsize='small',xytext=(0,3),
    textcoords='offset points',xy=(Lyman[-1],0),
    va='bottom',ha='right',rotation=90)
plt.vlines(Balmer,ymin,ymax,color='0.5',linestyle=':')
plt.annotate(s=r'Balmer ($m\to 2$)',fontsize='small',xytext=(0,3),
    textcoords='offset points',xy=(Balmer[-1],0),
    va='bottom',ha='right',rotation=90)
plt.vlines(Paschen,ymin,ymax,color='0.5',linestyle='-')
plt.annotate(s=r'Paschen ($m\to 3$)',fontsize='small',xytext=(0,3),
    textcoords='offset points',xy=(Paschen[-1],0),
    va='bottom',ha='right',rotation=90)
plt.xlabel(r'$\lambda$ (nm)')
plt.savefig('H-spectrum.pdf',format='pdf',bbox_inches='tight')
