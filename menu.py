print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")

extractor = my_scripts.addMenu("Extractor")
from channel_extractor import extract_channels
extractor.addCommand("Extract Channels", extract_channels, 'shift+e')
from crypto_ID_extractor import extract_crypto
extractor.addCommand("Extract Crypto IDs", extract_crypto)