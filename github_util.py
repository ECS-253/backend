import requests
import json
import base64
import networkx as nx
import matplotlib.pyplot as plt

from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file into environment variables

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_js_dependencies(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/contents/package.json"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        content = response.json()
        if content.get("encoding") == "base64":
            decoded = base64.b64decode(content["content"]).decode("utf-8")
            data = json.loads(decoded)
            deps = data.get("dependencies", {})
            return list(deps.keys())
    return []

def get_contributors(user, repo):
    url = f"https://api.github.com/repos/{user}/{repo}/contributors"
    response = requests.get(url, headers=HEADERS)
    contris = []
    if response.status_code == 200:
        data = response.json()
        for item in data:
            contris.append(item['login'])
    return contris

def add_repo(repo, user, graph):
        all_deps = get_js_dependencies(user, repo)
        if not graph.has_node(repo):
            graph.add_node(repo)

        for dep in all_deps:
            if not graph.has_node(dep):
                graph.add_node(dep) 
            graph.add_edge(repo, dep)

def add_repo_bipartite(repo, user, color, graph):
    all_deps = get_js_dependencies(user, repo)
    repo_node = f'repo: {repo}'

    if not graph.has_node(repo_node):
        graph.add_node(repo_node, color=color, bipartite=0)

    for dep in all_deps:
        dep_node = f'dep: {dep}'

        if not graph.has_node(dep_node):
            graph.add_node(dep_node, bipartite=1, red=0, lightblue=0)
        graph.nodes[dep_node][color] += 1

        graph.add_edge(repo_node, dep_node)

def add_user_bipartite(repo, user, color, graph):
    all_contris = get_contributors(user, repo)
    if not graph.has_node(repo):
        graph.add_node(repo, color=color, bipartite=0)

    for contri in all_contris:
        if not graph.has_node(contri):
            graph.add_node(contri, bipartite=1, red=0, lightblue=0)
        graph.nodes[contri][color]+=1
        graph.add_edge(repo, contri)