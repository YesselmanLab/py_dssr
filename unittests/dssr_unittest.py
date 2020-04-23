import unittest

from py_dssr import dssr, settings

pdb_path = "/Users/josephyesselman/projects/Rosetta.projects/motif_folding/runs/fixed_ends/TWOWAY.1S72.47/S_000001.pdb"

class Unittest(unittest.TestCase):

    def test_basic(self):
        try:
            dssr.DSSROutput(pdb_path)
        except:
            self.fail("should not raise error")

    def test_nts(self):
        d_out = dssr.DSSROutput(pdb_path)
        nts = d_out.get_nts()
        self.assertTrue(len(nts) == 11)
        self.assertTrue('G1' in nts)

        nt = nts['G1']
        self.assertTrue(nt.summary == "anti,~C3'-endo,BI,canonical,non-pair-contact,helix-end,stem-end,coaxial-stack")

    def test_pairs(self):
        d_out = dssr.DSSROutput(pdb_path)
        pairs = d_out.get_pairs()

    def test_splay_units(self):
        d_out = dssr.DSSROutput(pdb_path)
        splay_units = d_out.get_splay_units()
        for s_u in splay_units:
            print(s_u.nts_long)


def main():
    unittest.main()

if __name__ == '__main__':
    main()