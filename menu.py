print("Loading menu.py...")


menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")


from channel_and_crypto_extractor import *
extractor = my_scripts.addMenu("Extractor")
extractor.addCommand("Extract Channels", extract_channels, 'shift+e')
extractor.addCommand("Extract Crypto IDs", extract_crypto)