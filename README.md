# Sentiment Classification using Bag-of-Words and Logistic Regression

This repository contains a sentiment classification project developed as part of Tufts University's *Comp 135: Introduction to Machine Learning* (Fall 2023). The goal was to classify user reviews as positive or negative using logistic regression with two different approaches to text representation.

## Overview

The project is split into two parts:

### 1. Bag-of-Words Baseline Model

- **Preprocessing**: Reviews were lowercased, punctuation was replaced with spaces, and tokenization was performed using `CountVectorizer`. Single-character tokens were removed, and a frequency filter (`min_df=2`) was applied to limit the vocabulary.
- **Feature Representation**: 1912 unique tokens were used to build feature vectors.
- **Classifier**: Logistic regression (Scikit-learn, `liblinear` solver) was used.
- **Hyperparameter Tuning**:
  - Initial sweep via `RandomizedSearchCV` across penalty type (L1, L2), regularization strength (`C`), and max iterations.
  - Further tuning via `GridSearchCV` around optimal values.
  - Final hyperparameters: L2 penalty, `C=1.703`, `max_iter=98`.
- **Cross Validation**: 5-fold CV was used to evaluate AUROC on held-out data.
- **Performance**:
  - AUROC on held-out set: **0.873**
  - AUROC on test set: **0.892**

### 2. Open-Ended Challenge (Improved Representation)

- **Preprocessing**:
  - Lowercasing and lemmatization using NLTK’s `WordNetLemmatizer`
  - Tokenization using whitespace delimiters to better handle contractions.
  - Inclusion of both unigrams and bigrams. Stop word removal and POS filtering were tested but not used due to reduced performance.
- **Feature Representation**: Final dictionary had 2565 features.
- **Classifier and Tuning**:
  - Logistic regression using same methodology as above.
  - Final hyperparameters: L2 penalty, `C=80`, `max_iter=200`.
- **Performance**:
  - AUROC on test set: **0.8466**
  - Training error: **0** (suggesting overfitting)

## Error Analysis

Errors across both models were categorized into types:
- Clear sentiment misclassification
- Negation and double negation confusion
- Ambiguous or witty phrasing
- Sarcastic statements

The second model, although more complex, showed signs of overfitting and failed to generalize as well as the first.

## Conclusion

This project demonstrates the effectiveness and limitations of bag-of-words models and logistic regression for sentiment classification. While basic token-level representations can yield strong results, they struggle with nuanced language patterns such as sarcasm, negation, and double negatives. Including bigrams can help address some of these issues but may introduce overfitting.
