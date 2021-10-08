
class NumSquare():

    def __init__(self, num=None):
        """
        Constructor of the class

        Parameters
        ----------
            num: int
                number for which we have to check a perfect square
        """
        self.factors = []
        self.div_num = 2
        self.num_to_check = num


    def getNumber(self, num):
        """
        Gets the number on which the invoked method needs to operate on

        Parameters
        ----------
        num: int
            number provided to the invoked method

        Returns
        -------
        int
            COALESCE(num,self.num_to_check). Raises error if both are None
        """
        if num is not None:
            return num
        elif self.num_to_check is not None:
            return self.num_to_check
        else:
            raise ValueError('Number is not provided')


    def factorization(self, number):
        """
        Use to calculate the factors of an integer

        Parameters
        ----------
            number: int
                Number for which factors to be found
        Returns
        -------
            list
                list of factors
        """
        remainder = number % self.div_num
        quotient = number // self.div_num

        if(remainder == 0):
            self.factors.append(self.div_num)

            if(quotient >= self.div_num):
                self.factorization(quotient)     
            else:
                return self.factors
        else:
            self.div_num += 1
            self.factorization(number)
        
        
    def perfectSquareCheck(self, num=None):
        """
        Used to check whether a number is a perfect square or not

        Parameters
        ----------
            num: int
                Number to check for perfect square, if num is not provided while initialising, Needs to be provided now
        Returns
        -------
            str
                'message whether a number is perfect square or not'
        """
        num = self.getNumber(num)

        if(num < 0):
            return "Specified number is less than 0"
        elif(num == 0):
            return "Specified number is 0, which is a perfect square"
        elif(num == 1):
            return "Specified number is 1, which is a perfect square"
        else:
            # calling function to get the factors of a number
            self.factorization(num)
            print("{} Factorization :: {}".format(num, self.factors))

            # getting unique factors
            unique_factors = list(set(self.factors))

            for index, fact in enumerate(unique_factors):
                # checking count of each factors
                count = self.factors.count(fact)

                if(count%2 == 0):
                    if(index < len(unique_factors)-1):
                        continue
                    else:
                        return str(num) + " is a perfect square"
                else:
                    return str(num) + " is not a perfect square"




input_number = input("Enter the number: ")
print("\nNumber is :: ",input_number)

if(input_number.isdigit()):
    # instantiating the class
    square_class = NumSquare(int(input_number))

    # calling function for checking the perfect square for input number
    result = square_class.perfectSquareCheck()
    print(result)
else:
    print("Entered number should be integer")
