import os 
import platform
if (platform.system() == 'linux'):
    os.system("clear")
elif (platform.system() == 'windows'):
    os.system("cls")

import math
x = 5 
print(f"Faktorial dari (!{x}) = {math.factorial(x)}")
data = [2,3,3]
#fsum
print(f"hasil hasil tambah = {math.fsum(data)}")

print(f"hasil dari pembulatan coil 5,57 adalah {math.ceil(5.57)}")

