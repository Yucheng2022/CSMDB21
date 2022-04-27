#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#！/user/bin/env python
"""Mapper2.py"""

import sys
import re

for line in sys.stdin:
    
    line = line.strip()
    cols = line.split(',')
    print'%s\t%d'%(cols[0],1)

