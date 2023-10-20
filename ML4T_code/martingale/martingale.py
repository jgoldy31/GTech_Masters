""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
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
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt
import pandas as pd
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "jgoldsher"  # replace tb34 with your Georgia Tech username.
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 900897987  # replace with your GT ID number  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """
    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def run_one_episode():
    episode_winnings = 0
    #vector that stores the episode winnings after each spin
    track_winnings = [episode_winnings]
    for j in range(0, 1000):
        while episode_winnings < 80:
            won = False
            bet_amount = 1
            while not won:
                won = get_spin_result(float(18/39))
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                track_winnings.append(episode_winnings)
    #If we get to 80 before 1000 spins, fill with 80 as directed
    if len(track_winnings) < 1000:
        for k in range(len(track_winnings),1000):
            track_winnings.append(80)
    is_eighty = False
    if episode_winnings >= 80:
        is_eighty = True
    return (track_winnings,list(range(0,1000)), is_eighty)

#bankroll limits version
def run_one_episode_v2():
    episode_winnings = 0
    #vector that stores the episode winnings after each spin
    track_winnings = [episode_winnings]
    for j in range(0, 1000):
        while episode_winnings < 80:
            # Stop here if we have gone below our bankroll
            if episode_winnings < -256:
                break
            if len(track_winnings) >= 1000:
                break
            won = False
            bet_amount = 1
            while not won:
                won = get_spin_result(float(18/39))
                if won == True:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                    if (256 + episode_winnings) < bet_amount:
                        bet_amount = 256 + episode_winnings
                track_winnings.append(episode_winnings)
                if(len(track_winnings)) >= 1000:
                    break
    #If we get to 80/-256 before 1000 spins, fill  as directed
    if len(track_winnings) < 1000:
        for k in range(len(track_winnings),1000):
            if episode_winnings >=0:
                track_winnings.append(80)
            else:
                track_winnings.append(-256)
    is_eighty = False
    if episode_winnings >= 80:
        is_eighty = True
    return (track_winnings,list(range(0,1000)), is_eighty)

