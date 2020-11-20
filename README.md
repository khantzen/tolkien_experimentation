Énoncé
---

- POS : Part Of Speech
- POS Tag:
    - NOUN
    - ADV
    - VERB
    - PUNCT
    ...
- token : Suite de charactère non nuls, encadrés par des espaces

- Pour le fichier CHAPTER_1.txt

1. Coder une fonction de recherche retournant toutes les suites de "POS Tag" correspondant à un pattern donné.

Exemple:
```python
search_pattern(arr, ['NOUN', 'CCONJ', 'NOUN'])
 [
 'talk and excitement',
 'childhood and coming',
 'history and character',
 'gold and silver',
 'Cabbages and potatoes',
 'sorts and shapes',
 'squib or cracker',
 ...
 ...
 ]
```

2. Modifier cette méthode afin de pouvoir chercher également sur les tokens

```python
search_pattern(arr, [(any,'NOUN'), ('and', 'CCONJ'), (any, 'NOUN')])
 [
 'talk and excitement',
 'childhood and coming',
 'history and character',
 'gold and silver',
 'Cabbages and potatoes',
 'sorts and shapes',
 'dragons and sunflowers',
 'ropes and poles',
 'tents and pavilions',
 'food and drink',
 'lunch and tea',
 'barkers and thunder
 ...
 ...
 ]
 ```

3. Donner la possibilité d'afficher x token à gauche et à droite du résultat la recherche
