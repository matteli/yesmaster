#!/usr/bin/python
# -*- coding: utf8 -*-"
import collections
import random

def combinations(colors, nb):
    result = []
    if nb == 0:
        return [[]]
    for r in combinations(colors, nb-1):
        for c in colors:
            result.append([c] + r)
    return result

# The response is (misplaced, good):
# For example:
# (0, 0) => Eliminate all colors from proposal
# (0, 4) => Won
# (4, 0) => You have all colors but in the wrong order
def score_proposal(proposal, combination):
    misplaced = 0
    good = 0
    counted = set()
    # PPGA
    # WPYP
    for (i, p) in enumerate(proposal):
        if proposal[i] not in combination:
            continue
        if proposal[i] == combination[i]:
            good += 1
        else:
            for (j, c) in enumerate(combination):
                if proposal[i] == combination[j] and proposal[j] != combination[j] and j not in counted:
                    misplaced += 1
                    counted.add(j)
                    break
    return (misplaced, good)

# Returns a map from proposal to (a map from scores to how many combinations
# from candidates give this score).
# Consider all possible combinations.
def proposals_scores_stats_all(candidates, colors, nb):
    result = collections.defaultdict(lambda: collections.defaultdict(int))
    for candidate in candidates:
        for proposal in combinations(colors, nb):
            result[tuple(proposal)][score_proposal(proposal, candidate)] += 1
    return result

# Returns a map from proposal to (a map from scores to how many combinations
# from candidates give this score).
# Consider only potentially valid combinations (i.e matching previous scores).
def proposals_scores_stats_candidates(candidates):
    result = collections.defaultdict(lambda: collections.defaultdict(int))
    for candidate in candidates:
        for proposal in candidates:
            result[tuple(proposal)][score_proposal(proposal, candidate)] += 1
    return result

# Returns a map from proposition to the expectation of elimination.
def proposals_elimination_expectation(candidates, colors, nb, candidates_only):
    if candidates_only:
        stats = proposals_scores_stats_candidates(candidates)
    else:
        stats = proposals_scores_stats_all(candidates, colors, nb)
    result = {}
    N = len(candidates)
    for (prop, scores) in stats.items():
        expectation = 0
        for (score, nb) in scores.items():
            expectation += (N - nb) * nb / N
        result[prop] = expectation
    return result

def find_best_proposal(candidates, colors, nb, candidates_only):
    max_k, max_v, max_r = None, None, None
    for (k,v) in proposals_elimination_expectation(candidates, colors, nb, candidates_only).items():
        if max_v is None or (v > max_v and v > 0.0):
            max_k, max_v, max_r = k, v, random.random()
        elif v == max_v:
            r = random.random()
            if r > max_r:
                max_k, max_v, max_r = k, v, r
    # It's always better to take a candidate if it has the same score, has it
    # gives a chance to win immediately.
    if not candidates_only and list(max_k) not in candidates:
        #print("Proposal %s is not in candidates (value=%s)." % (max_k, max_v))
        for (k,v) in proposals_elimination_expectation(candidates, colors, nb, True).items():
            if v == max_v:
                #print("But %s is and has same value: %s." % (k, v))
                max_k = k
                break
    if max_k is None:
        print("max_k is None: %s" % candidates)
    return max_k


class Algo:

  def __init__(self):
    self.nb_slots = 4
    self.colors = ['R', 'O', 'G', 'B', 'Y', 'A', 'P', 'W']
    self.candidates = combinations(self.colors, self.nb_slots)
    self.nb_tries = 0

  def get(self):
    if self.nb_tries == 0:
        random.shuffle(self.colors)
        proposal = self.colors[:self.nb_slots]
    elif len(self.candidates) <= 3:
        proposal = find_best_proposal(self.candidates, self.colors, self.nb_slots, True)
    else:
        # Note: The last False could be a parameter of the algorithm: whether to
        # limit ourselves to valid candidates only for the whole game.
        proposal = find_best_proposal(self.candidates, self.colors, self.nb_slots, False)
    self.nb_tries += 1
    return "".join(proposal)

  def report(self, proposal, good, misplaced):
    self.candidates = [c for c in self.candidates if score_proposal(proposal, c) == (misplaced, good)]

