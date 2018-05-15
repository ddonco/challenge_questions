##### Question 2 #####
"""
Given a string a, find the longest palindromic substring
contained in a. Your function definition should look
like question2(a), and return a string.
"""

def quesiton2(a):
    """
    Check for even and odd palendromes separately while iterating over
    string.
    """
    palendrome = ""
    even_palendrome = ""
    odd_palendrome = ""
    step = 0
    if type(a) == str:
        for index in range(1, len(a)):
            # Check for palendrome with even number of letters
            if a[index] == a[index - 1]:
                step = 0
                while (index + step) < len(a) and (index - step) >= 0 and \
                        a[index + step] == a[index - step - 1] and \
                        a[index + step].isalpha():
                    step += 1
                even_palendrome = a[index - step:index + step]

            # Check for palendrome with odd number of letters
            if (index + 1) < len(a) and a[index + 1] == a[index - 1]:
                step = 1
                while (index + step) < len(a) and (index - step) >= 0 and \
                        a[index + step] == a[index - step] and \
                        a[index + step].isalpha():
                    step += 1
                odd_palendrome = a[index - step + 1:index + step]

            # Update palendrome variable with longest even or odd palendrome
            if len(even_palendrome) > len(palendrome):
                palendrome = even_palendrome
            if len(odd_palendrome) > len(palendrome):
                palendrome = odd_palendrome
    else:
        palendrome = None
    return palendrome


def main():
    test1 = "A girl named hannah went to the market."
    print("Question2: {0}".format(quesiton2(test1)))
    # Result: hannah

    test2 = "The racecar is fast."
    print("Question2: {0}".format(quesiton2(test2)))
    # Result: racecar

    test3 = 12321
    print("Question2: {0}".format(quesiton2(test3)))
    # Result: None

    test4 = None
    print("Question2: {0}".format(quesiton2(test4)))
    # Result: None


if __name__ == '__main__':
    main()
