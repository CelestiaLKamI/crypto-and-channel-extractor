from crypto_id_extractor import extract_crypto
from channel_extractor import extract_channels

print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")

extractor = my_scripts.addMenu("Extractor")
extractor.addCommand("Extract Channels", extract_channels, 'shift+e')
extractor.addCommand("Extract Crypto IDs", extract_crypto)
