import pickle
import numpy as np
import matplotlib.pyplot as plt

pkl_file = open('data/data2005.pkl', 'rb')
# note encoding='latin1' because pickle generated in python2
data = pickle.load(pkl_file, encoding='latin1')
pkl_file.close()

T = data['temp']
Q = data['flow'] - data['flow'].min()
Q /= Q.sum()
p = data['snowprop']
t = data['doy']

# Use mgrid as previously to define a 2D grid of parameters
T0min,T0max,T0step = 0,20,1
fmin,fmax,fstep = 0.01,0.2,0.01

T0,f = np.mgrid[T0min:T0max+T0step:T0step,\
                fmin:fmax+fstep:fstep]
print(T0.shape)

Q_ = Q[:,np.newaxis]


xp = 1
Q_nrf = model(T0,f,T,p,xp=xp)
err = Q_nrf - Q_
e2 = np.mean(err * err,axis=0)
print(e2.min())
imin = np.argmin(e2)
ip0min,ip1min = np.unravel_index(imin,T0.shape)

print(imin)
print(f'parameters {T0.ravel()[imin]} {f.ravel()[imin]}')
_T0 = T0.ravel()[imin]
_f = f.ravel()[imin]
_Q_nrf = model(_T0,_f,T,p,xp=xp)
plt.plot(_Q_nrf)
plt.plot(Q)
plt.savefig('work/qmin.png')
plt.figure()
plt.imshow(e2.reshape(T0.shape),vmax=0.00001)
plt.plot([ip1min],[ip0min],'r+')
plt.colorbar()
plt.savefig('work/modelmin.png')

