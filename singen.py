from math import sin
with open ('test.txt',"w") as file:
    file.write("0.001 0\n")
    i=-3.14
    str=''
    while i < 3.14:
        file.write(str(str(i)+' '))

        i=i+0.001
    i=-3.14
    while i<3.14:
        file.write(str(sin(i)+sin(21*i))+' ')
        i=i+0.001

