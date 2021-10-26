def countArithmeticMeans(a):
    """
    Used to find the count of numbers which are arithmetic mean of their adjacent numbers

    Parameters
    ----------
        list
            List of numbers to check for arithmetic mean
    Returns
    -------
        int
            count of numbers which are arithmetic mean
    """

    count = 0
    
    if(len(a) != 1):
        for idx, num in enumerate(a):
            if(idx == 0):
                # If it is a first element of list
                if(a[idx + 1] == 2 * a[idx]):
                    count = count + 1
            elif(idx == len(a)-1):
                # If it is the last element of list
                if(a[idx - 1] == 2 * a[idx]):
                    count = count + 1       
            elif(a[idx - 1] + a[idx + 1] == 2 * a[idx]):
                count = count + 1
            else:
                continue
        return count
    elif(len(a) == 1 and a[0] == 0):
        return count + 1
    else:
        return count

    #return count

#a = [2, 4, 6, 6, 3]

input_numbers = input("Enter the numbers seperated by space : ")
numbers_list = list(map(int, input_numbers.split()))

print("\nNumber List :: ",numbers_list)

num_count = countArithmeticMeans(numbers_list)
print("Count of numbers which are arithmetic mean of adjacent numbers :: ",num_count)

