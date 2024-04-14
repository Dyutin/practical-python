# bounce.py
#
# Exercise 1.5
height = 100
bounceFactor = 3/5

for i in range(10):
    height*=bounceFactor
    print(i+1, round(height, 4))