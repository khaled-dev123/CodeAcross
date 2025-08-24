import java.util.Scanner;

// Shopping Cart Program
public class ShoppingCartProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String item;
        float price;
        int quantity;

        System.out.println("Enter the item name:");
        item = scanner.nextLine();
        System.out.println("Enter the price of the item:");
        price = scanner.nextFloat();
        if (price < 0) {
            System.out.println("Price cannot be negative. Please enter a valid price.");
            price = scanner.nextFloat();
        }
        System.out.println("Enter the quantity of the item:");
        quantity = scanner.nextInt();

        float totalCost = price * quantity;
        System.out.println("You have added " + quantity + " " + item + "(s) to your cart.");
        System.out.println("The total cost is: $" + totalCost);

        System.out.println("Thank you for shopping with us!");

        scanner.close();
    } 
}
        