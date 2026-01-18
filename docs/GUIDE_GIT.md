# 🎓 Guide Git pour le projet

Ce guide explique comment utiliser Git efficacement pour le projet.

---

## 📋 Configuration initiale

### Première fois (séance 1)

```bash
# Configurer votre identité
git config user.name "Prénom Nom"
git config user.email "prenom.nom@reseau.eseo.fr"

# Vérifier la configuration
git config --list
```

---

## 🌳 Workflow Git recommandé

### Règle d'or
**Jamais de travail direct sur `main` !**

### Structure des branches

```
main (branche protégée)
  ├── feat/graph-structure    (Palier A)
  ├── feat/dfs-algorithm       (Palier B)
  ├── feat/bfs-algorithm       (Palier C)
  ├── feat/graph-problems      (Palier D)
  ├── feat/io-json             (Palier E)
  └── feat/ui-interface        (Palier F)
```

---

## 🔄 Cycle de travail typique

### 1. Créer une branche pour une nouvelle fonctionnalité

```bash
# S'assurer d'être à jour
git checkout main
git pull

# Créer et basculer sur une nouvelle branche
git checkout -b feat/graph-structure

# Vérifier sur quelle branche on est
git branch
```

### 2. Travailler et commiter régulièrement

**⚠️ IMPORTANT : Commits granulaires !**

Par exemple, pour le **Palier A (Séance 2)**, faire plusieurs commits au lieu d'un seul :

```bash
# Premier commit : initialisation
git add src/app/core/graph.py
git commit -m "feat(graph): initialiser la structure de données"

# Deuxième commit : add_node
git add src/app/core/graph.py
git commit -m "feat(graph): implémenter add_node et has_node"

# Troisième commit : add_edge
git add src/app/core/graph.py
git commit -m "feat(graph): implémenter add_edge et neighbors"

# etc. (au moins 3-4 commits par palier)
```

**Règle d'or** : 1 commit = 1 fonction ou 1 tâche logique

```bash
# Voir les fichiers modifiés
git status

# Ajouter les fichiers modifiés
git add src/app/core/graph.py
# ou tout ajouter (attention !)
git add .

# Commiter avec un message clair
git commit -m "feat(core): implémenter add_node et add_edge"

# Voir l'historique
git log --oneline
```

### 3. Pousser sa branche sur le dépôt distant

```bash
# Première fois (créer la branche distante)
git push -u origin feat/graph-structure

# Fois suivantes
git push
```

### 4. Créer une Pull Request (sur GitHub/GitLab)

1. Aller sur le site du dépôt
2. Cliquer sur "New Pull Request"
3. Sélectionner : `feat/graph-structure` → `main`
4. Remplir la description
5. Demander une revue à un coéquipier

### 5. Merger après validation

Une fois la PR approuvée :
```bash
# Retourner sur main
git checkout main

# Récupérer les changements (incluant le merge)
git pull

# Supprimer la branche locale (optionnel)
git branch -d feat/graph-structure
```

---

## 📝 Convention de messages de commit

Format recommandé :
```
<type>(<scope>): <description>

[corps optionnel]
```

### Types
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `test`: Ajout/modification de tests
- `refactor`: Refactoring de code
- `style`: Formatage, indentation

### Exemples
```bash
git commit -m "feat(core): implémenter la classe Graph"
git commit -m "test(graph): ajouter tests pour add_edge"
git commit -m "fix(algorithms): corriger boucle infinie dans DFS"
git commit -m "docs: compléter le README avec exemples"
```

---

## 🚨 Gérer les conflits

### Quand survient un conflit ?

Quand deux personnes modifient les mêmes lignes de code.

### Résolution

```bash
# Récupérer les dernières modifications
git pull

# Git signale un conflit
# CONFLICT (content): Merge conflict in src/app/core/graph.py
```

**Ouvrir le fichier en conflit :**
```python
<<<<<<< HEAD
def add_node(self, node):
    # Votre version
=======
def add_node(self, node: str):
    # Version du dépôt
>>>>>>> origin/main
```

**Résoudre manuellement :**
1. Supprimer les marqueurs `<<<<<<<`, `=======`, `>>>>>>>`
2. Garder la bonne version (ou fusionner les deux)
3. Sauvegarder

```bash
# Marquer comme résolu
git add src/app/core/graph.py

# Finaliser le merge
git commit -m "merge: résoudre conflit dans graph.py"

# Pousser
git push
```

---

## 🛠️ Commandes utiles

### Voir l'état actuel

```bash
git status           # Fichiers modifiés
git diff             # Voir les modifications en détail
git log --oneline    # Historique compact
git branch           # Lister les branches
```

### Annuler des modifications

```bash
# Annuler les modifications d'un fichier (non commité)
git checkout -- src/app/core/graph.py

# Annuler le dernier commit (garder les modifications)
git reset --soft HEAD~1

# Annuler le dernier commit (supprimer les modifications)
git reset --hard HEAD~1
```

### Récupérer du code perdu

```bash
# Voir tous les commits (même annulés)
git reflog

# Revenir à un commit spécifique
git checkout <hash-du-commit>
```

---

## 👥 Travail en équipe

### Bonne pratique : Revue de code

Avant de merger une Pull Request :
1. Un coéquipier lit le code
2. Vérifie que les tests passent
3. Fait des suggestions
4. Approuve la PR

### Communication

- ✅ Prévenir quand on travaille sur un fichier
- ✅ Pull régulièrement pour éviter les gros conflits
- ✅ Commits petits et fréquents
- ❌ Pas de `git push -f` (force push) sans accord

---

## 📊 Visualiser l'historique

### En ligne de commande
```bash
git log --oneline --graph --all
```

### Outils graphiques
- **GitHub Desktop**
- Extension VS Code : **GitLens**

---

## 🆘 Aide rapide

### Commandes essentielles par fréquence

**Très fréquent** (plusieurs fois par heure)
```bash
git status
git add .
git commit -m "..."
git push
```

**Fréquent** (plusieurs fois par jour)
```bash
git checkout -b feat/...
git pull
git log --oneline
```

**Occasionnel** (plusieurs fois par semaine)
```bash
git merge
git branch -d ...
```

---

## 🎯 Checklist avant chaque commit

- [ ] Code fonctionne (pas d'erreur)
- [ ] Tests passent (`pytest`)
- [ ] Fichiers inutiles exclus (pas de `__pycache__`, etc.)
- [ ] Message de commit clair

---

## 📚 Ressources

- **Pro Git (livre gratuit)** : https://git-scm.com/book/fr/v2
- **Learn Git Branching** : https://learngitbranching.js.org/?locale=fr_FR
- **Aide GitHub** : https://docs.github.com/fr
