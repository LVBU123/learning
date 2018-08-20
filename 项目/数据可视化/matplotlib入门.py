
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()


# In[24]:


import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Square Value',fontsize = 14)
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()


# In[32]:


import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)

plt.show()


# In[39]:


import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)

plt.show()
 


# In[63]:


import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,edgecolor='none',c=y_values,cmap=plt.cm.Blues,s=40)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("Value",fontsize = 14)
plt.ylabel("Square of Value",fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')


# In[66]:


import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [1,8,27,64,125]
plt.scatter(x_values,y_values,edgecolor = 'none',s=100)
plt.title('Cube Numbers',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Cube of Value',fontsize = 14)
plt.tick_params(axis = 'both',labelsize = 14)
plt.show()


# In[68]:


import matplotlib.pyplot as plt
x_values = list(range(5000))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Reds,edgecolor = 'none',s=40)
plt.title('Cube Number',fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Cube of Value',fontsize = 14)
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
plt.show()

