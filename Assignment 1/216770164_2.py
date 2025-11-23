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

def n_10_to_base(number,base):
    """
    Convert a base-10 number to any other base.

    Takes a number in base 10 and converts it to the specified base.
    Supports bases up to 36.

    How it works:
        1. Converts the input to an integer.
        2. Divides the number by the base repeatedly, storing remainders.
        3. Maps each remainder to its digit or letter.
        4. Reverses the list and joins it into a string.

    Args:
        number (int or str): The number in base 10.
        base (int): The target base (between 2 and 36).

    Returns:
        str: The number represented in the new base.
    """

    number = str(number)
    number_to_letter = {
0:"0",
1:"1",
2:"2",
3:"3",
4:"4",
5:"5",
6:"6",
7:"7",
8:"8",
9:"9",
10:"A",
11:"B",
12:"C",
13:"D",
14:"E",
15:"F",
16:"G",
17:"H",
18:"I",
19:"J",
20:"K",
21:"L",
22:"M",
23:"N",
24:"O",
25:"P",
26:"Q",
27:"R",
28:"S",
29:"T",
30:"U",
31:"V",
32:"W",
33:"X",
34:"Y",
35:"Z"
}
    n = strtoint(number)
    ans = []
    while n != 0:
        ans.append(number_to_letter[n % base])
        n //= base
    return listtostr(swap(ans))

#Ask for a number in base 10.
while True:
    try:
        number=str(input("Enter a number: "))
        for i in number:
            if strtoint(i) not in range(10):
                raise ValueError("Invalid number!")
        break
    except:
        print("Error: invalid number, please enter a number in base 10!")
#Ask for a base.
while True:
    try:
        base=strtoint(input("Enter a base: "))
        if base not in range(2,17):
            raise ValueError("Invalid base!")
        break
    except:
        print("Error: base out of range, please enter a base between 2 and 16!")


print(n_10_to_base(number,base))