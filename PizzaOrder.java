///////////////////////////////////////////////
//ISCI 201 Introduction to Computer Science  //
//Fall 2020 Semester                         //
//Oct 6, Tuesday, 9:09 P.M.                  //
//Bryan Herrera Mendoza                      //
//001468723                                  //
///////////////////////////////////////////////
import java.util.Scanner;  // Needed for the Scanner class

/**This program allows the user to order a pizza.*/


public class PizzaOrder
{
  public static void main (String[] args)
  {
    // Create a Scanner object to read input.
    Scanner keyboard = new Scanner (System.in);
    
    final double TAX_RATE = .08;      //Sales tax rate
    
    boolean discount = false;         //Flag for discount
    
    char choice;                      //User's choice
    char crustType;                   //For type of crust
    
    double cost = 12.99;              //Cost of the pizza
    double tax;                       //Amount of tax
    
    String crust = "Hand-tossed";     //Name of crust
    String firstName;                 //User's first name
    String ownerName_1 = "Mike";      //Owner 1's first name
    String ownerName_2 = "Diane";     //Owner 2's first name
    String input;                     //User input
    String toppings = "Cheese ";      //List of toppings
    
    int inches;                       // Size of the pizza
    int numberOfToppings = 0;         // Number of toppings
    
    // Prompt user and get first name.
    System.out.println("Welcome to Mike and Diane's Pizza");
    System.out.print("Enter your first name: ");
    firstName = keyboard.nextLine();
    
    // Determine if user is eligible for discount by
    // having the same first name as one of the owners.
    // ADD LINES HERE FOR TASK #1
    if ((ownerName_1.compareToIgnoreCase(firstName) == 0
           || ownerName_2.compareToIgnoreCase(firstName) == 0))
    {
      discount = true;                  //Makes the discount boolean true
    }
    
    // Prompt user and get pizza size choice.
    System.out.println("Pizza Size (inches)   Cost");
    System.out.println("        10            $10.99");
    System.out.println("        12            $12.99");
    System.out.println("        14            $14.99");
    System.out.println("        16            $16.99");
    System.out.println("What size pizza would you like?");
    System.out.print("10, 12, 14, or 16 " + "(enter the number only): ");
    inches = keyboard.nextInt();
    
    // Set price and size of pizza ordered.
    // ADD LINES HERE FOR TASK #2
    if (inches == 10)            //A 10-inch pizza is worth $10.99
      cost = 10.99;
    
    else if (inches == 12)        //A 12-inch pizza is worth $12.99
      cost = 12.99;
    
    else if (inches == 14)        //A 14-inch pizza is worth $14.99
      cost = 14.99;
    
    else if (inches == 16)        //A 16-inch pizza is worth $16.99
      cost = 16.99;
    
    else                          //If none of the selections above are made, else will occur
    {
      inches = 12;
      System.out.println("You have not entered a valid pizza size.");
      System.out.println("A 12-inch pizza will be made by default.");
      System.out.println();
    }
    
    
    // Consume the remaining newline character.
    keyboard.nextLine();
    
    // Prompt user and get crust choice.
    System.out.println("What type of crust do you want?");
    System.out.print("(H)Hand-tossed, " +
                     "(T) Thin-crust, or " +
                     "(D) Deep-dish " +
                     "(enter H, T, or D): ");
    input = keyboard.nextLine();
    crustType = input.charAt(0);
    
    // Set user's crust choice on pizza ordered.
    // ADD LINES FOR TASK #3
    switch (input)
    {
      case "h":               //The control structure for the inputs "H" or "h"
      case "H":
        crust = "Hand-tossed";
        System.out.print("You have selected a " + crust);
        System.out.print(" pizza."); 
        break;
        
      case "t":               //The control structure for the inputs "T" or "t"
      case "T":
        crust = "Thin-crust";
        System.out.print("You have selected a " + crust);
        System.out.print(" pizza.");
        break;
        
      case "d":               //The control structure for the inputs "D" or "d"
      case "D":
        crust = "Deep-dish";
        System.out.print("You have a selected a " + crust);
        System.out.print(" pizza.");
        break;
        
      default:                //The control structure if none of the inputs are entered
        crust = "Hand-tossed";
        System.out.println("You did not input one of the choices above.");
        System.out.println("A hand-tossed crust has been selected for you.");
    }
    
    System.out.println("\n");    //Will create a blank line to separate text
    
    
    // Prompt user and get topping choices one at a time.
    System.out.println("All pizzas come with cheese.");
    System.out.println("Additional toppings are $1.25 each, choose from:");
    System.out.println("Pepperoni, Sausage, Onion, Mushroom");
    
    // If topping is desired,
    // add to topping list and number of toppings
    System.out.print("Do you want Pepperoni? (Y/N): ");
    input = keyboard.nextLine();
    
    choice = input.charAt(0);
    
    if (choice == 'Y' || choice == 'y')
    {
      numberOfToppings += 1;
      toppings = toppings + "Pepperoni ";
    }
    
    System.out.print("Do you want Sausage? (Y/N): ");
    input = keyboard.nextLine();
    choice = input.charAt(0);
    
    if (choice == 'Y' || choice == 'y')
    {
      numberOfToppings += 1;
      toppings = toppings + "Sausage ";
    }
    
    System.out.print("Do you want Onion? (Y/N): ");
    input = keyboard.nextLine();
    choice = input.charAt(0);
    
    if (choice == 'Y' || choice == 'y')
    {
      numberOfToppings += 1;
      toppings = toppings + "Onion ";
    }
    
    System.out.print("Do you want Mushroom? (Y/N): ");
    input = keyboard.nextLine();
    choice = input.charAt(0);
    
    if (choice == 'Y' || choice == 'y')
    {
      numberOfToppings += 1;
      toppings = toppings + "Mushroom ";
    }
    
    // Add additional toppings cost to cost of pizza.
    cost = cost + (1.25 * numberOfToppings);
    
    // Display order confirmation.
    System.out.println();
    System.out.println("Your order is as follows: ");
    System.out.println(inches + " inch pizza");
    System.out.println(crust + " crust");
    System.out.println(toppings);
    
    // Apply discount if user is eligible.
    // ADD LINES FOR TASK #4 HERE
    if (discount)
    {
      System.out.println();
      System.out.println("*********************************************************");
      System.out.println("**                Congratulations!!!                   **");
      System.out.println("**       You are eligible for a $2.00 discount         **");
      System.out.println("*********************************************************");
      cost -= 2.0;
    }
    
    System.out.println();  
    
    // EDIT PROGRAM FOR TASK #5
    // SO ALL MONEY OUTPUT APPEARS WITH 2 DECIMAL PLACES
    System.out.printf("The cost of your order " +
                      "is: $%.2f\n", cost);
    
    // Calculate and display tax and total cost.
    tax = cost * TAX_RATE;
    System.out.printf("The tax is: $%.2f\n", tax);
    System.out.printf("The total due is: $%.2f\n",
                      (tax + cost));
    
    System.out.println("Your order will be ready " +
                       "for pickup in 30 minutes.");
  }
}

