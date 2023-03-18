#UML

L'uml est un langage de modélisation qui permet de représenter des objets et leurs interactions.

## Diagramme de cas d'utilisation

Un diagramme de cas d'utilisation est un diagramme qui permet de représenter les interactions entre un acteur et un système.

## Dragramme de classe

Un diagramme de classe est un diagramme qui permet de représenter les classes d'un système.

Exemple de diagramme de classe:

```plantuml
@startuml classDiagramExemple
skinparam classAttributeIconSize 0

abstract class Dragon {
    - int power
    # int getPower()
    # void setPower(int power)
}

class Dragonite {
    - int pokemonNumber
    + int getPokemonNumber()
    + Dragonite(int power, int pokemonNumber)
}

Dragon <|-- Dragonite

note left of Dragonite
    This is a note
    on two lines
end note

@enduml
```