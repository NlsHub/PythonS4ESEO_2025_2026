"""
Tests pour le module Graph (Palier A - Séance 2)

Ces tests doivent TOUS passer avant de passer au palier B.

Commandes:
    pytest tests/test_graph.py -v
    pytest tests/test_graph.py::test_add_node -v
"""

import pytest
from src.app.core import Graph


# ============================================================================
# Tests de base (création, ajout de nœuds)
# ============================================================================

@pytest.mark.palier_a
def test_empty_graph():
    """Un graphe vide doit avoir 0 nœuds."""
    g = Graph()
    assert len(g) == 0
    assert g.nodes() == []
    assert g.edges() == []


@pytest.mark.palier_a
def test_add_node():
    """Ajouter un nœud doit augmenter le nombre de nœuds."""
    g = Graph()
    g.add_node("A")
    assert len(g) == 1
    assert g.has_node("A")
    assert "A" in g.nodes()


@pytest.mark.palier_a
def test_add_node_idempotent():
    """Ajouter deux fois le même nœud ne doit pas dupliquer."""
    g = Graph()
    g.add_node("A")
    g.add_node("A")
    assert len(g) == 1


@pytest.mark.palier_a
def test_add_multiple_nodes():
    """Ajouter plusieurs nœuds."""
    g = Graph()
    for node in ["A", "B", "C", "D"]:
        g.add_node(node)
    assert len(g) == 4
    assert sorted(g.nodes()) == ["A", "B", "C", "D"]


# ============================================================================
# Tests des arêtes
# ============================================================================

@pytest.mark.palier_a
def test_add_edge():
    """Ajouter une arête entre deux nœuds."""
    g = Graph()
    g.add_edge("A", "B")
    assert g.has_edge("A", "B")
    assert g.has_edge("B", "A")  # Non orienté !


@pytest.mark.palier_a
def test_add_edge_creates_nodes():
    """Ajouter une arête doit créer les nœuds s'ils n'existent pas."""
    g = Graph()
    g.add_edge("A", "B")
    assert g.has_node("A")
    assert g.has_node("B")
    assert len(g) == 2


@pytest.mark.palier_a
def test_edges_list():
    """Liste des arêtes doit être correcte."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    edges = g.edges()
    assert len(edges) == 2
    # Ordre normalisé : (a, b) où a < b
    assert ("A", "B") in edges
    assert ("B", "C") in edges


@pytest.mark.palier_a
def test_add_edge_idempotent():
    """Ajouter deux fois la même arête ne doit pas dupliquer."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "B")
    g.add_edge("B", "A")  # Même arête (non orienté)
    assert len(g.edges()) == 1


# ============================================================================
# Tests des voisins
# ============================================================================

@pytest.mark.palier_a
def test_neighbors():
    """Récupérer les voisins d'un nœud."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    neighbors = g.neighbors("A")
    assert sorted(neighbors) == ["B", "C"]


@pytest.mark.palier_a
def test_neighbors_sorted():
    """Les voisins doivent être triés (important pour DFS/BFS déterministes)."""
    g = Graph()
    g.add_edge("A", "Z")
    g.add_edge("A", "B")
    g.add_edge("A", "M")
    neighbors = g.neighbors("A")
    assert neighbors == ["B", "M", "Z"]  # Ordre alphabétique


@pytest.mark.palier_a
def test_neighbors_empty():
    """Un nœud isolé n'a pas de voisins."""
    g = Graph()
    g.add_node("A")
    assert g.neighbors("A") == []


@pytest.mark.palier_a
def test_neighbors_nonexistent_node():
    """Demander les voisins d'un nœud inexistant doit lever une erreur."""
    g = Graph()
    with pytest.raises(ValueError):
        g.neighbors("X")


# ============================================================================
# Tests de suppression
# ============================================================================

@pytest.mark.palier_a
def test_remove_node():
    """Supprimer un nœud."""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    g.remove_node("A")
    assert not g.has_node("A")
    assert len(g) == 1


@pytest.mark.palier_a
def test_remove_node_with_edges():
    """Supprimer un nœud doit supprimer ses arêtes."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.remove_node("A")
    assert not g.has_node("A")
    assert not g.has_edge("A", "B")
    assert not g.has_edge("A", "C")
    # B et C existent toujours
    assert g.has_node("B")
    assert g.has_node("C")


@pytest.mark.palier_a
def test_remove_nonexistent_node():
    """Supprimer un nœud inexistant doit lever une erreur."""
    g = Graph()
    with pytest.raises(ValueError):
        g.remove_node("X")


@pytest.mark.palier_a
def test_remove_edge():
    """Supprimer une arête."""
    g = Graph()
    g.add_edge("A", "B")
    g.remove_edge("A", "B")
    assert not g.has_edge("A", "B")
    assert not g.has_edge("B", "A")
    # Les nœuds existent toujours
    assert g.has_node("A")
    assert g.has_node("B")


@pytest.mark.palier_a
def test_remove_nonexistent_edge():
    """Supprimer une arête inexistante doit lever une erreur."""
    g = Graph()
    g.add_node("A")
    g.add_node("B")
    with pytest.raises(ValueError):
        g.remove_edge("A", "B")


# ============================================================================
# Tests avancés (graphes plus complexes)
# ============================================================================

@pytest.mark.palier_a
def test_complete_graph():
    """Graphe complet K4 (tous les nœuds connectés)."""
    g = Graph()
    nodes = ["A", "B", "C", "D"]
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            g.add_edge(n1, n2)
    
    assert len(g) == 4
    assert len(g.edges()) == 6  # K4 a 6 arêtes
    
    # Chaque nœud a 3 voisins
    for node in nodes:
        assert len(g.neighbors(node)) == 3


@pytest.mark.palier_a
def test_disconnected_graph():
    """Graphe avec deux composantes séparées."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    
    assert len(g) == 4
    assert len(g.edges()) == 2
    
    # A et B connectés
    assert "B" in g.neighbors("A")
    # Mais pas A et C
    assert "C" not in g.neighbors("A")


@pytest.fixture
def sample_graph():
    """Fixture : graphe exemple pour tests."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    return g


@pytest.mark.palier_a
def test_sample_graph_structure(sample_graph):
    """Vérifier la structure du graphe exemple."""
    g = sample_graph
    assert len(g) == 4
    assert len(g.edges()) == 4
    assert sorted(g.nodes()) == ["A", "B", "C", "D"]
