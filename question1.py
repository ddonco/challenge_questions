##### Question 1 #####
"""
Given two strings s and t, determine whether some anagram of t
is a substring of s. For example: if s = "udacity" and t = "ad",
then the function returns True. Your function definition should
look like: question1(s, t) and return a boolean True or False.
"""

def question1(s, t):
    """
    First check that string 's' and substring 't' are both of type
    string, and t is not greater than s. Then check that each letter
    in t can be found in s.
    """
    if type(t) == str and type(s) == str and len(s) >= len(t):
        for letter in t:
            if letter not in s:
                return False
        return True
    else:
        return False


def main():

    s = "udacity"

    t = "ucy"
    print("Question1:", question1(s, t))
    # Result: True

    t = "udacity"
    print("Question1:", question1(s, t))
    # Result: True

    t = "tz"
    print("Question1:", question1(s, t))
    # Result: False

    t = 1
    print("Question1:", question1(s, t))
    # Result: False

    t = None
    print("Question1:", question1(s, t))
    # Result: False


if __name__ == '__main__':
    main()
