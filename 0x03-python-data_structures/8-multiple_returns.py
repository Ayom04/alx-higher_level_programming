#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ''):
        tuple_res = (len(sentence), None)
    else:
        tuple_res = (len(sentence), sentence[0])
    return (tuple_res)


multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))