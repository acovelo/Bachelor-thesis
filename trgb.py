#the abolute magnitude of the TRGB is -4. Apparent magnitudes must be corrected.
m_trgb=-4
ax.hlines(m_trgb-0.5,0.8,1.8,color='blue')
ax.hlines(m_trgb+0.5,0.8,1.8,color='blue')
ax.vlines(0.8,m_trgb-0.5,m_trgb+0.5,color='blue')
ax.vlines(1.8,m_trgb-0.5,m_trgb+0.5,color='blue')
plt.show()

megara_i=[]
megara_v=[]
megara_vi=[]
megara_ra=[]
megara_dec=[]
for i in range(len(M_i)):
	if M_i[i]>m_trgb-0.5 and M_i[i]<m_trgb+0.5 and vi[i]>0.8 and vi[i]<1.8:
		megara_i=np.append(megara_i,M_i[i])
		megara_vi=np.append(megara_vi,vi[i])
		megara_v=np.append(megara_v,M_v[i])
		megara_ra=np.append(megara_ra,centre_ra[i])
		megara_dec=np.append(megara_dec,centre_dec[i])
#we delete the stars which are closer than 1arcsec to each other:
I=[megara_i[0]]
v=[megara_v[0]]
vi=[megara_vi[0]]
ra=[megara_ra[0]]
dec=[megara_dec[0]]
for i in range(1,len(megara_i)):
	for j in range(i):
		if np.abs(megara_ra[j]-megara_ra[i])<1/3600 and np.abs(megara_dec[j]-megara_dec[i])<1/3600:
			break
		else:
			if i-j==1:
				I=np.append(I,megara_i[i])
				v=np.append(v,megara_v[i])
				vi=np.append(vi,megara_vi[i])
				ra=np.append(ra,megara_ra[i])
				dec=np.append(dec,megara_dec[i])	
#the 100 brightest:
selection=sorted(I)
brillante=max(selection[0:100])
I_final=[]
V_final=[]
VI_final=[]
ra_final=[]
dec_final=[]
for i in range(len(I)):
	if I[i]<brillante:
		I_final=np.append(I_final,I[i])
		V_final=np.append(V_final,v[i])
		VI_final=np.append(VI_final,vi[i])
		ra_final=np.append(ra_final,ra[i])
		dec_final=np.append(dec_final,dec[i])
		

results=zip(ra_final,dec_final,V_final,I_final,VI_final)
tabla=tabulate(results,headers=['RA (degree)','DEC (degree)','V','I','V-I'])
outfile = open("final.txt", 'w')
outfile.write(tabla)
outfile.close()