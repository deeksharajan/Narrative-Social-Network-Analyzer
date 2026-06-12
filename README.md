#  Narrative Social Network Analyzer

 **Live Demo:** https://github.com/deeksharajan/Narrative-Social-Network-Analyzer.git

A Python-based computational literary analysis tool that transforms narrative text into an interactive social network graph. By combining Natural Language Processing (NLP), graph theory, and community detection algorithms, the system automatically identifies characters, maps their relationships, detects narrative communities, and visualizes story structure through an interactive dashboard.

---

##  Overview

Narrative Social Network Analyzer treats a literary text as a complex social network where characters become nodes and their interactions become edges. Using NLP and graph analytics, the system uncovers hidden narrative structures, social groups, and character relationships that may not be immediately visible through traditional reading.

The project demonstrates how computational methods can complement literary analysis by providing measurable insights into narrative organization and character connectivity.

---

##  Features

###  Automated Character Extraction

* Uses **spaCy Named Entity Recognition (NER)** to identify character names from literary text.
* Processes raw text automatically without manual annotation.

###  Alias Normalization

* Consolidates multiple references to the same character.
* Examples:

  * Percy → Percy Jackson
  * Jackson → Percy Jackson
  * Grover's → Grover

###  Data Cleaning & Noise Reduction

* Removes incorrectly identified entities through custom blacklist filtering.
* Applies frequency thresholds to eliminate insignificant mentions.
* Uses degree-based node pruning to improve graph quality and readability.

###  Character Relationship Network

* Builds a weighted undirected graph using NetworkX.
* Models character interactions through paragraph-level co-occurrence.
* Edge weights represent interaction frequency.

###  Community Detection

* Implements the Louvain Community Detection Algorithm.
* Automatically discovers narrative communities and social clusters.
* Assigns color-coded groups for intuitive visualization.

###  Narrative Complexity Analysis

* Calculates Modularity Score to quantify narrative structure.
* Measures how interconnected or fragmented a story is.

###  Interactive Dashboard

* Generates an interactive HTML visualization using PyVis.
* Supports zooming, panning, and node manipulation.
* Displays weighted relationships between characters.

###  Character Hover Tooltips

* Hovering over a node displays character descriptions and contextual information.
* Provides quick insights into major characters without cluttering the graph.

###  Embedded Community Table

* Displays character names alongside their assigned communities.
* Integrated directly into the dashboard for easy interpretation.

---

##  Methodology

### 1. Text Processing

The input literary text is divided into paragraphs and processed using spaCy's NLP pipeline. Character entities are extracted using Named Entity Recognition.

### 2. Entity Normalization

Character aliases and naming variations are standardized using custom mappings to improve consistency.

### 3. Co-occurrence Modeling

An interaction is defined as two characters appearing within the same paragraph. This approach captures narrative proximity and shared participation in story events.

### 4. Noise Reduction

To improve analytical accuracy, the system applies:

* Blacklist filtering
* Frequency thresholding
* Degree-based node pruning

These techniques reduce false positives and improve signal-to-noise ratio.

### 5. Community Detection

The Louvain Algorithm partitions the network into communities by maximizing modularity. These communities often correspond to narrative groups, social circles, or subplot structures.

### 6. Narrative Complexity Measurement

The Modularity Score is used to quantify narrative organization:

* **High Modularity** → Distinct social groups and separated plotlines.
* **Low Modularity** → Highly interconnected narrative structure.

---

##  Dashboard Preview

![Dashboard Preview](assets/dashboard.png)

The generated dashboard includes:

* Interactive character relationship network
* Community-colored nodes
* Character hover tooltips with descriptions
* Weighted interaction edges
* Embedded community membership table
* Narrative complexity analysis using Modularity Score

Users can:

* Zoom and pan across the network
* Drag nodes to explore relationships
* Hover over characters to view descriptions
* Analyze narrative communities through color-coded groups

---

##  Technologies Used

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Core Development              |
| spaCy          | Named Entity Recognition      |
| NetworkX       | Graph Construction & Analysis |
| Python-Louvain | Community Detection           |
| Pandas         | Data Handling                 |
| PyVis          | Interactive Visualization     |
| HTML/CSS       | Dashboard Customization       |

---

##  Installation

### Install Dependencies

```bash
pip install spacy networkx pandas python-louvain pyvis
```

### Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

##  Project Structure

```text
Narrative-Social-Network-Analyzer/
│
├── assets/
│   └── dashboard.png
│
└── data/
│  └── percy_jackson.txt
├── README.md
├── requirements.txt
├── main.py
├── network.html

```

---

## ▶ Usage

Run the main script:

```bash
python main.py
```

After execution, an interactive visualization named `network.html` will be generated.

Open the file in your browser to explore the character network.

---

##  Output

The generated HTML dashboard contains:

### Interactive Character Network

* Characters represented as nodes
* Relationships represented as weighted edges
* Community-based color coding

### Character Information Tooltips

* Displayed when hovering over nodes
* Provide contextual descriptions of important characters

### Community Membership Table

* Lists characters and their assigned communities
* Embedded directly within the dashboard

### Narrative Complexity Metric

* Displays the network's Modularity Score
* Quantifies narrative structure and community separation

---

##  Example Application

The system was applied to the Percy Jackson literary series to analyze character interactions and narrative structure.

Key observations included:

* Percy Jackson emerged as a central figure connecting multiple narrative groups.
* Distinct clusters corresponding to Olympian gods, demigods, and supporting characters were automatically identified.
* Community detection revealed clear social structures within the story.
* Modularity analysis provided quantitative insight into the organization of narrative subplots.

These findings demonstrate how computational techniques can reveal hidden structures within literary works.

---

##  Future Improvements

* Betweenness Centrality Analysis
* Degree Centrality Ranking
* Sentiment Analysis of Character Interactions
* Advanced Named Entity Resolution
* Chapter-wise Temporal Network Evolution
* Multi-book Comparative Analysis
* Exportable Network Statistics Dashboard

---

##  Academic Significance

This project demonstrates the intersection of:

* Natural Language Processing
* Network Science
* Data Visualization
* Computational Literary Analysis

By transforming qualitative narrative information into measurable graph structures, the system provides an objective framework for studying literary relationships and story complexity.
