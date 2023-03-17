#JS

## Sommaire

- [Sommaire](#sommaire)
- [0 - Introduction](#0---introduction)
- [1 - Les bases](#1---les-bases)
  - [1.1 - Les variables](#11---les-variables)
  - [1.2 - Listes](#12---listes)
  - [1.3 - Les fonctions](#13---les-fonctions)
  - [1.4 - Les boucles](#14---les-boucles)
  - [1.5 - Les conditions](#15---les-conditions)
  - [1.6 - Les objets](#16---les-objets)
  - [1.7 - Les classes](#17---les-classes)
  - [1.8 - Les promesses](#18---les-promesses)
  - [1.9 - Les fonctions fléchées](#19---les-fonctions-fléchées)
  - [1.10 - Les modules](#110---les-modules)
  - [1.11 - Les imports](#111---les-imports)
  - [1.12 - Les API](#112---les-api)
  - [1.13 - Les fonctions asynchrones](#113---les-fonctions-asynchrones)
  - [1.14 - Modification de la page web](#114---modification-de-la-page-web)
    - [1.14.1 - La méthode innerHTML](#1141---la-méthode-innerhtml)
    - [1.14.2 - La méthode createElement](#1142---la-méthode-createelement)
    - [1.14.3 - La méthode appendChild](#1143---la-méthode-appendchild)
  - [1.15 - Les événements](#115---les-événements)
  - [1.16 - Les formulaires](#116---les-formulaires)
  - [1.17 - Les cookies](#117---les-cookies)
  - [1.18 - Les sessions](#118---les-sessions)
  - [1.19 - Query selector](#119---query-selector)
  - [1.20 - Query selector all](#120---query-selector-all)
  - [1.21 - JQUERY](#121---jquery)
    - [1.21.1 - Sélectionner un élément](#1211---sélectionner-un-élément)
    - [1.21.2 - Créer un élément](#1212---créer-un-élément)
    - [1.21.3 - Ajouter un élément](#1213---ajouter-un-élément)
    - [1.21.4 - Créer un événement](#1214---créer-un-événement)
    - [1.21.5 - Récupérer les données d'un formulaire](#1215---récupérer-les-données-dun-formulaire)
    - [1.21.6 - Récupérer les données d'un formulaire avec AJAX](#1216---récupérer-les-données-dun-formulaire-avec-ajax)
  - [1.22 - Les fichiers](#122---les-fichiers)
    - [1.22.1 - Créer un fichier](#1221---créer-un-fichier)
    - [1.22.2 - Lire un fichier](#1222---lire-un-fichier)
    - [1.22.3 - Supprimer un fichier](#1223---supprimer-un-fichier)
- [2 - Les frameworks](#2---les-frameworks)
- [3 - Bases de données](#3---bases-de-données)
  - [3.1 - Les bases de données relationnelles](#31---les-bases-de-données-relationnelles)
  - [3.2 - Utilisation en JS](#32---utilisation-en-js)
- [4 - Erreurs fréquentes](#4---erreurs-fréquentes)
  - [4.1 - SyntaxError](#41---syntaxerror)
  - [4.2 - ReferenceError](#42---referenceerror)
  - [4.3 - TypeError](#43---typeerror)
  - [4.4 - RangeError](#44---rangeerror)
  - [4.5 - EvalError](#45---evalerror)
  - [4.6 - URIError](#46---urierror)

## 0 - Introduction

Javascript est un langage de programmation qui permet de créer des sites web dynamiques. Il est utilisé pour créer des sites web, des applications mobiles, des jeux vidéos, des robots, des objets connectés, etc.

## 1 - Les bases

### 1.1 - Les variables

il existe 2 types de variables en javascript : les let et les const.

```js
let a = 1;
const b = 2;
```

Les let sont des variables qui peuvent être modifiées, les const sont des variables qui ne peuvent pas être modifiées.
/!\ Il est possible de modifier une constante si elle est un tableau ou un objet.
/!\ Il existait une troisième variable, les var, mais elles sont dépréciées et ne doivent plus être utilisées.

### 1.2 - Listes

Les listes sont des variables qui contiennent plusieurs valeurs. On peut les créer de plusieurs manières :

```js
let liste = [1, 2, 3];

let liste2 = new Array(1, 2, 3);

let liste3 = new Array(3);
liste3[0] = 1;
liste3[1] = 2;
liste3[2] = 3;
```

Pour accéder à une valeur d'une liste, on utilise l'index de la valeur dans la liste :

```js
let liste = [1, 2, 3];
console.log(liste[0]); // affiche 1
console.log(liste[1]); // affiche 2
console.log(liste[2]); // affiche 3
```

### 1.3 - Les fonctions

Les fonctions sont des morceaux de code qui peuvent être appelés plusieurs fois. Elles peuvent prendre des paramètres et renvoyer des valeurs.

```js
function maFonction(param1, param2) {
    return param1 + param2;
}

console.log(maFonction(1, 2)); // affiche 3
```

### 1.4 - Les boucles

Les boucles permettent de répéter un morceau de code plusieurs fois.

```js

// boucle for

for (let i = 0; i < 10; i++) {
    console.log(i);
}

// boucle while

let i = 0;

while (i < 10) {
    console.log(i);
    i++;
}

// boucle do while

let i = 0;

do {
    console.log(i);
    i++;
} while (i < 10);

// boucle for each
// Il permet de parcourir une liste et d'effectuer une action sur chaque élément

let liste = [1, 2, 3];

liste.forEach(function (element) {
    console.log(element);
});

// boucle for of
// Il correspond au for each de java

let liste = [1, 2, 3];

for (let element of liste) {
    console.log(element);
}

// boucle for in
// Il permet de parcourir les propriétés d'un objet

let objet = {
    a: 1,
    b: 2,
    c: 3
};

for (let propriete in objet) {
    console.log(propriete);
}
```

### 1.5 - Les conditions

Les conditions permettent d'exécuter un morceau de code si une condition est remplie.

```js

// if
if (condition) {
    // code
}

// if else

if (condition) {
    // code
} else {
    // code
}

// if else if else

if (condition) {
    // code
} else if (condition) {
    // code
} else {
    // code
}

// switch

switch (variable) {
    case valeur1:
        // code
        break;
    case valeur2:
        // code
        break;
    default:
        // code
        break;
}
```

### 1.6 - Les objets

Les objets sont des variables qui contiennent plusieurs propriétés.

```js

let objet = {
    propriete1: 1,
    propriete2: 2,
    propriete3: 3
};
```

Pour instancier un objet, on utilise le mot clé new :

```js

let objet = new Object();
```

Pour accéder à une propriété d'un objet, on utilise le point :

```js
console.log(objet.propriete1); // affiche la valeur de la propriété propriete1
```

### 1.7 - Les classes

Les classes sont des modèles qui permettent de créer des objets.

```js

class MaClasse {
    constructor(param1, param2) {
        this.propriete1 = param1;
        this.propriete2 = param2;
    }

    methode1() {
        return this.propriete1 + this.propriete2;
    }
}
```
Les constructeurs sont des fonctions qui sont appelées lors de l'instanciation d'un objet.

/!\ Les classes ne peuvent avoir qu'un seul constructeur.

Pour instancier un objet, on utilise le mot clé new :
```
let objet = new MaClasse(1, 2);

console.log(objet.methode1()); // affiche 3
```

### 1.8 - Les promesses

Les promesses permettent de gérer des actions asynchrones.

```js

let promesse = new Promise(function (resolve, reject) {
    // code
});

promesse.then(function (resultat) {
    // code
}).catch(function (erreur) {
    // code
});
```

### 1.9 - Les fonctions fléchées

Les fonctions fléchées sont des fonctions plus courtes et plus simples à écrire.
Aussi appelées arrow functions. Ou lambda en java.

```js

// fonction fléchée

let maFonction = (param1, param2) => {
    return param1 + param2;
};

// fonction fléchée avec un seul paramètre

let maFonction = param => {
    return param;
};

// fonction fléchée avec un seul paramètre et un seul retour

let maFonction = param => param;

// fonction fléchée avec plusieurs paramètres et un seul retour

let maFonction = (param1, param2) => param1 + param2;
```

### 1.10 - Les modules

Les modules permettent de découper un programme en plusieurs fichiers.

```js

// module.js

export function maFonction(param1, param2) {
    return param1 + param2;
}

// index.js

import { maFonction } from './module.js';

console.log(maFonction(1, 2)); // affiche 3
```

### 1.11 - Les imports

Les imports permettent d'importer des modules.

```js

// module.js

export function maFonction(param1, param2) {
    return param1 + param2;
}

// index.js

import { maFonction } from './module.js';

console.log(maFonction(1, 2)); // affiche 3
```

### 1.12 - Les API

Les API sont des interfaces qui permettent d'accéder à des données. Elles sont souvent utilisées pour récupérer des données depuis un serveur. Les API sont souvent au format JSON. Pour les utiliser, on utilise la fonction fetch.

```js

// API fetch

fetch('https://api.github.com/users/kevin-pierre')
    .then(function (reponse) {
        return reponse.json();
    })
    .then(function (donnees) {
        console.log(donnees);
    })
    .catch(function (erreur) {
        console.log(erreur);
    });
```

Cela permet de récupérer les données de l'utilisateur kevin-pierre sur github.

### 1.13 - Les fonctions asynchrones

Les fonctions asynchrones permettent d'exécuter du code de manière asynchrone. C'est à dire que le code suivant ne sera pas exécuté tant que le code asynchrone n'est pas terminé. Pour utiliser une fonction asynchrone, on utilise le mot clé async.

```js

// fonction asynchrone

async function maFonction() {
    let reponse = await fetch('https://api.github.com/users/kevin-pierre');
    let donnees = await reponse.json();
    console.log(donnees);
}

maFonction();
```

### 1.14 - Modification de la page web

Pour modifier le contenu d'une page web, on a plusieurs solutions.

#### 1.14.1 - La méthode innerHTML

La méthode innerHTML permet de selectionner (et donc de modifier) le contenu d'un élément HTML.

```js

// sélectionne l'élément HTML avec l'id "monElement"
let monElement = document.getElementById('monElement');

// modifie le contenu de l'élément

monElement.innerHTML = 'nouveau contenu';
```

#### 1.14.2 - La méthode createElement

La méthode createElement permet de créer un élément HTML.

```js

// crée un élément HTML
let monElement = document.createElement('div');

// modifie le contenu de l'élément

monElement.innerHTML = 'nouveau contenu';
```

#### 1.14.3 - La méthode appendChild

La méthode appendChild permet d'ajouter un élément HTML à un autre élément HTML.

```js

// sélectionne l'élément HTML avec l'id "monElement"
let monElement = document.getElementById('monElement');

// crée un élément HTML

let monElement2 = document.createElement('div');

// modifie le contenu de l'élément

monElement2.innerHTML = 'nouveau contenu';

// ajoute l'élément à l'élément parent

monElement.appendChild(monElement2);
```

### 1.15 - Les événements

Les événements permettent de déclencher une action lorsqu'un événement se produit.

```js

// sélectionne l'élément HTML avec l'id "monElement"

let monElement = document.getElementById('monElement');

// déclenche une action lorsqu'on clique sur l'élément

monElement.addEventListener('click', function () {
    console.log('click');
});
```

### 1.16 - Les formulaires

Les formulaires permettent de récupérer des données saisies par l'utilisateur.

```html

<form id="monFormulaire">
    <input type="text" name="nom" />
    <input type="text" name="prenom" />
    <input type="submit" value="Envoyer" />

    <div id="resultat"></div>

    <script src="index.js"></script>

</form>

```

```js

// sélectionne l'élément HTML avec l'id "monFormulaire"

let monFormulaire = document.getElementById('monFormulaire');

// déclenche une action lorsqu'on soumet le formulaire

monFormulaire.addEventListener('submit', function (e) {
    e.preventDefault();

    // récupère les données du formulaire

    let nom = document.querySelector('input[name="nom"]').value;
    let prenom = document.querySelector('input[name="prenom"]').value;

    // affiche les données dans le HTML

    document.getElementById('resultat').innerHTML = 'Bonjour ' + prenom + ' ' + nom;
});
```

### 1.17 - Les cookies

Les cookies sont des données stockées dans le navigateur de l'utilisateur. On peut les utiliser pour stocker des informations sur l'utilisateur.

```js

// crée un cookie

document.cookie = 'nom=kevin';

// récupère un cookie

let cookies = document.cookie.split(';');

console.log(cookies);
```

### 1.18 - Les sessions

Les sessions permettent de stocker des données côté serveur. On peut les utiliser pour stocker des informations sur l'utilisateur.

```js

// crée une session

req.session.nom = 'kevin';

// récupère une session

console.log(req.session.nom);
```

### 1.19 - Query selector

La méthode querySelector permet de sélectionner un élément HTML.

Il s'agit d'une méthode plus puissante que getElementById et getElementsByClassName. Elle permet de sélectionner un élément HTML avec un id, une classe ou les deux.

Attention, la méthode querySelector ne permet de sélectionner qu'un seul élément. Si plusieurs éléments correspondent à la sélection, seul le premier sera sélectionné.

```js

// sélectionne l'élément HTML avec l'id "monElement"

let monElement = document.querySelector('#monElement');

// sélectionne l'élément HTML avec la classe "maClasse"

let monElement2 = document.querySelector('.maClasse');

// sélectionne l'élément HTML avec l'id "monElement" et la classe "maClasse"

let monElement3 = document.querySelector('#monElement.maClasse');
```

### 1.20 - Query selector all

La méthode querySelectorAll permet de sélectionner plusieurs éléments HTML.

```js

// sélectionne tous les éléments HTML avec la classe "maClasse"

let mesElements = document.querySelectorAll('.maClasse');
```

### 1.21 - JQUERY

JQUERY est une librairie JS qui permet de simplifier le développement web.

JQuery permet de sélectionner des éléments HTML, de modifier leur contenu, de créer des événements, etc.

Il est possible d'utiliser JQuery en ajoutant le script suivant dans la page HTML :

```html

<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

```

#### 1.21.1 - Sélectionner un élément

La méthode $ permet de sélectionner un élément HTML.

```js

// sélectionne l'élément HTML avec l'id "monElement"

let monElement = $('#monElement');

// modifie le contenu de l'élément

monElement.html('nouveau contenu');
```

#### 1.21.2 - Créer un élément

La méthode $ permet de créer un élément HTML.

```js

// crée un élément HTML

let monElement = $('<div>');

// modifie le contenu de l'élément

monElement.html('nouveau contenu');
```

#### 1.21.3 - Ajouter un élément

La méthode append permet d'ajouter un élément HTML à un autre élément HTML.

```js

// sélectionne l'élément HTML avec l'id "monElement"

let monElement = $('#monElement');

// crée un élément HTML

let monElement2 = $('<div>');

// modifie le contenu de l'élément

monElement2.html('nouveau contenu');

// ajoute l'élément à l'élément parent

monElement.append(monElement2);
```

#### 1.21.4 - Créer un événement

La méthode on permet de créer un événement.

```js

// sélectionne l'élément HTML avec l'id "monElement"

let monElement = $('#monElement');

// déclenche une action lorsqu'on clique sur l'élément

monElement.on('click', function () {
    console.log('click');
});
```

#### 1.21.5 - Récupérer les données d'un formulaire

La méthode serializeArray permet de récupérer les données d'un formulaire.

```js

// sélectionne l'élément HTML avec l'id "monFormulaire"

let monFormulaire = $('#monFormulaire');

// déclenche une action lorsqu'on soumet le formulaire

monFormulaire.on('submit', function (e) {
    e.preventDefault();

    // récupère les données du formulaire

    let donnees = monFormulaire.serializeArray();

    console.log(donnees);
});
```

#### 1.21.6 - Récupérer les données d'un formulaire avec AJAX

AJAX est une technique qui permet de récupérer des données sans recharger la page.

La méthode ajax permet de récupérer les données d'un formulaire avec AJAX.

```js

// sélectionne l'élément HTML avec l'id "monFormulaire"

let monFormulaire = $('#monFormulaire');

// déclenche une action lorsqu'on soumet le formulaire

monFormulaire.on('submit', function (e) {
    e.preventDefault();

    // récupère les données du formulaire

    let donnees = monFormulaire.serializeArray();

    // envoie les données avec AJAX

    $.ajax({
        url: 'http://localhost:3000/formulaire',
        method: 'POST',
        data: donnees,
        success: function (data) {
            console.log(data);
        }
    });
});
```

### 1.22 - Les fichiers
	
Les fichiers permettent de stocker des données sur le disque dur de l'ordinateur.

#### 1.22.1 - Créer un fichier

La méthode writeFile permet de créer un fichier.

```js

// importe le module fs

const fs = require('fs');

// crée un fichier

fs.writeFile('monFichier.txt', 'contenu du fichier', function (err) {
    if (err) {
        console.log(err);
    }
});
```

#### 1.22.2 - Lire un fichier

La méthode readFile permet de lire un fichier.

```js

// importe le module fs

const fs = require('fs');

// lit un fichier

// le contenu du fichier est stocké dans la variable data

data = fs.readFile('monFichier.txt', function (err, data) {
    if (err) {
        console.log(err);
    }
});
```

#### 1.22.3 - Supprimer un fichier

La méthode unlink permet de supprimer un fichier.

```js

// importe le module fs

const fs = require('fs');

// supprime un fichier

fs.unlink('monFichier.txt', function (err) {
    if (err) {
        console.log(err);
    }
});
```


## 2 - Les frameworks

Il existe plusieurs frameworks pour le développement web. Les plus connus sont React, Angular et Vue.

Ils permettent de créer des applications web plus rapidement pour les développeurs qui ont déjà une certaine expérience.

## 3 - Bases de données

### 3.1 - Les bases de données relationnelles

Les bases de données relationnelles sont des bases de données qui permettent de stocker des données dans des tables. Les tables sont reliées entre elles par des clés étrangères.

### 3.2 - Utilisation en JS

Pour utiliser une base de données en JS, on utilise un ORM. Un ORM est un outil qui permet de faire le lien entre une base de données et un langage de programmation.

Les ORM les plus connus sont Sequelize et Mongoose.

plus d'informations sur :
https://www.npmjs.com/
MongoDB : https://www.mongodb.com/fr
Sequelize : https://sequelize.org/
Mongoose : https://mongoosejs.com/

## 4 - Erreurs fréquentes

### 4.1 - SyntaxError

Une erreur de syntaxe est une erreur qui survient lors de la compilation du code. Elle est souvent causée par une faute de frappe.

### 4.2 - ReferenceError

Une erreur de référence est une erreur qui survient lors de l'exécution du code. Elle est souvent causée par une faute de frappe.

### 4.3 - TypeError

Une erreur de type est une erreur qui survient lors de l'exécution du code. Elle est souvent causée par une mauvaise utilisation d'une fonction.

### 4.4 - RangeError

Une erreur de plage est une erreur qui survient lors de l'exécution du code. Elle est souvent causée par une mauvaise utilisation d'une fonction.

### 4.5 - EvalError

Une erreur d'évaluation est une erreur qui survient lors de l'exécution du code. Elle est souvent causée par une mauvaise utilisation d'une fonction.

### 4.6 - URIError

Une erreur d'URI est une erreur qui survient lors de l'exécution du code. Elle est souvent causée par une mauvaise utilisation d'une fonction.