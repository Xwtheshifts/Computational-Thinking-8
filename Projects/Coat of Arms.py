###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")

q1 = codesters.Square(100,100,200,'light blue')
q2 = codesters.Square(-100,100,200,'gold')
q3 = codesters.Square(-100,-100,200,'light blue')
q4 = codesters.Square(100,-100,200,'black')

s1 = codesters.Sprite("thegOat.png",100,100)
s2 = codesters.Sprite("haiti.jpeg",-100,100)
s2.set_size(0.5)
s3 = codesters.Sprite("basketball.gif",100,-100)
s3.set_size(2.0)
s4 = codesters.Sprite("cross.gif",-100,-100)
s4.set_size(0.5)

message1 = codesters.Text("Xavier Avril",0,220,"black")
message2 = codesters.Text("Give it 100% the first time",0,-220,"gold")