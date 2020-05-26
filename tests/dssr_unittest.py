import unittest

from pydssr import dssr, settings

pdb_path = settings.Paths.UNITTEST_PATH + "/resources/1GID.pdb"

class Unittest(unittest.TestCase):

    def test_basic(self):
        try:
            dssr.DSSROutput(pdb_path)
        except:
            self.fail("should not raise error")

    def test_nts(self):
        d_out = dssr.DSSROutput(pdb_path)
        nts = d_out.get_nts()
        #self.assertTrue(len(nts) == 11)
        #self.assertTrue('G1' in nts)

        nt = nts['A.C138']
        #self.assertTrue(nt.summary == "anti,~C3'-endo,BI,canonical,non-pair-contact,helix-end,stem-end,coaxial-stack")
        print(nt.frame)

    def test_pairs(self):
        d_out = dssr.DSSROutput(pdb_path)
        pairs = d_out.get_pairs()

    def test_splay_units(self):
        d_out = dssr.DSSROutput(pdb_path)
        splay_units = d_out.get_splay_units()
        #for s_u in splay_units:
        #    print(s_u.nts_long)

    def test_hairpins(self):
        d_out = dssr.DSSROutput(pdb_path)
        hairpins = d_out.get_hairpins()
        self.assertTrue(len(hairpins) == 6)
        self.assertTrue(hairpins[0].nts_long == "A.G149,A.G150,A.A151,A.A152,A.A153,A.C154")




def main():
    unittest.main()

if __name__ == '__main__':
    main()