def flip_case(string, letter):
    the_list = list(string)
    target_letter = letter.lower()
    
    for i in range(len(string)):
        if string[i].lower() == target_letter:
            if  string[i].islower():
                the_list[i] = target_letter.upper()
            elif string[i].isupper():
                the_list[i] = target_letter.lower()

    # the_string = str(the_list)

    return "".join(the_list)