Parser-Illustration.p# Create the directed graph for circular parsing logic visualization including all nodes
G = nx.DiGraph()

# Define nodes involved in the parsing process and existing APIs
nodes = [
    "Input OpenAPI Spec", "YAML/JSON Loader", "Reference Resolver", 
    "Validation Module", "Dataclass Mapping", "Serialization Module", 
    "Parsed OpenAPI Object",
    "Core Script Management API", "Character Service", "Central Sequence Service", 
    "Action Service", "Story Factory API", "Spoken Word Service", 
    "Session and Context Management API", "Performer Service", "Paraphrase Service",
    "Ensemble Service", "FountainAI OpenAPI Parser"
]

# Add nodes to the graph
for node in nodes:
    G.add_node(node)

# Define directed edges representing the flow of parsing logic
parsing_edges = [
    ("Input OpenAPI Spec", "YAML/JSON Loader"),
    ("YAML/JSON Loader", "Reference Resolver"),
    ("Reference Resolver", "Validation Module"),
    ("Validation Module", "Dataclass Mapping"),
    ("Dataclass Mapping", "Parsed OpenAPI Object"),
    ("Parsed OpenAPI Object", "Serialization Module"),
    ("Serialization Module", "Input OpenAPI Spec")  # Complete the circle to represent iterative process
]

# Define edges representing connections with the APIs
api_edges = [
    ("Ensemble Service", "Core Script Management API"), ("Ensemble Service", "Character Service"), 
    ("Ensemble Service", "Central Sequence Service"), ("Ensemble Service", "Action Service"),
    ("Ensemble Service", "Story Factory API"), ("Ensemble Service", "Spoken Word Service"),
    ("Ensemble Service", "Session and Context Management API"), ("Ensemble Service", "Performer Service"),
    ("Ensemble Service", "Paraphrase Service"), ("Ensemble Service", "FountainAI OpenAPI Parser"),
    ("FountainAI OpenAPI Parser", "Core Script Management API"),
    ("FountainAI OpenAPI Parser", "Character Service"),
    ("FountainAI OpenAPI Parser", "Central Sequence Service"),
    ("FountainAI OpenAPI Parser", "Action Service"),
    ("FountainAI OpenAPI Parser", "Story Factory API"),
    ("FountainAI OpenAPI Parser", "Spoken Word Service"),
    ("FountainAI OpenAPI Parser", "Session and Context Management API"),
    ("FountainAI OpenAPI Parser", "Performer Service"),
    ("FountainAI OpenAPI Parser", "Paraphrase Service")
]

# Add edges to the graph
G.add_edges_from(parsing_edges + api_edges)

# Define the positions for a circular layout and adjust manually to avoid overlap
pos = nx.circular_layout(G)

# Increase distance for better separation of nodes to avoid text overlap
for key in pos:
    pos[key] = pos[key] * 1.5  # Scale positions outward

# Draw the graph in a circular layout
plt.figure(figsize=(16, 16))

# Draw nodes with different colors to highlight different stages of parsing and APIs
node_colors = [
    "lightyellow" if node == "Input OpenAPI Spec" else
    "lightgreen" if node in ["YAML/JSON Loader", "Reference Resolver", "Validation Module"] else
    "skyblue" if node in ["Dataclass Mapping", "Parsed OpenAPI Object", "Serialization Module"] else
    "lightcoral" if node == "Ensemble Service" else
    "lightgreen" if node == "FountainAI OpenAPI Parser" else
    "lightblue"
    for node in G.nodes()
]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500)

# Draw the labels with appropriate font size, with adjusted position to prevent overlap
nx.draw_networkx_labels(G, pos, font_size=8, font_weight="bold", verticalalignment='center')

# Draw the edges with arrows in a circular manner
nx.draw_networkx_edges(G, pos, edgelist=parsing_edges, edge_color="black", arrows=True, connectionstyle="arc3,rad=0.2")
nx.draw_networkx_edges(G, pos, edgelist=api_edges, edge_color="gray", arrows=True, connectionstyle="arc3,rad=0.2")

# Remove gridlines and display the final result without a heading title
plt.axis('off')
plt.show()

