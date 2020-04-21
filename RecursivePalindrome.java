// Palindrome: a word that is symmetric across the mid

import java.util.Arrays;
import java.util.Scanner;

public class RecursivePalindrome{

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your word: ");
        String userWord = scanner.nextLine();
        System.out.println("All letters in actual order: ");
        printString(userWord);
        System.out.println("All letters in backward order: ");
        printBackward(userWord);
        System.out.println("Reversed string: ");
        System.out.println(reverseString(userWord));
        System.out.println("Is Palindrome: ");
        System.out.println(isPalindrome(userWord));
    }

    // 1. a method called printString that takes a string as a parameter and that displays the letters of the string, 
    // one on each line
    public static void printString(String userWord){
        while(length(userWord) > 0){
            System.out.println(first(userWord));
            userWord = rest(userWord);
        }
    }

    // 2. a method called printBackward that does the same thing as printString but that displays the string 
    // backward, one character per line
    public static void printBackward(String userWord){
        char[] stringChars = new char[userWord.length()];
        int i = 0;
        while(length(userWord) > 0){
            stringChars[i] = first(userWord);
            userWord = rest(userWord);
            i += 1;
        }
        for (int j = stringChars.length - 1; j >= 0; j -= 1){
            System.out.println(stringChars[j]);
        }
    }

    // 3. a method called reverseString that takes a string as a parameter and that returns a new string as a return value.
    public static String reverseString(String userWord){
        String reversedString = "";
        char[] stringChars = new char[userWord.length()];
        int i = 0;
        while(length(userWord) > 0){
            stringChars[i] = first(userWord);
            userWord = rest(userWord);
            i += 1;
        }
        for (int j = stringChars.length - 1; j >= 0; j -= 1){
            reversedString += stringChars[j];
        }
        return(reversedString);
    }

    // 4.  a recursive method named isPalindrome that takes a String and returns a boolean indicating whether the word 
    // is a palindrome
    public static boolean isPalindrome(String userWord){
        char[] userWordArray = userWord.toCharArray();
        boolean detected = false;
        if(userWordArray.length == 1){
            detected = true;
        }else if(userWordArray.length == 2){
            if(userWordArray[0] == userWordArray[1]){
                detected = true;
            }else{
                detected = false;
            }
        }else{
            userWord = middle(userWord);
            detected = (userWordArray[0] == userWordArray[userWordArray.length - 1]) && isPalindrome(userWord);
        }
        return(detected);
    }


    // Returns the first character of the given String.
    public static char first(String s) {
        return s.charAt(0);
    }

    // Returns all but the first letter of the given String.
    public static String rest(String s) {
        return s.substring(1);
    }

    // Returns all but the first and last letter of the String.
    public static String middle(String s) {
        return s.substring(1, s.length() - 1);
    }

    // Returns the length of the given String.
    public static int length(String s) {
        return s.length();
    }
}