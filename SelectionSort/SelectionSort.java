package SelectionSort;

public class SelectionSort {
public static void selectionSort(int [] arr){
for (int i = 0; i < arr.length - 1; i++){
	int min  = i ;
	for(int j = i + 1; j < arr.length; j++){
		if( arr[min] > arr[j]){
			min = j;
		}
	}
	int temp = arr[i];
	arr[i] = arr[min];
	arr[min] = temp;
	}
}
public static void main(String[] args){
	        int[][] tests = {
            {1, 2, 3, 4, 5},    // posortowana
            {5, 4, 3, 2, 1},    // odwrotnie
            {3, 1, 2, 3, 1},    // duplikaty
            {7},                // jeden element
            {},                 // pusta
            {5, 3, 8, 4, 2}     // losowa
        };

        int[][] expected = {
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4, 5},
            {1, 1, 2, 3, 3},
            {7},
            {},
            {2, 3, 4, 5, 8}
        };

        for (int i = 0; i < tests.length; i++) {
            selectionSort(tests[i]);
            System.out.print("Test " + (i+1) + ": ");
            System.out.print("Output = ");
            for (int x : tests[i]) System.out.print(x + " ");
            System.out.print("| Expected = ");
            for (int x : expected[i]) System.out.print(x + " ");
            System.out.println();
        }
    
}

}	