import numpy as np
import LinRegLearner as lrl
import BagLearner as bl
class InsaneLearner(object):
    def __init__(self,verbose=False):
        self.verbose = verbose
        self.learners = [bl.BagLearner(lrl.LinRegLearner, kwargs={}, bags=20) for _ in range(20)]
        pass
    def author(self):
        return "jgoldsher3"
    def add_evidence(self, data_x, data_y):
        for l in self.learners:
            l.add_evidence(data_x,data_y)
        pass
    def query(self, points):
        predictions = []
        for l in self.learners:
            predictions.append(l.query(points))
        return np.mean(np.array(predictions), axis=0)

