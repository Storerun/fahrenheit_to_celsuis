#!/usr/bin/env python
# coding: utf-8

#  # Fahrenheit to Celsius  temperature converter

# In[10]:


temp= int(input("Enter temperature: "))
temp_type= input(" Fahrenheit (F) or Celsius (C): ")
if temp_type.lower() == 'f':
    converted = temp / 33.8
    print('Temperature is {} celsius'.format(converted))
else:
    converted = temp * 33.8
    print('Temperature is {} fahrenheit'.format(converted))
    


# In[ ]:




