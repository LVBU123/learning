
# coding: utf-8

# In[23]:


class Restaurant():
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number_served = 0
    def describe_restaurant(self):
        print("Here's {}.".format(self.name))
        print("We specialize in {}.".format(self.type))
    def open_restaurant(self):
        print("We are open.")
    def read_number(self):
        print("We have served {} guests.".format(self.number_served))
    def set_number_served(self,new_number):
        self.number_served = new_number
    def increment_number_served(self,increment_number):
        self.number_served += increment_number
        
restaurant = Restaurant("a","b")
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
restaurant.read_number()
restaurant.increment_number_served(10)
restaurant.read_number()

class IceCreamStand(Restaurant):
    def __init__(self,name,type = "ice cream"):
        
        super().__init__(name,type)
        self.flavors = []
    def read_flavors(self):
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print("- "+flavor.title())
IceCreamStand = IceCreamStand("IceCreamStand","ice cream")
IceCreamStand.flavors = ["cherry","banana","chocolate"]
IceCreamStand.describe_restaurant()
IceCreamStand.read_flavors()        


# In[13]:


canting = Restaurant("荷塘月色","牛欢喜")
wangjingze = Restaurant("真香","炒饭")
mianjinge = Restaurant("香香的口味","烤面筋")
canting.describe_restaurant()
wangjingze.describe_restaurant()
mianjinge.describe_restaurant()


# In[14]:


class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greet_user(self):
        print(self.first_name+self.last_name)
d = User("a","b")
d.describe_user()
d.greet_user()
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = []
    def show_privileges(self):
        print("Admin's privileges are following:")
        for privilege in self.privileges:
            print("- "+privilege)
LVBU = Admin("LV","BU")
LVBU.privileges=["can add post","can delete post","can ban user"]
LVBU.show_privileges()
        
    


# In[30]:


class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
    def describe_user(self):
        print(self.first_name,self.last_name)
    def greet_user(self):
        print(self.first_name+self.last_name)
d = User("a","b")
d.describe_user()
d.greet_user()


class Privileges():
    def __init__(self,privileges = []):
        self.privileges = privileges
    def show_privileges(self):
        print("Admin's privileges are following:")
        for privilege in self.privileges:
            print("- "+privilege)
            
class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.p = Privileges()
            
LVBU = Admin("LV","BU")
LVBU.p.privileges=["can add post","can delete post","can ban user"]
LVBU.p.show_privileges()
        
    


# In[ ]:




