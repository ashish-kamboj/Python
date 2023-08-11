"""
A string is beautiful if no two adjacent characters are either
- the same, for example 'aa'
- adjacent in the alphabet, for example 'ef'

The following operations can be performed on a string, s.
- choose any index i(0<= i < |s|) and change s[i] to any lowercase english letter

Find the minimum number of operations required to make the string beautiful
Example:
s="abdde"
String is not beautiful because:
- 'dd' voilates constraint 1, no two adjacent characters are same
- 'ab' and 'de' voilate constraint 2, no two adjacent characters are adjacent in the alphabet

The string can be converted into a beautiful string after 2 operations. One solution is below.
1. choose i=1 and change s[i] to 'z'. s becomes "azdde"
2. choose i=3 and change s[i] to 'k'. s becomes "azdke" which is beautiful

Note: There are many other solutions such as "ardze", "axdke", etc.

It can be shown that 2 is the minumum number of operations required to return 2

Function Description:
--------------------
Complete the function
    - getMinimumOperationCount in the editor below

getMinimumOperationCount has the following parameter:
    - s: a string

Returns
    - int: the minimum number of operations required to make s beautiful

constraints:
    1. 2<= |s| <= 100000
    2. The string s contains only lowercase English letters.

Example1:
---------
s = "bcbb"
output = 2

Explanation: "bcbb" contains adjacent characters which are adjacent in the alphabet i.e. "cb", "bc" and the adjacent matching characters "bb"
One alternative is:
1. Choose i=1, change s[i] to 'd'. s becomes "bdbb"
2. choose i=3, change s[i] to 'd'. s becomes "bdbd" which is beautiful

"""

def getMinimumOperationCount(s):
    string_length = len(s)
    operations = 0

    for index in range(1, string_length):
        # Check if two adjacent characters are either the same or adjacent in the alphabet
        if s[index] == s[index - 1] or abs(ord(s[index]) - ord(s[index - 1])) == 1:
            operations += 1

            # Choose the best character to replace the current character
            if index + 1 < string_length and abs(ord(s[index + 1]) - ord(s[index - 1])) != 1 and s[index + 1] != s[index - 1]:
                s = s[:index] + s[index - 1] + s[index + 1:]
            elif abs(ord(s[index]) - ord('a')) > abs(ord(s[index]) - ord('z')):
                s = s[:index] + 'a' + s[index + 1:]
            else:
                s = s[:index] + 'z' + s[index + 1:]

    return operations

if __name__ == '__main__':
    s = input("Enter String: ").strip()
    result = getMinimumOperationCount(s)
    print(f"Minimum operation required to get beautiful string is: {result}")
