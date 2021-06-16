# Importer l'ensemble de fonctions du module turtle

from turtle import * ;

# Créer une première fonction permettant de dessiner un cercle de rayon donné

def dessin_Cercle(r): 
    circle(r)
    '''
    Objectifs : Dessiner un cercle 
    Méthode : Utiliser la fonction circle de la bibliothèque Turtle
    Besoins : r
    Connus : -
    Entrées : r
    Sorties : -
    Résultats : Un cercle de rayon r
    Hypothèses : r > 0 
    '''
    

# Créer une fonction permettante de dessiner un demi cercle de rayon donné

def dessin_Demi_Cercle(r):
    '''
    Objectifs : Dessiner un demi cercle 
    Méthode : Utiliser la fonction circle de la bibliothèque Turtle
    Besoins : r
    Connus : -
    Entrées : r
    Sorties : -
    Résultats : Un demi cercle de rayon r
    Hypothèses : r > 0 
    '''
    circle(r,180)
    

# Créer une fonction permettant de dessiner un carré de coté donné

def dessin_Carre(a):
    '''
    Objectifs : Dessiner un carré 
    Méthode : Usage d'une structure itérative ainsi que les fonctions forward et left de Turtle
    Besoins : a
    Connus : -
    Entrées : a
    Sorties : -
    Résultats : Un carré de coté a
    Hypothèses : a > 0 
    '''
    t = Turtle()
    for i in range(4): 
        t.forward(a) 
        t.left(90)
    

# Créer une fonction permettant de dessiner un triangle de coté donné

def dessin_Triangle(a):
    '''
    Objectifs : Dessiner un triangle
    Méthode : Usage d'une structure itérative ainsi que les fonctions forward et left de Turtle
    Besoins : a
    Connus : -
    Entrées : a
    Sorties : -
    Résultats : Un triangle de coté a
    Hypothèses : a > 0 
    '''
    t = Turtle()
    for i in range(3):
        t.forward(a)
        t.left(120)
   

# Créer une fonction permettant de dessiner un rectangle de dimensions données

def dessin_Rectangle(a,b):
    '''
    Objectifs : Dessiner un rectangle
    Méthode : Usage d'une structure itérative ainsi que les fonctions forward et left de Turtle
    Besoins : a , b
    Connus : -
    Entrées : a , b
    Sorties : -
    Résultats : Un rectangle de dimensions a et b 
    Hypothèses : a > 0 ; b > 0
    '''
    t = Turtle()
    for i in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)
        

# Créer ue fonction permettant de créer un polygone paramétrable

def dessin_Polygone(a,b):
    '''
    Objectifs : Dessiner polygone 
    Méthode : Usage de la fonction circle de Turtle
    Besoins : a , b
    Connus : -
    Entrées : a , b
    Sorties : -
    Résultats : Un polygone de coté a et nombre de coté b
    Hypothèses : a > 0 , b > 0
    '''
    circle(a,steps=b)
    

#Créer un trapèze 
def dessin_Trapeze(base,angle,hauteur):
        '''
        Objectifs : Dessiner un trapèse
        Méthode : Usage de formules trigonométrique ainsi que les fonction foraward et left de Turtle
        Besoins : base, angle, hauteur
        Connus : -
        Entrées : base, angle, hauteur
        Sorties : -
        Résultats : Un trapèze de paramètres prédéfinis
        Hypothèses : base > 0, 0 < angle < 180 , hauteur > 0
        '''
   
        assert 0 < angle < 180
        import math
        slope = hauteur / math.sin(math.radians(angle))
        top = base - 2 * (hauteur / math.tan(math.radians(angle)))

        forward(base)
        left(180 - angle)
        forward(slope)
        left(angle)
        forward(top)
        left(angle)
        forward(slope)
        left(angle - 180)

def dessin_losange(a):
    '''
    Objectifs : Dessiner un losange 
    Méthode : Usage de la fonction circle de Turtle
    Besoins : a 
    Connus : -
    Entrées : a 
    Sorties : -
    Résultats : Un losange de coté a 
    Hypothèses : a > 0 
    '''
    circle(a,steps=4)



def dessin_Ellipse(rayon):
    '''
    Objectifs : Dessiner un ellipse
    Méthode : Usage d'une structure itérative ainsi que la fonction circle de Turtle
    Besoins : rayon
    Connus : -
    Entrées : rayon
    Sorties : -
    Résultats : Un ellipse de rayon connu
    Hypothèses : rayon > 0
    '''
    for i in range(2):
        circle(rayon,90)
        circle(rayon//2,90)
