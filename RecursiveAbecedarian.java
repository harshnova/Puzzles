// Abecedarian: A word with all characters in alphabetical sequence

import java.util.Scanner;

public class RecursiveAbecedarian{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the string: ");
        String userWord = scanner.nextLine();
        System.out.println(isAbecedarian(userWord));
    }

    public static boolean isAbecedarian(String userWord){
        boolean detected = false;
        if(userWord.length() == 1){
            detected = true;
        }else if(userWord.length() == 2){
            if(Character.toString(userWord.charAt(1)).compareTo(Character.toString(userWord.charAt(0))) >= 0){
                detected = true;
            }else{
                detected = false;
            }
        }else{
            char userWordFirst = first(userWord);
            userWord = rest(userWord);
            detected = (Character.toString(userWord.charAt(1)).compareTo(Character.toString(userWordFirst)) >= 0 ) && (isAbecedarian(userWord));
        }
        return(detected);
    }

    public static String rest(String s) {
        return s.substring(1);
    }

    public static char first(String s) {
        return s.charAt(0);
    }
}