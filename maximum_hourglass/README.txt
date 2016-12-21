Algorithm to find the hourglass pattern with maximum sum of the integers constituting the pattern, within a 6x6 array.

A sample input sequence is:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

The hourglass here pattern is defined as:

abc
 d
efg

Therefore, the hourglasses embedded in the input array (with their sum indicated at the bottom) are:

111      110      010     440
 0        0        1       0
111      110      002     240
(6)      (4)      (4)     (14)

and so on, there are total 16 hourglasses, each with a sum = a+b+c+d+ef+g. 
This algorithm will find hourglass with maximum sum.

All working examples are provided in the source. 