'Program to find the maximum hourglass inside a 6x6 array of integers, by sum of numbers constituting all the hourglass patterns in the array'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 04, 2016'

#Defining the hourglass object
class Hourglass:
    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0):
        'a, b, c, d, e, f, g are numbers in pictorial representation of the hourglass'
        try:
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
            self.f = f
            self.g = g
        except:
            return('Invalid input(s) in describing hourglass object.')

    def hg_sum(self):
        'find the hourglass sum'
        return (self.a + self.b + self.c + self.d + self.e + self.f + self.g)

#Defining the method to find the maximum hourglass
#Command line inputs:
#1. Space separated six elemets containing six rows of the input 6x6 array  
def findMaximumHourglass():
    #Initiating storage
    input_array = [] 
    hourglass_sum = {}

    #Initiating indices
    i = 0
        
    #Populating the input arrays row by row conditioned to the input constraints
    #Should build a 6 x 6 input array with all numbers from -9 to 9
    #Each row consists of space separated six integers, input one row at a time as the program is onset
    print('Enter the 6x6 input array')
    while(i <= 5):    
        try:
            row_input = [int(x) for x in input().strip().split(' ')]
            if((not(len(row_input) == 6)) or (any(((y > 9) or (y < -9)) for y in row_input))):
                print('Invalid argument. Size should be 6 and number shall be within -9 and 9 both inclusive. Enter this row again.')
            else:
                input_array.append(row_input)
                i += 1                   
        except:
            print('Invalid input(s) in forming input array rows.')

    #Finding hourglasses in the input array, calculting their sum, populating sum in the hourglass_sum storage, and recording the hourglass pattern
    for i in range(len(input_array)):
        j = 0
        try:
            while((i < len(input_array) - 2) and (j < len(input_array[0]) - 2)):
                a = input_array[i][j]
                b = input_array[i][j+1]
                c = input_array[i][j+2]
                d = input_array[i+1][j+1]
                e = input_array[i+2][j]
                f = input_array[i+2][j+1]
                g = input_array[i+2][j+2]    
                hg = Hourglass(a, b, c, d, e, f, g)
                pattern = (a, b, c, d, e, f, g)
                hourglass_sum[hg.hg_sum()] = pattern
                i += 1
                j += 1
        except:
            pass

    #returning the maximum hourglass result
    pic = str(list(hourglass_sum[max(hourglass_sum)])[0]) + str(list(hourglass_sum[max(hourglass_sum)])[1]) + str(list(hourglass_sum[max(hourglass_sum)])[2]) +\
          '\n' + str(' ') + str(list(hourglass_sum[max(hourglass_sum)])[3]) + '\n' + str(list(hourglass_sum[max(hourglass_sum)])[4]) +\
          str(list(hourglass_sum[max(hourglass_sum)])[5]) + str(list(hourglass_sum[max(hourglass_sum)])[6])        
        
    result = '\nMaximum hourglass = ' + str(max(hourglass_sum)) + '\nwith pattern \n' + str(pic) 
    return(result)
        
#Example
#As soon the program is set on run, enter these six sets of space separated six integers, each set constituting a row, one row at a time, followed by return key
#1 1 1 0 0 0 <return> 0 1 0 0 0 0 <return> 1 1 1 0 0 0 <return> 0 0 2 4 4 0 <return> 0 0 0 2 0 0 <return> 0 0 1 2 4 0

#If any improper input is provided, user will be prompted to enter the input again

#Allowing user to provide input as the program runs, and display maximum hourglass
print(findMaximumHourglass())
        
    
    
        
        

    
    
