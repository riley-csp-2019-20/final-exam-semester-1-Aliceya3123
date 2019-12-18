import turtle as trtl
import random
#Ms. Haubold


#Name
# Aliceya Badget
#Date
# 12/18/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors


#import required libraries


#create turtle
A = trtl.Turtle()           #this allows your turtle to be res and import as A
A.color("red")
A.resizemode("auto")







#movement functions
def A_up():
    A.setheading(90)            # makes turtle go up 
    A.forward(10)
def A_down():
    A.setheading(270)           #makes turtle go down 
    A.forward(10)
def A_left():
    A.setheading(180)           # makes turtle go left 
    A.forward(10)
def A_right():
    A.setheading(0)             # makes turtle go right 
    A.forward(10)


               #clears turtle 




        

    




#color/drawing functions



#create screen

#bind to keypresses


#listen


#mainloop # this code makes the aarrow keys work with the code so the turtle can go up down left and right 
wn = trtl.Screen()
wn.onkeypress(A_up,"Up")
wn.onkeypress(A_down,"Down")
wn.onkeypress(A_left,"Left")
wn.onkeypress(A_right,"Right")
wn.listen()
wn.mainloop()
