""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import math  		  	   		  		 		  		  		    	 		 		   		 		  
import sys  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import LinRegLearner as lrl
import DTLearner as dt
import BagLearner as bl
import InsaneLearner as it
import matplotlib.pyplot as plt
import time

""""""
"""  		  	   		   	 		  		  		    	 		 		   		 		  
Test a learner.  (c) 2015 Tucker Balch  		  	   		   	 		  		  		    	 		 		   		 		  

Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		   	 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		   	 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		   	 		  		  		    	 		 		   		 		  

Template code for CS 4646/7646  		  	   		   	 		  		  		    	 		 		   		 		  

Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		   	 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		   	 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		   	 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		   	 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		   	 		  		  		    	 		 		   		 		  
or edited.  		  	   		   	 		  		  		    	 		 		   		 		  

We do grant permission to share solutions privately with non-students such  		  	   		   	 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		   	 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		   	 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		   	 		  		  		    	 		 		   		 		  

-----do not edit anything above this line---  		  	   		   	 		  		  		    	 		 		   		 		  
"""

import math
import sys
import numpy as np
import DTLearner as dt
import RTLearner as rt
import LinRegLearner as lrl
# import BagLearner as bl
# import InsaneLearner as il
# import matplotlib.pyplot as plt
# from datetime import datetime


def get_sample(x, y):
    if len(y.shape) == 1:
        y = np.reshape(y, (-1, 1))
    data = np.append(x, y, axis=1)
    obs = data.shape[0]
    rand_ind = np.random.randint(obs, size=obs)
    new_data = np.zeros(data.shape)
    for row in range(0, obs):
        new_data[row] = data[rand_ind[row]]
    new_x = new_data[:, 0:data.shape[1] - 1]
    new_y = new_data[:, -1]
    return new_x, new_y





