import subprocess
import json
import os
import glob

from dssr_classes import *

def get_dssr_json_output(dssr_path, pdb_path):
    json_str = subprocess.check_output(dssr_path + "-i=" + pdb_path + " --json --more", shell=True)
    data = json.loads(json_str)

    files = glob.glob("dssr-*")
    for f in files:
        os.remove(f)

    return data

class DSSROutput(object):
    def __init__(self, pdb_path):
        pass
