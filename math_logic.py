# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Вариант 1

import sys


def statement():    
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (x or y or z) != (not x and not y and not z):
                    sys.exit('Statement is FALSE!')
    print('Statement is TRUE!')                                 

  
statement()
print()

# Вариант 2
 

left = []
right = []
       
for x in range(2):
    for y in range(2):
        for z in range(2): 
            left.append(not (x or y or z))
            right.append(not x and not y and not z)
           
print(left)
print(right)
print()

if left == right:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
