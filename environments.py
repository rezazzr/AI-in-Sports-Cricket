import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt

#env for 1st agent as it needs to set a target
class EnvSetTarget:

	#max_time_steps - total num of darsts
	#max_lives_lost -total lives
    def __init__(self,max_time_steps,max_lives_lost):
        self.min_time_steps_elapsed = 0
        self.max_time_steps_elapsed=max_time_steps
        self.min_lives_lost=0
        self.max_lives_lost=max_lives_lost
        #self.max_steps = 120
        
        #state variables
        self.time_steps_elapsed = 0 #this represents the #darts you have thrown so far(0,119)
        self.lives_lost = 0#lives lost so far(min=0,max=9)you have atmost 10 lives
        
        #action sapce
        self.action_space={
            0:self.__one,
            1:self.__two,
            2:self.__four,
            3:self.__six
        }

    @property
    def time_steps_elapsed(self):
        return self.__time_steps_elapsed

    @time_steps_elapsed.setter
    def time_steps_elapsed(self,time_steps_elapsed):
        if time_steps_elapsed >= self.min_time_steps_elapsed and time_steps_elapsed<=self.max_time_steps_elapsed:
            self.__time_steps_elapsed = time_steps_elapsed
        else:
            print("time_steps_elapsed needs to be within ",
                  self.min_time_steps_elapsed," and ",self.max_time_steps_elapsed)
            raise Exception

    @property
    def lives_lost(self):
        return self.__lives_lost

    @lives_lost.setter
    def lives_lost(self,lives_lost):
        if lives_lost >= self.min_lives_lost and lives_lost <= self.max_lives_lost:
            self.__lives_lost = lives_lost
        else:
            print("lives_lost needs to be within ",self.min_lives_lost," and ",self.max_lives_lost)
            raise Exception


    def set_state(self,state_vector):
        """
        Set the state to some arbitrary value
        May be helpful in learning for exploratory starts
        :param state_vector: array([time_steps_elapsed,lives_lost])
        :return:
        """
        self.time_steps_elapsed = state_vector[0]
        self.lives_lost = state_vector[1]

    def reset(self):
        """
        reset the environment to start state
        :return:
        """
        self.time_steps_elapsed = 0
        self.lives_lost = 0
        return np.array([self.time_steps_elapsed,self.lives_lost])

    def step(self,action):
        """

        :param action:
        :return:
        """
        reward = self.action_space[action]()
        done=False
        self.time_steps_elapsed +=1
        if reward == 0:
            self.lives_lost +=1
        done = self.__all_lives_lost() or self.__time_over()
        observation = np.array([self.time_steps_elapsed,self.lives_lost])
        info=None
        return observation,reward,done,info

    def __all_lives_lost(self):
        """

        :return: True if all lives lost else returns False
        """
        if self.lives_lost == self.max_lives_lost:
            return True
        else:
            return False

    def __time_over(self):
        """
        Returns true if end of episode due to finishing of time(thrown all the darts)
        :return:
        """
        if self.time_steps_elapsed == self.max_time_steps_elapsed:
            return True
        else:
            return False


    def __one(self):
        val = np.random.random()
        if val <= 0.95:
            return 1
        else:
            return 0

    def __two(self):
        val = np.random.random()
        if val <= 0.88:
            return 2
        else:
            return 0

    def __four(self):
        val = np.random.random()
        if val <= 0.8:
            return 4
        else:
            return 0

    def __six(self):
        val = np.random.random()
        if val <= 0.6:
            return 6
        else:
            return 0




#second agent
class EnvChaseTarget(EnvSetTarget):

    def __init__(self,max_time_steps,max_lives_lost,target):
        EnvSetTarget.__init__(self,max_time_steps,max_lives_lost)
        self.distance_from_target = target
        self.init_target = target

    def reset(self,target):
        """

        :return:
        """
        arr = EnvSetTarget.reset(self)
        self.distance_from_target = target
        return np.append(arr,self.distance_from_target)

    def set_state(self,state_vector):
        """

        :param state_vector:
        :return:
        """
        EnvSetTarget.set_state(self,state_vector)
        self.distance_from_target = state_vector[2]

    def step(self,action):
        """

        :param action:
        :return:
        """

        observation, reward, done, info = EnvSetTarget.step(self,action)
        self.distance_from_target -= reward
        observation = np.append(observation,self.distance_from_target)
        reward = 0
        if done: #if already ended due to time over or loosing of all lives
            done = True
            reward = -1

        if self.__target_achieved():
            done = True
            reward = +1

        return observation, reward, done, info

    def __target_achieved(self):
        if self.distance_from_target <= 0:
            return True
        else:
            return False


