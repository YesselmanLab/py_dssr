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


def default_class_setup(data, name):
    items = data[0].items()
    attrib_str = get_attribute_str(items)
    nt_str = class_str.format(name=name, attributes=attrib_str, args="")
    return nt_str



def setup_dssr_classes():
    # get nt members
    exe_path = "resources/x3dna-dssr "
    pdb_path = "resources/4p95.pdb"

    data = dssr.get_dssr_json_output(exe_path, pdb_path)

    pprint.pprint(data['splayUnits'])
    #print(data['atom2bases'][0])

    nt_str = setup_nt_class(data['nts'])
    pair_str = setup_pair_class(data['pairs'])
    hairpin_str = default_class_setup(data['hairpins'], "DSSR_HAIRPIN")

    f = open("dssr_classes.py", "w")
    f.write("from typing import List, Dict\n\n")
    f.write(nt_str + "\n")
    f.write(pair_str + "\n")

    keys = "hairpins,helices,stems,iloops,junctions,ssSegments,kissingLoops,Aminors,riboseZippers,HtypePknots,hbonds".split(",")
    class_names = "HAIRPIN,HELIX,STEM,ILOOP,JUNCTION,SINGLE_STRAND,KISSING_LOOP,AMINOR,RIBOSE_ZIPPER,PSEUDOKNOT,HBOND".split(",")

    for key, class_name in zip(keys,class_names):
        f.write(default_class_setup(data[key],"DSSR_"+class_name) + "\n")
    f.close()


    #for key in data['nts'][0].keys():
    #    print("self." + key + "=None")




def main():
    exe_path = "resources/x3dna-dssr "
    pdb_path = "/Users/josephyesselman/projects/Rosetta.projects/motif_folding/runs/fixed_ends/TWOWAY.1S72.47/S_000001.pdb"
    #pdb_path = "resources/4p95.pdb"

    setup_dssr_classes()

    exit()

    data = dssr.get_dssr_json_output(exe_path, pdb_path)

    #print(data['pairs'])

    nts = {}
    for nt_info in data['nts']:
        nt = dssr.DSSR_NT(**nt_info)
        nts[nt.nt_id] = nt

    for nt in nts.values():
        print(nt.nt_id, nt.splay_angle, nt.splay_distance)

    pairs = []

    for pair_info in data['pairs']:
        nt1 = nts[pair_info['nt1']]
        nt2 = nts[pair_info['nt2']]
        del pair_info['nt1']
        del pair_info['nt2']
        pairs.append(dssr.DSSR_PAIR(nt1, nt2, **pair_info))

    #m = dssr.DSSR_MOTIF(pairs)


    #print(data['refCoords'])





if __name__ == "__main__":
    main()
