import numpy as np
import sklearn.linear_model
import sklearn.pipeline
import sklearn.model_selection

#Use at least 3 folds, searching over at least 5 possible hyperparameter configurations to avoid overfitting.
def cross_validation(x_NF, y_N, n_folds):

    folds = sklearn.model_selection.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1)
    folds.get_n_splits(x_NF, y_N)
    
    for i in range(0, n_folds):
        test_ids_fold.insert(i, )
        train_id_fold

#get folds
#get probabilities associated with each fold


