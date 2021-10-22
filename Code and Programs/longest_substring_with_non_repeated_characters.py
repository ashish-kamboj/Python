## Find the longest substring which has no character repeating more than once

input_string = input("Enter any string: ")
print("\nEntered String is :: ",input_string)

def longestSubstring(input_str):

    element_list = []
    substr_list = []

    for indx, str_char in enumerate(input_str):

        element_list.append(str_char)
        second_pointer = indx + 1
        str_2 = str_char

        for i in range(second_pointer, len(input_str)):
            if(input_str[i] in element_list):
                element_list = []
                break
            else:
                element_list.append(input_str[i])
                str_2 = str_2 + input_str[i]
        if(str_2):
            substr_list.append(str_2)

    return max(substr_list, key=len)


long_substr = longestSubstring(input_string)
print("Longest substring with no repeated characters :: ", long_substr)






