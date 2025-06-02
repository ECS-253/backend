import networkx as nx
import pickle
from github_util import add_user_bipartite
from visual_util import get_projection

G = nx.Graph()

GRAPH_PATH = 'user_h.gpickle'

high_star_repos = [
("acdlite", "recompose"),
("bootstrap-vue", "bootstrap-vue"),
("bower", "bower"),
("chartjs", "Chart.js"),
("commitizen", "cz-cli"),
("dvajs", "dva"),
("emotion-js", "emotion"),
("eslint", "eslint"),
("facebook", "react"),
("fastify", "fastify"),
("fengyuanchen", "cropperjs"),
("frappe", "charts"),
("graphql", "dataloader"),
("gulpjs", "gulp"),
("http-party", "node-http-proxy"),
("hubotio", "hubot"),
("HumanSignal", "label-studio"),
("iamkun", "dayjs"),
("infernojs", "inferno"),
("jlmakes", "scrollreveal"),
("josdejong", "mathjs"),
("knex", "knex"),
("koajs", "koa"),
("ladjs", "superagent"),
("ladjs", "supertest"),
("liriliri", "eruda"),
("markdown-it", "markdown-it"),
("marko-js", "marko"),
("mdx-js", "mdx"),
("mochajs", "mocha"),
("Modernizr", "Modernizr"),
("moment", "luxon"),
("motdotla", "dotenv"),
("myliang", "x-spreadsheet"),
("mysqljs", "mysql"),
("Netflix", "falcor"),
("nfl", "react-helmet"),
("node-red", "node-red"),
("NodeBB", "NodeBB"),
("nodejs", "node"),
("OpenZeppelin", "openzeppelin-contracts"),
("pinojs", "pino"),
("pouchdb", "pouchdb"),
("reactstrap", "reactstrap"),
("redux-form", "redux-form"),
("restify", "node-restify"),
("riot", "riot"),
("rollup", "rollup"),
("rwaldron", "johnny-five"),
("sequelize", "sequelize"),
("shelljs", "shelljs"),
("strongloop", "loopback"),
("Tencent", "wepy"),
("validatorjs", "validator.js"),
("videojs", "video.js"),
("winstonjs", "winston"),
("yabwe", "medium-editor"),
("you-dont-need", "You-Dont-Need-Momentjs")
]

user_map = {}

for user, repo in high_star_repos:
    user_map[repo] = user

with open('high_star.gpickle', "rb") as f:
    G = pickle.load(f)

B = get_projection(G, bipartite=0)

U = nx.Graph()

for repo in B.nodes:
    repo_name = repo.split(' ')[-1]
    add_user_bipartite(repo_name, user_map[repo_name], G.nodes[repo]['color'], U)

with open(GRAPH_PATH, "wb") as f:
    pickle.dump(U, f)