#https://www.wikihow.com/Find-Initial-Velocity

#This is what happens when you challeng a student to bring a formula to the lesson that they have used in a different subject!

#1- If you have values for the final velocity, acceleration, and time involved, use Vi = Vf - (a * t)
#2- If you know values for the distance, time, and acceleration, use Vi = (d / t) - [(a * t) / 2]
#3- If you're given the final velocity, acceleration, and distance, use Vi = √ [Vf2 - (2 * a * d)]
#4- If you're given the final velocity, time, and distance, use Vi = 2(d/t) - Vf.

import math

#1 Initial Velocity when you know final velocity, acceleration and time involved
#Vi = Vf - (a * t)

Vi=0    #Vi - Initial Velocity
Vf=200  #Vf - Final Velocity m/s
a=10    #a - Acceleration m/s**2
t=12    #t - time s

Vi=Vf-(a*t)
print("#1",Vi,"m/s")


#2 Initial Velocity when you know distance, time and acceleration
#Vi = (d / t) - [(a * t) / 2]

Vi=0    #Vi - Initial Velocity
d=150   #d - distance m
t=30    #t - time s
a=7     #a - acceleration m/s**2

Vi=(d/t)-((a*t)/2)
print("#2",Vi,"m/s")



#3 Initial Velocity when you know Final Velocity, Acceleration and Distance
#Vi = √ [Vf2 - (2 * a * d)]

Vi=0    #Vi - Initial Velocity
Vf=12   #Vf - Final Velocity m/s
a=5     #a - Acceleration m/s**2
d=10    #s - distance m

Vi=math.sqrt(Vf**2 - (2*a*d))
print("#3",Vi,"m/s")


#4 Initial Velocity when you know final velocity, time, and distance
#Vi = 2(d/t) - Vf.

Vi=0   #Vi - Initial Velocity
Vf=3   #Vf - Final Velocity m/s
t=15   #t - time s
d=45   #d - distance m

Vi=2*(d/t)-Vf
print("#4",Vi,"m/s")