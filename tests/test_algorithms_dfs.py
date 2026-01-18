"""
Tests pour DFS (Palier B - Séance 3)

Ces tests doivent passer après avoir implémenté les algorithmes DFS.

Commandes:
    pytest tests/test_algorithms_dfs.py -v
    pytest -m palier_b
"""

import pytest
from src.app.core import Graph, dfs, dfs_path


@pytest.fixture
def linear_graph():
    """Graphe linéaire : A - B - C - D"""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    return g


@pytest.fixture
def tree_graph():
    """
    Graphe en arbre:
           A
          / \\
         B   C
        /
       D
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    return g


@pytest.fixture
def cycle_graph():
    """Graphe avec cycle : A - B - C - D - A"""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("D", "A")
    return g


# ============================================================================
# Tests de base DFS
# ============================================================================

@pytest.mark.palier_b
def test_dfs_single_node():
    """DFS sur un graphe à un seul nœud."""
    g = Graph()
    g.add_node("A")
    result = dfs(g, "A")
    assert result == ["A"]


@pytest.mark.palier_b
def test_dfs_linear_graph(linear_graph):
    """DFS sur un graphe linéaire."""
    result = dfs(linear_graph, "A")
    assert len(result) == 4
    assert result[0] == "A"  # Commence par A
    assert set(result) == {"A", "B", "C", "D"}  # Tous les nœuds visités


@pytest.mark.palier_b
def test_dfs_tree_graph(tree_graph):
    """DFS sur un graphe en arbre."""
    result = dfs(tree_graph, "A")
    assert len(result) == 4
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D"}
    
    # Ordre spécifique attendu (voisins triés alphabétiquement)
    # Graphe:
    #     A
    #    / \
    #   B   C
    #  /
    # D
    #
    # DFS explore: A → voisins [B, C] → B avant C (ordre alpha)
    #            → A.B.D (DFS explore D complètement) → puis A.C
    # Résultat : [A, B, D, C]
    assert result == ["A", "B", "D", "C"]


@pytest.mark.palier_b
def test_dfs_cycle_graph(cycle_graph):
    """DFS sur un graphe avec cycle."""
    result = dfs(cycle_graph, "A")
    assert len(result) == 4
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D"}


@pytest.mark.palier_b
def test_dfs_disconnected():
    """DFS sur un graphe déconnecté visite uniquement la composante du départ."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    
    result = dfs(g, "A")
    assert set(result) == {"A", "B"}  # Ne visite pas C, D


@pytest.mark.palier_b
def test_dfs_nonexistent_start():
    """DFS avec un nœud de départ inexistant doit lever une erreur."""
    g = Graph()
    g.add_node("A")
    
    with pytest.raises(ValueError):
        dfs(g, "X")


# ============================================================================
# Tests DFS avec chemin
# ============================================================================

@pytest.mark.palier_b
def test_dfs_path_direct(linear_graph):
    """Trouver un chemin direct."""
    path = dfs_path(linear_graph, "A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"
    # Vérifier que c'est un chemin valide
    for i in range(len(path) - 1):
        assert linear_graph.has_edge(path[i], path[i+1])


@pytest.mark.palier_b
def test_dfs_path_tree(tree_graph):
    """Trouver un chemin dans un arbre."""
    path = dfs_path(tree_graph, "A", "D")
    assert path is not None
    assert path == ["A", "B", "D"]


@pytest.mark.palier_b
def test_dfs_path_same_node():
    """Chemin d'un nœud vers lui-même."""
    g = Graph()
    g.add_node("A")
    path = dfs_path(g, "A", "A")
    assert path == ["A"]


@pytest.mark.palier_b
def test_dfs_path_no_path():
    """Aucun chemin entre deux nœuds déconnectés."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    
    path = dfs_path(g, "A", "C")
    assert path is None


@pytest.mark.palier_b
def test_dfs_path_cycle(cycle_graph):
    """Trouver un chemin dans un graphe avec cycle."""
    path = dfs_path(cycle_graph, "A", "C")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "C"


# ============================================================================
# Tests de propriétés DFS
# ============================================================================

@pytest.mark.palier_b
def test_dfs_visits_all_reachable_nodes():
    """DFS visite tous les nœuds atteignables, et seulement ceux-là."""
    g = Graph()
    # Composante 1
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    # Composante 2
    g.add_edge("X", "Y")
    
    result = dfs(g, "A")
    assert set(result) == {"A", "B", "C"}


@pytest.mark.palier_b
def test_dfs_deterministic():
    """DFS doit être déterministe (voisins triés)."""
    g = Graph()
    g.add_edge("A", "C")
    g.add_edge("A", "B")
    g.add_edge("A", "D")
    
    # Doit visiter dans l'ordre alphabétique
    result1 = dfs(g, "A")
    result2 = dfs(g, "A")
    assert result1 == result2
