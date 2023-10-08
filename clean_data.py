import numpy as np
import pandas as pd
import os


def tokenize_text(text_list):
    # Separate text at each space.
    token_list = list() #List of 2400 elements, each element is 1 review
    for reviewIdx in range(len(text_list)): # 0 to 2399
        cur_token = text_list[reviewIdx].split() # cur_token should be 1 review, split by space???
        print('curr token size: ', np.shape(cur_token))
        print('curr token type: ', type(cur_token))
        print('curr token: ', cur_token)
        #print('curr token', cur_token[:])

        # Remove punction
        for word in cur_token:
            #print('word', word)
            
            print(token_list)
            for punc in ['...','?', '!', '_', '.', ',', '"', '/']:
                cleaned_word = word.replace(punc, '')
            clean_token = cleaned_word.lower()
            token_list.append(clean_token)         
        # Turn to lower coase
        
        # Replace the cleaned token in the original list
        

        # token_list[pp] = clean_token
        
    #merged_tokens = []
    #for line in tokens:
    #    for word in line:
    #        merged_tokens.append(word)
    print('in clean data', token_list)
    return token_list


# building a fixed-size vocabulary:
def create_dictionary(tokens):
    tok_count_dict = dict()

    for line in tokens:
        #for tok in tok_list:
            if tok in tok_count_dict:
                tok_count_dict[tok] += 1
            else:
                tok_count_dict[tok] = 1
                
    sorted_tokens = list(sorted(tok_count_dict, key=tok_count_dict.get, reverse=True))

    #threshold of words that are infrequent is 3 right now. Change later(?)
    vocab_list = [w for w in sorted_tokens if tok_count_dict[w] >= 3]
    return vocab_list

