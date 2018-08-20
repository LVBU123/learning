
# coding: utf-8

# In[2]:


def name(City,Country,population = 0):
    if population:
        result = City + "," + Country + "- population "+ str(population)
    else:
        result = City + "," + Country
    return result.title()


# In[5]:


class Employee():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    def give_raise(self,increment = 5000):
        self.salary += increment

