import networkx as nx

def cross_group_density(G, group1, group2):
    total_weight = 0
    possible_edges = len(group1) * len(group2)
    for u in group1:
        for v in group2:
            if G.has_edge(u, v):
                total_weight += G[u][v].get('weight', 1)
    return total_weight / possible_edges if possible_edges > 0 else 0

def group_density(G, group):
    total_weight = 0
    possible_edges = len(group) * (len(group)-1) // 2
    for u in group:
        for v in group:
            if G.has_edge(u, v):
                total_weight += G[u][v].get('weight', 1)
    return total_weight / possible_edges if possible_edges > 0 else 0

def mean(lst):
    return sum(lst)/len(lst) if lst else 0

def compare(B, high_star, low_star):
    density_cross = cross_group_density(B, high_star, low_star)
    print(f"cross group weighted edge density: {density_cross:.3f}")

    high_star_density= group_density(B, high_star)
    print(f"high star group weighted edge density: {high_star_density:.3f}")
    
    low_star_density= group_density(B, low_star)
    print(f"low star group weighted edge density: {low_star_density:.3f}")

    partition = {}
    for n in B.nodes():
        partition[n] = 0 if B.nodes[n]['serves'] > 0 else 1

    mod_score = nx.algorithms.community.modularity(B, [set(k for k,v in partition.items() if v==0),
            set(k for k,v in partition.items() if v==1)])
    print("Modularity:", mod_score)

    within_high_weights = []
    within_low_weights = []
    between_weights = []

    for u, v, data in B.edges(data=True):
        weight = data.get('weight', 1) 
        
        if u in high_star and v in high_star:
            within_high_weights.append(weight)
        elif u in low_star and v in low_star:
            within_low_weights.append(weight)
        else:
            between_weights.append(weight)

    print("Avg weight within high-star:", mean(within_high_weights))
    print("Avg weight within low-star:", mean(within_low_weights))
    print("Avg weight between groups:", mean(between_weights))

def get_projection(G, bipartite=0):
    repo_nodes = {n for n, d in G.nodes(data=True) if d['bipartite'] == bipartite}
    B = nx.bipartite.weighted_projected_graph(G, repo_nodes)
    return B

def get_high_low_rev(B):
    high_star = [n for n, d in B.nodes(data=True) if d['serves'] > 0]
    low_star = [n for n, d in B.nodes(data=True) if d['serves'] <= 0]
    return high_star, low_star

def get_high_low(B):
    high_star = [n for n, d in B.nodes(data=True) if d['color'] == 'lightblue']
    low_star = [n for n, d in B.nodes(data=True) if d['color'] == 'red']
    return high_star, low_star