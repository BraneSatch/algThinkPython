"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
import urllib2
import matplotlib.pyplot as plt
import math

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
number_of_nodes = 352768


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


def plot_graph_distribution(graph):
    distribution = in_degree_distribution(graph)
    print distribution
    y_values = []
    x_values = []
    sum = 0.0
    max = 0
    min = 1000.0
    x_range = len(distribution);

    for i in distribution:
        sum += distribution[i]

    for i in distribution:
        y_values.append(distribution[i] / sum)
        # Just to make our graph more clear on the plot
        if distribution[i] / sum < min:
            min = distribution[i] / sum
        if distribution[i] / sum > max:
            max = distribution[i] / sum


    plt.figure(figsize=(1280/96, 800/96), dpi=96)
    plt.plot(y_values, 'ro')
    plt.yscale('log')
    plt.xscale('log')
    plt.axis([0, 700, math.log(0.01), math.log(2)])
    plt.ylabel('Distribution normalized')
    plt.xlabel('Number of in-degrees')
    plt.title('In-degree distribution plot from Question 1')
    plt.show()


plot_graph_distribution(load_graph(CITATION_URL))
