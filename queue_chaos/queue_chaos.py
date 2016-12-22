'''
Consider n people, labelled from 1 to n are standing in a queue for something. If a person i+1 standing behind i wants to swap position with i,
he shall make a swap deal with i. After swap, the person will be labelled same as earlier. Only their positions are changed.
There can be constraints on the number of maximum swap deals per person. Suppose a queue where everyone is standing in increasing order of their labels initially,
few people make swap deals and arrive at a final configuration of the queue.

Given the final configuration of the queue, this program finds the number of swap deals and deal details that the queue members must have gone through
to make the final configuration of the queue from the given initial configuration. If there is a constraint on the number of swap deals, this program
will also tell that the arrangement is too chaotic and will tell the label of person who tried to make more than permitted number of deals.

Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'

First commit: Dec 23, 2016
'''

import sys
from copy import copy

#check if inputs are valid
def sanity_check(finalSeq, maxChaos):
    try:
        if(len(finalSeq) >= 2):
            for i in range(len(finalSeq)):
                try:
                    j = int(i+1)
                    if(j not in finalSeq):
                        sys.stderr.write('The sequence is non continuous, person ' + str(j) + ' is missing.\n')
                        return(-1)
                except Exception as e:
                    sys.stderr.write('Non numerical input found. ' + str(e) + '.\n')
                    return(-1)
        else:
            sys.stderr.out('Atleast two people are expected in the queue.\n')
            return(-1)
        for people in finalSeq:
            if(finalSeq.count(people) > 1):
                sys.stderr.write('One person can occur only once in the queue. ' + str(people) + ' has multiple occurances.\n')
                return(-1)
    except Exception as e:
        sys.stderr.write('Some error has occured. ' + str(e) + '.\n')
        return(-1)
    try:
        if(not(type(maxChaos) == type(0))):
            sys.stderr.write('Maximum allowed chaos must be an integer.\n')
            return(-1)
    except Exception as e:
        sys.stderr.write('Some error has occured. ' + str(e) + '.\n')
        return(-1)
            
#main function to calculate the number of deals to the final arrangement
#input: finalSeq = integer list containing the final rearrangement of people indices
#input: maxChaos (optional input) = maximum number of allowed deals per person
#outputs: error code given by -1, or
#         no chaos situation given by a list of deal sequences, or
#         chaos situation given by number of times each person tried to exceed the maximum number of deals allowed per person
def find_chaos_counts(finalSeq, maxChaos = -1):
    if(not(sanity_check(finalSeq, maxChaos) == -1)):
        swapRecord = {1:0, 2:0, 3:0, 4:0, 5:0}
        swapSequence = []
        try:
            originalSeq = [x+1 for x in range(len(finalSeq))]
            originalSeq.reverse()
            originalSeqRearranged = copy(originalSeq)
            finalSeq.reverse()
            while(not(originalSeq == finalSeq)):
                for i,person in enumerate(finalSeq):
                    if(i > originalSeq.index(person)):
                        swapRecord[person] += 1
                        swapSequence.append('{0} dealt with {1}'.format(person, originalSeq[originalSeq.index(person)+1]))
                        temp = originalSeqRearranged[originalSeqRearranged.index(person)]
                        p = originalSeqRearranged.index(person)
                        originalSeqRearranged[p] = originalSeqRearranged[p+1]
                        originalSeqRearranged[p+1] = temp
                        if((not(maxChaos) == -1) and (swapRecord[person] > maxChaos)):
                            return(swapRecord,maxChaos)
                originalSeq = originalSeqRearranged
            return(swapSequence)
        except Exception as e:
            sys.stderr.write('Some error has occured. ' + str(e) + '.\n')
            return(-1)

#calling the main function
if __name__ == '__main__':
    #example input with no constrain on maximum deals
    response = find_chaos_counts([2,1,5,3,4])
    #example input with no constrain on maximum deals
    #response = find_chaos_counts([2,5,1,3,4])
    #example input with a constrain on maximum deals
    #response = find_chaos_counts([2,1,5,3,4],2)
    if(not(response == -1)):
        if(type(response) == type([])):
            sys.stdout.write('There are total {0} deals.\n'.format(len(response)))
            sys.stdout.write('The sequence of deals is: \n')
            for deal in response:
                sys.stdout.write(deal + '\n')
        elif(type(response[0]) == type({})):
            sys.stdout.write('This rearrangement is too chaotic becuase someone tried to have more number of deals than permitted.\n')
            for person in response[0]:
                if(response[0][person] > response[1]):
                    sys.stdout.write('{0} tried deal {1} times.\n'.format(person, response[0][person]))
            
        
    
