import dessinMSDA as d
import turtle 

turtle.fillcolor('sky blue')
turtle.color('sky blue')
turtle.begin_fill()
d.dessin_Rectangle(150,20)
turtle.forward(150)
d.dessin_Demi_Cercle(10)

turtle.up()
turtle.forward(50)
turtle.down()
turtle.right(170)
d.dessin_Trapeze_droite(10,80,80)

turtle.up()
turtle.goto(26,12)
turtle.down()

d.dessin_Trapeze_droite(10,80,80)

turtle.up()
turtle.goto(-7,15)
turtle.right(170)
turtle.down()
d.dessin_Trapeze_droite(10,80,50)

turtle.up()
turtle.goto(30,20)
turtle.left(60)
turtle.down()
d.dessin_Trapeze_droite(10,80,50)


turtle.end_fill()
turtle.done()
