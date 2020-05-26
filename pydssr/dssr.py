import subprocess
import json
import os
import glob

from typing import List, Dict

from pydssr import dssr_classes, settings


def get_dssr_json_output(dssr_path, pdb_path):
    json_str = subprocess.check_output(dssr_path + "-i=" + pdb_path + " --json --more 2> /dev/null", shell=True)
    data = json.loads(json_str)

    files = glob.glob("dssr-*")
    for f in files:
        os.remove(f)

    return data


class DSSROutput(object):
    def __init__(self, pdb_path):
        self.__dssr_path = settings.Paths.DSSR_EXE
        self.__pdb_path = pdb_path
        self.__data = get_dssr_json_output(self.__dssr_path, pdb_path)
        # data will be populated as the user requests it via getters
        self.__nts : Dict[str, dssr_classes.DSSR_NT] = None
        self.__pairs : Dict[str, dssr_classes.DSSR_PAIR] = None
        self.__splay_units : List[dssr_classes.DSSR_SPLAY_UNITS] = None
        self.__hbonds : List[dssr_classes.DSSR_HBOND] = None
        self.__hairpins : List[dssr_classes.DSSR_HAIRPIN] = None
        self.__helices : List[dssr_classes.DSSR_HELIX] = None
        self.__stems : List[dssr_classes.DSSR_STEM] = None
        self.__iloops : List[dssr_classes.DSSR_ILOOP] = None
        self.__juctions : List[dssr_classes.DSSR_JUNCTION] = None
        self.__single_strands : List[dssr_classes.DSSR_SINGLE_STRAND] = None

    def __has_data(self, data_name):
        if data_name not in self.__data:
            return False
        else:
            return True

    def __if_set_return(self, atr):
        if atr is not None:
            return atr

    def __populate_attribute(self, data_name, cls):
        atr_data = []
        for d_info in self.__data[data_name]:
            atr_data.append(cls(**d_info))
        return atr_data

    def __get_attribute(self, atr, data_name, cls):
        self.__if_set_return(atr)
        atr = []
        if self.__has_data(data_name):
            atr = self.__populate_attribute(data_name, cls)
        return atr

    # getters
    def get_nts(self) -> Dict[str, dssr_classes.DSSR_NT]:
        self.__if_set_return(self.__nts)

        self.__nts = {}
        if not self.__has_data('nts'):
            return self.__nts

        for nt_info in self.__data['nts']:
            nt = dssr_classes.DSSR_NT(**nt_info)
            self.__nts[nt.nt_id] = nt

        return self.__nts


    def get_pairs(self) -> Dict[str, dssr_classes.DSSR_PAIR]:
        if self.__pairs is not None:
            return self.__pairs

        nts = self.get_nts()
        self.__pairs = {}
        if not self.__has_data('pairs'):
            return self.__pairs

        for pair_info in self.__data['pairs']:
            nt1 = nts[pair_info['nt1']]
            nt2 = nts[pair_info['nt2']]
            del pair_info['nt1']
            del pair_info['nt2']
            id = nt1.nt_id + " " + nt2.nt_id
            self.__pairs[id] = dssr_classes.DSSR_PAIR(nt1, nt2, **pair_info)

        return self.__pairs


    def get_splay_units(self) -> List[dssr_classes.DSSR_SPLAY_UNITS]:
        self.__if_set_return(self.__splay_units)
        self.__splay_units = []
        if self.__has_data("splayUnits"):
            self.__splay_units = self.__populate_attribute("splayUnits", dssr_classes.DSSR_SPLAY_UNITS)
        return self.__splay_units


    def get_hbonds(self) -> List[dssr_classes.DSSR_HBOND]:
        self.__if_set_return(self.__hbonds)
        self.__hbonds = []
        if self.__has_data("hbonds"):
            self.__hbonds = self.__populate_attribute("hbonds", dssr_classes.DSSR_HBOND)
        return self.__hbonds


    def get_hairpins(self) -> List[dssr_classes.DSSR_HAIRPIN]:
        return self.__get_attribute(self.__hairpins, "hairpins",
                                    dssr_classes.DSSR_HAIRPIN)





























