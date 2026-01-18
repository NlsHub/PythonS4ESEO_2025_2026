"""
Tests pour Import/Export (Palier E - Séance 7)

Tests pour save_graph et load_graph.

Commandes:
    pytest tests/test_io.py -v
    pytest -m palier_e
"""

import pytest
import json
from pathlib import Path
import tempfile
import os

from src.app.core import Graph, save_graph, load_graph
from src.app.core.io import graph_to_dict, dict_to_graph


@pytest.fixture
def temp_file():
    """Crée un fichier temporaire pour les tests."""
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    yield path
    # Cleanup
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def sample_graph():
    """Graphe exemple pour tests."""
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("A", "C")
    return g


# ============================================================================
# Tests graph_to_dict / dict_to_graph
# ============================================================================

@pytest.mark.palier_e
def test_graph_to_dict_empty():
    """Graphe vide vers dict."""
    g = Graph()
    data = graph_to_dict(g)
    assert data == {"nodes": [], "edges": []}


@pytest.mark.palier_e
def test_graph_to_dict_simple(sample_graph):
    """Graphe simple vers dict."""
    data = graph_to_dict(sample_graph)
    
    assert "nodes" in data
    assert "edges" in data
    assert set(data["nodes"]) == {"A", "B", "C"}
    assert len(data["edges"]) == 3


@pytest.mark.palier_e
def test_dict_to_graph_empty():
    """Dict vide vers graphe."""
    data = {"nodes": [], "edges": []}
    g = dict_to_graph(data)
    assert len(g) == 0


@pytest.mark.palier_e
def test_dict_to_graph_simple():
    """Dict simple vers graphe."""
    data = {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    g = dict_to_graph(data)
    
    assert len(g) == 3
    assert g.has_edge("A", "B")
    assert g.has_edge("B", "C")


@pytest.mark.palier_e
def test_dict_to_graph_invalid_missing_key():
    """Dict invalide (clé manquante) doit lever une erreur."""
    data = {"nodes": ["A", "B"]}  # Manque "edges"
    
    with pytest.raises(KeyError):
        dict_to_graph(data)


# ============================================================================
# Tests save_graph
# ============================================================================

@pytest.mark.palier_e
def test_save_graph_empty(temp_file):
    """Sauvegarder un graphe vide."""
    g = Graph()
    save_graph(g, temp_file)
    
    # Vérifier que le fichier existe
    assert os.path.exists(temp_file)
    
    # Vérifier le contenu
    with open(temp_file, "r") as f:
        data = json.load(f)
    assert data == {"nodes": [], "edges": []}


@pytest.mark.palier_e
def test_save_graph_simple(sample_graph, temp_file):
    """Sauvegarder un graphe simple."""
    save_graph(sample_graph, temp_file)
    
    with open(temp_file, "r") as f:
        data = json.load(f)
    
    assert "nodes" in data
    assert "edges" in data
    assert len(data["nodes"]) == 3
    assert len(data["edges"]) == 3


# ============================================================================
# Tests load_graph
# ============================================================================

@pytest.mark.palier_e
def test_load_graph_empty(temp_file):
    """Charger un graphe vide."""
    # Créer le fichier
    with open(temp_file, "w") as f:
        json.dump({"nodes": [], "edges": []}, f)
    
    g = load_graph(temp_file)
    assert len(g) == 0


@pytest.mark.palier_e
def test_load_graph_simple(temp_file):
    """Charger un graphe simple."""
    # Créer le fichier
    data = {
        "nodes": ["A", "B", "C"],
        "edges": [["A", "B"], ["B", "C"]]
    }
    with open(temp_file, "w") as f:
        json.dump(data, f)
    
    g = load_graph(temp_file)
    assert len(g) == 3
    assert g.has_edge("A", "B")
    assert g.has_edge("B", "C")


@pytest.mark.palier_e
def test_load_graph_nonexistent_file():
    """Charger un fichier inexistant doit lever une erreur."""
    with pytest.raises(FileNotFoundError):
        load_graph("nonexistent_file.json")


@pytest.mark.palier_e
def test_load_graph_invalid_json(temp_file):
    """Charger un fichier JSON invalide doit lever une erreur."""
    # Créer un fichier avec JSON invalide
    with open(temp_file, "w") as f:
        f.write("{invalid json")
    
    with pytest.raises(ValueError):
        load_graph(temp_file)


@pytest.mark.palier_e
def test_load_graph_missing_keys(temp_file):
    """Charger un fichier JSON avec clés manquantes doit lever une erreur."""
    # Créer un fichier avec structure incorrecte
    with open(temp_file, "w") as f:
        json.dump({"nodes": ["A", "B"]}, f)  # Manque "edges"
    
    with pytest.raises(KeyError):
        load_graph(temp_file)


# ============================================================================
# Tests round-trip (save puis load)
# ============================================================================

@pytest.mark.palier_e
def test_save_load_roundtrip(sample_graph, temp_file):
    """Sauvegarder puis charger doit donner un graphe identique."""
    # Sauvegarder
    save_graph(sample_graph, temp_file)
    
    # Charger
    g_loaded = load_graph(temp_file)
    
    # Vérifier l'égalité
    assert len(g_loaded) == len(sample_graph)
    assert set(g_loaded.nodes()) == set(sample_graph.nodes())
    assert set(g_loaded.edges()) == set(sample_graph.edges())


@pytest.mark.palier_e
def test_save_load_roundtrip_complex(temp_file):
    """Round-trip avec un graphe plus complexe."""
    # Créer un graphe
    g1 = Graph()
    for i in range(5):
        for j in range(i+1, 5):
            g1.add_edge(str(i), str(j))
    
    # Sauvegarder
    save_graph(g1, temp_file)
    
    # Charger
    g2 = load_graph(temp_file)
    
    # Vérifier l'égalité
    assert len(g1) == len(g2)
    assert set(g1.nodes()) == set(g2.nodes())
    assert set(g1.edges()) == set(g2.edges())


@pytest.mark.palier_e
def test_save_load_isolated_nodes(temp_file):
    """Round-trip avec des nœuds isolés."""
    g1 = Graph()
    g1.add_node("A")
    g1.add_node("B")
    g1.add_edge("C", "D")
    
    save_graph(g1, temp_file)
    g2 = load_graph(temp_file)
    
    assert set(g1.nodes()) == set(g2.nodes())
    assert g2.has_node("A")
    assert g2.has_node("B")
    assert len(g2.neighbors("A")) == 0


# ============================================================================
# Tests avec Path (pathlib)
# ============================================================================

@pytest.mark.palier_e
def test_save_graph_pathlib(sample_graph, temp_file):
    """Sauvegarder avec un objet Path."""
    path = Path(temp_file)
    save_graph(sample_graph, path)
    assert path.exists()


@pytest.mark.palier_e
def test_load_graph_pathlib(sample_graph, temp_file):
    """Charger avec un objet Path."""
    save_graph(sample_graph, temp_file)
    path = Path(temp_file)
    g = load_graph(path)
    assert len(g) == len(sample_graph)
