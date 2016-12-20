DOCUMENTATION

This program identifies all those integers that are included between two integer sets.
An integer x is said to be included between two sets A nd B if all elements of A 
are factors of x and x is a factor of all the elements of B.

For all integers in A to be the factors of x, all those integers must also be the 
factor of the highest integer in A. We check this condition in lines 32 - 35. 
We select the largest number of set A as a possible inlcusion, on line 36. We make this selection
because the largest number in A is the most probable integer that can constitute atleast one 
inclusion. 
We then check if this number factors all elements in B, on line 39. If it factors, then it is the 
first inclusion. Naturally, the next inclusion will be atleast twice of the first inclusion.
It means, all the possible inclusions will be multiple of the first inclusion. 
The highest inclusion will never be greater than smallest element of B.
So, on lines 38-41, we test all possible numbers to be inclusions, and construct the set of 
final inclusions.

The source contains a working example.