"""
Tests pour les problèmes sur graphes (Palier D - Séance 5)

Tests pour is_connected, reachable_from, shortest_path.

Commandes:
    pytest tests/test_problems.py -v
    pytest -m palier_d
"""

import pytest
from src.app.core import Graph, is_connected, reachable_from, shortest_path


@pytest.fixture
def connected_graph():
    """Graphe connexe simple."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    return g


@pytest.fixture
def disconnected_graph():
    """Graphe avec deux composantes."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    return g


@pytest.fixture
def complete_graph():
    """Graphe complet K4."""
    g = Graph()
    nodes = ["A", "B", "C", "D"]
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            g.add_edge(n1, n2)
    return g


# ============================================================================
# Tests is_connected
# ============================================================================

@pytest.mark.palier_d
def test_is_connected_empty():
    """Un graphe vide est considéré connexe (convention)."""
    g = Graph()
    assert is_connected(g) is True


@pytest.mark.palier_d
def test_is_connected_single_node():
    """Un graphe avec un seul nœud est connexe."""
    g = Graph()
    g.add_node("A")
    assert is_connected(g) is True


@pytest.mark.palier_d
def test_is_connected_true(connected_graph):
    """Graphe connexe."""
    assert is_connected(connected_graph) is True


@pytest.mark.palier_d
def test_is_connected_false(disconnected_graph):
    """Graphe non connexe."""
    assert is_connected(disconnected_graph) is False


@pytest.mark.palier_d
def test_is_connected_complete(complete_graph):
    """Graphe complet est forcément connexe."""
    assert is_connected(complete_graph) is True


@pytest.mark.palier_d
def test_is_connected_three_components():
    """Graphe avec trois composantes."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    g.add_node("E")  # Nœud isolé
    assert is_connected(g) is False


# ============================================================================
# Tests reachable_from
# ============================================================================

@pytest.mark.palier_d
def test_reachable_from_single_node():
    """Nœud isolé : seulement lui-même est atteignable."""
    g = Graph()
    g.add_node("A")
    reachable = reachable_from(g, "A")
    assert reachable == {"A"}


@pytest.mark.palier_d
def test_reachable_from_connected(connected_graph):
    """Dans un graphe connexe, tous les nœuds sont atteignables."""
    reachable = reachable_from(connected_graph, "A")
    assert reachable == {"A", "B", "C", "D"}


@pytest.mark.palier_d
def test_reachable_from_disconnected(disconnected_graph):
    """Dans un graphe déconnecté, seulement la composante est atteignable."""
    reachable_a = reachable_from(disconnected_graph, "A")
    reachable_c = reachable_from(disconnected_graph, "C")
    
    assert reachable_a == {"A", "B"}
    assert reachable_c == {"C", "D"}


@pytest.mark.palier_d
def test_reachable_from_nonexistent():
    """Nœud inexistant doit lever une erreur."""
    g = Graph()
    g.add_node("A")
    
    with pytest.raises(ValueError):
        reachable_from(g, "X")


# ============================================================================
# Tests shortest_path
# ============================================================================

@pytest.mark.palier_d
def test_shortest_path_direct():
    """Plus court chemin direct."""
    g = Graph()
    g.add_edge("A", "B")
    path = shortest_path(g, "A", "B")
    assert path == ["A", "B"]


@pytest.mark.palier_d
def test_shortest_path_indirect(connected_graph):
    """Plus court chemin indirect."""
    path = shortest_path(connected_graph, "A", "D")
    assert path is not None
    assert len(path) == 4  # A-B-C-D


@pytest.mark.palier_d
def test_shortest_path_no_path(disconnected_graph):
    """Pas de chemin entre deux composantes."""
    path = shortest_path(disconnected_graph, "A", "C")
    assert path is None


@pytest.mark.palier_d
def test_shortest_path_same_node():
    """Chemin vers soi-même."""
    g = Graph()
    g.add_node("A")
    path = shortest_path(g, "A", "A")
    assert path == ["A"]


@pytest.mark.palier_d
def test_shortest_path_optimal():
    """
    Vérifie que shortest_path trouve vraiment le chemin optimal.
    
    Graphe :
        A - B - C
        |       |
        +-------+
    
    Chemin A->C : direct (A-C) est plus court que A-B-C
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("A", "C")  # Raccourci
    
    path = shortest_path(g, "A", "C")
    assert path == ["A", "C"]


@pytest.mark.palier_d
def test_shortest_path_complete(complete_graph):
    """Dans un graphe complet, tous les chemins font 1 arête."""
    path = shortest_path(complete_graph, "A", "D")
    assert len(path) == 2  # A-D direct


# ============================================================================
# Tests intégrés (plusieurs fonctions ensemble)
# ============================================================================

@pytest.mark.palier_d
def test_connected_implies_reachable():
    """Si un graphe est connexe, tous les nœuds sont atteignables depuis n'importe quel nœud."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")
    
    assert is_connected(g)
    
    for start in g.nodes():
        reachable = reachable_from(g, start)
        assert reachable == set(g.nodes())


@pytest.mark.palier_d
def test_shortest_path_exists_iff_reachable():
    """Un chemin existe si et seulement si le nœud cible est atteignable."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_node("C")  # Isolé
    
    # B est atteignable depuis A
    assert "B" in reachable_from(g, "A")
    assert shortest_path(g, "A", "B") is not None
    
    # C n'est pas atteignable depuis A
    assert "C" not in reachable_from(g, "A")
    assert shortest_path(g, "A", "C") is None


@pytest.mark.palier_d
def test_graph_properties():
    """
    Test intégré vérifiant plusieurs propriétés à la fois.
    
    Graphe :
        A --- B --- C
              |
              D
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("B", "D")
    
    # Connexité
    assert is_connected(g)
    
    # Atteignabilité
    assert reachable_from(g, "A") == {"A", "B", "C", "D"}
    
    # Plus courts chemins
    assert len(shortest_path(g, "A", "D")) == 3  # A-B-D
    assert len(shortest_path(g, "C", "D")) == 3  # C-B-D
