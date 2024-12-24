import nuke

def extract_channels():
    """
    Extracts all unique channel layers from selected 'Read' nodes
    and creates Shuffle nodes for each layer.
    """
    # Get selected nodes of type 'Read'
    nodes = nuke.selectedNodes(filter='Read')
    
    if not nodes:
        # Show message if no 'Read' nodes are selected
        nuke.message("Please select a 'Read' node/s")
        return
    
    try:
        for read in nodes:
            # Get all channel names in the node
            channels_list_all = read.channels()
            
            channels_list_each = []
            
            # Extract unique layer names from channels
            for each in channels_list_all:
                layer_name = each.split('.')[0]
                if not layer_name in channels_list_each:
                    channels_list_each.append(layer_name)

            for each in channels_list_each:
                # Create Shuffle node for each unique layer
                shuffle = nuke.createNode('Shuffle')
                shuffle['in'].setValue(each)
                shuffle.setXpos(read.xpos() + ((channels_list_each.index(each) + 1) * 200))
                shuffle.setYpos(read.ypos() + 20)
                shuffle['label'].setValue("<b>[value in]</b>")
                shuffle['note_font_color'].setValue(int("FFFFFFFF", 16))
                
                # Deselect the last node in the list
                if channels_list_each[-1] == each:
                    shuffle['selected'].setValue(False)
                
                # Connect the first Shuffle node to the Read node
                elif channels_list_each[0] == each:
                    shuffle.setInput(0, read)
                    
    except Exception as e:
        # Display any errors that occur
        nuke.message(str(e))