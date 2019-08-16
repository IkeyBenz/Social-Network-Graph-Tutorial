from graph import Graph


def file_to_graph(file_path):
    lines = open(file_path).read().splitlines()

    g_type, _, edges = lines[0], lines[1], lines[2:]

    assert g_type in ['G', 'D', 'g', 'g'], "Unrecognized graph type"

    graph = Graph(g_type)

    for edge in map(string_to_tuple, edges):
        graph.add_edge(*edge)

    return graph


def string_to_tuple(string):
    """ Turns a string into a tuple object """
    # Remove front and back parenthesis:
    string = string[1:-1]

    # Split remainder by commas:
    elements = string.split(',')

    # Handle type casting for integers:
    elements = map(lambda s: int(s) if s.isdigit() else s, elements)

    return tuple(elements)
