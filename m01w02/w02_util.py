def max_kernel(num_list, k):
    # Check special condition: if list is null or if k <= 0, return empty list
    if not num_list or k <= 0:
        return []

    # Result to be return
    result = []

    for i in range(len(num_list) - k + 1):
        # Create a window from i to i + k
        window = num_list[i:i + k]

        # Find max value in window
        max_value = max(window)

        # Add max value to the result
        result.append(max_value)

    # Return final result
    return result


def character_count(word):
    """
    Count frequency of each character in a word.

    Parameter:
    word (str): string to count character.

    Return:
    dict: A dictionary with key is character, value is frequency of character in word.
    """
    # Init an empty dictionary
    frequency_dict = {}

    # Loop for each character in word
    for char in word:
        # if character already exist in the dictionary, increase frequency to 1
        if char in frequency_dict:
            frequency_dict[char] += 1
        # if character did not exist, add character to the dictionary with init value is 1
        else:
            frequency_dict[char] = 1

    # Return frequency of characters
    return frequency_dict


def count_word(file_path):
    """
    Read sentence in file txt, count frequency of word and return a dictionary
    with key is word and value is frequency.

    Parameters:
    file_path (str): Path to the txt file.

    Return:
    dict: Dictionary with key is word and value is frequency.
    """
    # Init a dictionary
    word_frequency = {}

    try:
        # Open file to read
        with open(file_path, 'r') as file:
            # Read each line in file
            for line in file:
                # Change all work to lower case
                line = line.lower()

                # Split line into array of words
                words = line.split()

                # Loop for each word in line
                for word in words:
                    # If work already exist in the dictionary, increase value to 1
                    if word in word_frequency:
                        word_frequency[word] += 1
                    # If word does not exist in the dictionary, add word into dictionary with initial value 1
                    else:
                        word_frequency[word] = 1
    except FileNotFoundError:
        print(f"File {file_path} does not exist.")
        return {}

    # return word frequency dictionary
    return word_frequency


def check_the_number(number):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)

    if number in list_of_numbers:
        results = "True"
    if number not in list_of_numbers:
        results = "False"
    return results


def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


def my_function_xy(x, y):
    result = []
    result.extend(x)
    result.extend(y)
    return result


def my_function_min(n):
    return min(n)


def my_function_max(n):
    return max(n)


def my_function_compare(integers, number=1):
    return any(x == number for x in integers)


def my_function_average(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


def my_function_div3(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


def my_factorial(y):
    var = 1

    while y > 1:
        var *= y
        y -= 1
    return var


def my_function_reverse(x):
    return x[::-1]


def function_helper(x):
    if x > 0:
        return "T"
    else:
        return "N"


def my_function_helper(data):
    res = [function_helper(x) for x in data]
    return res


def function_helper_check_duplicate(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function_helper_remove_duplicate(data):
    res = []
    for i in data:
        if (function_helper_check_duplicate(i, res)):
            res.append(i)
    return res
