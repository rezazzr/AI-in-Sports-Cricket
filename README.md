# Reinforcement Learning in Sports: Cricket

Reinforcement learning has already made its mark of expertise in two player strategy games such as chess and GO that require sequential decision making. The game of cricket is also a game between two high level entities (teams) and involves sequential decision making under uncertainty. It requires customizing one's strategy according to the situation they are facing. At the heart of it, we can  view it with similar reinforcement learning problem formulation where the teams can be modeled as agents. In this project we are aiming to find the optimal strategy, using reinforcement learning techniques, for the 2 teams playing against each other.If you are not familiar with the game of cricket, you can read more about the game, [here](https://en.wikipedia.org/wiki/Cricket).<br>
<br>
The goal for the first team (agent 1) is to set a high target (high enough that the second team could not beat it). In our designed environemnt ([environments.py](https://github.com/rezazzr/AI-in-Sports-Cricket/blob/master/environments.py)) the agent would like to set a high value for the target through *(EnvSetTarget)*.<br>
<br>
The state space for this agent is defined as follows:

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 
