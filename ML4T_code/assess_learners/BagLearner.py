import numpy as np
import LinRegLearner as lrl
import DTLearner as dt
import RTLearner as rt
import random
class BagLearner(object):
    """
    This is a Random Tree Learner

    :param verbose: If “verbose” is True, your code can print out information for debugging.
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.
    :type verbose: bool
    """

    def __init__(self, learner=object, kwargs={}, bags=10, boost=False, verbose=False):
        """
        Constructor method
        """
        self.verbose = verbose
        l = []
        for i in range(0, bags):
            l.append(learner(**kwargs))
        self.learners = l
        self.learner = learner
        self.boost = False
        self.bags = bags
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "jgoldsher3"  # replace tb34 with your Georgia Tech username

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        data_all = np.column_stack((data_x, data_y))
        for l in self.learners:
            x, y = self.get_bags(data_all)
            l.add_evidence(x,y)
        pass

    def get_bags(self, data_all):
        for b in range(self.bags):
            new_rand = random.sample(range(data_all.shape[0]), data_all.shape[0])
            this_x = data_all[new_rand, :-1]
            this_y = data_all[new_rand, -1]
            return this_x, this_y
    def query(self, points):
        predictions = []
        for l in self.learners:
            predictions.append(l.query(points))
        return np.mean(np.array(predictions), axis=0)

