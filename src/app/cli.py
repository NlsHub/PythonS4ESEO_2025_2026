"""
Module cli
----------
Interface en ligne de commande pour le projet.

Permet de tester les algorithmes sans lancer l'UI.
Très utile pour debug et tests rapides.

Usage:
    python -m src.app.cli --load graph.json --dfs A
    python -m src.app.cli --load graph.json --bfs A --goal B
    python -m src.app.cli --create --nodes A B C --edges A-B B-C --save test.json
"""

import argparse
import sys
from pathlib import Path

from .core import (
    Graph,
    dfs,
    bfs,
    shortest_path,
    is_connected,
    load_graph,
    save_graph,
)


def create_parser() -> argparse.ArgumentParser:
    """
    Crée le parser d'arguments en ligne de commande.
    
    Returns:
        Parser configuré
    """
    parser = argparse.ArgumentParser(
        description="Explorateur de graphes - Interface CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  # Créer un graphe simple
  python -m src.app.cli --create --nodes A B C --edges A-B B-C --save graph.json
  
  # Charger et analyser
  python -m src.app.cli --load graph.json --info
  
  # Parcours DFS
  python -m src.app.cli --load graph.json --dfs A
  
  # Plus court chemin
  python -m src.app.cli --load graph.json --bfs A --goal C
        """
    )
    
    # Chargement/création
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--load", type=str, help="Charger un graphe depuis JSON")
    input_group.add_argument("--create", action="store_true", help="Créer un nouveau graphe")
    
    # Création de graphe
    parser.add_argument("--nodes", nargs="+", help="Liste des nœuds (si --create)")
    parser.add_argument("--edges", nargs="+", help="Liste des arêtes au format A-B (si --create)")
    
    # Sauvegarde
    parser.add_argument("--save", type=str, help="Sauvegarder le graphe en JSON")
    
    # Opérations
    parser.add_argument("--info", action="store_true", help="Afficher les infos du graphe")
    parser.add_argument("--dfs", type=str, help="Lancer DFS depuis un nœud")
    parser.add_argument("--bfs", type=str, help="Lancer BFS depuis un nœud")
    parser.add_argument("--goal", type=str, help="Nœud cible (pour chemin)")
    parser.add_argument("--connected", action="store_true", help="Vérifier la connexité")
    
    return parser


def build_graph_from_args(nodes: list[str], edges: list[str]) -> Graph:
    """
    Construit un graphe depuis les arguments CLI.
    
    Args:
        nodes: Liste des nœuds
        edges: Liste des arêtes au format "A-B"
    
    Returns:
        Le graphe construit
    
    Raises:
        ValueError: Si le format des arêtes est invalide
    """
    # TODO: implémenter
    # 1. Créer un graphe
    # 2. Ajouter les nœuds
    # 3. Parser et ajouter les arêtes (format "A-B")
    pass


def print_graph_info(graph: Graph):
    """
    Affiche des informations sur un graphe.
    
    Args:
        graph: Le graphe à analyser
    """
    # TODO: implémenter
    # Afficher: nombre de nœuds, arêtes, connexité, liste des nœuds
    pass


def main():
    """Point d'entrée du CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    # TODO: implémenter la logique principale
    # 
    # Structure suggérée:
    # 1. Charger ou créer le graphe
    # 2. Effectuer les opérations demandées
    # 3. Sauvegarder si --save
    # 4. Gérer les erreurs proprement
    
    try:
        # Chargement/création du graphe
        if args.load:
            print(f"Chargement du graphe depuis {args.load}...")
            graph = load_graph(args.load)
            print(f"✓ Graphe chargé ({len(graph)} nœuds)")
        elif args.create:
            if not args.nodes:
                print("Erreur: --nodes requis avec --create", file=sys.stderr)
                sys.exit(1)
            print("Création d'un nouveau graphe...")
            graph = build_graph_from_args(args.nodes, args.edges or [])
            print(f"✓ Graphe créé ({len(graph)} nœuds)")
        
        # Opérations
        if args.info:
            print_graph_info(graph)
        
        if args.dfs:
            # TODO: implémenter DFS
            pass
        
        if args.bfs:
            # TODO: implémenter BFS
            pass
        
        if args.connected:
            # TODO: implémenter vérification connexité
            pass
        
        # Sauvegarde
        if args.save:
            print(f"Sauvegarde dans {args.save}...")
            save_graph(graph, args.save)
            print("✓ Graphe sauvegardé")
    
    except Exception as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
