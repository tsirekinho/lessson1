#by ; tsireka


from turtle import*



# we try to paint a mini house



# I step ; first construction ; Square ;



speed(5) 



begin_fill()
color("orange")


forward(150)
left(90)


forward(150)
left(90)

forward(150)
left(90)

forward(150)
left(90)

end_fill()

# end first construction

# II step ; roof

penup()
goto(150,150)
pendown()




color("gray")
begin_fill()


left(120)
forward(150)
left(120)
forward(150)
end_fill()

penup()
goto(150,-1)
pendown()

# roof ended



# III  WE START DRAWING WINDOWS 
color()
begin_fill()
penup()
goto(85,-1)
pendown()

right(150)
forward(55)

left(90)
forward(25)

left(90)
forward(55)

left(90)
forward(25)


penup()
left(90)
goto(45,97)
pendown()

left(90)
forward(35)

right(90)
forward(35)

right(90)
forward(35)

right(90)
forward(35)


penup()
goto(97,95)
pendown()

left(90)
forward(35)

left(90)
forward(35)

left(90)
forward(35)

left(90)
forward(35)



# III END - 

# color("Green")
# begin_fill()

# penup()
# goto(-45,-1)
# pendown()

# left(90)
# forward(499)

# right(90)
# forward(255)
 
# right(90)
# forward(1000)

# right(90)
# forward(255)

# right(90)
# forward(555) ///////////// nvm


exitonclick()