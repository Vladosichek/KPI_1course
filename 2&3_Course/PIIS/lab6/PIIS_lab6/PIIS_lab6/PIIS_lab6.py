def runValueIteration(self):
# Write value iteration code here
"*** YOUR CODE HERE ***"
for iteration in range(self.iterations):
temp = util.Counter()
for state in self.mdp.getStates():
if self.mdp.isTerminal(state):
temp[state] = 0
else:
maximumValue = -99999
actions = self.mdp.getPossibleActions(state)
for action in actions:
t = self.mdp.getTransitionStatesAndProbs(state, action)
value = 0
for stateProb in t:
value += stateProb[1] * (self.mdp.getReward(state, action,
stateAndProb[1]) + self.discount * self.values[stateAndProb[0]])
maximumValue = max(value, maximumValue)
if maximumValue != -99999:
temp[state] = maximumValue
self.values = temp
