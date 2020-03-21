#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 06:28:59 2020

@author: maihai
"""


#0 Importing libs
import random


#1 Importing datasets

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?",
}

ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


#2 Defining functions

# 2.1 Encoder: 0, 1, 2.. -> questions.keys
def int_to_key(number, data=ingredients):
    keys = list(data.keys())
    return keys[number]

#2.2 Answers must be 0|1 && not charaters.
def verify_answer():
    while True:
        try:
            answer = int(input('0 or 1 \n'))
            
        except ValueError:
            print('Not a integer. Try again.')
            continue
        else:
            break
    while answer not in [0, 1]:
        print('Nor 0 or 1! Try again.')
        answer = int(input('0 or 1 \n'))
    return answer

#2.3 Questioning customer of his tastes
def required_tastes(data=questions):
    '''
    This func receives customer requirements.
    
    Parameters
    ----------
    data : a dict. 
        DESCRIPTION. The default is the given questions at #1.

    Returns
    -------
    requirements : list of integer.
        DESCRIPTION. Ex: [1, 0, 1, 1, 0] corresonding to questions.keys()

    '''
    
    # instructions: yes or no
    print('Please answer questions with ONLY: 1 for Yes or 0 for No \n')
    requirements = []
    
    # Questions and Answers
    for value in questions.values():
        print(value)
        choosen_taste = verify_answer()
        requirements.append(choosen_taste)
    return requirements

#2.4
def randomly_match_ingredients(requirements=required_tastes(), data=ingredients):
    '''
    Randomly match customer's requirements to ingredients.
    
    Parameters
    ----------
    requirements : a list of int.
        SUCH AS. [1, 0, 1, 0, 1]
    data : a dict.
        DESCRIPTION. The default is the given ingredients at #1.

    Returns
    -------
    selected_ingredients : a list of str.
        SUCH AS: ['splash of gin', 'rasher of bacon', 'shake of bitters']

    '''
    selected_ingredients = []
    
    # giving offer
    ## in case: he requires NOTHING
    is_nothing = sum(requirements[i] for i in range(len(requirements)))
    if is_nothing == 0:
        print('\n Our pub offer you a cup of PURE water.')
        return
    
    ## in case: he require SOMETHING    
    for i, choice in enumerate(requirements):
        if choice == 1:
            key_of_choice = int_to_key(i)
            randomly_match = random.choice(data[key_of_choice])
            selected_ingredients.append(randomly_match)
            
    print('\n Based on your choices, the pub offers a drink with:')
    print(selected_ingredients)
    
    return selected_ingredients
    


#3 Driving code
selected_ingredients = randomly_match_ingredients() 







