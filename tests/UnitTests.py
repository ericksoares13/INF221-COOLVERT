from ContratanteTest import ContratanteTest
from DadosBancariosTest import DadosBancariosTest
from DemandaTest import DemandaTest
from ImagemTest import ImagemTest
from MatchTest import MatchTest
from MensagemTest import MensagemTest
from MusicoTest import MusicoTest
from PessoaTest import PessoaTest
from UsuarioTest import UsuarioTest
import unittest


class UnitTests(unittest.TestSuite):
    def __init__(self):
        super(UnitTests, self).__init__()
        self.addTest(unittest.makeSuite(ContratanteTest))
        self.addTest(unittest.makeSuite(DadosBancariosTest))
        self.addTest(unittest.makeSuite(DemandaTest))
        self.addTest(unittest.makeSuite(ImagemTest))
        self.addTest(unittest.makeSuite(MatchTest))
        self.addTest(unittest.makeSuite(MensagemTest))
        self.addTest(unittest.makeSuite(MusicoTest))
        self.addTest(unittest.makeSuite(PessoaTest))
        self.addTest(unittest.makeSuite(UsuarioTest))


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(UnitTests())
