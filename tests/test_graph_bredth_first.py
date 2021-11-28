from data_structure.graph_breadth_first.graph_breadth_first import *

def test_bredth_first():
    expected = [1, 2, 0, 3]
    
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    actual = g.graph_breadth_first(1)

