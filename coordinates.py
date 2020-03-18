from drizzlepac import pixtosky
#if tabulate is not installed, type in the terminal: pip install tabulate
from tabulate import tabulate
import numpy as np
visible=np.loadtxt('visible.dat')
xv=visible[:,0]
yv=visible[:,1]
mag_v=visible[:,2]
verr=visible[:,3]
infrared=np.loadtxt('infrared.dat')
xi=infrared[:,0]
yi=infrared[:,1]
mag_i=infrared[:,2]
ierr=infrared[:,3]
rav=[]
decv=[]
for i in range(len(xv)):
	r,d=pixtosky.xy2rd("imageV.fits[1]",xv[i],yv[i],hms=False)
	rav=np.append(rav,r)
	decv=np.append(decv,d)
rai=[]
deci=[]
for i in range(len(xi)):
	r,d=pixtosky.xy2rd("imageI.fits[1]",xi[i],yi[i],hms=False)
	rai=np.append(rai,r)
	deci=np.append(deci,d)
resultsv=zip(rav,decv,mag_v,verr)
tablev=tabulate(resultsv,headers=['#RA(V)','#DEC(V)','#MAG(V)','#Verr'])
outfile = open("resultsv.dat", 'w')
outfile.write(tablev)
outfile.close()
resultsi=zip(rai,deci,mag_i,ierr)
tablei=tabulate(resultsi,headers=['#RA(I)','#DEC(I)','#MAG(I)','#Ierr'])
outfile = open("resultsi.dat", 'w')
outfile.write(tablei)
outfile.close()