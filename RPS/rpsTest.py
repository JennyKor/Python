#Jenny Korkeamäki

import unittest
import rps

class MyTest(unittest.TestCase):

    def test_IfUserInput_and_RandomItemFromTheListAreTheSame(self):

        ##Arrange

        rchoice = "paper"
        choice = "paper"
        expected = "It's a tie."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)
        

    def test_WinningWhenUserInputIsRock_and_RandomItemFromTheListIsScissors(self):

        ##Arrange

        rchoice = "scissors"
        choice = "rock"
        expected = "You won."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)

    def test_WinningWhenUserInputIsPaper_and_RandomItemFromTheListIsPaper(self):

        ##Arrange

        rchoice = "rock"
        choice = "paper"
        expected = "You won."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)


    def test_WinningWhenUserInputIsScissors_and_RandomItemFromTheListIsPaper(self):

        ##Arrange

        rchoice = "paper"
        choice = "scissors"
        expected = "You won."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)
        

    def test_LosingWhenUserInputIsPaper_and_RandomItemFromTheListIsScissors(self):

        ##Arrange

        rchoice = "scissors"
        choice = "paper"
        expected = "You lost."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)


    def test_LosingWhenUserInputIsScissors_and_RandomItemFromTheListIsRock(self):

        ##Arrange

        rchoice = "rock"
        choice = "scissors"
        expected = "You lost."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)
        

    def test_LosingWhenUserInputIsRock_and_RandomItemFromTheListIsSPaper(self):

        ##Arrange

        rchoice = "paper"
        choice = "rock"
        expected = "You lost."

        ##Act

        receive = rps.RockPaperScissors(choice, rchoice)

        ##Assert

        self.assertEqual(receive, expected)
        

if __name__=='__main__':
    unittest.main()
