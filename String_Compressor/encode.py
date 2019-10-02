#encode.py:

def encode(input_string):
    """

    :param input_string:
    :return:
    """
    # create new string
    result = ""

    # get each letter
    for i in input_string:
        # count occurrences
        count = input_string.count(i)
        # add letter to the new string
        result += i
        # add occurrences if more than one
        if count != 1:
            result += str(count)

    return input_string
