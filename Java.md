JAVA
=========

Mise en forme : 
* les notes sont après un *note :
* le format est : *note : __texte__ (en gras)
    __un truc à changer__ : c'est les trucs à changer (y'a jamais de __ autour)
* les exemples sont dans les zones java, après les commentaires

# 0) SOMMAIRE :

* [1) IMPORTS](#1-imports)
* [2) CLASSES](#2-classes)
* [3) METHODES](#3-methodes)
* [4) VARIABLES](#4-variables)
    [4.1 Portée des variables](#41-portee-des-variables)
* [5) BOUCLES](#5-boucles)
    [5.1 For :](#51-for)
    [5.2 While :](#52-while)
    [5.3 Foreach :](#53-foreach)
* [6) STRUCTURES DE DONNEES](#6-structures-de-donnees)
    [6.1 TABLEAU](#61-tableau)
    [6.2 LISTE](#62-liste)
    [6.3 MAP](#63-map)
    [6.4 SET](#64-set)
    [6.5 INTERFACE](#65-interface)
* [7) HERITAGE](#7-heritage)
    [7.1 Classes abstraites](#71-classes-abstraites)
    [7.2 Classes filles](#72-classes-filles)
* [8) EXCEPTIONS](#8-exceptions)
* [9) ENUMERATIONS](#9-enumerations)
* [10) FICHIERS](#10-fichiers)
* [11) THREADS](#11-threads)
* [SPECIAL](#special-conception)
    [Conception](#special-conception)
    [Points virgules](#special-points-virgules)
    [Commentaires](#commentaires)
    [GIT](#git)
    [UML](#uml)


# 1) IMPORTS
les imports sont les classes externes que tu appel dans ton code. Si une autre classe est dans le meme "package" que la tienne, tu n'as pas besoin de l'importer.

    ```java
    /*
    import __nom de la classe__;
    */
    import java.util.Scanner;
    ```

# 2) CLASSES

    ```java
    /*
    public class __nom de la classe__ ((extends __nom de la classe parente__)) ((implements __nom de l'interface__)) {
    */
    public class Dragon extends Animal implements Volant {}
    // Le Dragon est un Animal et on peut lui appeler les méthodes de l'interface Volant
    ```

# 3) METHODES
static : la méthode est appelée depuis la classe et non depuis un objet (en gros elle est globale), comme la méthode main ou un constructeur global

    ```java
    /*
    public ((static)) __type de retour__ __nom de la méthode__ (__type du paramètre__ __nom du paramètre__) {
    */
    
    public static void main(String[] args) {}

    public void manger(Dragon quiQuiMange, Eatable quoiQuiEstManger) {}
    ```

# 4) VARIABLES
*static : la variable est globale à la classe et non à l'objet
*final : la variable ne peut pas être modifiée

## 4.1 Portée des variables
si tu précise pas ca sera private par défaut

*private : la variable ne peut pas être modifiée depuis l'extérieur de la classe (- en UML)
*protected : la variable peut être modifiée depuis les classes filles (# en UML)
*public : la variable peut être modifiée depuis n'importe où (+ en UML)

    ```java
    /*
    ((__portée de la variable__)) ((static)) ((final)) __type de la variable__ __nom de la variable__;
    */

    private static final int nombreDePattesDunDragon = 4;

    public Dragon didierLeDragon;
    ```

    *les variables globales sont en camelCase : nombreDePattesDunDragon

# 5) BOUCLES
## 5.1 For :

    ```java
    /*
        for (__type de l'élément__ __nom de l'élément__ = __valeur de départ__; __condition__; __incrémentation__) {
            //code
        }
    */

    for (int i = 0; i < 10; i++) {}

    for (int i = 0; i < list.Length; i += 2) {}
    ```

## 5.2 While :

    ```java
    /*
        while (__condition__) {
            //code
        }
    */  

    while (true) {}

    while (didier.isAlive()) {}
    ```

 * doWhile : pareil que while mais le code est executé au moins une fois

## 5.3 Foreach :
*note : foreach est une boucle qui ne peut être utilisée que sur des listes

    ```java
    /*
        for (__type de l'élément__ __nom de l'élément__ : __nom de la liste__) {
            //code
        }
    */

    for (String nom : listeDeNomsDeDragons) {}
    ```

# 6) STRUCTURES DE DONNEES
## 6.1 TABLEAU
un tableau est une structure de données qui permet de stocker des éléments de même type. Tu peux accéder à un élément du tableau en utilisant son indice (commence à 0). La taille du tableau est fixe.

### CREATION D'UN TABLEAU

    ```java
    /*
        __type de l'élément__[] __nom du tableau__ = new __type de l'élément__[__taille du tableau__];
    */

    int[] tableau = new int[10];
        
    Dragon[] dragons = new Dragon[10];
            
    ```

### ASSIGNATION DE VALEURS DANS UN TABLEAU

    ```java
    /*
        __type de l'élément__[] __nom du tableau__ = {__valeur 1__, __valeur 2__, __valeur 3__};
        OU
        __nom du tableau__[__indice de l'élément__] = __valeur__;
    */

    int[] tableau = {1, 2, 3};

    tableau[0] = 1;

    tableau[tableau.Length - 1] = 3; // pour la dernière case
    ```

### Tableau à 2 dimensions

```java
    /*
        __type de l'élément__[][] __nom du tableau__ = new __type de l'élément__[__taille du tableau__][__taille du tableau__];
    */

    int[][] tableau = new int[10][10];
```

    Les données sont stockées dans le tableau comme ça : [numéro de la ligne][numéro de la colonne]

```java
    int[][] tableau = new int[3][3];
    tableau[1][0] = 1;
    tableau[1][1] = 2;
    tableau[1][2] = 3;
```

tableau :

|0|0|0|
|-|-|-|
|1|2|3|
|0|0|0|


## 6.2 LISTE
une liste est une structure de données qui permet de stocker des éléments de même type (comme un tableau) mais qui peut être redimensionné dynamiquement. Donc tu peux ajouter des éléments à la liste sans avoir à redéfinir la taille du tableau.

### CREATION D'UNE LISTE
*note : ArrayList est UN type de liste, il y en a d'autres (mais celui là il est bien)

    ```java
    /*
        ArrayList<__type de l'élément__> __nom de la liste__ = new ArrayList<__type de l'élément__>();
    */

    ArrayList<String> listeDeNomsDeDragons = new ArrayList<String>();
    ```

### MODIDIER UNE LISTE
*Je te met toutes les fonctions pratiques de la liste (y'en a d'autres mais celles là sont les plus utilisées)
*PAS LENGTH pour la taille, c'est SIZE

    ```java
    /*
        AJOUTER
        __nom de la liste__.add(__valeur__);

        SUPPRIMER
        __nom de la liste__.remove(__indice de l'élément__);

        TROUVER UN ELEMENT PAR SON INDICE
        __nom de la liste__.get(__indice de l'élément__);

        MODIFIER UN ELEMENT PAR SON INDICE
        __nom de la liste__.set(__indice de l'élément__, __nouvelle valeur__);

        TAILLE DE LA LISTE
        __nom de la liste__.size();

        VIDER TOUT
        __nom de la liste__.clear();

        BOOLEEN, SI L'ELEMENT EST DANS LA LISTE
        __nom de la liste__.contains(__valeur__);

        RETOURNE L'INDICE DE L'ELEMENT
        __nom de la liste__.indexOf(__valeur__);

        BOOLEEN, SI LA LISTE EST VIDE
        __nom de la liste__.isEmpty();
    */

    listeDeNomsDeDragons.add("Didier");

    listeDeNomsDeDragons.remove(0);

    listeDeNomsDeDragons.get(0);

    listeDeNomsDeDragons.set(0, "Didier");

    listeDeNomsDeDragons.size();

    listeDeNomsDeDragons.clear();

    boolean didierEstLa = listeDeNomsDeDragons.contains("Didier");

    int indiceDeDidier = listeDeNomsDeDragons.indexOf("Didier");

    boolean listeVide = listeDeNomsDeDragons.isEmpty();
    ```

## 6.3 MAP
une map est une structure de données qui permet de stocker des éléments de même type mais qui est organisé en clé/valeur. Tu peux accéder à un élément de la map en utilisant sa clé.

### CREATION D'UNE MAP

    ```java
    /*
        HashMap<__type de la clé__, __type de la valeur__> __nom de la map__ = new HashMap<__type de la clé__, __type de la valeur__>();
    */

    HashMap<String, Integer> mapDeNomsDeDragonsEtDePoids = new HashMap<String, Integer>();
    ```

### MODIDIER UNE MAP

    ```java
    /*
        AJOUTER
        __nom de la map__.put(__clé__, __valeur__);

        SUPPRIMER
        __nom de la map__.remove(__clé__);

        TROUVER UNE VALEUR PAR SA CLE
        __nom de la map__.get(__clé__);

        TAILLE DE LA MAP
        __nom de la map__.size();

        VIDER TOUT
        __nom de la map__.clear();

        BOOLEEN, SI LA CLE EST DANS LA MAP
        __nom de la map__.containsKey(__clé__);

        BOOLEEN, SI LA VALEUR EST DANS LA MAP
        __nom de la map__.containsValue(__valeur__);

        BOOLEEN, SI LA MAP EST VIDE
        __nom de la map__.isEmpty();
    */

    mapDeNomsDeDragonsEtDePoids.put("Didier", 100);

    mapDeNomsDeDragonsEtDePoids.remove("Didier");

    mapDeNomsDeDragonsEtDePoids.get("Didier");

    mapDeNomsDeDragonsEtDePoids.size();

    mapDeNomsDeDragonsEtDePoids.clear();

    boolean didierEstLa = mapDeNomsDeDragonsEtDePoids.containsKey("Didier");

    boolean poidsDeDidierEstLa = mapDeNomsDeDragonsEtDePoids.containsValue(100);

    boolean mapVide = mapDeNomsDeDragonsEtDePoids.isEmpty();
    ```

## 6.4 SET
un set est une structure de données qui permet de stocker des éléments de même type mais qui ne peut pas contenir de doublons. Tu peux accéder à un élément de la map en utilisant son indice.
*c'est pas très utile mais si un jour on te demande d'en faire...

*ca marche comme une liste mais sans doublons

### CREATION D'UN SET

    ```java
    /*
        HashSet<__type de l'élément__> __nom du set__ = new HashSet<__type de l'élément__>();
    */

    HashSet<String> setDeNomsDeDragons = new HashSet<String>();
    ```

### MODIDIER UN SET

    ```java
    /*
        AJOUTER
        __nom du set__.add(__valeur__);

        SUPPRIMER
        __nom du set__.remove(__valeur__);

        TROUVER UN ELEMENT PAR SON INDICE
        __nom du set__.get(__indice de l'élément__);

        TAILLE DU SET
        __nom du set__.size();

        VIDER TOUT
        __nom du set__.clear();

        BOOLEEN, SI L'ELEMENT EST DANS LE SET
        __nom du set__.contains(__valeur__);

        BOOLEEN, SI LE SET EST VIDE
        __nom du set__.isEmpty();
    */

    setDeNomsDeDragons.add("Didier");

    setDeNomsDeDragons.remove("Didier");

    setDeNomsDeDragons.get(0);

    setDeNomsDeDragons.size();

    setDeNomsDeDragons.clear();

    boolean didierEstLa = setDeNomsDeDragons.contains("Didier");

    boolean setVide = setDeNomsDeDragons.isEmpty();
    ```

## 6.5 INTERFACE
une interface est une classe qui ne peut pas être instanciée (donc tu ne peux pas faire new __nom de la classe__). Elle sert à définir des méthodes qui seront implémentées dans les classes filles. Comme par exemple une interface "animal", elle existe pas toute seule mais ca regroupe tout ce qui est commun à tous les animaux (comme le fait qu'ils ont tous une couleur).

### CREATION D'UNE INTERFACE

    ```java
    /*
        interface __nom de l'interface__ {
            __attributs__
            __constructeur__
            __méthodes__
        }
    */

    interface Animal {
        String couleur;
        int positionX;
        int positionY;

        public Animal(String couleur, int positionX, int positionY) {
            this.couleur = couleur;
            this.positionX = positionX;
            this.positionY = positionY;
        }

        public void seDeplacer(int positionX, int positionY);
    }
    ```

### IMPLEMENTATION D'UNE INTERFACE

    ```java

    class Dragon implements Animal {
        String couleur;
        int positionX;
        int positionY;

        public Dragon(String couleur, int positionX, int positionY) {
            this.couleur = couleur;
            this.positionX = positionX;
            this.positionY = positionY;
        }

        public void seDeplacer(int positionX, int positionY) {
            this.positionX = positionX;
            this.positionY = positionY;
        }
    }
    ```

    *ca marche comme une classe abstraite mais tu peux pas instancier une interface
    La différence c'est que 
    - Interface = tu définis les méthodes mais tu ne les implémentes pas (aucun code, juste une liste de méthodes) communes
    - Classe abstraite = tu définis les méthodes et tu les implémentes (avec du code) communes (t'écris le code que tu veux dedans ou pas)

# 7) HERITAGE

## 7.1 CLASSES ABSTRAITES
une classe abstraite est une classe qui ne peut pas être instanciée (donc tu ne peux pas faire new __nom de la classe__). Elle sert à définir des méthodes qui seront implémentées dans les classes filles. Comme par exemple une classe "piece d'échec", elle existe pas toute seule mais ca regroupe tout ce qui est commun à toutes les pièces d'échec (comme le fait qu'elles ont toutes une couleur).

### CREATION D'UNE CLASSE ABSTRAITE

    ```java
    /*
        abstract class __nom de la classe__ {
            __attributs__
            __constructeur__
            __méthodes__
        }
    */

    abstract class PieceEchec {
        String couleur;
        int positionX;
        int positionY;

        public PieceEchec(String couleur, int positionX, int positionY) {
            this.couleur = couleur;
            this.positionX = positionX;
            this.positionY = positionY;
        }

        // méthode abstraite : elle n'a pas de corps, elle est juste déclarée pour être implémentée dans les classes filles et que tu puisse l'appeler sur n'importe quelle pièce (qui en hérite)
        public abstract void deplacer(int positionX, int positionY);
    }
    ```

### UTILISATION D'UNE CLASSE ABSTRAITE

    ```java
    /*
        __nom de la classe__ __nom de l'objet__ = new __nom de la classe__();
    */

    PieceEchec piece = new PieceEchec();
    ```

## 7.2 CLASSES FILLES
une classe fille est une classe qui hérite d'une classe mère. Elle peut donc utiliser toutes les méthodes et attributs de la classe mère. Elle peut aussi redéfinir des méthodes de la classe mère (comme par exemple la méthode toString() qui est redéfinie dans la classe String).

### CREATION D'UNE CLASSE FILLE

    ```java
    /*
        class __nom de la classe__ extends __nom de la classe mère__ {
            __attributs__
            __constructeur__
            __méthodes__
        }
    */

    class Cavalier extends PieceEchec {
        public Cavalier(String couleur, int positionX, int positionY) {
            super(couleur, positionX, positionY);
        }

        // redéfinition de la méthode deplacer de la classe mère
        public void deplacer(int positionX, int positionY) {
            this.positionX = positionX;
            this.positionY = positionY;
        }
    }
    ```

### UTILISATION D'UNE CLASSE FILLE

    ```java
    /*
        __nom de la classe__ __nom de l'objet__ = new __nom de la classe__();
    */

    Cavalier cavalier = new Cavalier();
    ```

# 8) EXCEPTIONS
## 8.1 EXCEPTIONS
une exception est une erreur qui peut arriver pendant l'exécution du programme. Par exemple, tu veux diviser un nombre par 0, tu vas avoir une exception. Il existe plusieurs types d'exceptions, tu peux les trouver [ici](https://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html).

### CREATION D'UNE EXCEPTION

    ```java
    /*
        try {
            __code qui peut lever une exception__
        } catch (__type de l'exception__) {
            __code à exécuter si une exception est levée__
        }
    */

    // le try catch permet de pas faire planter tout le programme en enfermant l'erreur dans un bloc try/catch

    try {
        int resultat = 1 / 0;
    } catch (ArithmeticException e) {
        System.out.println("Division par 0");
    }
    ```

# 9) ENUMERATIONS
## 9.1 ENUM
une énumération est une liste de valeurs possibles. Par exemple, tu peux créer une énumération pour les couleurs, et tu pourras utiliser les couleurs "rouge", "bleu", "vert" dans ton programme.
(c'est pas très très utile, c'est juste pour faire joli)

### CREATION D'UNE ENUMERATION

    ```java
    /*
        enum __nom de l'énumération__ {
            __valeur 1__,
            __valeur 2__,
            __valeur 3__,
            ...
        }
    */

    enum Couleur {
        ROUGE,
        BLEU,
        VERT
    }
    ```

### UTILISATION D'UNE ENUMERATION

    ```java
    /*
        __nom de l'énumération__ __nom de l'objet__ = __nom de l'énumération__.__valeur__;
    */

    Couleur couleur = Couleur.ROUGE;
    ```

# 10) FICHIERS
## 10.1 FICHIERS

### CREATION D'UN FICHIER

    ```java
    /*
        __nom de l'objet__ = new File(__chemin du fichier__);
    */

    File fichier = new File("C:\\Users\\Utilisateur\\Desktop\\fichier.txt");
    ```

### LECTURE D'UN FICHIER
*Scanner est une classe qui permet de lire un fichier, il y a d'autres classes qui permettent de lire des fichiers, comme BufferedReader, FileReader, etc...*

    ```java
    /*
        import java.util.Scanner; <- il faut importer la classe Scanner

        __nom de l'objet__ = new Scanner(__nom du fichier__);
        __lecture du fichier__
    */

    //dans la partie import
    import java.util.Scanner;

    Scanner scanner = new Scanner(fichier);
    String contenu = scanner.nextLine();
    ```

### ECRITURE DANS UN FICHIER
*je te donne une seule méthode, mais il y en a d'autres*

    ```java
    /*
        import java.io.FileWriter; <- il faut importer la classe FileWriter

        __nom de l'objet__ = new FileWriter(__nom du fichier__);
        __ecriture dans le fichier__
    */

    //dans la partie import
    import java.io.FileWriter;

    FileWriter writer = new FileWriter(fichier);
    writer.write("Bonjour");
    ```

# 11) THREADS
## 11.1 THREADS
un thread est un processus qui s'exécute en parallèle d'un autre processus. Par exemple, tu peux avoir un thread qui s'occupe de l'affichage, et un autre qui s'occupe de la logique du programme.
Ca permet de faire des choses en paralèlle et donc de découper le programme en plusieurs parties sur les différents coeurs de ton processeur.

### CREATION D'UN THREAD

    ```java
    /*
        __nom de la classe__ extends Thread {
            __attributs__
            __constructeur__
            __méthodes__
        }

        __nom de l'objet__ = new __nom de la classe__();
        __nom de l'objet__.start();
    */

    class MonThread extends Thread {
        public void run() {
            System.out.println("Bonjour");
        }
    }

    MonThread thread = new MonThread();
    thread.start();
    ```

# SPECIAL) CONCEPTION

## 1) CONCEPTION

Pour savoir si une classe en implémente (interface) une autre, en hérite une autre, etc...

### HERITAGE :
Etre de la classe parent, mais etre un truc plus précis
Animal <|--- Chat <|--- ChatGriffu

### INTERFACE :
Etre de la classe parent, pour avoir des méthodes obligatoires communes
Animal <|--- Chat
Animal <|--- Renard

Les deux doivent avoir les méthodes communes à l'interface

### COMPOSITION :
Etre de la classe parent, mais avoir un truc en plus
*C'est compliqué, t'occupe pas de ça (je note juste que ca existe)
Animal <|--- Chat <|--- ChatGriffu
Animal <|--- Renard

### AGGREGATION :
Etre de la classe parent, mais avoir un truc en plus
*C'est compliqué, t'occupe pas de ça (je note juste que ca existe)
Animal <|--- Chat <|--- ChatGriffu
Animal <|--- Renard

## POINTS VIRGULES :
 à la fin d'une instruction, pas après }

## COMMENTAIRES :
    // pour un commentaire sur une ligne
    /* pour un commentaire sur plusieurs lignes */

## GIT :
Git permet de gérer les versions de ton code, et de travailler en équipe sur un même projet. En envoyant des modifications sur le serveur, tu peux récupérer les modifications des autres personnes, et tu peux revenir à une version précédente du code.

### CREATION D'UN REPERTOIRE GIT
*(en local)
    ```bash
    git init
    ```

### CONNETION AU SERVEUR
Pour connecter un dépot local, au dépot sur le serveur

    ```bash
    git remote add origin __lien du serveur__
    ```

### AJOUTER DES FICHIERS
    ```bash
    git add __nom du fichier__
    ```

    *marche avec le REGEX donc tu peux faire :*
    ```bash
    git add *
    ```
    ou alors
    ```bash
    git add *.java
    ```

    *pour ajouter tous les fichiers*

### ENVOYER DES FICHIERS
    ```bash
    git commit -m "__message__"
    ```

### RECUPERER LES MODIFICATIONS
    ```bash
    git pull
    ```

### ENVOYER LES MODIFICATIONS
    ```bash
    git push
    ```

### CREER UNE BRANCHE
    ```bash
    git branch __nom de la branche__
    ```

### Problèmes de merge
Si tu as des conflits de merge, c'est que tu as modifié le même fichier que quelqu'un d'autre, et que tu as des modifications différentes. Il faut que tu résolves les conflits, et que tu commit à nouveau.

### RESOLUTION DES CONFLITS
    ```bash
    git status
    git add __nom du fichier__
    git commit -m "__message__"
    ```

### Problèmes de push
Si tu as des problèmes de push, c'est que tu as modifié le même fichier que quelqu'un d'autre, et que tu as des modifications différentes. Il faut que tu résolves les conflits, et que tu commit à nouveau.

### RESOLUTION DES CONFLITS
    ```bash
    git status
    git add __nom du fichier__
    git commit -m "__message__"
    ```
    
## UML
* la partie sur l'UML viendra après... (en DLC)
