import nuke
import ast

def extract_channels():

    nodes = nuke.selectedNodes(filter = 'Read')

    if not nodes:
        nuke.message("Please select a 'Read' node/s")
        return

    for read in nodes:
        
        channels_list_all = read.channels()

        channels_list_each = []

        for each in channels_list_all:
            layer_name = each.split('.')[0]
            if not layer_name in channels_list_each:
                
                channels_list_each.append(layer_name)

        for each in channels_list_each:
            shuffle = nuke.createNode('Shuffle')
            shuffle['in'].setValue(each)
            shuffle.setXpos(read.xpos() + ((channels_list_each.index(each) + 1) * 200))
            shuffle.setYpos(read.ypos() + 20)
            shuffle['label'].setValue("<b>[value in]</b>")
            shuffle['note_font_color'].setValue(int("FFFFFFFF", 16))

            if channels_list_each[-1] == each:
                shuffle['selected'].setValue(False)

            elif channels_list_each[0] == each:
                shuffle.setInput(0, read)

def extract_crypto():
    """
    Extracts Cryptomatte data from the metadata of the selected node in Nuke
    and creates Cryptomatte nodes for each unique ID found in the manifest.
    """
    try:
        node = nuke.selectedNode()  # Get the currently selected node

        metadata = node.metadata()  # Retrieve metadata from the selected node

        keys = metadata.keys()  # Get all metadata keys

        for key in keys:
            # Find key with Cryptomatte manifest
            if "cryptomatte" in key and "manifest" in key:
                # Store the manifest key
                manifest = key

        # Convert manifest string to dictionary
        manifest_dict = ast.literal_eval(metadata[manifest])

        # Declaring an empty list to store IDs later
        id_list = []

        # Loop through each Item in the manifest
        for each_item in manifest_dict:
            id_list.append(each_item)

        # Loop through each unique ID in the list
        for each_id in id_list:
            crypto_node = nuke.createNode("Cryptomatte")
            crypto_node["matteList"].setValue(each_id)
            crypto_node.setYpos(node.ypos() + ((id_list.index(each_id) + 1) * 200))

    # Handle and Display any exceptions that occur         
    except Exception as e:  
        nuke.message(str(e))