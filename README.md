# crypto-and-channel-extractor

This repository contains two Python scripts designed to enhance productivity and automation within Foundry Nuke.

---

## Files Overview

### 1. **channel_extractor.py**

#### Description
This script automates the extraction of all unique channel layers from selected `Read` nodes in Nuke and creates `Shuffle` nodes for each layer.

#### Features
- Identifies all unique channel layers from selected `Read` nodes.
- Creates `Shuffle` nodes for each layer with appropriate labeling.
- Automatically positions nodes relative to the `Read` node for better organization.

#### Usage
1. Select one or more `Read` nodes in your Nuke script.
2. Run the script to generate `Shuffle` nodes for each unique layer.

#### Notes
- Ensure you have selected at least one `Read` node before running the script. If no nodes are selected, a message will prompt you to select one.

---

### 2. **crypto_ID_extractor.py**

#### Description
This script extracts Cryptomatte data from the selected node's metadata and creates `Cryptomatte` nodes for each unique ID found in the manifest.

#### Features
- User-friendly GUI built with PySide2.
- Dynamically lists Cryptomatte layers from the selected node.
- Generates `Cryptomatte` nodes for each unique ID found in the manifest.

#### Usage
1. Select a node containing Cryptomatte metadata.
2. Run the script to open a GUI.
3. Choose the desired Cryptomatte layer and click "Select" to generate the nodes.

#### Notes
- Ensure the selected node contains Cryptomatte metadata.
- Clicking "Cancel" will close the GUI without making any changes.

---

## Prerequisites

- Foundry Nuke (with Python scripting enabled)
- PySide2 library installed for `crypto_ID_extractor.py`

---

## How to Use

1. Place the scripts in a directory accessible by Nuke.
2. Add the scripts to your Nuke menu or run them manually in the Script Editor.

---

Happy compositing!