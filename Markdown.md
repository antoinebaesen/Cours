# Markdown

Le markdown est un langage de balisage léger qui permet de formater du texte. Il est utilisé par de nombreux sites web pour écrire des articles, des commentaires, des messages, etc.

## Sommaire

- [Markdown](#markdown)
  - [Sommaire](#sommaire)
  - [Syntaxe](#syntaxe)
    - [Titres](#titres)
    - [Listes](#listes)
    - [Gras](#gras)
    - [Italique](#italique)
    - [Lien](#lien)
    - [Images](#images)
    - [Code](#code)
    - [Bloc de code](#bloc-de-code)
    - [Citation](#citation)
    - [Tableau](#tableau)
    - [Ligne horizontale](#ligne-horizontale)
    - [Saut de ligne](#saut-de-ligne)
    - [Exemples](#exemples)
  - [Web](#web)
  - [Lien vers d'autres pages](#lien-vers-dautres-pages)
  - [Sommaire](#sommaire-1)

## Syntaxe

### Titres

Les titres sont définis par des caractères `#` en début de ligne. Plus il y a de caractères `#`, plus le titre est petit.

```markdown
# Titre 1

## Titre 2

### Titre 3
```

### Listes

Les listes sont définies par des caractères `-` ou `*` en début de ligne.

```markdown
- Liste 1
- Liste 2
- Liste 3
```

### Gras

Le gras est défini par des caractères `**` en début et fin de mot.

```markdown

**gras**
```

### Italique

L'italique est défini par des caractères `*` en début et fin de mot.

```markdown

*italique*
```

### Lien

Les liens sont définis par des caractères `[]` en début et fin de mot, et des caractères `()` en début et fin de lien.

```markdown

[lien](https://www.google.com)
```

### Images

Les images sont définies par des caractères `![]()` en début et fin de mot, et des caractères `()` en début et fin de lien.

```markdown

![image](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)
```

### Code

Le code est défini par des caractères `` ` `` en début et fin de mot.

```markdown

`code`
```

### Bloc de code

Le bloc de code est défini par des caractères ``` en début et fin de mot.

```markdown

```

### Citation

La citation est définie par des caractères `>` en début de ligne.

```markdown

> citation
```

### Tableau

Les tableaux sont définis par des caractères `|` en début et fin de ligne, et des caractères `-` en début de ligne.

```markdown

| Colonne 1 | Colonne 2 |
| --------- | --------- |
| Ligne 1   | Ligne 2   |
```

* On peut définir la largeur des colonnes en ajoutant des caractères `-` après le caractère `|` de début de ligne.

* On peut définir l'alignement des colonnes en ajoutant des caractères `:` après le caractère `|` de début de ligne.
    * Exemple : 
    ```
    | Colonne 1 | Colonne 2 |
    | :-------: | --------: |
    | Ligne 1   | Ligne 2   |
    ```
    * `:` à gauche : aligné à gauche
    * `:` de chaque coté : centré
    * `:` à droite : aligné à droite

### Ligne horizontale

La ligne horizontale est définie par des caractères `---` en début de ligne.

```markdown

---

```

### Saut de ligne

Le saut de ligne est défini par des caractères `  ` en fin de ligne.

```markdown

Ligne 1

Ligne 2
```

### Exemples

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| **2** | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
| **3** | 3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 |

## Web

    On peut ouvrir un fichier markdown dans un navigateur web pour le lire.

## Lien vers d'autres pages

    Pour mettre un lien vers une autre page, il suffit de mettre le nom du fichier markdown entre crochets, et le lien entre parenthèses.

    Exemple : [Markdown](Markdown.md)

    Si le fichier markdown est dans un dossier, il faut mettre le nom du dossier entre crochets, et le nom du fichier markdown entre parenthèses.

    Exemple : [Markdown](Dossier/Markdown.md)

    On peut mettre un lien vers une partie particulière d'un fichier markdown en ajoutant un `#` suivi du nom de la partie.

    Exemple : [Markdown](Dossier/Markdown.md#markdown)

## Sommaire

    Pour générer le sommaire, il suffit de mettre un lien vers une partie particulière d'un fichier markdown en ajoutant un `#` suivi du nom de la partie.

    Exemple : [Sommaire](#sommaire)

    Pour générer le sommaire automatiquement, il faut ajouter le code suivant en début de fichier markdown.

    ```markdown
<!-- TOC -->

- [Markdown](#markdown)
  - [Sommaire](#sommaire)
  - [Syntaxe](#syntaxe)
    - [Titres](#titres)
    - [Listes](#listes)
    - [Gras](#gras)
    - [Italique](#italique)
    - [Lien](#lien)
    - [Images](#images)
    - [Code](#code)
    - [Bloc de code](#bloc-de-code)
    - [Citation](#citation)
    - [Tableau](#tableau)
    - [Ligne horizontale](#ligne-horizontale)
    - [Saut de ligne](#saut-de-ligne)
    - [Exemples](#exemples)
  - [Web](#web)
  - [Lien vers d'autres pages](#lien-vers-dautres-pages)
  - [Sommaire](#sommaire-1)

<!-- /TOC -->
    ```

