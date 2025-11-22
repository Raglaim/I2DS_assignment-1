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

def add_in_base(n1,n2,base):
    """
    Add two numbers in a given base.

    Converts both numbers from the specified base to base 10, adds them,
    and then converts the result back to the original base.

    How it works:
        1. Convert n1 and n2 from the given base to base 10.
        2. Add the two base-10 numbers.
        3. Convert the sum back to the specified base.

    Args:
        n1 (str or int): The first number in the given base.
        n2 (str or int): The second number in the given base.
        base (int): The base of the numbers (between 2 and 36).

    Returns:
        str: The sum of the two numbers in the given base.
    """

    n1_10 = n_to_10(n1,base)
    n2_10 = n_to_10(n2,base)
    ans = n_10_to_base(n1_10 + n2_10,base)
    return ans

while True:
    list = ["0","1","2","3","4","5","6","7","8","9","a","A","b","B","c","C","d","D","e","E","f","F"]
    try:
        n1=str(input("Enter a number: "))
        for i in n1:
            if i not in list:
                raise ValueError("Invalid number!")
        break
    except:
        print("Error: invalid number, please enter a number up to base 16!")
while True:
    list = ["0","1","2","3","4","5","6","7","8","9","a","A","b","B","c","C","d","D","e","E","f","F"]
    try:
        n2=str(input("Enter a number: "))
        for i in n2:
            if i not in list:
                raise ValueError("Invalid number!")
        break
    except:
        print("Error: invalid number, please enter a number up to base 16!")

while True:
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
        "F": 15, "f": 15
    }
    list1 = sorted(strtolist(n1))
    list2 = sorted(strtolist(n2))
    if list1 > list2:
        min_base = letter_to_number[list1[-1]] + 1
    else:
        min_base = letter_to_number[list2[-1]] + 1
    try:
        if min_base == 16:
            base = 16
            break
        else:
            base = base = strtoint(input(f"Enter the base of the number (between {min_base} and 16): "))
            if base < min_base or base > 16:
                raise ValueError("Invalid base!")
        break
    except:
        print("Error: base is out of range!")


print("The sum of",n1,"and",n2,"in base",base,"is",add_in_base(n1,n2,base))