#!/usr/bin/python
# -*- coding: utf8 -*-"

import one_step_ahead
import unittest

class TestOneStepAhead(unittest.TestCase):

  def testScoreProposalNoCommon(self):
    self.assertEqual(one_step_ahead.score_proposal([0, 0, 0, 0], [1, 1, 1, 1]), (0, 0))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [4, 5, 6, 7]), (0, 0))

  def testScoreProposalMisplaced(self):
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [1, 4, 5, 6]), (1, 0))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [4, 5, 1, 2]), (2, 0))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [1, 2, 3, 6]), (3, 0))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [1, 2, 3, 0]), (4, 0))

  def testScoreProposalGood(self):
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [0, 4, 5, 6]), (0, 1))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [4, 1, 2, 5]), (0, 2))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [6, 1, 2, 3]), (0, 3))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [0, 1, 2, 3]), (0, 4))

  def testScoreProposalMisplacedAndGood(self):
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [0, 4, 5, 1]), (1, 1))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [3, 1, 2, 5]), (1, 2))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [6, 1, 3, 2]), (2, 1))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [0, 1, 3, 2]), (2, 2))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [3, 1, 0, 2]), (3, 1))

  def testScoreProposalRepetitions(self):
    self.assertEqual(one_step_ahead.score_proposal([1, 1, 2, 3], [0, 4, 1, 6]), (1, 0))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [1, 1, 5, 6]), (0, 1))
    self.assertEqual(one_step_ahead.score_proposal([1, 1, 1, 1], [0, 1, 2, 3]), (0, 1))
    self.assertEqual(one_step_ahead.score_proposal([0, 1, 2, 3], [1, 1, 1, 1]), (0, 1))
    self.assertEqual(one_step_ahead.score_proposal([1, 1, 2, 3], [1, 1, 1, 1]), (0, 2))
    self.assertEqual(one_step_ahead.score_proposal([1, 1, 2, 3], [1, 1, 3, 2]), (2, 2))

  def testScoreProposalMisc(self):
    self.assertEqual(one_step_ahead.score_proposal([0, 4, 3, 4], [4, 3, 6, 3]), (2, 0))

  def testScoreProposalMisc2(self):
    to_guess = 'WPYP'
    self.assertEqual(one_step_ahead.score_proposal('OGWR', to_guess), (1, 0))
    self.assertEqual(one_step_ahead.score_proposal('AYPO', to_guess), (2, 0))
    self.assertEqual(one_step_ahead.score_proposal('BRYA', to_guess), (0, 1))
    self.assertEqual(one_step_ahead.score_proposal('GPPY', to_guess), (2, 1))
    self.assertEqual(one_step_ahead.score_proposal('PPGA', to_guess), (1, 1))
    self.assertEqual(one_step_ahead.score_proposal('YPYG', to_guess), (0, 2))

if __name__ == '__main__':
    unittest.main()
