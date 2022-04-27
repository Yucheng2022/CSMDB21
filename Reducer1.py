#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/user/bin/env python
"""Reducer1.py"""

import sys

airport = ""
airport_airport = ""
airport_count = 0

for line in sys.stdin:
    airport, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    
    if airport_airport == airport:
        airport_count += count
    else:
        if airport_airport:
            print'%s\t%d'%(airport_airport, airport_count)
            
        airport_count = count
        airport_airport = airport
if airport_airport == airport:
    print '%s\t%d' % (airport_airport, airport_count)

