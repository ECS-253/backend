from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import networkx as nx
import pickle
from visual_util import get_projection, get_high_low_rev, compare, get_high_low

app = FastAPI()

# Enable frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/graph")
def get_graph(file: str = Query('', description="graph"), bipartite: int = Query(0)):
    with open(file, "rb") as f:
        G = pickle.load(f)
    B = get_projection(G, bipartite=bipartite)
    for n in G.nodes:
        print(n, list(G.nodes[n].keys()))
    # if bipartite == 1:
    #     high, low = get_high_low_rev(B)
    # else:
    #     high, low = get_high_low(B)
    # compare(B, high, low)
    data = nx.json_graph.node_link_data(B)
    return data