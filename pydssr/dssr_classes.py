from typing import List, Dict


class DSSR_NT (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.index_chain : int = None 
        self.chain_name : str = None 
        self.nt_resnum : int = None 
        self.nt_name : str = None 
        self.nt_code : str = None 
        self.nt_id : str = None 
        self.dbn : str = None 
        self.summary : str = None 
        self.alpha = None 
        self.beta = None 
        self.gamma : float = None 
        self.delta : float = None 
        self.epsilon : float = None 
        self.zeta : float = None 
        self.epsilon_zeta : float = None 
        self.bb_type : str = None 
        self.chi : float = None 
        self.glyco_bond : str = None 
        self.C5prime_xyz : list = None 
        self.P_xyz : list = None 
        self.form : str = None 
        self.ssZp : float = None 
        self.Dp : float = None 
        self.splay_angle : float = None 
        self.splay_distance : float = None 
        self.splay_ratio : float = None 
        self.eta = None 
        self.theta = None 
        self.eta_prime = None 
        self.theta_prime = None 
        self.eta_base = None 
        self.theta_base = None 
        self.v0 : float = None 
        self.v1 : float = None 
        self.v2 : float = None 
        self.v3 : float = None 
        self.v4 : float = None 
        self.amplitude : float = None 
        self.phase_angle : float = None 
        self.puckering : str = None 
        self.sugar_class : str = None 
        self.bin : str = None 
        self.cluster : str = None 
        self.suiteness : float = None 
        self.filter_rmsd : float = None 
        self.frame : dict = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_PAIR (object): 
    def __init__(self, nt1 : DSSR_NT, nt2 : DSSR_NT, **kwargs):
        self.nt1 = nt1
        self.nt2 = nt2
        self.index : int = None 
        self.bp : str = None 
        self.name : str = None 
        self.Saenger : str = None 
        self.LW : str = None 
        self.DSSR : str = None 
        self.chi1 : float = None 
        self.conf1 : str = None 
        self.pucker1 : str = None 
        self.lambda1 : float = None 
        self.chi2 : float = None 
        self.conf2 : str = None 
        self.pucker2 : str = None 
        self.lambda2 : float = None 
        self.C1C1_dist : float = None 
        self.N1N9_dist : float = None 
        self.C6C8_dist : float = None 
        self.CNNC_torsion : float = None 
        self.hbonds_num : int = None 
        self.hbonds_desc : str = None 
        self.interBase_angle : float = None 
        self.planarity : float = None 
        self.simple_Shear : float = None 
        self.simple_Stretch : float = None 
        self.simple_Buckle : float = None 
        self.simple_Propeller : float = None 
        self.bp_params : list = None 
        self.frame : dict = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_HAIRPIN (object): 
    def __init__(self, **kwargs):
        self.mtype = 'HAIRPIN'
        self.index : int = None
        self.type : str = None 
        self.bridging_nts : list = None 
        self.stem_indices : list = None 
        self.summary : str = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 
        self.num_stems : int = None 
        self.bridges : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.nts_long = self.nts_long.split(",")


class DSSR_HELIX (object): 
    def __init__(self, **kwargs):
        self.mtype = 'HEXIX'
        self.index : int = None
        self.num_stems : int = None 
        self.strand1 : str = None 
        self.strand2 : str = None
        self.nts_long = self.strand1 + "," + self.strand2
        self.bp_type : str = None 
        self.helix_form : str = None 
        self.helical_rise : float = None 
        self.helical_rise_std : float = None 
        self.helical_radius : float = None 
        self.helical_radius_std : float = None 
        self.helical_axis : list = None 
        self.point1 : list = None 
        self.point2 : list = None 
        self.num_pairs : int = None 
        self.pairs : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_STEM (object): 
    def __init__(self, **kwargs):
        self.mtype = 'STEM'
        self.index : int = None 
        self.helix_index : int = None 
        self.strand1 : str = None 
        self.strand2 : str = None
        self.helix_form : str = None
        self.helical_rise : float = None 
        self.helical_rise_std : float = None 
        self.helical_radius : float = None 
        self.helical_radius_std : float = None 
        self.helical_axis : list = None 
        self.point1 : list = None 
        self.point2 : list = None 
        self.num_pairs : int = None 
        self.pairs : list = None
        self.bp_type : str = None

        for key, value in kwargs.items():
            setattr(self, key, value)

        nts = []
        for p in self.pairs:
            nts.append(p['nt1'])
            nts.append(p['nt2'])
        self.nts_long = nts


class DSSR_ILOOP (object): 
    def __init__(self, **kwargs):
        self.mtype = 'ILOOP'
        self.index : int = None 
        self.type : str = None 
        self.bridging_nts : list = None 
        self.stem_indices : list = None 
        self.summary : str = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 
        self.num_stems : int = None 
        self.bridges : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.nts_long = self.nts_long.split(",")


class DSSR_JUNCTION (object): 
    def __init__(self, **kwargs):
        self.mtype = 'JUNCTION'
        self.index : int = None 
        self.type : str = None 
        self.bridging_nts : list = None 
        self.stem_indices : list = None 
        self.summary : str = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 
        self.num_stems : int = None 
        self.bridges : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.nts_long = self.nts_long.split(",")



class DSSR_SINGLE_STRAND (object): 
    def __init__(self, **kwargs):
        self.mtype = 'SINGLE_STRAND'
        self.index : int = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.nts_long = self.nts_long.split(",")


class DSSR_KISSING_LOOP (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.stem_index : int = None 
        self.is_isoCanonPair = None 
        self.hairpin_indices : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_AMINOR (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.type : str = None 
        self.desc_short : str = None 
        self.desc_long : str = None 
        self.A_nt1 : dict = None 
        self.A_nt2 : dict = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_RIBOSE_ZIPPER (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_PSEUDOKNOT (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.desc : str = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_HBOND (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.atom1_serNum : int = None 
        self.atom2_serNum : int = None 
        self.donAcc_type : str = None 
        self.distance : float = None 
        self.atom1_id : str = None 
        self.atom2_id : str = None 
        self.atom_pair : str = None 
        self.residue_pair : str = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_SPLAY_UNITS (object): 
    def __init__(self, **kwargs):
        self.index : int = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 

        for key, value in kwargs.items():
            setattr(self, key, value)


class DSSR_BULGE (object): 
    def __init__(self, **kwargs):
        self.mtype = 'BULGE'
        self.index : int = None 
        self.type : str = None 
        self.bridging_nts : list = None 
        self.stem_indices : list = None 
        self.summary : str = None 
        self.num_nts : int = None 
        self.nts_short : str = None 
        self.nts_long : str = None 
        self.num_stems : int = None 
        self.bridges : list = None 

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.nts_long = self.nts_long.split(",")


