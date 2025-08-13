def checkspeed(speed):
    point=0
    if speed <=70:
            print("ok")
    else:
            excessspeed=speed-70
            point =excessspeed//5
            print("points :",point)
            
   
    if point==12:
        print("Licence suspended")


speed=int(input("speeds of vehicle"))
checkspeed(speed)



