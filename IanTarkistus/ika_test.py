##Jenny Korkeamäki
import unittest
import ian_tarkistus

class MyTest(unittest.TestCase):

    def test_AssignNumberToInt_ika_and_CheckIfAgeIsUnder18(self):
        ##Arrange
        ika = 9
        expected = "Olet lapsi"
        
        ##Act

        receive = ian_tarkistus.tarkista_ika(ika)

        ##Assert

        self.assertEqual(receive, expected)
        
    def test_AssignNumberToInt_ika_and_CheckIfAgeIsEqualOrAbove18ButUnder70(self):
        ##Arrange
        ika = 20
        expected = "Olet aikuinen"
        
        ##Act

        receive = ian_tarkistus.tarkista_ika(ika)

        ##Assert

        self.assertEqual(receive, expected)

    def test_AssignNumberToInt_ika_and_CheckIfAgeIsEqualOrAbove70(self):
        ##Arrange
        ika = 70
        expected = "Olet eläkeläinen"
        
        ##Act

        receive = ian_tarkistus.tarkista_ika(ika)

        ##Assert

        self.assertEqual(receive, expected)


if __name__=='__main__':
    unittest.main()
