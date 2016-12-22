DOCUMENTATION

Consider n people, labelled from 1 to n are standing in a queue for something. If a person i+1 
standing behind i wants to swap position with i to come forward, he shall make a swap deal with i. 
After swap, people will be labelled same as earlier. Only their positions are changed.
There can be constraints on the number of maximum swap deals per person. Suppose a queue where
everyone is initially standing in increasing order of their labels, few people make swap deals and 
arrive at a final configuration of the queue. This final configuration is given to us.

Given the final configuration of the queue, this program finds the number of swap deals and deal 
details that the queue members must have gone through to make the final configuration of the queue 
from the given initial configuration. If we put a constraint on the number of swap deals, this program
will also tell that the arrangement is too chaotic and will tell the label of the person who tried to 
make more than permitted number of deals.

----------------------------------------
Solution methodology
----------------------------------------

A person can make a deal only with the person standing in fron of him. Therefore the first person
in the queue can not initiate a deal. Due to this, we will analyze this problem from the last person.
We need a terminal person to start with. First person can not initiate a deal. So we start with the 
last person.Therefore, before deals happen, we assume an initial/original sequence where every person is 
standing in an increasing order of their label (line 61) and we reverse it (line 62) to begin our
analysis with the last person.

We will swap people in the original sequence until final sequence is achieved, where we stop our 
analysis. This condition is met on line 65.

We take last person on the final sequence and verify if he was standing at a later position in
the original sequence, on line 67. Definitely there can not be a later position for the last
person in the sequence. We move to the second last person in the final sequence and test for the
same. If the person was standing in a later position in the original sequence, he must had 
executed a swap deal with the person standing at front of him. We record the swaps made by
that person on line 68. And then we create a copy (originalSeqRearranged) of the original sequence 
on line 63. This copy will be rearranged at every swap, so that the notion of original sequence 
in originalSeq is not disturbed. So, to record a swap deal, we represent the swap on the
originalSeqRearranged by swapping the corresponding elements in the list. We continue this till 
all the elements of the final sequence are analyzed by reverse traversing.

If there were n people in the queue, there can be more than n deals to reach at final configuration.
But reverse traversing only once across the final sequence can provide information about maximum 
n deals. Therefore at the end of first traversal, we render the rearranged original sequence to
be the original sequence, on line 76, and compare the positions of people again like earlier, and
swap.

Once all swaps are done to reach final configuration, we have the history of deal sequences
recorded with us. If a constraint is set on maximum number of deals per person, we detect
if someone is making more deals, on line 74, and inform the user about it.