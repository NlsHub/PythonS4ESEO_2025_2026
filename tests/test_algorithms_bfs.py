"""
Tests pour BFS (Palier C - Séance 4)

Ces tests doivent passer après avoir implémenté les algorithmes BFS.

Commandes:
    pytest tests/test_algorithms_bfs.py -v
    pytest -m palier_c
"""

import pytest
from src.app.core import Graph, bfs, bfs_path


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
        /     \\
       D       E
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    return g


@pytest.fixture
def diamond_graph():
    """
    Graphe en diamant:
         A
        / \\
       B   C
        \\ /
         D
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    return g


# ============================================================================
# Tests de base BFS
# ============================================================================

@pytest.mark.palier_c
def test_bfs_single_node():
    """BFS sur un graphe à un seul nœud."""
    g = Graph()
    g.add_node("A")
    result = bfs(g, "A")
    assert result == ["A"]


@pytest.mark.palier_c
def test_bfs_linear_graph(linear_graph):
    """BFS sur un graphe linéaire."""
    result = bfs(linear_graph, "A")
    assert len(result) == 4
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D"}
    # BFS explore par couches : A, puis B, puis C, puis D
    assert result == ["A", "B", "C", "D"]


@pytest.mark.palier_c
def test_bfs_tree_graph(tree_graph):
    """BFS sur un graphe en arbre."""
    result = bfs(tree_graph, "A")
    assert len(result) == 5
    assert result[0] == "A"
    
    # BFS par couches :
    # Graphe:
    #     A          Couche 0 : A
    #    / \         Couche 1 : B, C (ordre alpha)
    #   B   C       Couche 2 : D, E (ordre alpha)
    #  /     \
    # D       E
    #
    # BFS visite par couches : A (couche 0) → B, C (couche 1) → D, E (couche 2)
    # Résultat : [A, B, C, D, E]
    assert result == ["A", "B", "C", "D", "E"]


@pytest.mark.palier_c
def test_bfs_diamond_graph(diamond_graph):
    """BFS sur un graphe en diamant."""
    result = bfs(diamond_graph, "A")
    assert len(result) == 4
    
    # Couche 0 : A
    # Couche 1 : B, C
    # Couche 2 : D
    assert result == ["A", "B", "C", "D"]


@pytest.mark.palier_c
def test_bfs_disconnected():
    """BFS sur un graphe déconnecté visite uniquement la composante du départ."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    
    result = bfs(g, "A")
    assert set(result) == {"A", "B"}


@pytest.mark.palier_c
def test_bfs_nonexistent_start():
    """BFS avec un nœud de départ inexistant doit lever une erreur."""
    g = Graph()
    g.add_node("A")
    
    with pytest.raises(ValueError):
        bfs(g, "X")


# ============================================================================
# Tests BFS avec chemin (plus court chemin)
# ============================================================================

@pytest.mark.palier_c
def test_bfs_path_direct(linear_graph):
    """Trouver le plus court chemin."""
    path = bfs_path(linear_graph, "A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"
    assert len(path) == 4  # A-B-C-D


@pytest.mark.palier_c
def test_bfs_path_diamond(diamond_graph):
    """BFS trouve le plus court chemin dans un diamant."""
    path = bfs_path(diamond_graph, "A", "D")
    assert path is not None
    assert len(path) == 3  # A-B-D ou A-C-D (tous deux de longueur 3)
    # Avec tri alphabétique, devrait être A-B-D
    assert path == ["A", "B", "D"]


@pytest.mark.palier_c
def test_bfs_path_same_node():
    """Chemin d'un nœud vers lui-même."""
    g = Graph()
    g.add_node("A")
    path = bfs_path(g, "A", "A")
    assert path == ["A"]


@pytest.mark.palier_c
def test_bfs_path_no_path():
    """Aucun chemin entre deux nœuds déconnectés."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    
    path = bfs_path(g, "A", "C")
    assert path is None


@pytest.mark.palier_c
def test_bfs_path_optimal():
    """
    BFS trouve le chemin optimal (plus court en nombre d'arêtes).
    
    Graphe:
        A --- B
        |     |
        C --- D
    
    Chemin A->D : BFS trouve A-B-D ou A-C-D (longueur 2)
    (pas A-C-B-D qui serait trouvé par un mauvais algo)
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    
    path = bfs_path(g, "A", "D")
    assert path is not None
    assert len(path) == 3  # 2 arêtes


# ============================================================================
# Comparaison DFS vs BFS
# ============================================================================

@pytest.mark.palier_c
def test_bfs_vs_dfs_path_length(diamond_graph):
    """BFS garantit le plus court chemin, pas DFS."""
    from src.app.core import dfs_path
    
    bfs_result = bfs_path(diamond_graph, "A", "D")
    dfs_result = dfs_path(diamond_graph, "A", "D")
    
    assert bfs_result is not None
    assert dfs_result is not None
    
    # BFS trouve toujours le chemin optimal
    assert len(bfs_result) <= len(dfs_result)


# ============================================================================
# Tests de propriétés BFS
# ============================================================================

@pytest.mark.palier_c
def test_bfs_layer_order():
    """
    BFS visite par couches (tous les voisins avant leurs voisins).
    
    Graphe :
          A
         /|\\
        B C D
        |
        E
    
    Ordre : A (couche 0), B C D (couche 1), E (couche 2)
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")
    g.add_edge("B", "E")
    
    result = bfs(g, "A")
    
    # A en premier
    assert result[0] == "A"
    # B, C, D avant E
    e_index = result.index("E")
    b_index = result.index("B")
    c_index = result.index("C")
    d_index = result.index("D")
    
    assert b_index < e_index
    assert c_index < e_index
    assert d_index < e_index


@pytest.mark.palier_c
def test_bfs_deterministic():
    """BFS doit être déterministe (voisins triés)."""
    g = Graph()
    g.add_edge("A", "D")
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    
    result1 = bfs(g, "A")
    result2 = bfs(g, "A")
    assert result1 == result2
    
    # Ordre alphabétique des voisins
    assert result1 == ["A", "B", "C", "D"]
