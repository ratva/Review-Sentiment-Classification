import numpy as np
import pandas as pd
import os


def tokenize_text(text_list):
    # Separate text at each space
    token_list = list() #List of 2400 elements, each element is 1 review
    for reviewIdx in range(len(text_list)): # 0 to 2399
        cur_token = text_list[reviewIdx].split() # cur_token is 1 review
        
        # Remove punction
        for word in cur_token: # word contains 1 word of current review at a time
            
            for punc in ['...','?', '!', '_', '.', ',', '"', '/']:
                word = word.replace(punc, '')
                
            clean_token = word.lower() #Turn to lower case
                # Replace the cleaned token in the original list
            token_list.append(clean_token)  # Append cleaned words to one master list

    print('in clean data', token_list)
    return token_list


# building a fixed-size vocabulary:
def create_dictionary(tokens):
    word_count_dict = dict()

    for word in tokens:
        #for tok in tok_list:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1
                
    return word_count_dict