if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python testlearner.py <filename>")
        sys.exit(1)
    inf = open(sys.argv[1])
    with inf as file:
        data = np.genfromtxt(file, delimiter=",")
        data = data[1:, 1:]

    print(data.shape[0])
    # # compute how much of the data is training and testing
    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    train_x = data[:train_rows, 0:-1]
    train_y = data[:train_rows, -1]
    test_x = data[train_rows:, 0:-1]
    test_y = data[train_rows:, -1]
  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"{test_x.shape}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"{test_y.shape}")  		  	   		  		 		  		  		    	 		 		   		 		  
  	#
    # # create a learner and train it
    # print('LRL learner')
    # learner = lrl.LinRegLearner(verbose=True)  # create a LinRegLearner
    # learner.add_evidence(train_x, train_y)  # train it
    # print(learner.author())
    #
    # # evaluate in sample
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    # print()
    # print("In sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0,1]}")
    #
    # # evaluate out of sample
    # pred_y = learner.query(test_x)  # get the predictions
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print()
    # print("Out of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0,1]}")

    # create a DT learner and train it
    # print('DT Learner testing')
    # learner = dt.DTLearner(leaf_size = 10,verbose=True)  # create a LinRegLearner
    # learner.add_evidence(train_x, train_y)  # train it
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    # print("In sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0, 1]}")
    #
    # # evaluate out of sample
    # pred_y = learner.query(test_x)
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print()
    # print("Out of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0, 1]}")
    #
    # # create a RT learner and train it
    # print('RT Learner testing')
    # learner = rt.RTLearner(leaf_size=1, verbose=True)
    # learner.add_evidence(train_x, train_y)  # train it
    # print(learner.author())
    #
    # # evaluate in sample
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    # print("In sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0, 1]}")
    #
    # # evaluate out of sample
    # pred_y = learner.query(test_x)  # get the predictions
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print()
    # print("Out of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0, 1]}")
    # print('Bag Learner testing')
    # learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": 50}, bags=20, boost=False, verbose=False)
    # learner.add_evidence(train_x, train_y)  # train it
    # print(learner.author())
    # pred_y = learner.query(train_x)  # get the predictions
    # rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])
    #
    # print("In sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=train_y)
    # print(f"corr: {c[0, 1]}")
    #
    # pred_y = learner.query(test_x)  # get the predictions
    # rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    # print()
    # print("Out of sample results")
    # print(f"RMSE: {rmse}")
    # c = np.corrcoef(pred_y, y=test_y)
    # print(f"corr: {c[0, 1]}")

    print('Insane Learner testing')
    learner = it.InsaneLearner(verbose = False) # constructor
    learner.add_evidence(train_x, train_y)  # train it
    print(learner.author())
    pred_y = learner.query(train_x)  # get the predictions
    rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])

    print("In sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=train_y)
    print(f"corr: {c[0, 1]}")

    pred_y = learner.query(test_x)  # get the predictions
    rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
    print()
    print("Out of sample results")
    print(f"RMSE: {rmse}")
    c = np.corrcoef(pred_y, y=test_y)
    print(f"corr: {c[0, 1]}")

    #Experiment 1, look at overfitting across leaf size
    bags = [1,5,10,20,30,40,50]
    rmse_save_is = []
    rmse_save_os = []
    for b in range(0,len(bags)):
        print('DT Learner testing')
        learner = dt.DTLearner(leaf_size=bags[b], verbose=True)  # create a LinRegLearner
        learner.add_evidence(train_x, train_y)  # train it
        pred_y = learner.query(train_x)  # get the predictions
        rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])

        print("In sample results")
        print(f"RMSE: {rmse}")
        rmse_save_is.append(rmse)
        c = np.corrcoef(pred_y, y=train_y)
        print(f"corr: {c[0, 1]}")

        pred_y = learner.query(test_x)  # get the predictions
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])

        print("Out of sample results")
        print(f"RMSE: {rmse}")
        rmse_save_os.append(rmse)
        c = np.corrcoef(pred_y, y=test_y)
        print(f"corr: {c[0, 1]}")
    plt.plot(bags[::-1], rmse_save_is, color='blue', label='In-Sample')
    plt.plot(bags[::-1],rmse_save_os, color='red', label='Out of Sample')
    plt.title('RMSE across leaf sizes')
    plt.ylabel('RMSE')
    plt.xlabel('Leaf Size INV')
    plt.legend()
    figure_1 = plt.gcf()
    figure_1.savefig('exp_1image.png')
    plt.clf()


   #Experiment 1, look at overfitting across leaf size
    bags = [10,20,30,20,40, 50,100]
    leaves = [1,5,10,20,30,40,50]

    for b in range(0,len(bags)):
        rmse_save_is = []
        rmse_save_os = []
        for l in range(0,len(leaves)):
            print('Bag Learner testing')
            learner = bl.BagLearner(learner=dt.DTLearner, kwargs={"leaf_size": leaves[l]}, bags=bags[b], boost=False, verbose=False)
            learner.add_evidence(train_x, train_y)  # train it
            pred_y = learner.query(train_x)  # get the predictions
            rmse = math.sqrt(((train_y - pred_y) ** 2).sum() / train_y.shape[0])

            print("In sample results")
            print(f"RMSE: {rmse}")
            rmse_save_is.append(rmse)
            c = np.corrcoef(pred_y, y=train_y)
            print(f"corr: {c[0, 1]}")

            pred_y = learner.query(test_x)  # get the predictions
            rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])

            print("Out of sample results")
            print(f"RMSE: {rmse}")
            rmse_save_os.append(rmse)
            c = np.corrcoef(pred_y, y=test_y)
            print(f"corr: {c[0, 1]}")
        plt.clf()
        plt.plot(leaves[::-1], rmse_save_is, color='blue', label='In-Sample')
        plt.plot(leaves[::-1],rmse_save_os, color='red', label='Out of Sample')
        plt.title('Bag size ' + str(bags[b]) + ' RMSE across leaf sizes')
        plt.ylabel('RMSE')
        plt.xlabel('Leaf Size INV')
        plt.legend()
        figure_1 = plt.gcf()
        figure_1.savefig('bag_size '+ str(bags[b]) + 'img.png')

    #Experiment 3, time to train and coeff of determination between DT and RT
    leaves = [1,5,10,25,50]
    dc = []
    dcr = []
    tt = []
    ttr = []
    for l in range(0,len(leaves)):
        print('DT Learner testing')
        start_time = time.time()
        learner = dt.DTLearner(leaf_size=leaves[l], verbose=True)  # create a LinRegLearner
        learner.add_evidence(train_x, train_y)  # train it
        diff = time.time() - start_time
        tt.append(diff)
        #training correlation
        pred_y = learner.query(train_x)  # get the predictions
        c = np.corrcoef(pred_y, y=train_y)

        #testing correlation
        pred_y = learner.query(test_x)  # get the predictions
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        c = np.corrcoef(pred_y, y=test_y)
        sq = c[0,1]**2
        dc.append(sq)

        print('RT Learner testing')
        start_time = time.time()
        learner = rt.RTLearner(leaf_size=leaves[l], verbose=True)  # create a LinRegLearner
        learner.add_evidence(train_x, train_y)  # train it
        diff = time.time() - start_time
        ttr.append(diff)
        # training correlation
        pred_y = learner.query(train_x)  # get the predictions
        c = np.corrcoef(pred_y, y=train_y)

        # testing correlation
        pred_y = learner.query(test_x)  # get the predictions
        rmse = math.sqrt(((test_y - pred_y) ** 2).sum() / test_y.shape[0])
        c = np.corrcoef(pred_y, y=test_y)
        sq = c[0,1] ** 2
        dcr.append(sq)
    plt.clf()
    plt.plot(leaves[::-1], dc, color='green', label='DT')
    plt.plot(leaves[::-1], dcr, color='yellow', label='RT')
    plt.title(' R-squared between DT and RT across leaf size')
    plt.ylabel('R-Squared')
    plt.xlabel('Leaf Size INV')
    plt.legend()
    figure_1 = plt.gcf()
    figure_1.savefig('dt_rt_img.png')

    plt.clf()

    plt.plot(leaves, tt, color='green', label='DT')
    plt.plot(leaves, ttr, color='yellow', label='RT')
    plt.title('Training Time between DT and RT across leaf size')
    plt.ylabel('Training Time (Seconds)')
    plt.xlabel('Leaf Size INV')
    plt.legend()
    figure_1 = plt.gcf()
    figure_1.savefig('dt_rt_time_img.png')


