# Tests - Explorateur de graphes

Ce dossier contient tous les tests unitaires du projet, organisés par paliers.

## 🧪 Lancer les tests

### Tous les tests
```bash
pytest
```

### Tests d'un palier spécifique
```bash
pytest -m palier_a     # Graphe de base
pytest -m palier_b     # DFS
pytest -m palier_c     # BFS
pytest -m palier_d     # Problèmes
pytest -m palier_e     # I/O
```

### Tests d'un fichier spécifique
```bash
pytest tests/test_graph.py -v
pytest tests/test_algorithms_dfs.py -v
```

### Test individuel
```bash
pytest tests/test_graph.py::test_add_node -v
```

### Avec couverture de code
```bash
pytest --cov=src/app/core --cov-report=html
```

## ✅ Objectifs par séance

### Séance 2
**Objectif** : `test_graph.py` doit passer à 100%

### Séance 3
**Objectif** : `test_algorithms_dfs.py` doit passer à 100%

### Séance 4
**Objectif** : `test_algorithms_bfs.py` doit passer à 100%

### Séance 5
**Objectif** : `test_problems.py` doit passer à 100%

### Séance 7
**Objectif** : `test_io.py` doit passer à 100%

## 📊 Interpréter les résultats

```
tests/test_graph.py::test_add_node PASSED                  [  5%]
```
- ✅ `PASSED` : Test réussi
- ❌ `FAILED` : Test échoué (lire le message d'erreur)
- ⚠️ `SKIPPED` : Test ignoré (normal si palier non encore implémenté)

## 🐛 Débugger un test qui échoue

1. **Lire le message d'erreur** (en bas de la sortie pytest)
2. **Lancer le test seul** avec `-v` pour plus de détails
3. **Utiliser `pytest --pdb`** pour lancer le debugger sur échec
4. **Ajouter des `print()`** dans votre code pour inspecter

Exemple :
```bash
pytest tests/test_graph.py::test_add_node -v --pdb
```

## 📝 Bonnes pratiques

- ✅ Lancer les tests **avant chaque commit**
- ✅ Vérifier que **tous les tests d'un palier passent** avant de passer au suivant
- ✅ Ne pas modifier les tests (sauf si instructeur le demande)
- ✅ Comprendre **pourquoi** un test échoue, pas juste le faire passer

## 🎯 Critères de réussite pour le projet

- Tous les tests doivent passer
- Couverture de code > 80% sur le module `core`
- Code lisible et bien documenté
- Commits Git réguliers et clairs
