import java.util.Scanner;
//Mid labs game
public class Midlibsgame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String place;
        String noun;
        String adjetive2;
        String verb;
        String adjetive3;

        System.out.println("Enter a place:");
        place = scanner.nextLine();
        System.out.println("Enter a noun:");
        noun = scanner.nextLine();
        System.out.println("Enter another adjective:");
        adjetive2 = scanner.nextLine();
        System.out.println("Enter a verb:");
        verb = scanner.nextLine();
        System.out.println("Enter a final adjective:");
        adjetive3 = scanner.nextLine();
       
        System.out.println("today I went to go to " + place + " and I saw a " + noun + " that was " + adjetive2 + ". I decided to " + verb + " it because it looked " + adjetive3 + "."); 

        scanner.close();
    }
}
