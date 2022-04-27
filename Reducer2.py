#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/user/bin/env python
"""Reducer2.py"""

import sys

passenger = ""
passenger_passenger = ""
passenger_count = 0




for line in sys.stdin:
    airport, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    
    if passenger_passenger == passenger:
        passenger_count += count
    else:
        if passenger_passenger:
            print'%s\t%d'%(passenger_passenger, passenger_count)
            
            passenger_count = count
            passenger_passenger = passenger
if passenger_passenger == passenger:
    print '%s\t%d' % (passenger_passenger, passenger_count)

