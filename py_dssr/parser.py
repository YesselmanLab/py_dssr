import subprocess
import json
import os
import glob
import argparse
import pprint

import dssr

class_str = """
class {name} (object): 
    def __init__(self, {args}**kwargs):
{attributes}
        for key, value in kwargs.items():
            setattr(self, key, value)
"""

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-setup', help='dataframe in csv format', required=True)
    args = parser.parse_args()
    return args


def parse_type_info(type_info):
    if  type_info == int:
        return "int"
    elif type_info == float:
        return "float"
    elif type_info == str:
        return "str"
    elif type_info == list:
        return "list"
    elif type_info == dict:
        return "dict"
    else:
        return None


def get_attribute_str(attribute_list):
    attribute_str = ""
    for attr, val in attribute_list:
        type_info = parse_type_info(type(val))
        if type_info is None:
            attribute_str += "        self." + str(attr) + " = None \n"
        else:
            attribute_str += "        self." + str(attr) + " : " + type_info + " = None \n"
    return attribute_str

def setup_nt_class(nts_data):
    items = nts_data[0].items()
    attrib_str = get_attribute_str(items)
    nt_str = class_str.format(name="DSSR_NT", attributes=attrib_str, args="")
    return nt_str


def setup_pair_class(pair_data):
    items = list(pair_data[0].items())
    # going to add in values for these
    i = 0
    while i < len(items):
        if items[i][0] == 'nt1' or items[i][0] == 'nt2':
            items.pop(i)
        else:
            i += 1
    attrib_str = get_attribute_str(items)
    attrib_str  =  "        self.nt1 = nt1\n        self.nt2 = nt2\n" + attrib_str
    pair_str = class_str.format(name="DSSR_PAIR", attributes=attrib_str,
                                args="nt1 : DSSR_NT, nt2 : DSSR_NT, ")
    return pair_str


def setup_dssr_classes():
    # get nt members
    exe_path = "resources/x3dna-dssr "
    pdb_path = "resources/4p95.pdb"
    json_str = subprocess.check_output(exe_path + "-i=" + pdb_path + " --json --more", shell=True)
    cleanup()

    data = json.loads(json_str)

    #pprint.pprint(data['pairs'])
    #print(data['atom2bases'][0])

    nt_str = setup_nt_class(data['nts'])
    pair_str = setup_pair_class(data['pairs'])

    f = open("dssr.py", "w")
    f.write(nt_str + "\n")
    f.write(pair_str + "\n")
    f.close()


    #for key in data['nts'][0].keys():
    #    print("self." + key + "=None")


"""class DSSROutput(object):
    def __init__(self):
        pass


class DSSR_NT(object):
    def __init__(self, **kwargs):
        self.index = None
        self.index_chain = None
        self.chain_name = None
        self.nt_resnum = None
        self.nt_name = None
        self.nt_code = None
        self.nt_id = None
        self.dbn = None
        self.summary = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.delta = None
        self.epsilon = None
        self.zeta = None
        self.epsilon_zeta = None
        self.bb_type = None
        self.chi = None
        self.glyco_bond = None
        self.C5prime_xyz = None
        self.P_xyz = None
        self.form = None
        self.ssZp = None
        self.Dp = None
        self.splay_angle = None
        self.splay_distance = None
        self.splay_ratio = None
        self.eta = None
        self.theta = None
        self.eta_prime = None
        self.theta_prime = None
        self.eta_base = None
        self.theta_base = None
        self.v0 = None
        self.v1 = None
        self.v2 = None
        self.v3 = None
        self.v4 = None
        self.amplitude = None
        self.phase_angle = None
        self.puckering = None
        self.sugar_class = None
        self.bin = None
        self.cluster = None
        self.suiteness = None
        self.filter_rmsd = None
        self.frame = None
        self.is_broken = None

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_PAIR(object):
    def __init__(self, **kwargs):
        pass
"""

def cleanup():
    files = glob.glob("dssr-*")
    for f in files:
        os.remove(f)


def main():
    exe_path = "resources/x3dna-dssr "
    pdb_path = "/Users/josephyesselman/projects/Rosetta.projects/motif_folding/runs/fixed_ends/TWOWAY.1S72.47/S_000001.pdb"

    #setup_dssr_classes()

    #exit()

    # need to call analyze first
    ##subprocess.call(exe_path + "-i=" + pdb_path + " --analyze", shell=True)
    #print(exe_path + "-i=" + pdb_path + " --json --more ")
    json_str = subprocess.check_output(exe_path + "-i=" + pdb_path + " --json --more", shell=True)
    cleanup()
    data = json.loads(json_str)

    #print(data['pairs'])

    nts = {}
    for nt_info in data['nts']:
        nt = dssr.DSSR_NT(**nt_info)
        nts[nt.nt_id] = nt

    pairs = []

    for pair_info in data['pairs']:
        nt1 = nts[pair_info['nt1']]
        nt2 = nts[pair_info['nt2']]
        del pair_info['nt1']
        del pair_info['nt2']
        pairs.append(dssr.DSSR_PAIR(nt1, nt2, **pair_info))

    #print(data['refCoords'])





if __name__ == "__main__":
    main()
