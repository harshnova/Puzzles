'Program to find how many numbers are included between two given integer sets'
'A number x is included between two sets A and B if all elements in A are factors of x and x is factor of all elements in B'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 20, 2016'

import sys

#function to determine if an integer called factor is factor of all the numbers in an integer set, called integerSet
def factors_all(integerSet, factor):
    factorsAll = True
    for element in integerSet:
        if(not(element%factor == 0)):
            factorsAll = False
            break
    return(factorsAll)

#main function to find what all numbers are included between two sets
#inputs, two sets, setA and setB as python list
#outputs, how many numbers are included between two sets and what are those numbers
def chain_factor(setA, setB):
    if(not((type(setA) == type([])) or (type(setB) == type([])) or (type(setA) == type(())) or (type(setB) == type(())))):
        sys.stderr.write('Invalid input types. Must be list or tuple.\n')
        return(-1)
    else:
        if((len(setA) == 0) or (len(setB) == 0)):
            sys.stderr.write('Sets cant be empty.\n')
            return(-1)
        else:
            try:
                maxA = max(setA)
                minB = min(setB)
                for entry in setA:
                    if(not(maxA%entry == 0)):
                        sys.stderr.write('Inconsistent set A. All numbers must be factor of largest number of set A.\n')
                        return
                probedNumber = maxA
                includedNumbers = []
                while(probedNumber <= minB):
                    if(factors_all(setB, probedNumber)):
                        includedNumbers.append(probedNumber)
                    probedNumber = probedNumber + maxA
                return(includedNumbers)
            except Exception as e:
                sys.stderr.write('Invalid entries in input arguments: ' + str(e) + '.\n')
                return(-1)

if __name__ == '__main__':
    #example sets: setA and setB
    setA = [2,4]
    setB = [16,32,96]
    includedNumbers = chain_factor(setA, setB)
    if((len(includedNumbers) > 0) and (type(includedNumbers) == type([]))):
        sys.stdout.write('There are {0} included numbers: {1}\n'.format(len(includedNumbers), includedNumbers))
    elif(includedNumbers == -1):
        sys.stderr.write('There is an error.\n')
    else:
        sys.stdout.write('There are no included numbers.\n')
                         
