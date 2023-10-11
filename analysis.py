import numpy as np
import sklearn.linear_model as sklm
import sklearn.pipeline as pipe
import sklearn.model_selection as skms
import sklearn.feature_selection 
from sklearn.feature_extraction.text import CountVectorizer

# from sklearn.linear_model import LogisticRegression
# from skms import RandomizedSearchCV
from scipy.stats import uniform

#Create a pipeline:
# def make_pipeline():
#     bow_pipeline = pipe.Pipeline([
#         ("step1", sklearn.feature_extraction.text())
#     ])


#Use at least 3 folds, searching over at least 5 possible hyperparameter configurations to avoid overfitting.
def cross_validation(x_NF, y_N, n_folds):

    folds = skms.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1)
    folds.get_n_splits(x_NF, y_N)
    
    test_ids_fold = []
    train_ids_fold = []

    for i, (train_ids, test_ids) in enumerate(folds.split(x_NF)):
        test_ids_fold.insert(i, test_ids)
        train_ids_fold.insert(i, train_ids)

#get folds
#get probabilities associated with each fold


############### Cleaning USING SKLEAN FUNCTIONS #####################
def clean_words(web_list, reviews_list, stars_list, n_folds):
    bow_classifier = pipe.Pipeline([
        ('bow feature extractor', CountVectorizer(ngram_range=(1,1), min_df=1, max_df=1.0, binary=False)),
        ('classifying', sklm.LogisticRegression()),
        ('cross validating', skms.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1))
        ])
    
    x_N = bow_classifier.fit_transform(reviews_list)
    
    # Is the fit_transform doing the bow_classifier.fit() and bow_classifier.transform()?
    # bow_classifier.transform()
    # bow_classifier.transform(reviews_list)
    
    return x_N

# Did some tests over in tests.ipynb
# iris = load_iris()
# logistic = sklm.LogisticRegression(solver='saga', tol=1e-2, max_iter=200,random_state=0)
# distributions = dict(C=uniform(loc=0, scale=4), penalty=['l2', 'l1'])
# clf = skms.RandomizedSearchCV(logistic, distributions, random_state=0)
# search = clf.fit(iris.data, iris.target)
# search.best_params_
