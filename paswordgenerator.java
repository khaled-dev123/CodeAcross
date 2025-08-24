import java.util.Random;
import java.util.Scanner;

public class paswordgenerator {
    public static void main(String[] args) {
        String keyword = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        System.out.println("Enter the desired length of the password:");
        int length = scanner.nextInt();
        StringBuilder password = new StringBuilder();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(keyword.length());
            password.append(keyword.charAt(index));
        }

        System.out.println("Generated Password: " + password.toString());
        scanner.close();
    }
      
}
