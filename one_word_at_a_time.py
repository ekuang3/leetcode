def one_word_at_a_time(sentence):
    """ 
    Time: O(n^2), join() has complexity O(n) and one iteration

    Space: O(n^2), a new list of substrings is created with each 
    substring having a length that is at most equal to the length 
    of the original sentence
    """
    lst = sentence.split(' ')

    res = []
    for i in range(len(lst)):
        tmp = lst[:i+1]
        tmp = ' '.join(tmp)
        res.append(tmp)

    return res 

if __name__=='__main__':
    
    sentence = 'I am so tired'
    res = one_word_at_a_time(sentence)
    print(res) # ['I', 'I am', 'I am so', 'I am so tired']