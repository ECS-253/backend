from github_util import add_repo_bipartite
import networkx as nx
import pickle

G = nx.Graph()

GRAPH_PATH = 'high_star.gpickle'

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

for repo, user in high_star_repos:
    add_repo_bipartite(user, repo, 'lightblue', G)

with open(GRAPH_PATH, "wb") as f:
    pickle.dump(G, f)