"""
Configuration pytest et fixtures partagées entre les tests.

Les fixtures définies ici sont disponibles dans tous les fichiers de test.
"""

import pytest
from src.app.core import Graph


@pytest.fixture
def empty_graph():
    """Graphe vide."""
    return Graph()


@pytest.fixture
def simple_graph():
    """
    Graphe simple :
        A --- B
              |
              C
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    return g


@pytest.fixture
def complete_graph():
    """
    Graphe complet K4 : tous les nœuds connectés.
    
    A, B, C, D où chaque nœud est connecté à tous les autres.
    """
    g = Graph()
    nodes = ["A", "B", "C", "D"]
    for i, n1 in enumerate(nodes):
        for n2 in nodes[i+1:]:
            g.add_edge(n1, n2)
    return g


@pytest.fixture
def disconnected_graph():
    """
    Graphe déconnecté avec deux composantes.
    
    Composante 1 : A - B
    Composante 2 : C - D
    """
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("C", "D")
    return g


@pytest.fixture
def linear_graph():
    """Graphe linéaire : A - B - C - D."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    return g


@pytest.fixture
def cyclic_graph():
    """Graphe avec cycle : A - B - C - D - A."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("D", "A")
    return g


@pytest.fixture
def diamond_graph():
    """
    Graphe en diamant :
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
