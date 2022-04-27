#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#！/user/bin/env python
"""Mapper1.py"""

import sys
import re

for line in sys.stdin:
    
    line = line.strip()
    cols = line.split('\t')
    print'%s\t%d'%(cols[2],1)

