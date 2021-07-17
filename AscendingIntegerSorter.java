/**
   This program demonstrates the functionality of 
   sorting algorithms. This program sorts the hardcoded
   integers in ascending order.
 */

public class AscendingIntegerSorter 
{
    public static void main(String[] args)
    {
        int[] values = {5, 1, 3, 6, 4, 2};

        System.out.println("Original Order: ");
        for (int accumulator : values)
        {
            System.out.println(accumulator + " ");
        }

        AscendingIntegerSorterClass.AscendingSort(values);

        System.out.println("\nSorted order: ");
        for (int accumulator : values)
        {
            System.out.println(accumulator + " ");
        }

        System.out.println();
    }
}
