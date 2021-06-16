# Importer l'ensemble de fonctions du module turtle

from turtle import * ;

# Créer une première fonction permettant de dessiner un cercle de rayon donné

def dessin_Cercle(r): 
    circle(r)
    done()

# Créer une fonction permettante de dessiner un demi cercle de rayon donné

def dessin_Demi_Cercle(r):
    circle(r,180)
    done()

# Créer une fonction permettant de dessiner un carré de coté donné

def dessin_Carre(a):
    t = Turtle()
    for i in range(4): 
        t.forward(a) 
        t.left(90)
    done()

# Créer une fonction permettant de dessiner un triangle de coté donné

def dessin_Triangle(a):
    t = Turtle()
    for i in range(3):
        t.forward(a)
        t.left(120)
    done()

# Créer une fonction permettant de dessiner un rectangle de dimensions données

def dessin_Rectangle(a,b):
    t = Turtle()
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
    done()

# Créer ue fonction permettant de créer un polygone paramétrable

def dessin_Polygone(a,b):
    circle(a,b)
    done()