import numpy as np
import pandas as pd
import os
# import nltk

# from nltk import word_tokenize
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

def tokenize_text(text_list):
    # Separate text at each space
    token_list = list() 
    for reviewIdx in range(len(text_list)): # 0 to 2399
        cur_token = text_list[reviewIdx].split() # cur_token is 1 review
        # Remove punction
        for word in cur_token: # word contains 1 word of current review at a time
            for punc in ['...','?', '!', '_', '.', ',', '"', '/']:
                word = word.replace(punc, '')
            clean_token = word.lower() #Turn to lower case
                # Replace the cleaned token in the original list
            token_list.append(clean_token)  # Append cleaned words to one master list
    #print('in clean data', token_list)
    return token_list #List of 2400 elements, each element is 1 review


def tokenize(text_list):
    # Separate text at each space
    token_list = list() 
    
    cur_token = text_list.split() # cur_token is 1 review
    # Remove punction
    for word in cur_token: # word contains 1 word of current review at a time
        for punc in ['...','?', '!', '_', '.', ',', '"', '/']:
            word = word.replace(punc, '')
        clean_token = word.lower() #Turn to lower case
            # Replace the cleaned token in the original list
        token_list.append(clean_token)  # Append cleaned words to one master list
    #print('in clean data', token_list)
    return token_list #List of 2400 elements, each element is 1 review


# building a fixed-size dictionary with words and count:
def create_word_list(tokens):
    word_count_dict = dict()

    for word in tokens:
        #for tok in tok_list:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
    
    return word_count_dict

#Finally makes dictionary for modeling.
def create_dict(token_list):
    #Creates vocab term to integer defining its order in vocab.
    vocab_dict = dict()
    for vocab_id, tok in enumerate(token_list):
        vocab_dict[tok] = vocab_id
    return vocab_dict


#Creates vectorized version of review. 
def make_feature_vector(review, vocab_dict):
    #Produce feature vector from review and dictionary
    V = len(vocab_dict.keys())  
    count_V = np.zeros(V)
    print(review)
    for word in tokenize(review):
        #print(word)
        if word in vocab_dict:
            vv = vocab_dict[word]
            count_V[vv] += 1
    return count_V
