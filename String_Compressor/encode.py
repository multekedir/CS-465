# encode.py:

def encode(input_string):
    """

    :param input_string:
    :return:
    """
    # create new string
    result = ""
    count = 1
    index = 0

    # get each letter
    for j in range(len(input_string)):
        i = input_string[j]
        # add letter to the new string

        if result is "":
            result += i

        elif result[index] != i:
            print( result[index] + " is not " + i)

            index += 1

            # add occurrences if more than one
            if count > 1:
                result += str(count)
                index += 1
                count = 1
            result += i
        else:
            # count occurrences
            count += 1
        if j == (len(input_string) - 1) and count > 1:
            print("done")
            result += str(count)
        print(result)
    return result


print(encode("aabcccccaaa"))
