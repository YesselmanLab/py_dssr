
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

