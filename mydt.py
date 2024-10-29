# CART on the Bank Note dataset
from random import seed
from random import randrange
import pandas as pd


class mydt:
    def __init__(self, dataset, n_folds, max_depth, min_size):
        self.dataset = dataset
        self.n_folds = n_folds
        self.max_depth = max_depth
        self.min_size = min_size


    # Split a dataset into k folds
    def cross_validation_split(self, dataset, n_folds):
        dataset_split = list() 
        dataset_copy = list(dataset)
        fold_size = int(len(dataset) / n_folds) # the row size of each of the splits
        for i in range(n_folds): # numbers 0 to nfolds -1
            fold = list() # this will store the new rearranged data
            while len(fold) < fold_size: 
                index = randrange(len(dataset_copy)) # gives a random number inside the dataset
                fold.append(dataset_copy.pop(index)) # appends a row using the  random number above 
            dataset_split.append(fold) # adds the fold to the dataset split list and repeats for another fold
        return dataset_split # produces the new split data set inside one list
     
    # Calculate accuracy percentage
    def accuracy_metric(self, actual, predicted):
        correct = 0
        for i in range(len(actual)):
            if actual[i] == predicted[i]:
                correct += 1
        return correct / float(len(actual)) * 100.0
     
    # Evaluate an algorithm using a cross validation split
    def evaluate_algorithm(self):
        folds = self.cross_validation_split(self.dataset, self.n_folds)
        scores = list()
        for fold in folds:
            train_set = list(folds)
            train_set.remove(fold)
            train_set = sum(train_set, [])
            test_set = list()
            for row in fold:
                row_copy = list(row)
                test_set.append(row_copy)
                row_copy[-1] = None
            predicted = self.decision_tree(train_set, test_set, self.max_depth, self.min_size)
            actual = [row[-1] for row in fold]
            accuracy = self.accuracy_metric(actual, predicted)
            scores.append(accuracy)
        print('Scores: %s' % scores)
        print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
        return scores
     
    # Split a dataset based on an attribute and an attribute value
    def test_split(self, index, value, dataset):
        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right
     
    # Calculate the Gini index for a split dataset
    def gini_index(self, groups, classes):
        # count all samples at split point
        n_instances = float(sum([len(group) for group in groups]))
        # sum weighted Gini index for each group
        gini = 0.0
        for group in groups:
            size = float(len(group))
            # avoid divide by zero
            if size == 0:
                continue
            score = 0.0
            # score the group based on the score for each class
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            # weight the group score by its relative size
            gini += (1.0 - score) * (size / n_instances)
        return gini
     
    # Select the best split point for a dataset
    def get_split(self, dataset):
        class_values = list(set(row[-1] for row in dataset)) # returns list of class values ['Lemon', 'Apple', 'Grape']
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for index in range(len(dataset[0])-1): # column loop
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups, class_values)
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index':b_index, 'value':b_value, 'groups':b_groups}
     
    # Create a terminal node value
    def to_terminal(self, group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)
     
    # Create child splits for a node or make terminal
    #recursive algorithm
    def split(self, node, max_depth, min_size, depth):
        left, right = node['groups']
        del(node['groups'])
        # check for a no split
        if not left or not right:
            node['left'] = node['right'] = self.to_terminal(left + right)
            return
        # check for max depth
        if depth >= max_depth:
            node['left'], node['right'] = self.to_terminal(left), self.to_terminal(right)
            return
        # process left child
        if len(left) <= min_size:
            node['left'] = self.to_terminal(left)
        else:
            node['left'] = self.get_split(left)
            self.split(node['left'], max_depth, min_size, depth+1)
        # process right child
        if len(right) <= min_size:
            node['right'] = self.to_terminal(right)
        else:
            node['right'] = self.get_split(right)
            self.split(node['right'], max_depth, min_size, depth+1)

     
    # Build a decision tree
    def build_tree(self, train, max_depth, min_size):
        root = self.get_split(train)
        self.split(root, max_depth, min_size, 1)
        return root

     
    # Make a prediction with a decision tree
    # recursive algorithm
    def predict(self, node, row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predict(node['right'], row)
            else:
                return node['right']

     
    # Classification and Regression Tree Algorithm
    def decision_tree(self, train, test, max_depth, min_size):
        tree = self.build_tree(train, max_depth, min_size)
        predictions = list()
        for row in test:
            prediction = self.predict(tree, row)
            predictions.append(prediction)
        return(predictions)
        


# Test CART on Bank Note dataset
seed(1)

# load and prepare data
filename = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
df = pd.read_csv(filename, sep=',')
dataset = df.values.tolist()

# evaluate algorithm
n_folds = 5
max_depth = 10
min_size = 10

scores = mydt(dataset, n_folds, max_depth, min_size).evaluate_algorithm()





