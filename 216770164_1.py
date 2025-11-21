import math
def strtolist(string):
    """
    Turn a string into a list of its characters.

    Takes a string and splits it into individual characters, returning them as a list.

    Args:
        string (str): The input string.

    Returns:
        list: A list where each element is one character from the string.
    """

    str_list = []
    for i in string:
        str_list.append(i)
    return str_list
def listtostr(list):
    """
    Combine a list of characters into a single string.

    Joins all elements of the list into one continuous string.

    Args:
        list (list): A list of characters or elements that can be converted to strings.

    Returns:
        str: The combined string.
    """

    string = ""
    for i in list:
        string += str(i)
    return string
def swap(list):
    """
    Reverse the elements of a list.

    Swaps elements from the start and end until the list is reversed.

    Args:
        list (list): The list to reverse.

    Returns:
        list: The same list, but reversed.
    """

    temp = 0
    for i in range (math.floor(len(list)/2)):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
def strtoint(string):
    """
    Convert a string of digits into an integer.

    Reads the string from left to right, converts each digit to its numeric value,
    and calculates the final integer. Stops if a non-digit character is found.

    Args:
        string (str): The input string containing digits.

    Returns:
        int: The integer value represented by the string.
    """

    swaped_sting = listtostr(swap(strtolist(string)))
    number = 0
    x = 0
    numbers_dictionary = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    for i in swaped_sting:
        if i in numbers_dictionary:
            number += numbers_dictionary[i] * (10 ** x)
            x += 1
        else:
            break
    return number

def n_to_10(number,base):
    """
    Convert a number from any base to base 10.

    This function takes a number (which can include digits and letters) in a given base
    and calculates its value in base 10. Supports bases up to 36.

    How it works:
        1. Turns the number into a string.
        2. Reverses the order to start from the least significant digit.
        3. Converts each character to its numeric value.
        4. Adds everything up using position value: value * (base ** position).

    Args:
        number (int or str): The number in its original base.
        base (int): The base of the number (between 2 and 36).

    Returns:
        int: The number converted to base 10.
    """

    number = str(number)
    letter_to_number = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10, "a": 10,
        "B": 11, "b": 11,
        "C": 12, "c": 12,
        "D": 13, "d": 13,
        "E": 14, "e": 14,
        "F": 15, "f": 15,
        "G": 16, "g": 16,
        "H": 17, "h": 17,
        "I": 18, "i": 18,
        "J": 19, "j": 19,
        "K": 20, "k": 20,
        "L": 21, "l": 21,
        "M": 22, "m": 22,
        "N": 23, "n": 23,
        "O": 24, "o": 24,
        "P": 25, "p": 25,
        "Q": 26, "q": 26,
        "R": 27, "r": 27,
        "S": 28, "s": 28,
        "T": 29, "t": 29,
        "U": 30, "u": 30,
        "V": 31, "v": 31,
        "W": 32, "w": 32,
        "X": 33, "x": 33,
        "Y": 34, "y": 34,
        "Z": 35, "z": 35

    }
    ans = 0
    number_list_swaped = swap(strtolist(number))
    x = 0
    for i in number_list_swaped:
        ans += letter_to_number[i] * (base ** x)
        x += 1
    return ans

number=str(input("Enter a number: "))
base=int(input("Enter the base of the number: "))
print(n_to_10(number,base))
