## models

* Humains
    +  0 : Lancier
    +  2 : Worker
    +  4 : Archer
    +  6 : Griffon
    +  8 : Chevalier
    + 10 : Paladin
    + 12 : Mage
    + 14 : Engin de siege
* Orcs
    + 16 : Grunt
    + 18 : Peon
    + 20 : Warlock
    + 22 : Hog Rider
    + 24 : Head Hunter
    + 26 : Drake
    + 28 : Berserker
    + 30 : Engin de siege volé
* Elfes
    + 32 : Gnome
    + 34 : Ranger
    + 36 : Dryad
    + 38 : Druide
    + 40 : Assassin
    + 42 : Griffon
    + 44 : Golem
    + 46 : Treant
* Morts
    + 48 : Squelette guerrier
    + 50 : Esclave
    + 52 : Arbalétrier squelette
    + 54 : Spadassin mort
    + 56 : Chevalier de la mort
    + 58 : Wyrm
    + 60 : Liche mage noir
    + 62 : Engin de siege mort
* Neutres
    + 64 : Chauve souris
    + 66 : Dragon boule
    + 68 : Mage noir
    + 70 : Golem machine
    + 72 : Plante carnivore
    + 74 : Orc sauvage
    + 76 : Squelette
    + 78 : Slime
    + 80 : Araignée
    + 82 : Turtle shell
    + 84 : Grosoeil rose
    + 86 : Paladin noir
    + 88 : Mimic
    + 90 : Crab
    + 92 : Démon volant
    + 94 : Lizard
    + 96 : Rat assassin
    + 98 : Spectre
    + 100 : Loup Garou
    + 102 : Ver géant
* Stuffs
    + 104 : Hache
    + 112 : Faux
    + 113 : Arc
    + 116 : Arbalete
    + 119 : Marteau
    + 122 : Massue
    + 126 : Couteau
    + 131 : Carquois
    + 132 : Bouclier
    + 138 : Lance
    + 140 : Baton
    + 141 : Epée
    + 147 : Lance bois

Terrain : [Humain] 0 = plain, 1 = villes ; [Elfes] 2 = forêt, 3 = foret magique ; [Orcs] 4 = desert, 5 = aride ; [Mort] 6 = cimetière, 7 = neige

---

