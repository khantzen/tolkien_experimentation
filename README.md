Énoncé
---

- POS : Part Of Speech
- POS Tag:
    - NOUN
    - ADV
    - VERB
    - PUNCT

- Pour le fichier CHAPTER_1.txt

1. Coder un parser retournant toutes les suites de "POS Tag" suivant un pattern donné

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
search_pattern(arr, ['NOUN', ('and', 'CCONJ'), 'NOUN'])
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

 3. Récupérer toutes les phrases commençant par `And`