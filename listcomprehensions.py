

#Horsepower using list comprehensions

'''pressure = [value for value in range(100,3000,100)]
flow = [value for value in range(5,100,10)]

for i in flow:
    for j in pressure:
        hp = round((i*j)/1714)
        print(f'Flow: {i} gpm, Pressure: {j} psi, Horsepower: {hp}')'''
        
#Torque lbs-ft given rpm and horsepower
hp = [.25,.33,.5,.75,1,1.5,2,3,5,7.5,10,15,20,25,30,40,50,60,75,100,125,150,200,250]
rpm = [100,500,750,1000,1200,1500,1800,2400,3000,3600]

for i in hp:
    for j in rpm:
        torque = round((i*5252)/j,2)
        print(f'Horsepower = {i} hp | rpm = {j} rpm | Torque = {torque} lbs-ft')
        
