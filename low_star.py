from github_util import add_repo_bipartite
import networkx as nx
import pickle

G = nx.Graph()

GRAPH_PATH = 'low_star.gpickle'

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

for repo, user in low_star_repos:
    add_repo_bipartite(user, repo, 'red', G)

with open(GRAPH_PATH, "wb") as f:
    pickle.dump(G, f)