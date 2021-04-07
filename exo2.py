import numpy as np
import math

sec = 1

print("Pour", sec, "secondes : ")

instruction = (float(sec)) / 10**-7

print("Nombre d'instruction possible :", instruction)
print("log(n) :"  , np.log10(instruction))
print("n :"       , instruction)
print("n log(n) :", instruction * math.log10(instruction))
print("n² :"      , pow(instruction, 2))
print("2^n :"     , pow(2, instruction)) # Infini

