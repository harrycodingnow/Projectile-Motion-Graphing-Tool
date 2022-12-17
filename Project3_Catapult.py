#CMPSC 131
#Harry (Kai-Teng) Hou
#Project 3 Catapult
import math
import turtle


def inputData():
    velocity = int(input("Velocity:"))
    angle = int(input("Angle:"))
    horDistance = int(input("Horizontal Distance:"))
    height = int(input("Vertical Distance:"))
    return(velocity, angle, horDistance, height)

def calcProjectileMotion(vel, ang, dist, h):
    time = round(math.sin(math.radians(ang))*2*vel/9.8,2)
    xDisplacement = round(vel * time*math.cos(math.radians(ang)),2)
    timeatWall = round(dist/(vel*math.cos(math.radians(ang))),2)
    yDisplacement = round(vel*timeatWall*math.sin(math.radians(ang))-0.5*9.8*timeatWall**2,2)
    targetArea = int(dist+(h*2))
    HitTarget = 0
    if xDisplacement < dist:
        HitTarget = HitTarget -1
    elif xDisplacement > targetArea:
        HitTarget = HitTarget +1
    elif xDisplacement > dist and xDisplacement < targetArea and yDisplacement < h:
        HitTarget = HitTarget -1
    else:
        HitTarget = HitTarget + 0
    


    result = {
        "Time" : time,
        "DistanceTravelled" : xDisplacement,
        "HitTarget" : HitTarget
    }

    return result


def outputResults(result):
    print("Total Time is", result["Time"], "seconds." )
    print("Total Distance Travelled is", result["DistanceTravelled"], "meters.")
    if result["HitTarget"] == 0:
        print("You Hit the Target!")
    else:
        print("You Didn't Hit the Target.")

def drawProjectile(vel, ang, dist, h):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Bar Graph")
    turtle.colormode(255)
    t = turtle.Turtle()
    turtle.speed(0)
    t.pensize(5)
    
    #ground
    t.penup()
    t.goto(-200,0)
    t.pendown()
    t.goto(0,0)
    #target area
    t.goto(dist,0)
    t.color('red')
    t.goto(dist+(2*h), 0)
    t.color('black')
    t.forward(400)

    #structure
    t.penup()
    t.color('blue')
    t.goto(dist, 0)
    t.pendown()
    t.goto(dist, h)

    t.penup()
    t.goto(0, 0)
    

    t.color('white')
    time = round((math.sin(math.radians(ang))*2*vel/9.8))
    

    for x in range(0,time+1):
        t.pendown()
        t.goto(vel * x*math.cos(math.radians(ang)),vel*x*math.sin(math.radians(ang))-0.5*9.8*x**2)
        
    
    wn.mainloop()

    



vel, ang, dist, h = inputData()
result = calcProjectileMotion(vel, ang, dist, h)
outputResults(result)
drawProjectile(vel, ang, dist, h)



#Unit Test COde
if __name__ == "__main__":
    #Test 1 - Happy Path (Hit Target Area)
    #Note: inputData and drawProjectile will be tested manually
    results = calcProjectileMotion(35, 70, 50, 20)
    assert results != {}
    assert 6.71 == results["Time"]
    assert 80.32 == results["DistanceTravelled"]
    assert 0 == results["HitTarget"]
    print("Test #1 Completed")


