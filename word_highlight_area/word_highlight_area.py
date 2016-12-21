'Program to find the highlight area of a word'
'considers width as the number of letters highlighted and height as the length of the tallest letter in the selection'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 20, 2016'

import sys

#main function to calculate highlight area
#inputs, heights = array containing the heights of all 26 alphabets arranged in alphabetical order
#inputs, word = highlighted string whose area is to be identified
#output, area of the highlighted string
def find_highlight_area(heights, word):    
    try:
        for x in heights:
            if(int(y) > 7 or int(x) < 1):
                sys.stderr.write('Error in height specification. Should be in [1,7].\n')
                return
        if(not(len(heights) == 26)):
            sys.stderr.write('Exactly 26 height values are needed.\n')
            return
        else:
            wordWidth = len(word)
            if(wordWidth <= 0 or wordWidth > 10):
                sys.stdout.write('\nword length must be between 1 and 10.\n')
                return
            else:
                alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                constituentHeights = []
                for i in range(wordWidth):
                    constituentHeights.append(heights[alphabetList.index(word[i])])
                sys.stdout.write('The highlight area is {0}.\n'.format(wordWidth*max(constituentHeights)))
    except Exception as e:
        sys.stdout.write('\nCould not accept this input: ' + str(e) + '.\n')
                
if __name__ == '__main__':
    #following array contains the heights of all 26 alphabets arranged in alphabetical order
    heights = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    #example word, here 'b' is the tallest letter
    word = 'abc'
    find_highlight_area(heights, word)
            