def test_code():
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = float(18/37) # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once  		  	   		  		 		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))
    # test the roulette spin
    # add your code here to implement the experiments
    #Experiment 1 - Figure 1 - 10 episode runs w/chart
    for i in range(0,10):
        a = run_one_episode()
        the_text = 'Episode ' + str(i)
        plt.plot(a[1], a[0], label=the_text)
    plt.xlim(0,300)
    plt.ylim(-100,256)
    plt.title('10 Episodes')
    plt.xlabel('Spin Number')
    plt.ylabel('Episode Winnings')
    figure_1 = plt.gcf()
    figure_1.savefig('images/ten_episodes.png')
    #plt.show()
    plt.clf()
    #Figure 2 - mean and sd of winnings at each spin (1000 reps)
    #initilaize dataframe
    df_orig = pd.DataFrame({'spin_num': [], 'winnings': []})
    track_eighties = 0
    for j in range(0,1000):
        a = run_one_episode()
        if a[2] == True:
            track_eighties+=1
        df = pd.DataFrame({'spin_num': a[1], 'winnings': a[0]})
        df_orig = pd.concat([df_orig, df])
    # Question 1 - proportion of $80 winners
    print('Proportion of 80 with v1:')
    print(float(track_eighties/1000))

    #Get mean and sd of each point, then add upper/lower boundaries
    summary_vals_df = df_orig.groupby(['spin_num'], as_index=False).agg({'winnings':['mean','std']})
    summary_vals_df.columns = ['spin_num', 'mean', 'sd']
    summary_vals_df['lower_bound'] = summary_vals_df['mean'] - summary_vals_df['sd']
    summary_vals_df['upper_bound'] = summary_vals_df['mean'] + summary_vals_df['sd']
    plt.plot(summary_vals_df['spin_num'] , summary_vals_df['lower_bound'] , label=the_text)
    plt.plot(summary_vals_df['spin_num'], summary_vals_df['upper_bound'], label=the_text)
    plt.plot(summary_vals_df['spin_num'], summary_vals_df['mean'], label=the_text)
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('1000 Episodes - Strategy 1')
    plt.xlabel('Spin Number')
    plt.ylabel('Episode Winnings (Avg and SD)')
    figure_2 = plt.gcf()
    figure_2.savefig('images/summary_episodes.png')
    #plt.show()
    plt.clf()

    # Question 2 - expected value
    print('expected value v1')
    print(summary_vals_df['mean'][999])
    #Figure 3, median
    median_vals_df = df_orig.groupby('spin_num').agg({'winnings':np.median}).reset_index()
    median_vals_df.columns = ['spin_num', 'median']
    median_vals_df = median_vals_df.merge(summary_vals_df, on='spin_num', how='left')
    plt.plot(median_vals_df['spin_num'] , median_vals_df['lower_bound'], label=the_text)
    plt.plot(median_vals_df['spin_num'], median_vals_df['upper_bound'], label=the_text)
    plt.plot(median_vals_df['spin_num'], median_vals_df['median'], label=the_text)
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('1000 Episodes - Strategy 1')
    plt.xlabel('Spin Number')
    plt.ylabel('Episode Winnings (Median and SD)')
    figure_3 = plt.gcf()
    figure_3.savefig('images/summary_episodes_median.png')
    #plt.show()
    plt.clf()

    #figure 4 - change strategy, plot mean, sd +/-
    df_orig_v2 = pd.DataFrame({'spin_num': [], 'winnings': []})
    track_eighties = 0
    for j in range(0, 1000):
        a = run_one_episode_v2()
        if a[2] == True:
            track_eighties +=1
        df = pd.DataFrame({'spin_num': a[1], 'winnings': a[0]})
        df_orig_v2 = pd.concat([df_orig_v2, df])
    # Question 4 - proportion of $80 winners
    print('Proportion of 80 with v2:')
    print(float(track_eighties / 1000))
    #Get mean and sd of each point, then add upper/lower boundaries
    summary_vals_df = df_orig_v2.groupby(['spin_num'], as_index=False).agg({'winnings':['mean','std']})
    summary_vals_df.columns = ['spin_num', 'mean', 'sd']
    summary_vals_df['lower_bound'] = summary_vals_df['mean'] - summary_vals_df['sd']
    summary_vals_df['upper_bound'] = summary_vals_df['mean'] + summary_vals_df['sd']
    plt.plot(summary_vals_df['spin_num'] , summary_vals_df['lower_bound'] , label=the_text)
    plt.plot(summary_vals_df['spin_num'], summary_vals_df['upper_bound'], label=the_text)
    plt.plot(summary_vals_df['spin_num'], summary_vals_df['mean'], label=the_text)
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('1000 Episodes - Strategy 2')
    plt.xlabel('Spin Number')
    plt.ylabel('Episode Winnings (Avg and SD)')
    figure_2 = plt.gcf()
    figure_2.savefig('images/summary_episodes_v2.png')
   # plt.show()
    plt.clf()

    #Question 5 - expected value
    print('expected value v2')
    print(summary_vals_df['mean'][999])
    #Figure 5, median
    median_vals_df = df_orig_v2.groupby('spin_num').agg({'winnings':np.median}).reset_index()
    median_vals_df.columns = ['spin_num', 'median']
    median_vals_df = median_vals_df.merge(summary_vals_df, on='spin_num', how='left')
    plt.plot(median_vals_df['spin_num'] , median_vals_df['lower_bound'], label=the_text)
    plt.plot(median_vals_df['spin_num'], median_vals_df['upper_bound'], label=the_text)
    plt.plot(median_vals_df['spin_num'], median_vals_df['median'], label=the_text)
    plt.xlim(0,300)
    plt.ylim(-256,100)
    plt.title('1000 Episodes - Strategy 2')
    plt.xlabel('Spin Number')
    plt.ylabel('Episode Winnings (Median and SD)')
    figure_3 = plt.gcf()
    figure_3.savefig('images/summary_episodes_median_v2.png')
   # plt.show()
    plt.clf()
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  

