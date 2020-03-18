import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
#if tabulate is not installed, type in the terminal: pip install tabulate
from tabulate import tabulate

datosv=np.loadtxt('resultsv.dat')
centrei_ra=datosv[:,0]
centrei_dec=datosv[:,1]
mag_v=datosv[:,2]
datosi=np.loadtxt('resultasi.dat')
mag_i=datosi[:,2]
both=np.loadtxt("results".dat')
#vectors which tell us how the magnitudes must be sorted:
orden_v=both[:,5]
orden_i=both[:,4]
#as they do not start in 0, we have to normalise them and make the numbers integers:
orden_v-=np.amin(orden_v)
orden_v=orden_v.astype(int)
orden_i-=np.amin(orden_i)
orden_i=orden_i.astype(int)
#sort the magnitudes:
M_v=np.array([])
M_i=np.array([])
centre_ra=np.array([])
centre_dec=np.array([])
for i in range(len(orden_v)):
	M_v=np.append(M_v,mag_v[orden_v[i]])
	M_i=np.append(M_i,mag_i[orden_i[i]])
	centre_ra=np.append(centre_ra,centrei_ra[orden_i[i]])
	centre_dec=np.append(centre_dec,centrei_dec[orden_i[i]])
vi=M_v-M_i
#now, we can plot the color-magnitude diagram
ax=plt.gca()
ax.invert_yaxis()
ax.scatter(vi,M_i,s=1,color='black')

ax.tick_params(which='both', direction='in')
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(1/10))
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(1/4))
xax = ax.get_xaxis()
ax.set_ylim(bottom=25)
yax = ax.get_yaxis()


ax_top = ax.twiny()
ax_top.tick_params(which='both', direction='in')
ax_top.set_xlim(ax.get_xlim())
ax_top.xaxis.set_major_locator(MultipleLocator(1))
ax_top.xaxis.set_minor_locator(MultipleLocator(1/10))
ax_top.get_shared_x_axes().join(ax_top, ax)
ax_top.set_xticklabels([])

ax_right = ax.twinx()
ax_right.tick_params(which='both', direction='in')
ax_right.set_ylim(ax.get_ylim())
ax_right.yaxis.set_major_locator(MultipleLocator(1))
ax_right.yaxis.set_minor_locator(MultipleLocator(1/4))
ax_right.get_shared_y_axes().join(ax_right, ax)
ax_right.set_yticklabels([])

ax.set_xlabel('V-I',fontsize=15)
ax.set_ylabel('I',fontsize=15)
plt.show()