# LAB 05: METHODS

# Problem 2:

def factorial( num ):        # define function factorial with a single parameter num
    result = 1                
    if num == 0:             # if num is 0 the result of the factorial is 1 ie 0! = 1
        return 1
        
    else:                   # if num is not 0 go ahead and do the factorial calculation
        for i in range( num, 0, -1 ):
            result = result * i
        
    return result           # return result
    
    
    
    
# Problem 3

def fibonacci( num ):   # function definition with number of fibonacci element as parameter
    my_list = []        # empty list to store the series generated thus far
    fib_sum = 1
    my_list.append(fib_sum)   # if argument provided is 1 then the series is a 1

    init = 0
    end = fib_sum
    while len(my_list) < num:       # find fibonacci numbers if num is not equal to 1
        fib_sum = end + init
        my_list.append(fib_sum)
        init = end
        end = fib_sum

    return my_list



# Problem 4

def prime( num ):   # function definition here with 'num' as parameter
    divisors = 0     # initialize a 'divisors' variable to store the current number of divisors
    for i in range( 1, num + 1):  # loop through '1' to 'num + 1' and check if num has a divisors
        if ( num % i) == 0:       # if num has a divisor
            divisors += 1         # increment the 'divisors' variable
    if divisors == 2:
        return True             # break from the function and print 'True' if num is a prime
        
    return False                 # if num is not a prime numbe return 'False'
    
    
# Challenge Problems:

# Problem 4:

def isPalindrome( input_string ):     # function definiton with the 'input_string' as parameter
  
    register = []                     # An empty register to record if there is a character match
    
    for n in range( 0, len(input_string)-1):           # loop until every character in my string is exhausted
      
        if input_string[ n ] == input_string[ -( n + 1 ) ]:  # Perform character match and add a 'T' to register if there is a match
            register.append('T')
        
        else:                         # if there is no match add an 'F' to register
            register.append('F')
        
    if 'F' not in register:           # check if register is all 'Ts' and return 'True' if it is
        return True
        
    return False                   # if the register contains an 'F' return 'False'
    
    
# Problem 5

def isSubstring( string_1, string_2 ):  #function definition with the two strings as parameters
  
    for i in range( 0, len(string_2) - len(string_1) + 1 ):  #loop through 0 to the difference in length of the given strings
        
        if string_1 == string_2[ i:i+len(string_1) ]:   #test if string_1 is contained in string_2 by 
            return True                     # if string_1 is a subset of string_2, return 'True'
        
    else:
        return False     # return 'False' if string_1 is not a subset of string_2
    
# Problem 7

    
def max_Score( string_1, string_2, string_3):  # function definition taking scores as argument
    score_sum = 0                          # register to keep track of current sum of scores
    n = 0                       # string indexer
    for score in string_1:       # loop through the first string of wrong scores
        if score == string_2[n] and score == string_3[n]:   # if Jill and Fred choose the same answer as me, sum of score is 0
            score_sum += 0
        
        elif score != string_2[n] and score != string_3[n] and string_2[n] == string_3[n]: # if both Jill and Fred chose the same 
            score_sum += 2                              # different from mine, add 2 to score_sum
        
        else:
            score_sum += 1              # if all the other conditions are not satisfied, then aded 1 to score_sum
        n += 1
    return score_sum        
        
    
    
        
