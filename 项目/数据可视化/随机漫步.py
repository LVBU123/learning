
# coding: utf-8

# In[ ]:


from random import choice
class RandomWalk():
    def __init__(self,num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance
        return step
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            
            if x_step ==0 and y_step == 0:
                continue
                
            x_value = self.x_values[-1] + x_step
            y_value = self.y_values[-1] + y_step
            self.x_values.append(x_value)
            self.y_values.append(y_value)

import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.figure(dpi = 128,figsize = (10,6))
    number = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,linewidth=10)
    plt.scatter(0,0,c = 'green',s = 200)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',s = 100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input('Make another walk?(y/n):')
    if keep_running == 'n':
        break

 


# In[4]:




