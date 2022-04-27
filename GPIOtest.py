#!/usr/bin/env python
# coding: utf-8

# In[2]:


import RPi.GPIO as GPIO
import time

pinnum = 17 #pin number for output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinnum, GPIO.OUT)

t = 0
print('turning on')
while t < 60:
    GPIO.output(pinnum, GPIO.HIGH)
    time.sleep(1)
    t = t + 1
    if t == 55:
        print('turning off in 5 seconds')
    
GPIO.cleanup()
print('done')


# In[ ]:




