## Jenny Korkeamäki
import unittest
import Kolmiot

class MyTest(unittest.TestCase):

    def test_AssignLengthsToTrianglSides_and_CheckIfTwoAreEqual(self):

        # Arrange

        sivu1 = float(4)
        sivu2 = float(2.6)
        sivu3 = float(2.6)
        expected = "tasakylkinen"

        # Act

        receive = Kolmiot.LueSivut(sivu1 ,sivu2, sivu3)

        # Assert

        self.assertEqual(receive, expected)

    def test_AssignLengthsTriangleSides_and_CheckIfAllAreEqual(self):

        ##Arrange

        sivu1 = float(4)
        sivu2 = float(4)
        sivu3 = float(4)
        expected = "tasasivuinen"

        ##Act

        receive = Kolmiot.LueSivut(sivu1 ,sivu2, sivu3)

        ##Assert

        self.assertEqual(receive, expected)

    def test_AssignLengthsToTriangleSides_and_CheckIfNoneAreEqual(self):

        ##Arrange

        sivu1 = float(2)
        sivu2 = float(5)
        sivu3 = float(3.1)
        expected = "epäsäännöllinen"

        ##Act

        receive = Kolmiot.LueSivut(sivu1 ,sivu2, sivu3)

        ##Assert

        self.assertEqual(receive, expected)

if __name__=='__main__':
    unittest.main()
