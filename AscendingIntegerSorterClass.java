/**
   This program demonstrates the functionality of
   sorting algorithms. This program serves as the "class"
   for the ascending sorter.
 */

public class AscendingIntegerSorterClass
{
    /**
       The AscendingSort method will sort the contents
       of an integer array in ascending order
       @param array
     */
    public static void AscendingSort(int[] array)
    {
        int last;
        int index;
        int swap;

        for (last = array.length - 1; last >= 0; last--)
        {
            for (index = 0; index <= last - 1; index++)
            {
                if (array[index] > array[index + 1])
                {
                    swap = array[index];
                    array[index] = array[index + 1];
                    array[index + 1] = swap;
                }
            }
        }
    }
}
