import numpy as np
import sklearn.linear_model
import sklearn.pipeline
import sklearn.model_selection
import sklearn.feature_selection
from sklearn.feature_extraction.text import CountVectorizer

#Create a pipeline:
def make_pipeline():
    bow_pipeline = sklearn.pipeline.Pipeline([
        ("step1", sklearn.feature_extraction.text())
    ])


#Use at least 3 folds, searching over at least 5 possible hyperparameter configurations to avoid overfitting.
def cross_validation(x_NF, y_N, n_folds):

    folds = sklearn.model_selection.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1)
    folds.get_n_splits(x_NF, y_N)
    
    for i in range(0, n_folds):
        test_ids_fold.insert(i, )
        train_id_fold

#get folds
#get probabilities associated with each fold


############### Cleaning USING SKLEAN FUNCTIONS #####################
def clean_words(web_list, reviews_list, stars_list, n_folds):
    #change min_df and max_df later.
    bow_classifier = sklearn.pipeline.Pipeline([
        ('bow feature extractor', CountVectorizer(ngram_range=(1,1), min_df=1, max_df=1.0, binary=False)),
        ('classifying', sklearn.linear_model.LogisticRegression())
        ('cross validating', sklearn.model_selection.RepeatedKFold(n_splits = n_folds, n_repeats = 1, random_state = 1))
        ])
    
    
    x_N = vectorizer.fit_transform(reviews_list)
    vectorizer.transform()

