import networkx as nx
import pickle
from github_util import add_user_bipartite
from visual_util import get_projection

G = nx.Graph()

GRAPH_PATH = 'user_l.gpickle'

low_star_repos = [
("addyosmani", "critical"),
("akxcv", "vuera"),
("AlaSQL", "alasql"),
("apollographql", "react-apollo"),
("aui", "art-template"),
("babel", "minify"),
("bda-research", "node-crawler"),
("bpmn-io", "bpmn-js"),
("brave", "browser-laptop"),
("c3js", "c3"),
("chaijs", "chai"),
("chancejs", "chancejs"),
("cnodejs", "nodeclub"),
("codecombat", "codecombat"),
("conventional-changelog", "standard-version"),
("coryhouse", "react-slingshot"),
("davidjbradshaw", "iframe-resizer"),
("didi", "cube-ui"),
("expressjs", "cors"),
("expressjs", "morgan"),
("expressjs", "session"),
("fengyuanchen", "viewerjs"),
("final-form", "react-final-form"),
("fluent-ffmpeg", "node-fluent-ffmpeg"),
("gitalk", "gitalk"),
("grommet", "grommet"),
("Hacker0x01", "react-datepicker"),
("hagopj13", "node-express-boilerplate"),
("ipfs", "js-ipfs"),
("jaywcjlove", "hotkeys-js"),
("jely2002", "youtube-dl-gui"),
("jprichardson", "node-fs-extra"),
("json5", "json5"),
("kbrsh", "moon"),
("kentcdodds", "cross-env"),
("Laverna", "laverna"),
("ljharb", "qs"),
("lukeed", "clsx"),
("Mango", "slideout"),
("mediaelement", "mediaelement"),
("metalsmith", "metalsmith"),
("mgonto", "restangular"),
("node-formidable", "formidable"),
("npm", "cli"),
("oliviertassinari", "react-swipeable-views"),
("postmanlabs", "newman"),
("reactjs", "react-modal"),
("rebassjs", "rebass"),
("redux-utilities", "redux-actions"),
("remarkjs", "remark"),
("Rob--W", "cors-anywhere"),
("sbstjn", "timesheet.js"),
("senchalabs", "connect"),
("share", "sharedb"),
("shutterstock", "rickshaw"),
("sindresorhus", "execa"),
("sinonjs", "sinon"),
("testing-library", "jest-dom"),
("uncss", "uncss"),
("visionmedia", "page.js"),
("webpack", "webpack-dev-server"),
("webslides", "WebSlides"),
("wilsonpage", "fastdom"),
("WordPress", "gutenberg"),
("yagop", "node-telegram-bot-api")
]

user_map = {}

for user, repo in low_star_repos:
    user_map[repo] = user

with open('low_star.gpickle', "rb") as f:
    G = pickle.load(f)

B = get_projection(G, bipartite=0)

U = nx.Graph()

for repo in B.nodes:
    repo_name = repo.split(' ')[-1]
    add_user_bipartite(repo_name, user_map[repo_name], G.nodes[repo]['color'], U)

with open(GRAPH_PATH, "wb") as f:
    pickle.dump(U, f)