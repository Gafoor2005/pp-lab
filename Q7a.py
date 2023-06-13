def ball_collide(b1,b2):
    distance = ((b2[1]-b1[1])**2 + (b2[0]-b1[0])**2)**0.5
    if(distance<= (b1[2]+b2[2])):
       return True
    return False
b1 = (0,20,10)
b2 = (0,0,10)
print(ball_collide(b1,b2))