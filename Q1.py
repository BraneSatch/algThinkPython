"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
import urllib2
import matplotlib.pyplot as plt
import math

# Set timeout for CodeSkulptor if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def compute_in_degrees(digraph):
    """
    This funciton return in-degrees as a dictionary.
    Keys are nodes and values are in-degrees.
    :param digraph:
    """
    degrees = {}

    for setter in digraph:
        degrees[setter] = 0

    for node_i in digraph:
        for node_j in digraph[node_i]:
            degrees[node_j] += 1

    return degrees


def in_degree_distribution(digraph):
    """
    This funciton return in-degree distribution as a dictionary.
    Keys are number of in-degrees and values are the frequencies or the distribution, unnormalized.
    :param digraph:
    """
    distribution = {}
    in_degrees = compute_in_degrees(digraph)

    for setter in in_degrees:
        distribution[in_degrees[setter]] = 0

    for node in in_degrees:
        distribution[in_degrees[node]] += 1
    return distribution


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


# citation_graph = load_graph(CITATION_URL)

def plot_graph_distribution(graph):
    distribution = in_degree_distribution(graph)
    y_values = []
    x_values = []
    sum = 0.0
    max = 0.0

    xrange = len(distribution);

    for i in distribution:
        sum += distribution[i]

    for i in distribution:
        y_values.append(math.log10(distribution[i] / sum))
        # Just to make our graph more clear on the plot
        if math.log10(distribution[i] / sum) > max:
            max = math.log10(distribution[i] / sum)

    x_values = range(xrange)
    for i in xrange(xrange):
        x_values[i] = math.log10(x_values[i]);

    plt.plot(x_values, y_values)
    plt.axis([0, xrange, 0, max])
    plt.ylabel('Distribution normalized')
    plt.xlabel('Number of in-degrees')
    plt.show()


plot_graph_distribution(load_graph(CITATION_URL))
