# **Coding a K-Nearest Algorithm From Scratch**

#### **Peter McClintock**

#### **24/10/2021**

# **Overview**

* The goal of this tutorial is to introduce the main features of coding the k-nearest neighbours algorithm  
* The language used in this project is Python  
* Other key skills are working with python in the command line  
* The code will be introduced in order of run time with the full code file included at the end of the page.

# **Setup**

## **Python Instalation**

To check if you have Python already installed open command prompt and type python or py and hit enter. The build version of python should return if installed. The version of python that this tutorial is built on is python 3.9.7 and hopefully future updates will not wreck any of the tutorial. If you do not have python installed a quick google search should direct you to the main website to download it. For the tutorial we are using the Windows Installer (64-bit) version.

## Virtual Environment with uv
A virtual environment provides an isolated space for your Python project, keeping its libraries and scripts separate from your system's main Python installation. This is a crucial best practice for managing project dependencies.

We'll use uv, a fast and modern Python package installer, to handle both the virtual environment and package installation. If you don't have uv installed, you can find the installation instructions on its official website.

First, navigate to where you want the project to live (the folder it should live in):


<pre><code class="language-Bash">
cd path/to/Desktop
</code></pre>

Now, create the project folder using uv. This command will create a folder in your directory.

<pre><code class="language-Bash">
uv init project-name
</code></pre>

Now all we need is to add some packages which is super fast using uv. <code>cd project-name</code> to get into your folder then run the command below.

<pre><code class="language-Bash">
uv add pandas
</code></pre>

uv has also setup a main.py file which we can use to write our code in. Open this in your favourite IDE and to run it, you can type uv run main.py in the command line. Uv will ensure it uses the virtual environment in the same directory. 

Lets write some code!

# **K-Nearest Neighbours**

## **Background**

The k-nearest-neighbours algorithm despite its simplicity can be quite succesful in classification problems. The algorithm essentially groups together data points based on a criteria. This criteria is usually the Eucludean distance from other points. When predicting the k-most similar data points are used to make the prediction. As data is taken from other points, the k-nearest-neighbour method can be used for classification and regression.

## **The Algorithm**

Below is the overall process of the algorithm.

* Perform K-Fold Cross Validation  
* For each fold run the decision tree algorithm  
* Build the the tree using tree depth and size parameters  
* Data is split using the Gini Index  
* Calculate the accuracy score for each fold and print that to the terminal

As such the sections from now will roughly follow the flow of the tree. Each section will break down the methods within the overall class

## **Evaluate Algorithm**

The only command needed to run everything is evaluate\_algorithm() which runs the subsequent methods in the class. It starts by implementing cross validation on the dataset taking the n\_folds parameter to determine how many folds are created. We then intialise a list to store the accuracy scores and begin a for loop for each fold created. The for loop creates the standard cross validation procedure of testing a different individual subset of the data on each iteration.


# Evaluate an algorithm using a cross validation split  
<pre><code class="language-python">
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
        predicted = self.k_nearest_neighbours(train_set, test_set, self.num_neighbours)  
        actual = [row[-1] for row in fold]  
        accuracy = self.accuracy_metric(actual, predicted)  
        scores.append(accuracy)  
    print('Scores: %s' % scores)  
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))  
    return scores
</code></pre>

After the training and test sets are split the algorithm runs <code>k_nearest_neighbours()</code> using the split data which returns an array of predicted values from the algorithm. Finally, the accuracy value is calculated for each fold and returned in the scores list that we initialised. Accuracy = (Number of Correct Predictions)/Total Number of Predictions

The algorithm is designed in this initial stage that cross validation can be implemented regardless of what algorithm is used. One would simply need to add different methods to apply a separate machine learning model and call it at the <code>k_nearest_neighbours()</code> stage.

## **K Fold Cross Validation**

Attempting to reduce bias in the testing I have used K fold cross validation. This involves splitting the training data into multiple different sets in order to train the model using different variations of the data. The general procedure is as follows:

* Shuffle the dataset randomly.  
* Split the dataset into k groups  
* For each unique group:  
* Take the group as a hold out or test data set  
* Take the remaining groups as a training data set  
* Fit a model on the training set and evaluate it on the test set  
* Retain the evaluation score and discard the model  
* Summarize the skill of the model using the sample of model evaluation scores

<pre><code class="language-python">
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
</code></pre>

The code takes the full dataset, randomly rearranges it, and splits it into folds based on the user input. It then stores the folds in a list named dataset\_split. As explained in the evaluate\_algorithm() method, the fitting the model on each fold occurs there.

## **K-Nearest-Neighbours**
<pre><code class="language-python">
def k_nearest_neighbours(self, train, test, num_neighbours):
  predictions = list()
  for row in test:
      output = self.predict_classification(train, row, num_neighbours)
      predictions.append(output)
  return(predictions)
