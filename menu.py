print("Loading menu.py...")

from channel_and_crypto_extractor import *
extractor = my_scripts.addMenu("Extractor")
extractor.addCommand("Extract Channels", extract_channels, 'shift+e')
extractor.addCommand("Extract Crypto IDs", extract_crypto)