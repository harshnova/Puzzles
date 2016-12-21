'Find out the maximum first quadrant sum of a 2n x 2n matrix after a series of row and column reversals to generate the maximum first quadrant sum'
'Author: Harsh Vardhan(harshvardhan.mse@gmail.com)'
'First commit: Dec 22, 2016'

import sys

#check if the input matrix is eligible to be analyzed (must be square matrix with even dimension > 0)
def sanity_check(A):
    try:
        m = len(A)
        if(m == 0):
            sys.stderr.write('Empty matrix.\n')
            return(-1)
        elif(not(m%2==0)):
            sys.stderr.write('Only even number of columns accepted.\n')
            return(-1)
        elif(not(len(A[0])%2==0)):
            sys.stderr.write('Only even number of rows accepted.\n')
            return(-1)
        for row in A:
            if(not(len(row) == m)):
                sys.stderr.write('Only square matrices are accepted.\n')
                return(-1)
        else:
            return(m)           
    except Exception as e:
        sys.stderr.write('An error occured in sanity check. ' + str(e) + '.\n')
        return(-1)

#find maximum of four input numbers and the position of the maximum number in the inputs
def max_of_four(p,q,r,s):
    try:
        setFour = [p,q,r,s]
        maxFour = max(setFour)
        i = setFour.index(maxFour)
        return(maxFour, i)
    except Exception as e:
        sys.stderr.write('An error occured in finding maximum number on mirror positions. ' + str(e) + '.\n')
        return(-1)

#reverse a row or a column
def reverse(vector):
    try:
        vector.reverse()
        return(vector)
    except Exception as e:
        sys.stderr.write('An error occured in reversing the vector. ' + str(e) + '.\n')
        return(-1)

#main function to reverse the rows and columns to generate matrix with maximum first quadrant sum
#input: A = input matrix
#output: if analysis is successful, it gives the maximum sum, the sequence of operations and final matrix, else an error code -1
def find_first_maximum_submatrix(A):
    try:
        sequences = []
        maxSum = 0
        m = sanity_check(A)
        if(not(m == -1)):
            n=int(m/2)
            try:
                i = n-1
                j = n-1
                while((i>=0) and (j>=0)):
                    maxResult = max_of_four(A[i][j], A[i][m-1-j], A[m-1-i][m-1-j], A[m-1-i][j])
                    maxSum += maxResult[0]
                    if((not(maxResult == -1)) and (not(maxResult[1] == 0))):
                        if(maxResult[1] == 1):
                            A[i]=reverse(A[i])
                            sequences.append('Reverse row ' + str(i+1))
                        elif(maxResult[1] in [2,3]):
                            col = []
                            for k in range(m):
                                col.append(A[k][m-1-j])
                            col = reverse(col)
                            for k,element in enumerate(col):
                                A[k][m-1-j] = element
                            sequences.append('Reverse column ' + str(m-j))
                    j-=1
                    if(j < 0):
                        j = n-1
                        i-=1                
                return(maxSum,sequences,A)    
            except Exception as e:
                sys.stderr.write('Only numerical matrices are accepted. ' + str(e) + '.\n')
                return(-1)
    except:
        sys.stderr.write('An error occured. ' + str(e) + '.\n')
        return(-1)
        
#call the main function and if matrix analyzed successfully, then print the maximum sum, the sequence of operations and the final matrix after operations
if __name__ == '__main__':
    #consider following input matrix
    A = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
    result = find_first_maximum_submatrix(A)
    if(not(result == -1)):
        sys.stdout.write('The maximum sum is: ' + str(result[0]) + '\n\n')
        sys.stdout.write('The sequence of operations is:\n')
        for sequence in result[1]:
            sys.stdout.write(sequence+'\n')
        sys.stdout.write('\n\n')
        sys.stdout.write('The final matrix is:\n')
        for row in result[2]:
            sys.stdout.write(str(row)+'\n')
            


        
        
