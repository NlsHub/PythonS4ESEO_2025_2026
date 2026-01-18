# 🎯 Explorateur de graphes interactif

> **Projet fil rouge** – Python S4 – ESEO 2025/2026

## 📋 Description

Application Python avec interface graphique permettant de :
- Créer et manipuler des graphes (villes, réseaux, cartes...)
- Visualiser les algorithmes de parcours (DFS, BFS)
- Résoudre des problèmes concrets (chemins, accessibilité, connexité)
- Travailler en équipe avec Git

---

## 🏗️ Architecture du projet

```
graph-explorer/
  ├── src/
  │   └── app/
  │       ├── core/          # Cœur algorithmique (100% testable)
  │       │   ├── graph.py       → Structure de graphe
  │       │   ├── algorithms.py  → DFS, BFS, problèmes
  │       │   └── io.py          → Import/Export JSON
  │       ├── ui/            # Interface graphique
  │       │   ├── app.py         → Fenêtre principale
  │       │   ├── controller.py  → Liaison UI ↔ Core
  │       │   └── render.py      → Dessin du graphe
  │       └── cli.py         # Interface ligne de commande (bonus)
  └── tests/                 # Tests unitaires (jalons)
      ├── test_graph.py
      ├── test_algorithms_dfs.py
      ├── test_algorithms_bfs.py
      ├── test_problems.py
      └── test_io.py
```

---

## 🎓 Progression par séances

### ✅ Palier A – Graphe de base (Séance 2)
**Tests à valider** : `test_graph.py`
- Créer un graphe non orienté
- Ajouter des nœuds et arêtes
- Récupérer les voisins

### ✅ Palier B – DFS (Séance 3)
**Tests à valider** : `test_algorithms_dfs.py`
- Implémenter DFS (parcours en profondeur)
- Retourner l'ordre de visite
- Trouver un chemin entre deux nœuds

### ✅ Palier C – BFS (Séance 4)
**Tests à valider** : `test_algorithms_bfs.py`
- Implémenter BFS (parcours en largeur)
- Retourner l'ordre de visite par couches
- Trouver le plus court chemin

### ✅ Palier D – Problèmes sur graphes (Séance 5)
**Tests à valider** : `test_problems.py`
- Vérifier la connexité d'un graphe
- Trouver tous les nœuds atteignables
- Calculer le plus court chemin (wrapper BFS)

### ✅ Palier E – Import/Export (Séance 7)
**Tests à valider** : `test_io.py`
- Sauvegarder un graphe en JSON
- Charger un graphe depuis JSON
- Gérer les erreurs de fichier

### ✅ Palier F – Interface graphique (Séances 6-8)
**Pas de tests automatisés**
- Afficher le graphe
- Boutons DFS/BFS
- Animation/coloration des parcours

---

## 🚀 Installation & utilisation

### Prérequis
- Python 3.10+
- pip

### Installation
```bash
# Cloner le dépôt
git clone <votre-repo>
cd PythonS4ESEO_2025_2026

# Créer un environnement virtuel (recommandé)
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -e .
```

### Lancer les tests
```bash
# Tous les tests
pytest

# Tests d'un palier spécifique
pytest tests/test_graph.py
pytest tests/test_algorithms_dfs.py -v

# Avec couverture de code
pytest --cov=src/app/core
```

### Lancer l'application
```bash
# Interface graphique
python -m src.app.ui.app

# Ligne de commande (bonus)
python -m src.app.cli --help
```

---

## 📊 Évaluation

- **Projet** : 55% (code + architecture + tests)
- **Git** : 15% (commits, branches, collaboration)
- **Oral/Restitution** : 30% (démo + explications techniques)

---

## 📦 API Core (contrat à respecter)

### `Graph` (graph.py)
```python
graph.add_node(node: str) -> None
graph.add_edge(a: str, b: str) -> None
graph.remove_node(node: str) -> None
graph.remove_edge(a: str, b: str) -> None
graph.neighbors(node: str) -> list[str]
graph.has_node(node: str) -> bool
graph.has_edge(a: str, b: str) -> bool
graph.nodes() -> list[str]
graph.edges() -> list[tuple[str, str]]
```

### Algorithmes (algorithms.py)
```python
dfs(graph: Graph, start: str) -> list[str]
dfs_path(graph: Graph, start: str, goal: str) -> list[str] | None
bfs(graph: Graph, start: str) -> list[str]
bfs_path(graph: Graph, start: str, goal: str) -> list[str] | None
```

### Problèmes (algorithms.py)
```python
is_connected(graph: Graph) -> bool
reachable_from(graph: Graph, start: str) -> set[str]
shortest_path(graph: Graph, start: str, goal: str) -> list[str] | None
```

---

## 🛠️ Bonnes pratiques

### Git
- ✅ Commit réguliers et clairs
- ✅ Branches pour chaque fonctionnalité
- ✅ Pull requests avec revue de code
- ❌ Pas de `git push -f` sur main

### Code
- ✅ Noms de variables explicites
- ✅ Docstrings pour chaque fonction
- ✅ Gestion des cas d'erreur
- ✅ Tests avant merge

### Tests
- ✅ Un test = une fonctionnalité
- ✅ Noms de tests clairs (`test_add_node_increases_node_count`)
- ✅ Arrange / Act / Assert

---

## 🆘 Ressources

- **Documentation Python** : https://docs.python.org/fr/3/
- **Pytest** : https://docs.pytest.org/
- **Tkinter** : https://docs.python.org/3/library/tkinter.html
- **Git** : https://git-scm.com/book/fr/v2

---

## 👥 Équipe

*(Ajouter ici les noms des membres de votre groupe)*

- Membre 1
- Membre 2

---

## 📝 Notes de séances

### Séance 1 – Setup
- [ ] Repo créé
- [ ] Premier commit
- [ ] Structure du projet en place

### Séance 2 – Graphe
- [ ] `test_graph.py` passe

### Séance 3 – DFS
- [ ] `test_algorithms_dfs.py` passe

*(À compléter au fur et à mesure)*

---

**Bon courage ! 🚀**
