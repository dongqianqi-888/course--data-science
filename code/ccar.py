#!/usr/bin/env python
# coding: utf-8

# In[2]:


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfun(self):
        print('hello, my name is '+self.name+'~')


# In[3]:


class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def descriptive(self):
        long=str(self.year)+' '+self.make+' '+self.model
        return long.title()
    def read_odometer(self):
        print('this car has '+str(self.odometer_reading)+' miles on it.')
    def update_odometer(self,mile):
        self.odometer_reading=mile
    def increment_odometer(self,miles):
        self.odometer_reading+=miles


# In[4]:


class electriccar(car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print('this car has a '+str(self.battery_size)+'-kWh battery.')


# In[ ]:




