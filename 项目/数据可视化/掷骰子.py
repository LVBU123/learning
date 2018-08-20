
# coding: utf-8

# In[3]:


from random import randint
import pygal

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)

die = Die()
results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(number) for number in range(1,die.num_sides+1)]

print(frequencies)
 
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [str(x) for x in range(1,die.num_sides+1)]
hist.x_title = 'Number'
hist.y_title = 'Frequency of Result'
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')


# In[3]:


from random import randint
import pygal

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)

die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(number) for number in range(2,max_result+1)]

print(frequencies)
 
hist = pygal.Bar()
hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = [str(x) for x in range(2,max_result + 1)]
hist.x_title = 'Number'
hist.y_title = 'Frequency of Result'
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')

