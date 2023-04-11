# UML

L'UML est un langage de modélisation graphique qui permet de représenter des objets, leurs relations et leurs interactions.

On va voir ici principalement les diagrammes de classes et de séquences.

## Diagramme de classes

Un diagramme de classes est un diagramme UML qui permet de représenter les classes d'un système.

### Classes

Les classes sont représentées par des rectangles. Le nom de la classe est écrit en haut du rectangle.

la classe est découpée en 3 parties :

- nom de la classe
- attributs
- méthodes

*note : si une partie est vide, on ne la représente pas*

avant un attribut ou une méthode, on peut mettre un caractère qui indique son visibilité :

`+` : public

`-` : private

`#` : protected

`~` : package

On représente les attributs selon ce format :

`[visibilité] [nom] : [type]`

On représente les méthodes selon ce format :

`[visibilité] [nom]([paramètres]) : [type de retour]`

exemple :

```plantuml



```


### Relations