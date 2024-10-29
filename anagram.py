# Anagram is a word or phrase formed by rearranging the letters of another 
# word or phrase, using all the original letters exactly once.

def is_anagram(s1, s2):
    """
    Time: O(n)
    Space: O(n)
    """
    # Check if strings are the same length
    if len(s1) != len(s2):
        return False

    # Create dictionary to store character frequencies
    freq = {}

    # Increment frequencies for characters in first string
    for char in s1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Decrement frequencies for characters in second string
    for char in s2:
        if char in freq:
            freq[char] -= 1
        else:
            return False # character not in first string

        # Check if frequency became negative
        if freq[char] < 0:
            return False

    # Check if all frequencies are zero
    for count in freq.values():
        if count != 0:
            return False

    return True

def group_anagrams(strings):
    """ 
    Time: O(nk log k), where n is total strings & k is the max length of a word
    Space: O(nk), each word and its anagram key are stored in the dictionary
    """
    anagram_dict = {}
    for string in strings:
        # Sort the string to get its anagram key
        key = ''.join(sorted(string))
        if key in anagram_dict:
            anagram_dict[key].append(string)
        else:
            anagram_dict[key] = [string]
    return list(anagram_dict.values())

if __name__=='__main__':

    s1 = 'cinema'
    s2 = 'iceman'
    res = is_anagram(s1, s2) # True
    print(res)

    strings = ['eat','tea','tan','ate','nat','bat']
    res = group_anagrams(strings) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(res)