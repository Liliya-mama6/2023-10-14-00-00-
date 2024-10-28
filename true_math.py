import unittest
import ege
import kontest


case=unittest.TestSuite()
case.addTest(unittest.TestLoader().loadTestsFromTestCase(ege.TournamentTest))
case.addTest(unittest.TestLoader().loadTestsFromTestCase(kontest.RunnerTest))
text=unittest.TextTestRunner(verbosity=2)
text.run(case)
