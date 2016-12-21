DOCUMENTATION

This program calculates the area of a word. Assume that a word is highlighted in a text editor
or a pdf document. The highlight is rectangular. We have to find the area of this rectangle.

We consider the length of rectangle as the count of letters in the word. The height of 
tallest word is height of the rectangle.

We construct an integer array of size 26, that represents the height of all 26 letters
supposed to be in alphabetical order. Using that, we identify the tallest integer and 
multiply that with the length of the input word to return the highlight area.