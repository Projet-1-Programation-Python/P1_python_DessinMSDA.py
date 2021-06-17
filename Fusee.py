import dessinMSDA as d 
import turtle 
#Cacher le curseur 
turtle.shape("blank") 

#Dessiner le carre 
d.dessin_Carre(100)  

#Deplacer le curseur
turtle.up()
turtle.right(90)
turtle.backward(100)
turtle.down()
turtle.right(90)
turtle.forward(20)
turtle.right(180)

#Dessiner le triangle
d.dessin_Triangle(140)

#Deplacer le curseur
turtle.up()
turtle.forward(110)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.backward(15)
turtle.down()
# dessiner le carre
d.dessin_Carre(140)
# retourner le curseur
turtle.up()
turtle.goto(0,0)
turtle.left(20)
turtle.down()
# dessiner un cube 
d.dessin_cube()
# forming front square face
for i in range(4):
 turtle.forward(100)
turtle.left(90)
# Deplacer a gauche
turtle.goto(50,50)
# forming back square face
for i in range(4):
 turtle.forward(50)
turtle.left(90)
# deplacer a droite
turtle.goto(100,50)
turtle.goto(100,0)
# revenir au point de depart 
turtle.goto(100,100)
turtle.goto(100,100)
turtle.goto(50,100)
turtle.goto(0,100)
