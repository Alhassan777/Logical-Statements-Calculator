#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#define a function for each of the logical connectors.
def conditional(a,b):
    return not a or b
def conjunction(a,b):
    return a and b
def inclusive_or(a,b):
    return a or b
def exclusive_or(a,b):
    return (a and not b) or (not a and b)
def biconditional(a,b):
    return (not a or b) and (not b or a)
def conjunction_negation (a,b):
    return not a or not b
def disjunction_negation (a,b):
    return not a and not b
def negation(a):
    return not a
first_atomic_sentence= input("what is your atomic sentence number 1 Truth value?")# Truth value variable for 1st atomic sentence(True/False)
second_atomic_sentence= input("what is your atomic sentence number 2 Truth value?")# Truth value variable for 2nd atomic sentence
# input variable for 1st connective, showing the proper input of each connective
First_connective=input("what is you connective[if, if and only if, inclusive or, exclusive or, and, not (a or b), not (a and b)]?")
# define a list whose elements are the value of 1st and 2nd atomic sentences.
# List will be used for determining the validity of a set
validity=[first_atomic_sentence,second_atomic_sentence]
#define a function with 3 variables(2 atomic sentences, 1 connector)
#function will respond to the input connector by doing the proper operation on atomic sentences
def Truth_value_of_statment(a, b,c):
    if c== "if and only if":
         Truth_value_1=biconditional(a,b)
    if c== "inclusive or":
         Truth_value_1=inclusive_or(a,b)
    if c== "exclusive or":
         Truth_value_1=exclusive_or(a,b)
    if c== "and":
         Truth_value_1=conjunction(a,b)
    if c== "if":
         Truth_value_1=conditional(a,b)
    if c == "not a and b":
         Truth_value_1 = conjunction_negation(a, b)
    if c == "not a or b":
         Truth_value_1 = disjunction_negation(a, b)
    if c == "not a":
         Truth_value_1=negation(a)
    return Truth_value_1 #return the output truth value of logical opertaion in the function
# variable that will determine if you wish to add more statements to the set or end the set with the first statement only
decision_1=input(print("do you wish to continue? yes/no"))
#determine the Truth value of the first statement
Truth_value_of_first_statment=Truth_value_of_statment(first_atomic_sentence, second_atomic_sentence, First_connective)
#in case your answer was no on decision_1, deteremine the validity of the set based on first statment
if decision_1=="no":
# determine if the number of apperance of True in the list validity is equal to the total number of its elements.
    if validity.count(True) == int(len(validity)): # if True, then all elements of the validity list has True value, that means the set is valid
        print("This set is Valid")
    else:# if false, some elements of the validity list don't have True value, that means the set is invalid
        print("this set is invalid")
# if your answer to the first question on your decision was yes --> which to continue adding statements to set
if decision_1=="yes":
 while True:# make infinite while loop which will do the next process until you order it to stop
     # asks you if you are inputing a single atomic sentence or a compound sentence(connective and 2 atomic sentences)
    decision_2=input(print("are you comparing to a atomic sentence or compound sentence"))
    if decision_2== str("atomic"): #you choose to add atomic sentence
        n_atomic_sentence=input(print("what is your atomic sentence ?"))#truth value of the new sentence
        # connective between atomic sentence and the first sentence(compound setnece established between 1st and 2nd atomic sentences)
        n_connective=input(print("what is your connective ?"))
        # determine the truth value of the whole new statement by putting the Truth value of first sentence and new atomic sentence and apply the chosen connective
        Truth_value_of_new_statment= Truth_value_of_statment(Truth_value_of_first_statment,n_atomic_sentence,n_connective)
        Truth_value_of_first_statment=Truth_value_of_new_statment
        validity.append(Truth_value_of_new_statment)#add this new truth value to the validity list
    elif decision_2== str("compound"):#you choose to add compound sentence
        n_atomic_sentence_1 = input(print("what is your first atomic sentence ?"))#truth value of the 1st new sentence
        n_atomic_sentence_2 = input(print("what is your second atomic sentence ?"))#truth value of the 2nd new sentence
        n_connective = input(print("what is your connective ?")) # connective of the new statement (between new 1st and 2nd sentence)
        # determine the truth value of compound just like in line 48
        Truth_value_of_new_compound=Truth_value_of_statment(n_atomic_sentence_1,n_atomic_sentence_2,n_connective) 
        # determine the truth value of the whole new statement by putting the Truth value of first sentence and new compound sentence and apply the chosen connective
        Truth_value_of_new_statment= Truth_value_of_statment(Truth_value_of_first_statment,Truth_value_of_new_compound, n_connective)
        Truth_value_of_first_statment=Truth_value_of_new_statment
        validity.append(Truth_value_of_new_statment)#add this new truth value to the validity list
     # loop termination option if you wish to end adding anoter sentences to the set
    break_button = int(input("if you wish to stop, press 0")) 
    if break_button==0:# if x=0, end the loop while printing if the set is valid or invalid, otherwise continue the loop
        if validity.count(True)==int(len(validity)):
            print("This set is valid")
        else:
            print("this set is invalid")
    break #end the loop and the whole program

