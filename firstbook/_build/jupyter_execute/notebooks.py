#!/usr/bin/env python
# coding: utf-8

# # Data Science
# 
# Como una de las ventajas de implementar estos libros es que además de poder implementar contenido en la web también podemos mostrar nuestros notebooks con los procesos e implementaciones en código de nuestras investigaciones.
# 
# Aquí se puede ver como podemos implementar código python dentro de nuestro libro

# In[1]:


#Muestra de gráficos
import numpy as np
import matplotlib.pyplot as plt
x1 = np.linspace(0,5*np.pi,1000)
y1 = np.cos(x1)
y2 = np.sin(x1)

plt.plot(x1,y1,'b.')
plt.plot(x1,y2,'r.')
plt.xlabel('Tiempo (s)',size=14)
plt.ylabel('Valor Señal',size=14)
plt.title('Señal coseno y seno',
         fontdict={
          'size':16,
          'family':'serif',
          'color':'darkblue',
          'weight':'bold'
         })
plt.grid(True)
plt.show()

