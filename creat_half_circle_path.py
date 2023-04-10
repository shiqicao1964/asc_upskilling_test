#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


def calculate_angle(A,B,C,dist):
    # Define the three points
    # Calculate the vectors AB and BC
    BA = np.array(A) - np.array(B)
    BC = np.array(C) - np.array(B)
    # Calculate the dot product of AB and BC
    dot_product = np.dot(BA, BC)
    # Calculate the magnitudes of AB and BC
    norm_BA = np.linalg.norm(BA)
    norm_BC = np.linalg.norm(BC)
    # Calculate the cosine of the angle between BA and BC
    cos_theta = dot_product / (norm_BA * norm_BC)
    # Calculate the angle in radians
    theta = np.arccos(cos_theta)
    theta = theta /2
    
    BA_normalizd = BA/norm_BA
    BC_normalizd = BC/norm_BC
    
    BO_ = BA_normalizd + BC_normalizd
    norm_BO_ = np.linalg.norm(BO_)
    BO_normalizd = BO_/norm_BO_
    
    # calcul r 
    r = dist/(1/np.sin(theta) - 1)
    
    BO = r/np.sin(theta) * BO_normalizd
    O = B + BO
    return theta,O,r


# In[5]:


x1,y1 = 2,1
x2,y2 = 0,0
x3,y3 = 0,-3

fig = plt.figure(figsize=(6, 6))
plt.plot([x1,x2],[y1,y2])
plt.plot([x2,x3],[y2,y3])
plt.axis('equal')
plt.show()


# In[6]:


angle,O,r = calculate_angle([x1,y1],[x2,y2],[x3,y3],0.2)
print(angle)

t = np.linspace(0, 2*np.pi, num=100)
circleX = r * (np.cos(t) )+ O[0]
circleY = r * (np.sin(t) )+ O[1]

fig = plt.figure(figsize=(6, 6))
plt.plot([x1,x2],[y1,y2])
plt.plot([x2,x3],[y2,y3])
plt.plot(circleX,circleY,c='green')
plt.scatter(O[0],O[1])
plt.axis('equal')
plt.show()


# In[ ]:





# In[ ]:




