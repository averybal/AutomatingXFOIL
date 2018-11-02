# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:45:27 2018

@author: avery
"""

import subprocess as sp
#import os
import shutil
import sys
import string
 
"""
class Popen(args, bufsize=0, executable=None,
            stdin=None, stdout=None, stderr=None,
            preexec_fn=None, close_fds=False, shell=False,
            cwd=None, env=None, universal_newlines=False,
            startupinfo=None, creationflags=0):
"""
 
ps = sp.Popen(['xfoil.exe'],
              stdin = sp.PIPE)
              #stdout = None,
              #stderr = None) 

airfoil = "naca 0020"

inst = str.join('\n', [airfoil,
                                       "oper",
                                       "v 3e6",
                                       "alfa 0.0",
                                       "pacc",
                                       str.join("",[airfoil,".dat"]),
                                       "",
                                       "aseq -21 20 .5",
                                       "pacc"])
    
res = ps.communicate(inst.encode())

print(res)