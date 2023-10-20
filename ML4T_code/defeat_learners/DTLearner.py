import numpy as np


def get_split_col(data):
    dx = data[:, :-1]
    dy = data[:, -1]
    max_correlation = 0
    col = 0
    for c in range(dx.shape[1]):
        data_col = dx[:, c]
        correlation = np.corrcoef(data_col, dy)[0, 1]

        if float(abs(correlation)) > max_correlation:
            col = c
            max_correlation = float(abs(correlation))
    return col


def get_median(data, col):
    dx = data[:, :-1]
    data_col = dx[:, col]
    med = np.median(data_col)
    return med


def build_tree(data_x, data_y, leaf_size=10):
    data_all = np.column_stack((data_x, data_y))

    if data_all.shape[0] <= leaf_size:
        return np.asarray([["leaf", np.mean(data_y), "NA", "NA"]])

    if len(np.unique(data_all[:, -1])) == 1:
        return np.asarray([["leaf", np.unique(data_all[:, -1])[0], "NA", "NA"]])

    col = get_split_col(data_all)
    med = get_median(data_all, col)

    ldx = data_all[data_all[:, col] <= med, :-1]
    ldy = data_all[data_all[:, col] <= med, -1]
    rdx = data_all[data_all[:, col] > med, :-1]
    rdy = data_all[data_all[:, col] > med, -1]

    if ldy.shape[0] == 0 or rdy.shape[0] == 0:
        return np.asarray([["leaf", np.mean(data_y), "NA", "NA"]])


    left_tree = build_tree(ldx, ldy, leaf_size)
    right_tree = build_tree(rdx, rdy, leaf_size)

    new_entry = np.append(np.array([[str(col), med, 1, left_tree.shape[0] + 1]]), left_tree, axis=0)
    return np.append(new_entry, right_tree, axis=0)


class DTLearner(object):
    """
    This is a Decision Tree Learner

    :param verbose: If “verbose” is True, your code can print out information for debugging.
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.
    :type verbose: bool
    """
    def __init__(self, leaf_size = 10, verbose=False):
        """
        Constructor method
        """
        self.verbose = verbose
        self.leaf_size = leaf_size
        self.tree = None
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
        :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
        """
        return "jgoldsher3"  # replace tb34 with your Georgia Tech username



    def add_evidence(self, data_x, data_y):
        self.tree = build_tree(data_x, data_y, self.leaf_size)


    def query(self, points):
        #create array for predictions
        assignments = np.array([])
        #loop thru all the data anad traverse the tree
        for p in range(0, points.shape[0]):
            #get the data
            this_value = points[p, :]

            #start at root node (0), stop when we get to a leaf row
            current_row = 0
            while (self.tree[current_row, 0] != 'leaf'):
                #split value at index 1
                split_value = float(self.tree[current_row, 1])
                #node name at index 0
                column_name = self.tree[current_row, 0]

                #if the value in our data at the given index is less than the
                #split value, get the value for the left row, otherwise get right value row
                compare_value = this_value[int(float(column_name))]

                if compare_value <= split_value:
                    increment = int(self.tree[current_row, 2])
                else:
                    increment = int(self.tree[current_row, 3])
                current_row = current_row + increment
            #If we are at end, get value and add that to the list
            new_pred = float(self.tree[current_row, 1])
            assignments = np.append(assignments, new_pred)

        return assignments