</code></pre>

We initialise a list to store the predictions then loop through each row in the test set and create a prediction using the predict\_classification() method. This is then added to the predictions list and we return our list at the end of the method.

## **Predict Classification**
<pre><code class="language-python">
def predict_classification(self, train, test_row, num_neighbours):
  neighbours = self.get_neighbours(train, test_row, num_neighbours)
  output_values = [row[-1] for row in neighbours]
  prediction = max(set(output_values), key=output_values.count)
  return prediction
</code></pre>

<code>predict_classification()</code> takes in the training data, the data used for prediction and the number of neighbours that it should search for. The `get_neighbours()` method returns the nearest data points to the row of data currenlty being assessed. It then stores this data in the neigbors variable. A list of the class values of these points is stored and we return the most common class value in the neighbours data. The method ends by returning the most common class value.

## Get Neighbours  
The next two methods provide the main math behind the algorithm  
<pre><code class="language-python">
def get_neighbours(self, train, test_row, num_neighbours):
  distances = list()
  for train_row in train:
      dist = self.euclidean_distance(test_row, train_row)
      distances.append((train_row, dist))
  distances.sort(key=lambda tup: tup[1])
  neighbours = list()
  for i in range(num_neighbours):
      neighbours.append(distances[i][0])
  return neighbours

def euclidean_distance(self, row1, row2):
  distance = 0.0
  for i in range(len(row1)-1):
      distance += (row1[i] - row2[i])**2
  return sqrt(distance)
</code></pre>

Firstly we initialise a list to store distances. Then for every row in the training data set the Eucludean distance to the data you are testing is calculated. The Euclidean distance can be calculated by passing in each row to the formula meaning it scales with feature size. Finally, the nearest neighbours are selected based on the user input value and returned in a list.

# **The End**

Congratulations if you made it to the end of the tutorial and have managed to run the model on some of your own data\! If you haven't managed to run the code or are encountering errors a full page of my code is included below with an example that should work. Good luck in your future projects.

<pre><code class="language-python">
from random import seed
from random import randrange
import pandas as pd
from math import sqrt

class mykn:
    def __init__(self, dataset, n_folds, num_neighbours):
        self.dataset = dataset
        self.n_folds = n_folds
        self.num_neighbours = num_neighbours

    # Split a dataset into k folds
    def cross_validation_split(self, dataset, n_folds):
        dataset_split = list()
        dataset_copy = list(dataset)
        fold_size = int(len(dataset) / n_folds) # the row size of each of the splits
        for i in range(n_folds): # numbers 0 to nfolds -1
            fold = list() # this will store the new rearranged data
            while len(fold) < fold_size:
                index = randrange(len(dataset_copy)) # gives a random number inside the dataset
                fold.append(dataset_copy.pop(index)) # appends a row using the random number above
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
            predicted = self.k_nearest_neighbours(train_set, test_set, self.num_neighbours)
            actual = [row[-1] for row in fold]
            accuracy = self.accuracy_metric(actual, predicted)
            scores.append(accuracy)
        return scores

    # Calculate the Euclidean distance between two vectors
    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1)-1):
            distance += (row1[i] - row2[i])**2
        return sqrt(distance)

    # Locate the most similar neighbours
    def get_neighbours(self, train, test_row, num_neighbours):
        distances = list()
        for train_row in train:
            dist = self.euclidean_distance(test_row, train_row)
            distances.append((train_row, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbours = list()
        for i in range(num_neighbours):
            neighbours.append(distances[i][0])
        return neighbours

    # Make a prediction with neighbours
    def predict_classification(self, train, test_row, num_neighbours):
        neighbours = self.get_neighbours(train, test_row, num_neighbours)
        output_values = [row[-1] for row in neighbours]
        prediction = max(set(output_values), key=output_values.count)
        return prediction

    # kNN Algorithm
    def k_nearest_neighbours(self, train, test, num_neighbours):
        predictions = list()
        for row in test:
            output = self.predict_classification(train, row, num_neighbours)
            predictions.append(output)
        return(predictions)

# Test CART on Bank Note dataset
from random import seed
import pandas as pd # Assuming pandas is imported for pd.read_csv

# load and prepare data
filename = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
df = pd.read_csv(filename, sep=',')
dataset = df.values.tolist()

# evaluate algorithm
n_folds = 5
num_neighbours = 5

# Assuming 'mykn' is a class or function defined elsewhere that needs to be imported or defined.
# For the purpose of just reformatting the provided code snippet,
# I'll keep 'mykn' as is, but it would raise a NameError if not defined.
# Example: from my_module import mykn 
scores = mykn(dataset, n_folds, num_neighbours).evaluate_algorithm()
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores)))) 
</code></pre>