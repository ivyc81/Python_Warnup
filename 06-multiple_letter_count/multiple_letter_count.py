def multiple_letter_count(string):
    
    the_set = set(string)

    return {letter: string.count(letter) for letter in the_set}
    