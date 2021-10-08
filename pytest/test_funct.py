#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:25:56 2021

@author: kishore7
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:16:35 2021

@author: kishore7
"""

import funct

def test_add():
    assert funct.add(3,4) == 7
    assert funct.add(3,4) == 6
    
def test_sub():
    assert funct.sub(4,3) == 1
    
def test_mul():
    assert funct.mul(3,4) == 12
    
def test_div():
    assert funct.div(8,4) == 2
    