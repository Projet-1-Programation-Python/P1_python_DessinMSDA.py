# Ceci est un implementation de codes qui perpet de dessiner une maison avec la documentation de turtle 
# Il a ete concu a partir de differents figures geometrique ex: Carrer,Rectangle,Triangle ect.....


#Importer le namespace du package que nous avons créé
import dessinMSDA as d 

import turtle 
#Cacher le curseur 
turtle.shape("blank") 

#Dessiner les murs 
d.dessin_Carre(100)  

#Deplacer le curseur
turtle.up()
turtle.right(90)
turtle.backward(100)
turtle.down()
turtle.right(90)
turtle.forward(20)
turtle.right(180)

#Dessiner le toit
d.dessin_Triangle(140)

#Deplacer le curseur
turtle.up()
turtle.forward(110)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.backward(15)
turtle.down()

#Dessiner la souche de la cheminée
turtle.fillcolor('white')
turtle.begin_fill()
d.dessin_Rectangle(15,40)
turtle.end_fill()

#Deplacer le curseur
turtle.up()
turtle.goto(0,0)
turtle.down()

#Dessiner la base
turtle.fillcolor('black')
turtle.begin_fill()
d.dessin_Rectangle(100,10)
turtle.end_fill()

#Deplacer le curseur
turtle.up()
turtle.goto(20,10)
turtle.down()

#Dessiner la porte
d.dessin_Rectangle(20,50)

#Deplacer le curseur
turtle.up()
turtle.goto(15,0)
turtle.down()

#Dessiner un rectangle rempli en gris
turtle.fillcolor('gray')
turtle.begin_fill()
d.dessin_Rectangle(30,9.5)
turtle.end_fill()

#Deplacer le curseur
turtle.up()
turtle.goto(60,60)
turtle.down()

#Dessiner la fenêtre
d.dessin_Carre(30)
turtle.up()
turtle.goto(75,60)
turtle.down()
turtle.left(90)
turtle.forward(30)
turtle.up()
turtle.goto(60,75)
turtle.right(90)
turtle.down()
turtle.forward(30)

turtle.done()
