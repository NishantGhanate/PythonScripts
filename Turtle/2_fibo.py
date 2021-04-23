
import turtle  
skk = turtle.Turtle() 

f = int(input(' : '))
one = 0 
two = 1

for i in range(1,f):
    temp = one + two
    one = two
    two = temp
    print(temp)
    turtle.circle(temp,-180)

print(turtle.position())
print(turtle.heading())

# turtle.circle(130,-180)
# print(turtle.position())
# print(turtle.heading())

turtle.done() 


