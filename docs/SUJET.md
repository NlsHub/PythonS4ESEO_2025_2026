# Sujet de projet - Explorateur de graphes interactif

**Contexte** : Projet fil rouge du semestre - Python S4 ESEO  
**Durée** : 12 séances de 2h  
**Modalité** : Équipes de 2-3 étudiants

---

## 🎯 Objectif

Développer une **application Python avec interface graphique** permettant de :
- Créer et manipuler des **graphes non orientés**
- Visualiser les **algorithmes de parcours** (DFS, BFS)
- Résoudre des **problèmes concrets** (chemins, connexité)
- Collaborer en utilisant **Git**

---

## 📋 Fonctionnalités attendues

### Cœur algorithmique (module `core`)

✅ **Structure de données** : Graphe non orienté basé sur une liste d'adjacence

✅ **Algorithmes de parcours** :
- DFS (Depth-First Search / Parcours en profondeur)
- BFS (Breadth-First Search / Parcours en largeur)

✅ **Problèmes sur graphes** :
- Vérifier la connexité : `is_connected(graph) -> bool`
- Nœuds atteignables : `reachable_from(graph, start) -> set[str]`
- Plus court chemin : `shortest_path(graph, start, goal) -> list[str] | None`

✅ **Import/Export** : Sauvegarder et charger des graphes au format JSON

### Interface graphique (module `ui`)

✅ **Visualisation** :
- Affichage graphique du graphe (nœuds et arêtes)
- Coloration des parcours DFS/BFS

✅ **Interactions** :
- Boutons pour lancer DFS/BFS
- Chargement/sauvegarde de graphes
- Ajout de nœuds et arêtes (via dialogues ou fichier)

### Bonus (optionnel)

🎁 **Interface en ligne de commande (CLI)** : Commandes pour tester les algorithmes sans UI  
🎁 **Animation des parcours** : Affichage pas à pas des parcours DFS/BFS  
🎁 **Détection de cycles** : Identifier les cycles dans le graphe  
🎁 **Composantes connexes** : Trouver les composantes séparées du graphe

**Note** : `src/app/cli.py` est fourni comme squelette. Son implémentation complète est un bonus optionnel.

---

## 🛠️ Contraintes techniques

### Langage et outils
- **Python 3.10+** obligatoire
- **Tkinter** pour l'interface graphique
- **pytest** pour les tests
- **Git** pour la gestion de versions

### Architecture imposée

```
src/app/
  ├── core/           # Cœur algorithmique (TESTABLE)
  │   ├── graph.py       → Structure de graphe
  │   ├── algorithms.py  → DFS, BFS, problèmes
  │   └── io.py          → Import/Export JSON
  └── ui/             # Interface graphique
      ├── app.py         → Fenêtre principale
      ├── controller.py  → Lien UI ↔ Core
      └── render.py      → Rendu visuel
```

### API à respecter

**Classe Graph** :
```python
graph.add_node(node: str) -> None
graph.add_edge(a: str, b: str) -> None
graph.remove_node(node: str) -> None
graph.remove_edge(a: str, b: str) -> None
graph.neighbors(node: str) -> list[str]  # ⚠️ Doit retourner triée !
graph.has_node(node: str) -> bool
graph.has_edge(a: str, b: str) -> bool
graph.nodes() -> list[str]
graph.edges() -> list[tuple[str, str]]
len(graph) -> int
```

**Algorithmes** :
```python
dfs(graph: Graph, start: str) -> list[str]
dfs_path(graph: Graph, start: str, goal: str) -> list[str] | None
bfs(graph: Graph, start: str) -> list[str]
bfs_path(graph: Graph, start: str, goal: str) -> list[str] | None
is_connected(graph: Graph) -> bool
reachable_from(graph: Graph, start: str) -> set[str]
shortest_path(graph: Graph, start: str, goal: str) -> list[str] | None
```

**Import/Export** :
```python
save_graph(graph: Graph, filepath: str | Path) -> None
load_graph(filepath: str | Path) -> Graph
graph_to_dict(graph: Graph) -> dict
dict_to_graph(data: dict) -> Graph
```

---


### Critères de réussite

✅ **Tous les tests passent** (5 fichiers de tests fournis)  
✅ **Application fonctionne sans erreur**  
✅ **Code propre et documenté**  
✅ **Git utilisé correctement**

---

## 📆 Jalons (deadlines)

| Séance | Palier | Tests à valider | Deadline |
|--------|--------|-----------------|----------|
| 2 | A | `test_graph.py` | Fin séance 2 |
| 3 | B | `test_algorithms_dfs.py` | Fin séance 3 |
| 4 | C | `test_algorithms_bfs.py` | Fin séance 4 |
| 5 | D | `test_problems.py` | Fin séance 5 |
| 7 | E | `test_io.py` | Fin séance 7 |
| 11 | F | UI fonctionnelle | Fin séance 11 |

**⚠️ Restitution finale : Séance 12**

---

## 🚀 Démarrage du projet

### 1. Cloner le dépôt
```bash
git clone <url-du-repo>
cd PythonS4ESEO_2025_2026
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -e ".[dev]"
```

### 3. Vérifier que les tests fonctionnent
```bash
pytest
```

Tous les tests vont échouer au début, c'est **normal** ! Votre objectif est de les faire passer progressivement.

### 4. Créer votre première branche
```bash
git checkout -b feat/setup
```

---

## 📚 Ressources fournies

✅ **Squelette de code complet** avec docstrings détaillées  
✅ **Tests progressifs** (5 fichiers, ~100 tests)  
✅ **Guide de séances** avec algorithmes expliqués  
✅ **Guide Git** avec workflow et exemples  
✅ **Grille d'évaluation** détaillée

---

## 🆘 Règles importantes

### ✅ Autorisé
- Documentation Python officielle
- Stackoverflow (pour syntaxe)
- Discussions entre groupes (concepts généraux)
- Utiliser les ressources fournies

### ❌ Interdit
- Copier-coller de code complet depuis Internet
- Utiliser des bibliothèques de graphes (NetworkX, etc.)
- Modifier les tests sans autorisation
- Générer du code avec ChatGPT/Copilot (sauf commentaires)

### ⚠️ En cas de doute
**Demandez à votre enseignant !**

---

## 💡 Conseils

1. **Suivez les paliers dans l'ordre** (A → B → C → D → E → F)
2. **Testez au fur et à mesure** (ne pas tout coder d'un coup)
3. **Commitez souvent** (petit commit > gros commit)
4. **Lisez les docstrings** (tout est expliqué)
5. **Comprenez avant de coder** (pas de copier-coller aveugle)

---

## 📞 Contact

**Questions sur le projet** : Posez-les en séance ou par email

**Problèmes Git** : Consultez `docs/GUIDE_GIT.md`

---

**Bon courage ! 🚀**
