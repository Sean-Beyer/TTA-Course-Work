Title = "kAPP's Turn"
print(Title)
Toon = "kAPP - Android Mechanic"
ToonS = 5
Drone = "Murco - Hover Drone"
DroneS = 2
Bad = "Drow - Soldier"
BadAC = 12
list_names = (Toon, Drone)
list_standing = (Toon + " stands at 34HP, " + Drone + " hovers at 15HP and, " + Bad + " is twitching at 8HP.")
import random
import time
rolled_num = random.randint(1,20)
dictionary = {'Android' : 'A synthetic life-form' , 'Mechanic' : 'A character class-type that creates and implaments and A.I. for various tasks' , 'Drone' : 'A robotic contstruct that utilizes a Mechanics A.I. to assist their creator.' , 'Drow' : 'A genetic off-shoot of the elvin race.' , 'Soldier' : 'A character class-type trained in various martial and weaopon types.'}
print(list_names)
print("May now take their turn!")
print(Bad + " prepares for the hit.")
print(dictionary['Drow'])
print(Toon + " uses his Move action to command his drone to shoot.")
print(dictionary['Android'])
print(dictionary['Mechanic'])
print("With a hoot "   + Drone + " takes a shot.")
print(dictionary['Drone'])
print(Drone + " circles... and circles... and fires!")
time.sleep(5)
if DroneS + rolled_num > BadAC:
    print(Bad + " took a birdshot.")
elif DroneS + rolled_num < BadAC:
    print(Bad + " nimbly dodges attack.")
else:
    print(Bad + " should have ducked sooner.")
print(Toon + " raises his handcoil pistol to shoot lighting at " + Bad)
time.sleep(5)
if ToonS + rolled_num >= BadAC:
    print(Bad.swapcase() + " is struck by lightning!")
elif ToonS + rolled_num <= BadAC:
    print(Bad + " steps out of the way of the lightning.")
else:
    print(Bad + " should have ducked sooner.")
    time.sleep(1)
print("End of round.")
print(list_standing)
