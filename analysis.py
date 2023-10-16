import numpy as np

import sklearn.linear_model as sklm
import sklearn.pipeline
import sklearn.model_selection as skms
import sklearn.feature_selection 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import RandomizedSearchCV

# from sklearn.linear_model import LogisticRegression
# from skms import RandomizedSearchCV
from scipy.stats import uniform

def binary_class():
    classifier = sklm.


#Use at least 3 folds, searching over at least 5 possible hyperparameter configurations to avoid overfitting.
def cross_validation(x_NF, y_N, n_folds):

    folds = skms.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1)
    folds.get_n_splits(x_NF, y_N)
    
    test_ids_fold = []
    train_ids_fold = []

    for i, (train_ids, test_ids) in enumerate(folds.split(x_NF)):
        test_ids_fold.insert(i, test_ids)
        train_ids_fold.insert(i, train_ids)






############### Cleaning USING SKLEAN FUNCTIONS #####################
#def clean_words(web_list, reviews_list, stars_list, n_folds):
    #bow_classifier = sklearn.pipeline.Pipeline([
    #    ('bow feature extractor', CountVectorizer(ngram_range=(1,1), min_df=1, max_df=1.0, binary=False)),
    #    ('classifying', sklm.LogisticRegression(C = 1.0, max_iter=20, random_state=101)),
        #('Random C search', )
        #('cross validating', skms.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1))
        
        #])
    
    
    #bow_classifier.fit(reviews_list, stars_list)
    #bow_classifier.predict()
#
    #bow_feature_extractor_bow_classifier = dict()
    #bow_feature_extractor_bow_classifier['bow_feature_extractor__min_df'] = [1, 2, 4]
    #bow_feature_extractor_bow_classifier['classifying__C'] = np.logspace(-4, 4, 9)
    #scoring_metric_name = 'ROC Area'
    #
    
    
    # Is the fit_transform doing the bow_classifier.fit() and bow_classifier.transform()?
    # bow_classifier.transform()
    # bow_classifier.transform(reviews_list)
    
    #return 

# Did some tests over in tests.ipynb
# iris = load_iris()
# logistic = sklm.LogisticRegression(solver='saga', tol=1e-2, max_iter=200,random_state=0)
# distributions = dict(C=uniform(loc=0, scale=4), penalty=['l2', 'l1'])
# clf = skms.RandomizedSearchCV(logistic, distributions, random_state=0)
# search = clf.fit(iris.data, iris.target)
# search.best_params_

