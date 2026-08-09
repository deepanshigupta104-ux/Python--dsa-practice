# print poem 
# i print(""" Twinkle, twinkle, little star,

# Use REPL And print table of 5 
#Write a python program to print the content of a directory using OS module search online
#0s ek built-in Python module hai jo file aur
#directory operations perform karne me
#madad karta hai.

import os

directory_path = "."  
 # yahan "." matlab current
                         # directory (jis folder me
                         # program run ho raha hai)

contents = os.listdir(directory_path)

print("Directory ke contents:")
for item in contents:
    print(item)