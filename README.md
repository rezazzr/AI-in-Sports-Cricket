# Reinforcement Learning in Sports: Cricket

Reinforcement learning has already made its mark of expertise in two player strategy games such as chess and GO that require sequential decision making. The game of cricket is also a game between two high level entities (teams) and involves sequential decision making under uncertainty. It requires customizing one's strategy according to the situation they are facing. At the heart of it, we can  view it with similar reinforcement learning problem formulation where the teams can be modeled as agents. In this project we are aiming to find the optimal strategy, using reinforcement learning techniques, for the 2 teams playing against each other.If you are not familiar with the game of cricket, you can read more about the game, [here](https://en.wikipedia.org/wiki/Cricket).<br>
<br>
The goal for the first team (agent 1) is to set a high target (high enough that the second team could not beat it). In our designed environment ([environments.py](https://github.com/rezazzr/AI-in-Sports-Cricket/blob/master/environments.py)) the environment for agent 1 is given by: **(EnvSetTarget)**.<br>
<br>
The **state space** for this agent is defined as follows:

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 

The **action space** for agent 1 is defined in the following chart:

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6

Upon taking an action if the action is successful then the maximum reward associated with that action will be achieved otherwise a reward of zero will be achieved. For example: on action 0 the maximum reward associated is 1. So if the action is successful then reward of 1 will be achieved otherwise the agent would be given a reward of zero.<br>
<br>
#### Start State (initial state)
At the start of the game no time steps have elapsed and no lives have been lost. Therefore we have:
* time_steps_elapsed = 0
* the lives_lost = 0

Which means the **Start State** is given by: [0,0]

#### Terminal State (episode termination)
The episodes terminates if the agent 1 reaches any of the following states:

* The time is over. That is the *time_steps_elapsed* becomes equal to *max_time_steps elapsed* that was set by the user when creating the environment.
* All the lives have been lost. That is the variable *lives_lost* becomes equal to the max lives that the user had set when creating the environment.

For example if the *env* was created and initialized with max time steps = 6, and max lives = 2 then all states [6,-] and [-,2] are terminal states.<br>
<br>

---

The second team (agent 2) should come up with a strategy to be able to beat the first team's high score. In other words agent 2 aims to beat/chase a target score set by the agent 1. n our designed environment ([environments.py](https://github.com/rezazzr/AI-in-Sports-Cricket/blob/master/environments.py)) the environment for agent 2 is given by: **(EnvChaseTarget)**.<br>
<br>
The **state space** for this agent is defined as follows:

Num | Observation | Min | Max
---|---|---|---
0 | time_steps_elapsed(number of darts thrown so far) | 0 | max_time_steps_elapsed set by the user
1 |  lives_lost | 0 | max_lives_lost set by the user 
2 | distance_from_target | -5 | target

The **action space** for agent 2 is defined in the following chart:

Action Number | Max Reward associated| Prob. of success
------------ | -------------|--------------
0 | 1 | 0.95
1 | 2 | 0.88
2 | 4 | 0.80
3 | 6 | 0.6

Agent 2 will receive a reward of +1 if it can achieve the target that was set by agent 1 otherwise if by the end of the episode the target is not achieved then a reward of -1 is given to agent 2. Hence, only upon reaching the terminal states a non-zero reward will be given to this agent.