| Nom                       | Race              | Rg|  category | id | atk | vit | def | effet |
|---------------            |:----------------- |:-:| :--------:|:--:|:---:|:---:|:---:|:-----:|
| Lancier                   | Humain            | 1 | Lancier   | 0  |  1  |  2  |  3  | /
| Ouvrier                   | Humain            | 1 | Infanterie| 1  |  1  |  1  |  1  | Joué : donne +1/1 à un humain
| Archer                    | Humain            | 2 | Archer    | 2  |  3  |  2  |  2  | Humain joué : gagne +1 atk
| Cavalier                  | Humain            | 2 | Cavalier  | 3  |  2  |  5  |  3  | Attaque : donne +1/1 à un humain
| Chevalier                 | Humain            | 3 | Cavalier  | 4  |  5  |  6  |  3  | Attaque : gagne (1/1) pour chaque humain alliés
| Sorcier                   | Humain            | 3 | Magicien  | 5  |  4  |  3  |  2  | **Magie+1**. Humain joué : donne +_1_ pv aux autres
| Ingénieur                 | Humain            | 3 | Infanterie| 6  |  2  |  3  |  2  | Joué : donne +2/2 à vos humains
| Spadassin                 | Humain            | 4 | Guerrier  | 7  |  3  |  3  |  3  | **Bouclier**
| Piquier                   | Humain            | 4 | Lancier   | 8  |  4  |  3  |  3  | Joué : donne 3 pv à vos humains
| Magicien                  | Humain            | 5 | Magicien  | 9  |  6  |  4  |  4  | **Magie+1**. Start : fait _1_ dégats aux ennemis
| Griffon                   | Humain            | 5 | Volant    | 10 |  3  |  6  |  7  | Attaque : donne _2/2_ à un humain
| Paladin                   | Humain            | 6 | Guerrier  | 11 |  6  |  5  |  5  | **Bouclier**. Attaque : donne +1/1 à un humain
| Machine de siè            | Humain            | 6 | Colosse   | 12 |  4  |  2  |  8  | Humain joué : gagne +2/2
| Hypogriffe                | Humain            | 7 | Volant    | 13 |  8  |  6  |  6  | Humain joué : Donne +_2/2_ à un humain
| Char                      | Humain            | 7 | Colosse   | 14 |  4  |  2  | 10  | Start : hitRandom(son attaque * 2)
| | | |
| Gobelin                   | Orc               | 1 | Infanterie| 15 |  
| Grunt                     | Orc               | 1 | Guerrier  | 16 |  
| Grunt bleu                | Orc               | 2 | Guerrier  | 17 |
| Guerrier Orc              | Orc               | 2 | Guerrier  | 18 |
| Tireur orc                | Orc               | 3 | Archer    | 19 |
| Chaman                    | Orc               | 3 | Magicien  | 20 |
| Ingénieur Gobelin         | Orc               | 4 | Infanterie| 21 |
| Chasseur de têtes         | Orc               | 4 | Archer    | 22 |
| Cavalier Orc              | Orc               | 4 | Cavalier  | 23 |
| Sorcier Orc               | Orc               | 5 | Magicien  | 24 |
| Berserker                 | Orc               | 5 | Guerrier  | 25 |
| Drake                     | Orc               | 5 | Volant    | 26 |
| Monteur de sanglier       | Orc               | 6 | Cavalier  | 27 |
| Machine volée             | Orc               | 6 | Colosse   | 28 |
| Char volé                 | Orc               | 7 | Colosse   | 29 |
| Dragon                    | Orc               | 7 | Volant    | 30 |
| | | |
| Gnome                     | Elfe              | 1 | Infanterie| 31 |
| Archer Elfe               | Elfe              | 1 | Archer    | 32 |
| Assassin Elfe             | Elfe              | 2 | Lancier   | 33 |
| Druide                    | Elfe              | 2 | Magicien  | 34 |
| Tireur d'élite            | Elfe              | 3 | Archer    | 35 |
| Centaure                  | Elfe              | 3 | Cavalier  | 36 |
| Gnome artisan             | Elfe              | 3 | Infanterie| 37 |
| Aigle                     | Elfe              | 4 | Volant    | 38 |
| Chasseur de nuit          | Elfe              | 4 | Lancier   | 39 |
| Archidruide               | Elfe              | 4 | Magicien  | 40 |
| Tréant                    | Elfe              | 5 | Colosse   | 41 |
| Dryade                    | Elfe              | 5 | Cavalier  | 42 |
| Golem                     | Elfe              | 5 | Colosse   | 43 |
| Aigle royal               | Elfe              | 6 | Volant    | 44 |
| Ancient                   | Elfe              | 7 | Colosse   | 45 |
| Golem ancien              | Elfe              | 7 | Colosse   | 46 |
| | | |
| Guerrier Squelette        | Mort              | 1 | Lancier   | 47 |
| Goule esclave             | Mort              | 1 | Infanterie| 48 |
| Guerrier goule            | Mort              | 2 | Guerrier  | 49 |
| Arbalétrier               | Mort              | 3 | Archer    | 50 |
| Goule ouvrière            | Mort              | 3 | Infanterie| 51 |
| Soldat Spectre            | Mort              | 3 | Lancier   | 52 |
| Tireur de nuit            | Mort              | 4 | Archer    | 53 |
| Liche                     | Mort              | 4 | Magicien  | 54 |
| Gargouille                | Mort              | 4 | Volant    | 55 |
| Chavalier mort            | Mort              | 5 | Cavalier  | 56 |
| Canon des cranes          | Mort              | 5 | Colosse   | 57 |
| Archiliche                | Mort              | 6 | Magicien  | 58 |
| Wyrm                      | Mort              | 6 | Volant    | 59 |
| Faucheuse                 | Mort              | 7 | Cavalier  | 60 |
| Artillecrane              | Mort              | 7 | Colosse   | 61 |
| | | |
| Slime                     | Monstre           | 1 | Infanterie| 62 |  1  |  3  |  1  | Troupe : donne +2/2 aux alliés
| Chauve souris             | Mob/Mort          | 1 | Volant    | 63 |  2  |  4  |  1  | Start : hit _1_
| Squelette                 | Monstre, Morts    | 1 | Guerrier  | 64 |  1  |  2  |  3  | Mort : donne +(2) atk
| Carnivore                 | Monstre, Elfe     | 2 | Colosse   | 65 |  2  |  2  |  3  | Start : hit random atk
| Mimic                     | Monstre           | 2 | Guerrier  | 66 |  1  |  3  |  5  | Bouclier. Defense : hit 2 ennemi
| Orc sauvage               | Monstre, Orc      | 2 | Guerrier  | 67 |  2  |  2  |  3  | Bouclier. Joué : donne +2 pv à un guerrier
| Slime tortue              | Monstre           | 2 | Lancier   | 68 |  1  |  3  |  3  | Mort : hit _2_ tous
| Lezard                    | Monstre           | 2 | Infanterie| 69 |  4  |  4  |  2  | Kill : gagne 1 or
| Loup garou                | Monstre           | 2 | Infanterie| 70 |  3  |  3  |  2  | Kill : donne +1/1 à un allié
| Rat assassin              | Monstre           | 2 | Infanterie| 71 |  2  |  5  |  1  | Joué : donne 2 or
| Arachnide                 | Elfe, Monstre     | 2 | Colosse   | 72 |  2  |  2  |  5  | Monstre joué : donne +_1_ atk aux alliés
| Chauve souris vampire     | Monstre, Mort     | 3 | Volant    | 73 |  5  |  4  |  1  | Volant joué : vos volants gagnent 1 pv
| Squelette maudis          | Monstre, Morts    | 3 | Guerrier  | 74 |  3  |  3  |  3  | Mort : Donne +(2/3) à un allié
| Plantoïde                 | Monstre, Elfe     | 3 | Colosse   | 75 |  2  |  2  |  3  | Quand quelqu'un meurt : hit random _2_
| Observateur               | Monstre           | 3 | Magicien  | 76 |  3  |  3  |  3  | Joué : ajoute un perso aléatoire à la main
| Bouldragon                | Monstre           | 3 | Volant    | 77 |  2  |  3  |  2  | Attack : +1/1
| Slime tortue géant        | Monstre           | 3 | Lancier   | 78 |  2  |  2  |  3  | Mort : invoque slime tortue
| Slime géant               | Monstre           | 3 | Infanterie| 79 |  2  |  3  |  2  | Troupe : donne +5 pv aux alliés. Joué : donne +2 pv à un allié
| Golem                     | Monstre           | 3 | Colosse   | 80 |  4  |  1  |  1  | Magicien joué : gagne _2_ pv
| Crabe                     | Monstre           | 3 | Guerrier  | 81 |  3  |  3  |  3  | Quand quelqu'un meurt : gagne (2) pv
| Spectre                   | Monstre           | 3 | Infanterie| 82 |  4  |  4  |  1  | Mort : donne atk en atk à un allié
| Ver géant                 | Monstre           | 3 | Colosse   | 83 |  3  |  3  |  4  | Quand quelqu'un meurt : donne +1/1 à un allié
| Mage noir                 | Monstre           | 4 | Magicien  | 84 |  2  |  2  |  3  | Magie + 1. Start : hit _2_ ennemis
| Rat géant                 | Monstre           | 4 | Infanterie| 85 |  1  |  4  |  1  | Mort : donne +2 atk aux alliés
| Spectre noir              | Monstre           | 4 | Infanterie| 86 |  4  |  4  |  3  | Start : gagne magie en atk
| Loup garou alpha          | Monstre           | 4 | Infanterie| 87 |  3  |  4  |  2  | Kill : gagne 2/1
| Mimic géant               | Monstre           | 4 | Guerrier  | 88 |  2  |  1  |  6  | Bouclier. Defense : hit 2 les ennemis
| Assassin lézard           | Monstre           | 4 | Lancier   | 89 |  3  |  3  |  3  | Joué : donne Bouclier à un allié
| Craboss                   | Monstre           | 4 | Guerrier  | 90 |  4  |  4  |  4  | Bouclier. Start : gagne 2 pv
| Dragonet                  | Monstre           | 5 | Volant    | 91 |  3  |  4  |  5  | Attack : hiy atk adjacents
| Ver colosses              | Monstre           | 5 | Colosse   | 92 |  5  |  3  |  6  | Boost : gagne +1/1
| Reine arachnide           | Elfe, Monstre     | 5 | Colosse   | 93 |  3  |  3  |  9  | Joué monstre : donne +1/2 aux alliés
| Démon ailé                | Monstre           | 5 | Volant    | 94 |  4  |  4  |  6  | Quand quelqu'un meurt : gagne +1/1
| Golem ancien              | Monstre           | 5 | Colosse   | 95 |  0  |  1  | 10  | Personnage joué : donne +_1_ atk aux alliés
| Grosoeil                  | Monstre           | 5 | Magicien  | 96 |  5  |  3  |  5  | Magie + 1. Quand quelqu'un meurt : hit random _3_
| Chevalier noir            | Monstre           | 5 | Guerrier  | 97 |  5  |  1  |  8  | Bouclier. Kill : gagne +2/3
| Seigneur de l'ombre       | Monstre           | 6 | Magicien  | 98 |  7  |  3  |  5  | Magie + 2. Start : donne +8/8 à un allié
| Paladin noir              | Monstre           | 7 | Guerrier  | 97 |  8  |  1  |  8  | Bouclier. Quand quelqu'un meurt : donne (4/4) à un allié
| Archidémon                | Monstre           | 7 | Volant    | 98 |  6  |  5  |  7  | Attack : hit atk tous les ennemis
