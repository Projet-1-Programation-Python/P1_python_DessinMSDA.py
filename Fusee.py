import dessinMSDA as d 
import turtle 
#Cacher le curseur 
turtle.shape("blank") 

#Dessiner trapèze
d.dessin_Trapeze(100,60,49)

#Deplacer le curseur
turtle.up()
turtle.right(120)
turtle.forward(25)
turtle.down()

#Dessiner le carre 
d.dessin_Carre(48)  

#Deplacer le curseur
turtle.up()
turtle.right(90)
turtle.backward(50)
turtle.down()
turtle.right(90)
turtle.forward(10)
turtle.right(180)

#Dessiner le triangle
d.dessin_Triangle(70)

# #Deplacer le curseur
turtle.up()
turtle.forward(20)
turtle.down()

# dessiner le carre
d.dessin_Carre(30)

# retourner le curseur
turtle.up()
turtle.goto(-25,-20)
turtle.down()

#Dessiner Trapèze
d.dessin_Trapeze(150,40,20)

#deplacer le curseur 
turtle.up()
turtle.goto(-25,-45)
turtle.right(80)
turtle.down()

#Dessiner rectangle 
d.dessin_Rectangle(150,25)

#Deplacer le curseur 
turtle.up()
turtle.forward(25)
turtle.down()

#dessiner le rectangle intérieur 
d.dessin_Rectangle(100,45)

#Deplacer le curseur
turtle.up()
turtle.forward(25)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.down()

#Dessiner carré
d.dessin_Carre(50)

#Deplacer le cruseur 
turtle.up()
turtle.goto(-25,-45)
turtle.down()

#Dessiner triangle 1
turtle.right(70)
turtle.forward(50)
turtle.left(151)
turtle.forward(50)

#Deplacer le cruseur 
turtle.up()
turtle.goto(125,-45)
turtle.down()

#dessiner triangle 2
turtle.left(169)
turtle.forward(50)
turtle.right(151)
turtle.forward(50)

#deplacer le curseur 
turtle.up()
turtle.goto(0,-120)
turtle.right(99)
turtle.down()

d.dessin_Rectangle(100,25)

#deplacer le curseur 
turtle.up()
turtle.goto(40,-200)
turtle.down()

d.dessin_Rectangle(20,80)

#deplacer le curseur 
turtle.up()
turtle.goto(0,-200)
turtle.down()

d.dessin_Trapeze(100,55,60)

#deplacer le curseur 
turtle.up()
turtle.goto(20,-70)
turtle.down()

d.dessin_Cercle(10)

turtle.up()
turtle.goto(100,-70)
turtle.down()

d.dessin_Cercle(10)

turtle.up()
turtle.goto(80,-135)
turtle.down()

d.dessin_Cercle(5)

turtle.up()
turtle.goto(30,-135)
turtle.down()

d.dessin_Cercle(5)
turtle.done()
