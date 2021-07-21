/**This program demonstrates the functionality of
   the bubble sorting algorithm.
 */

public class BubbleSorter
{
    /**The BubbleSorter method will sort an array of
       integers using the bubble sort algorithm to sort
       an integer array
       @param array The array to sort using bubble sort algorithm
     */

     public static void bubbleSort(int[] array)
     {
         int last;
         int index;
         int temporary;

         for (last = array.length - 1; last >= 0; last--)
         {
             for (index = 0; index <= last - 1; index++)
             {
                 if (array[index] > array[index + 1])
                 {
                     temporary = array[index];
                     array[index] = array [index + 1];
                     array[index + 1] = temporary;
                 }
             }
         }
     }

     public static void main(String[] args)
     {
         int[] values = { 2, 5, 3, 17, 12, 4};

         System.out.println("Starting values: ");

         for (int sentinel: values)
         {
             System.out.print(sentinel + " ");
         }

         System.out.println();

         BubbleSorter.bubbleSort(values);

         for (int sentinel: values)
         {
             System.out.print(sentinel + " ");
         }
     }
}