import nuke
from PySide2.QtWidgets import QWidget, QPushButton, QComboBox, QLabel, QVBoxLayout, QHBoxLayout

def extract_crypto():
    """
    Extracts Cryptomatte data from the metadata of the selected node in Nuke
    and creates Cryptomatte nodes for each unique ID found in the manifest.
    """
    class MainWindow(QWidget):
        def __init__(self):
            super().__init__()

            # Layouts for UI elements
            hbox1 = QHBoxLayout()
            hbox2 = QHBoxLayout()
            main_layout = QVBoxLayout()

            # UI components
            self.label = QLabel("Select Layer")
            self.comboBox = QComboBox()
            self.comboBox.setMinimumWidth(300)
            self.select_button = QPushButton("Extract")
            self.cancel_button = QPushButton("Cancel")

            # Cancel button functionality
            self.cancel_button.clicked.connect(self.cancel_operation)

            # Add components to layouts
            hbox1.addWidget(self.label)
            hbox1.addWidget(self.comboBox)

            hbox2.addWidget(self.select_button)
            hbox2.addWidget(self.cancel_button)

            main_layout.addLayout(hbox1)
            main_layout.addLayout(hbox2)

            self.setLayout(main_layout)
            self.setMinimumWidth(400)
            self.setMaximumWidth(400)

            # Initialize combo box with available layers
            self.update_combobox()
            self.select_button.clicked.connect(self.extract)

        
        def cancel_operation(self):
            """
            Close the window on cancel
            """
            window.close()

        def update_combobox(self):
            """
            This function updates the options based on the avalible cryptomatte layers from
            metadata of the read layers
            """
            # Populate combo box with Cryptomatte layer names
            self.node = nuke.selectedNode()
            self.metadata = self.node.metadata()
            keys = self.metadata.keys()

            if not self.node:
                nuke.message("Please select read node")
                return
            
            if not self.metadata:
                nuke.message("No Metadata available for Extraction")
                return
            
            if not keys:
                nuke.message("No Keys available for Extraction")
                return
            
            self.manifest_list = []
            self.layer_name_list = []

            for key in keys:
                if "cryptomatte" in key and "manifest" in key:
                    self.manifest_list.append(key)
                if "cryptomatte" in key and "name" in key:
                    self.layer_name_list.append(self.metadata[key])

            self.comboBox.addItems(self.layer_name_list)

        def extract(self):
            """
            This function is to create cryptomatte nodes each containing unique IDs
            when the user hits the extract button after selecting his choice of cryptomatte layer
            """
            # Convert manifest string to dictionary
            manifest_dict = eval(self.metadata[self.manifest_list[self.comboBox.currentIndex()]])

            if not  self.layer_name_list:
                nuke.message("No Crypto Layer available for Extraction")
                return

            if not manifest_dict:
                nuke.message("No Crypto Data available for Extraction")
                return

            id_list = []  # Store unique IDs

            # Extract IDs from the manifest
            for each_item in manifest_dict:
                id_list.append(each_item)

            # Create Cryptomatte nodes for each unique ID
            for each_id in id_list:
                if each_id != "default":
                    crypto_node = nuke.createNode("Cryptomatte") 
                    crypto_node.setYpos(crypto_node.ypos()+200)
                    crypto_node["matteList"].setValue(each_id)
                    crypto_node["cryptoLayerChoice"].setValue(self.comboBox.currentIndex())
                    crypto_node["label"].setValue(each_id)

            window.close()
          
    global window
    window = MainWindow()
    window.setWindowTitle("Crypto Extractor")
    window.show()