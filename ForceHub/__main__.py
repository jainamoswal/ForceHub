from pathlib import Path
from . import ForceBot
from ForceHub.utils import load_plugins
import sys
import importlib
import logging
import glob

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ForceHub/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        
if __name__ == "__main__":
    print('Bot started...')
    ForceBot.run_until_disconnected()
                    
                    
