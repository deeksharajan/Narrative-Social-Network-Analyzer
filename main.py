import logging
import spacy
import networkx as nx
import pandas as pd
import community.community_louvain as community_louvain
from itertools import combinations
from pathlib import Path
from pyvis.network import Network
from collections import Counter

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class CharacterNetwork:
    # --- CONFIGURATION ---
    BLACKLIST = ["Dad", "Gift", "Mist", "Golden drachmas"]
    MIN_PARA_THRESHOLD = 2
    DESCRIPTIONS = {
        "Percy Jackson": "The Protagonist: A demigod son of Poseidon.",
        "Annabeth": "The Strategist: Daughter of Athena, highly intelligent.",
        "Grover": "The Protector: A satyr and Percy's best friend.",
        "Luke": "The Antagonist/Mentor: Son of Hermes, complex character.",
        "Zeus": "The Authority: King of the Olympians.",
        "Hera": "The Matriarch: Queen of the Olympians."
    }

    def __init__(self, model_name="en_core_web_sm"):
        self.nlp = spacy.load(model_name)

    def unify_name(self, name):
        aliases = {"Jackson": "Percy Jackson", "Percy": "Percy Jackson", "Grover's": "Grover"}
        return aliases.get(name.strip(), name.strip())

    def build_network(self, file_path):
        graph = nx.Graph()
        with Path(file_path).open('r', encoding='utf-8') as f:
            paragraphs = [p for p in f.read().split('\n') if p.strip()]

        char_freq = Counter()
        para_data = []

        for para in paragraphs:
            doc = self.nlp(para)
            names = set(self.unify_name(ent.text) for ent in doc.ents if ent.label_ == "PERSON")
            valid_names = [n for n in names if n not in self.BLACKLIST]
            para_data.append(valid_names)
            for name in valid_names:
                char_freq[name] += 1

        for names in para_data:
            frequent_names = [n for n in names if char_freq[n] >= self.MIN_PARA_THRESHOLD]
            for c1, c2 in combinations(frequent_names, 2):
                graph.add_edge(c1, c2, weight=graph.get_edge_data(c1, c2, {'weight':0})['weight'] + 1)
        
        remove_nodes = [node for node, degree in graph.degree() if degree < 2]
        graph.remove_nodes_from(remove_nodes)
        return graph

    def save_to_html_with_table(self, graph, filename="network.html"):
        # 1. Analyze
        partition = community_louvain.best_partition(graph)
        modularity = community_louvain.modularity(partition, graph)
        
        # 2. Setup Nodes (Color, Label, Tooltip)
        colors = ['#FFadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff', '#bdb2ff', '#ffc6ff']
        table_rows = []
        for node in graph.nodes():
            comm_id = partition[node]
            graph.nodes[node]['color'] = colors[comm_id % len(colors)]
            graph.nodes[node]['label'] = f"{node} (G{comm_id})"
            graph.nodes[node]['title'] = self.DESCRIPTIONS.get(node, "Character in the story.")
            graph.nodes[node]['font'] = {'color': 'black', 'size': 16}
            table_rows.append({'Character': node, 'Group': comm_id})

        # 3. Create Network
        net = Network(height="100vh", width="100%", bgcolor="#ffffff", font_color="black")
        net.from_nx(graph)
        for u, v, data in graph.edges(data=True):
            data['label'] = str(data.get('weight', 1))
            data['font'] = {'color': 'black', 'size': 18, 'align': 'middle', 'background': 'white'}

        net.set_options("""
        var options = {
          "edges": {"color": {"color": "#848484"}, "smooth": {"type": "dynamic"}},
          "physics": {"barnesHut": {"gravitationalConstant": -10000, "springLength": 300}}
        }
        """)

        # 4. Inject Table and Modularity Score
        df = pd.DataFrame(table_rows)
        html = net.generate_html().replace("<body>", f"""<body>
        <style>
            #table-container {{ position: absolute; top: 20px; left: 20px; z-index: 10; 
            background: rgba(255, 255, 255, 0.9); padding: 15px; border-radius: 8px; 
            border: 1px solid #ccc; max-height: 80vh; overflow-y: auto; }}
        </style>
        <div id='table-container'>
            <h4>Narrative Complexity</h4>
            <p><strong>Modularity:</strong> {round(modularity, 3)}</p>
            {df.to_html(classes='table table-striped', index=False)}
        </div>""")
        
        with open(filename, "w+", encoding="utf-8") as out: out.write(html)
        logging.info("Dashboard generated with Table, Tooltips, and Modularity Score.")

if __name__ == "__main__":
    analyzer = CharacterNetwork()
    G = analyzer.build_network("data/percy_jackson.txt")
    analyzer.save_to_html_with_table(G)