'Program to determine if all the n chasers running in same direction at different speeds and at some separation, will meet at one point'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 04, 2016'

#numpy needs to be installed as external library, before importing it
import numpy as np

#Main method to determine if all chasers gather at one point
#Input: As the observation starts, the locations and speeds of all the chasers, comma separated, for one chaser after another
#Speed is assumed to be constant and location changes with every step of run
def chase_meet(*arg):
    try:
        if((len(arg)%2 == 0) and (len(arg) > 0)):
            params = locals()
            configuration = list(params['arg'])
            coeff = []
            position = []
            coeff_matrix = []
            position_vector = []
            padding = []
            chasers_count = len(arg)/2
            for i in range(chasers_count - 2):
                padding.append(0)            
            try:
                for i, conf in enumerate(configuration):
                    if(i%2 == 0):
                        position.append(conf)
                    else:
                        coeff.append([1, -conf]+padding)                
                coeff_matrix = np.array(coeff)
                position_vector = np.array(position)
                del coeff, position, padding
                result_vector = np.matmul(np.linalg.pinv(coeff_matrix), position_vector)
                print(result_vector)
                del coeff_matrix, position_vector
                if((result_vector[0] > 0) and (result_vector[1] > 0)):
                    return([result_vector[0], result_vector[1]])
                else:
                    return(-1)
            except ImportError, e:
                return('Please ensure that numpy is installed in your environment. ' + str(e))
            except ValueError, e:
                return('Invalid input(s). must be numeric. ' + str(e))           
        else:
            return('This is invalid input. Please check the number of arguments. Initial velocity of the last participant is missing.')
    except Exception, e:
        return('Invalid input(s). ' + str(e))

#Examples

#1. There are two chasers, who at the time of observation, are at locations 0 and 4 respectively and their speeds are 3 and 2 respectively
#chase_result = chase_meet(0,3,4,2)

#2. There are two chasers, who at the time of observation, are at locations 0 and 5 respectively and their speeds are 2 and 3 respectively
#chase_result = chase_meet(0,2,5,3)

#try:
#    if(int(chase_result) == -1):
#        print('The chasers DO NOT MEET.')
#except:
#    if(type(chase_result) == type([])):
#        print('The chasers MEET at position {0} and at time {1} from observation onset.'.format(chase_result[0], chase_result[1]))
#    else:
#        print(chase_result)
    



