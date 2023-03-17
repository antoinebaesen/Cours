#Quelques concepts d'informatique

*note : les exemples sont en python*

<!-- TOC -->

- [1. Les bases](#1-les-bases)
  - [1.1. Les variables](#11-les-variables)
  - [1.2. Les types](#12-les-types)
  - [1.3. Les opérateurs](#13-les-opérateurs)
  - [1.4. Les fonctions](#14-les-fonctions)
  - [1.5. Les conditions](#15-les-conditions)
  - [1.6. Les boucles](#16-les-boucles)
- [2. POO](#2-poo)
  - [2.1. Les classes](#21-les-classes)
  - [2.2. Les attributs](#22-les-attributs)
  - [2.3. Les méthodes](#23-les-méthodes)
  - [2.4. L'héritage](#24-lhéritage)
  - [2.5. L'encapsulation](#25-lencapsulation)
  - [2.6. Le polymorphisme](#26-le-polymorphisme)
- [3. Récurcivité](#3-récurcivité)
  - [3.1. Exemple](#31-exemple)
  - [3.2. Quelques règles](#32-quelques-règles)
  - [3.3. Exemples d'utilisation de la récursivité](#33-exemples-dutilisation-de-la-récursivité)
- [4. Les exceptions](#4-les-exceptions)
  - [4.1. Exemple](#41-exemple)
  - [4.2. Les exceptions personnalisées](#42-les-exceptions-personnalisées)
- [5. Calcul de la complexité](#5-calcul-de-la-complexité)
  - [5.1. Les notations](#51-les-notations)
  - [5.2. Exemple](#52-exemple)
- [6. Les algorithmes de tri](#6-les-algorithmes-de-tri)
  - [6.1. Tri à bulles](#61-tri-à-bulles)
  - [6.2. Tri par insertion](#62-tri-par-insertion)
  - [6.3. Tri par sélection](#63-tri-par-sélection)
  - [6.4. Tri fusion](#64-tri-fusion)
  - [6.5. Tri rapide](#65-tri-rapide)
- [7. Les algorithmes de recherche](#7-les-algorithmes-de-recherche)
  - [7.1. Recherche séquentielle](#71-recherche-séquentielle)
  - [7.2. Recherche dichotomique](#72-recherche-dichotomique)
- [8. Calcul logique](#8-calcul-logique)
  - [8.1 Opérateurs logiques](#81-opérateurs-logiques)
  - [8.2. Opérateurs de comparaison](#82-opérateurs-de-comparaison)

<!-- /TOC -->

## 1. Les bases

### 1.1. Les variables

Les variables sont des conteneurs qui peuvent contenir des données. Elles sont définies par un nom et une valeur. La valeur peut être de n'importe quel type (entier, flottant, chaîne de caractères, booléen, liste, dictionnaire, etc.).

```python
a = 1

b = 2.5

c = "Hello World"

d = True
```

### 1.2. Les types

Les types sont des catégories de données. Les types les plus courants sont les entiers, les flottants, les chaînes de caractères, les booléens, les listes, les dictionnaires, etc.

```python

a = 1 # Entier

b = 2.5 # Flottant

c = "Hello World" # Chaîne de caractères

d = True # Booléen

e = [1, 2, 3] # Liste

f = {"a": 1, "b": 2} # Dictionnaire
```

### 1.3. Les opérateurs

Les opérateurs sont des symboles qui permettent de réaliser des opérations sur des données. Les opérateurs les plus courants sont les opérateurs arithmétiques, les opérateurs de comparaison, les opérateurs logiques, etc.

```python

a = 1 + 2 # Addition

b = 2 - 1 # Soustraction

c = 2 * 2 # Multiplication

d = 4 / 2 # Division

e = 4 // 2 # Division entière

f = 4 % 2 # Modulo
```

### 1.4. Les fonctions

Les fonctions sont des blocs de code qui permettent d'effectuer des opérations sur des données. Les fonctions les plus courantes sont les fonctions d'entrée/sortie, les fonctions mathématiques, les fonctions de manipulation de chaînes de caractères, etc.

```python

print("Hello World") # Affiche "Hello World" dans la console

len("Hello World") # Retourne la longueur de la chaîne de caractères
```

### 1.5. Les conditions

Les conditions sont des blocs de code qui permettent d'exécuter du code en fonction d'une condition. Les conditions les plus courantes sont les conditions if, les conditions elif, les conditions else, etc.

```python

if a == 1:
    print("a est égal à 1")
elif a == 2:
    print("a est égal à 2")
else:
    print("a est différent de 1 et 2")
```

### 1.6. Les boucles

Les boucles sont des blocs de code qui permettent d'exécuter du code en boucle. Les boucles les plus courantes sont les boucles for, les boucles while, etc.

```python

for i in range(10):
    print(i)

i = 0

while i < 10:
    print(i)
    i += 1
```

## 2. POO

La POO ou Programmation Orientée Objet est un paradigme de programmation qui permet de créer des objets à partir de classes. Les objets sont des instances de classes. Les classes sont des modèles qui permettent de créer des objets. Les classes sont définies par un nom, des attributs et des méthodes. Les attributs sont des variables qui sont propres à l'objet. Les méthodes sont des fonctions qui sont propres à l'objet.

Pour schématiser on peut dire que les classes sont des "moules" et les objets sont des "gâteaux" qui sont créés à partir des "moules".

### 2.1. Les classes

Les classes sont des modèles qui permettent de créer des objets. Les classes sont définies par un nom, des attributs et des méthodes. Les attributs sont des variables qui sont propres à l'objet. Les méthodes sont des fonctions qui sont propres à l'objet.

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person = Person("John Doe", 30)

person.say_hello()
```

Ici Person est une classe qui représente une personne. Mais Person est juste le "modèle" qui permet de créer des objets. Pour créer un objet à partir de la classe Person on utilise le mot clé "new" suivi du nom de la classe. Ici on crée un objet de type Person qui est stocké dans la variable person. On peut ensuite appeler la méthode say_hello() de l'objet person :

```python

mathieu = Person("Mathieu", 18)
# ici on crée un objet de type Person qui est stocké dans la variable mathieu
```

### 2.2. Les attributs

Les attributs sont des variables qui sont propres à l'objet. Les attributs sont définis dans la méthode __init__() de la classe.

Dans la classe Person on a défini deux attributs : name et age. Ces attributs sont accessibles depuis l'objet person.

### 2.3. Les méthodes

Les méthodes sont des fonctions qui sont propres à l'objet. Les méthodes sont définies dans la classe. Elle sont accessible depuis l'objet.

Dans la classe Person on a défini une méthode : say_hello(). Cette méthode est accessible depuis l'objet person.

Exemple :

```python

mathieu.say_hello()
# ici on appelle la méthode say_hello() de l'objet mathieu
```

### 2.4. L'héritage

L'héritage permet de créer des classes qui héritent des attributs et des méthodes d'une autre classe. On peut dire que la classe fille hérite de la classe mère.

Par exemple, si on veut définir une classe animal qui représentera tous les animaux et une classe chat qui représentera tous les chats, on peut dire que la classe chat hérite de la classe animal. Ainsi il en récupérera tous les attributs et toutes les méthodes.

```python 

class Animal:
    def __init__(self, name):
        self.name = name

    def roar(self):
        print("Roar !")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print("Meow !")

potiLeChat = Cat("Poti")
potiLeChat.roar() # poti le chat hérite de la méthode roar() de la classe Animal
potiLeChat.meow()
```

### 2.5. L'encapsulation

L'encapsulation permet de rendre les attributs et les méthodes privés. Cela signifie qu'ils ne sont pas accessibles depuis l'extérieur de la classe. (En python, Pour rendre un attribut ou une méthode privé il faut les préfixer par deux underscores.)

### 2.6. Le polymorphisme

Le polymorphisme permet de redéfinir une méthode dans une classe fille. Ainsi, la méthode de la classe fille sera appelée à la place de la méthode de la classe mère.

```python

class Animal:
    def __init__(self, name):
        self.name = name

    def roar(self):
        print("Roar !")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def roar(self):
        print("Meow !")

potiLeChat = Cat("Poti")

potiLeChat.roar() # Ici la méthode roar() de la classe Cat sera appelée, on aura donc "Meow !" qui sera affiché dans la console.
```

## 3. Récurcivité

La récursivité est un concept qui permet de résoudre un problème en le décomposant en plusieurs sous-problèmes. Le sous-problème est lui-même décomposé en plusieurs sous-problèmes, etc. Le sous-problème le plus simple est résolu et le résultat est utilisé pour résoudre le sous-problème précédent, etc.

### 3.1. Exemple

Voici un exemple de récursivité qui permet de calculer la factorielle d'un nombre.

```python

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

print(factorielle(5))

# 5 * factorielle(4)
# 5 * 4 * factorielle(3)
# 5 * 4 * 3 * factorielle(2)
# 5 * 4 * 3 * 2 * factorielle(1)
# 5 * 4 * 3 * 2 * 1 * factorielle(0)
# 5 * 4 * 3 * 2 * 1 * 1
```

*Une fonction qui s'appelle elle-même est dite récursive.*

### 3.2. Quelques règles

- Une fonction récursive doit avoir une condition d'arrêt. Sinon la fonction va s'appeler à l'infini.

- Une fonction récursive doit être appelée dans la fonction elle-même.

- Une fonction récursive doit être appelée avec des paramètres différents à chaque fois.

- Une fonction récursive doit être appelée avec des paramètres qui tendent vers la condition d'arrêt.

### 3.3. Exemples d'utilisation de la récursivité

- Calculer la somme des éléments d'une liste

```python

def somme(liste):
    if len(liste) == 0:
        return 0
    else:
        # ici on appelle la fonction somme() avec une liste qui contient tous les éléments de la liste sauf le premier
        return liste[0] + somme(liste[1:])
```

- Compter le nombre d'éléments d'une liste

```python

def compter(liste):
    if len(liste) == 0:
        return 0
    else:
        # ici on appelle la fonction compter() avec une liste qui contient tous les éléments de la liste sauf le premier
        return 1 + compter(liste[1:])
```

- Calculer la puissance d'un nombre

```python

def puissance(nombre, exposant):
    if exposant == 0:
        return 1
    else:
        # ici on appelle la fonction puissance() avec un exposant qui est égal à l'exposant - 1
        return nombre * puissance(nombre, exposant - 1)
```

*La récursivité est très puissante mais elle peut aussi être très gourmande en ressources. Il faut donc faire attention à ne pas l'utiliser dans des cas où elle n'est pas nécessaire.*


## 4. Les exceptions

Les exceptions sont des erreurs qui peuvent survenir lors de l'exécution d'un programme. Les exceptions sont gérées par des blocs try/except. Le bloc try contient le code qui peut générer une exception. Le bloc except contient le code qui sera exécuté si une exception est levée.

```python

try:
    # ici on met le code qui peut générer une exception
except:
    # ici on met le code qui sera exécuté si une exception est levée
```

### 4.1. Exemple

```python

try:
    print(1 / 0)
except:
    print("Une erreur est survenue")
```

### 4.2. Les exceptions personnalisées

On peut créer ses propres exceptions en créant une classe qui hérite de la classe Exception.

```python

class MonException(Exception):
    pass

try:

    raise MonException("Une erreur est survenue")

except MonException as e:
    print(e)
```

## 5. Calcul de la complexité

La complexité d'un algorithme est une mesure de la quantité de ressources nécessaires pour exécuter l'algorithme. Plus la complexité est faible, plus l'algorithme est performant.

### 5.1. Les notations

- O(n) : la complexité est proportionnelle à la taille de l'entrée.

- O(n²) : la complexité est proportionnelle au carré de la taille de l'entrée.

- O(log n) : la complexité est proportionnelle au logarithme de la taille de l'entrée. (logarithme en base 2)
    > cette complexité est très performante, elle est utilisée dans les algorithmes de tri.

Pour calculer la complexité d'un algorithme, on compte le nombre d'opérations effectuées par l'algorithme. On peut aussi utiliser des formules mathématiques pour calculer la complexité.

### 5.2. Exemple

```python

def somme(liste):
    somme = 0
    for i in liste:
        somme += i
    return somme

# la complexité de cette fonction est O(n)
# car on effectue n opérations (n = taille de la liste)
```

## 6. Les algorithmes de tri

Les algorithmes de tri sont des algorithmes qui permettent de trier une liste. Il existe plusieurs algorithmes de tri, chacun a ses avantages et ses inconvénients.

### 6.1. Tri à bulles

Le tri à bulles est un algorithme de tri qui consiste à comparer deux éléments consécutifs et à les échanger si l'élément de gauche est plus grand que l'élément de droite. On répète cette opération jusqu'à ce que la liste soit triée.

```python

def triABulles(liste):
    for i in range(len(liste) - 1):
        for j in range(len(liste) - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste
```

* Le tri à bulles est très simple à implémenter mais il est très lent. Sa complexité est O(n²).

### 6.2. Tri par insertion

Le tri par insertion est un algorithme de tri qui consiste à prendre un élément de la liste et à le placer à sa place dans la liste triée. On répète cette opération jusqu'à ce que la liste soit triée.

```python

def triParInsertion(liste):
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j - 1]:
            liste[j], liste[j - 1] = liste[j - 1], liste[j]
            j -= 1
    return liste
```

* Sa complexité est O(n²).

### 6.3. Tri par sélection

Le tri par sélection est un algorithme de tri qui consiste à prendre le plus petit élément de la liste et à le placer à la première position. On répète cette opération jusqu'à ce que la liste soit triée.

```python

def triParSelection(liste):
    for i in range(len(liste) - 1):
        min = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[min]:
                min = j
        liste[i], liste[min] = liste[min], liste[i]
    return liste
```

* La complexité de cet algorithme est O(n²).

### 6.4. Tri fusion

Le tri fusion est un algorithme de tri qui consiste à diviser la liste en deux listes de taille égale, à trier ces deux listes et à fusionner les deux listes triées.

```python

def triFusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        milieu = len(liste) // 2
        gauche = triFusion(liste[:milieu])
        droite = triFusion(liste[milieu:])
        return fusion(gauche, droite)

def fusion(liste1, liste2):

    liste = []

    while len(liste1) > 0 and len(liste2) > 0:
        if liste1[0] < liste2[0]:
            liste.append(liste1[0])
            liste1.pop(0)
        else:
            liste.append(liste2[0])
            liste2.pop(0)

    if len(liste1) > 0:
        liste += liste1
    else:
        liste += liste2

    return liste
```

> **La complexité de cet algorithme est O(n log n). C'est l'algorithme de tri le plus performant.**

* Il existe une autre version du tri fusion qui utilise une fonction récursive.

```python

def triFusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        milieu = len(liste) // 2
        gauche = triFusion(liste[:milieu])
        droite = triFusion(liste[milieu:])
        return fusion(gauche, droite)

def fusion(liste1, liste2):

    liste = []

    while len(liste1) > 0 and len(liste2) > 0:
        if liste1[0] < liste2[0]:
            liste.append(liste1[0])
            liste1.pop(0)
        else:
            liste.append(liste2[0])
            liste2.pop(0)

    if len(liste1) > 0:
        liste += liste1
    else:
        liste += liste2

    return liste
```

### 6.5. Tri rapide

Le tri rapide est un algorithme de tri qui consiste à prendre un élément de la liste et à placer tous les éléments plus petits à sa gauche et tous les éléments plus grands à sa droite. On répète cette opération sur les deux listes obtenues jusqu'à ce que la liste soit triée.

```python

def triRapide(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        gauche = []
        droite = []
        for i in range(1, len(liste)):
            if liste[i] < pivot:
                gauche.append(liste[i])
            else:
                droite.append(liste[i])
        return triRapide(gauche) + [pivot] + triRapide(droite)
```

* La complexité de cet algorithme est O(n log n). C'est un autre algorithme de tri le plus performant.

## 7. Les algorithmes de recherche

Les algorithmes de recherche sont des algorithmes qui permettent de rechercher un élément dans une liste. Il existe plusieurs algorithmes de recherche, chacun a ses avantages et ses inconvénients.

### 7.1. Recherche séquentielle

La recherche séquentielle est un algorithme de recherche qui consiste à parcourir la liste jusqu'à trouver l'élément recherché.

```python

def rechercheSequentielle(liste, element):
    for i in range(len(liste)):
        if liste[i] == element:
            return i
    return -1
```

* La complexité de cet algorithme est O(n).

### 7.2. Recherche dichotomique

La recherche dichotomique est un algorithme de recherche qui consiste à diviser la liste en deux listes de taille égale, à choisir la liste qui contient l'élément recherché et à répéter cette opération jusqu'à trouver l'élément recherché.

```python

def rechercheDichotomique(liste, element):
    debut = 0
    fin = len(liste) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        if liste[milieu] == element:
            return milieu
        elif liste[milieu] < element:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1
```

* La complexité de cet algorithme est O(log n).

## 8. Calcul logique

### 8.1 Opérateurs logiques

Les opérateurs logiques sont des opérateurs qui permettent de réaliser des opérations logiques.

* L'opérateur **ET** est représenté par le symbole **&&** dans la plupart des languages et **and** en python. Il permet de vérifier si deux conditions sont vraies.

```python

a = 5

if a > 0 and a < 10:
    print("a est compris entre 0 et 10")
```

* L'opérateur **OU** est représenté par le symbole **||** dans la plupart des languages et **or** en python. Il permet de vérifier si au moins une des deux conditions est vraie.

```python

a = 5

if a < 0 or a > 10:
    print("a est inférieur à 0 ou supérieur à 10")
```

* L'opérateur **NON** est représenté par le symbole **!** dans la plupart des languages et **not** en python. Il permet de vérifier si une condition est fausse.

```python

a = 5

if not a > 0:
    print("a est inférieur ou égal à 0")
```

### 8.2. Opérateurs de comparaison

Les opérateurs de comparaison sont des opérateurs qui permettent de comparer deux valeurs.

* L'opérateur **==** permet de vérifier si deux valeurs sont égales.

```python

a = 5

if a == 5:
    print("a est égal à 5")
```

* L'opérateur **!=** permet de vérifier si deux valeurs sont différentes.

```python

a = 5

if a != 5:
    print("a est différent de 5")
```
* Le XOR est un opérateur logique qui permet de vérifier si deux conditions sont différentes.

il est représenté par le symbole **^** en python. Il permet de vérifier si au moins une des deux conditions est vraie mais pas les deux.

```python

a = 5

if a > 0 ^ a < 10:
    print("a est inférieur à 0 ou supérieur à 10")
```

* L'opérateur **<** permet de vérifier si une valeur est inférieure à une autre.

```python

a = 5

if a < 5:
    print("a est inférieur à 5")
```

* Tous les autres opérateurs de comparaison sont similaires. Ils sont représentés par **<=** pour inférieur ou égal, **>** pour supérieur et **>=** pour supérieur ou égal.

Les opérateurs logiques et les opérateurs de comparaison peuvent être combinés pour réaliser des opérations logiques plus complexes.

```python

for i in range(20):
    if i > 0 and i < 10 and i != 5 or i == 12:
        print(i)

    # 1 2 3 4 6 7 8 9 12
```

> **Note :** Les opérateurs logiques et les opérateurs de comparaison ont la même priorité. Les opérateurs logiques sont évalués en premier. On peut utiliser des parenthèses pour changer l'ordre d'évaluation.

```python

for i in range(20):
    if (i > 0 and i < 10) and (i != 5 or i == 12):
        print(i)

    # 1 2 3 4 6 7 8 9
```

Les opérateurs logiques réalisent enfait des opérations bit à bit. Ce sont enfait des calculs binaires.

tableau de vérité des opérateurs logiques :

| a | b | a and b | a or b | not a | xor |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 |