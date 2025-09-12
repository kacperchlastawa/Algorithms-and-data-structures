package InsertionSort;

public class Insertion{
	
	public static void insertionSort(int [] arr){
		
		for(int i = 1; i < arr.length; i++){
			int temp = arr[i];
			int j = i - 1;
			while( j >= 0 && arr[j] > temp) {
				
				arr[j + 1] = arr[j];
				j -= 1;
			}
			arr[j+1] = temp;
		
		}
		
		
	}
	
	public static void main(String [] args){
	
	int[][] tests = {
            {1, 2, 3, 4, 5},
            {5, 4, 3, 2, 1},
            {3, 1, 2, 3, 1},
            {7},
            {5, 3, 8, 4, 2}
        };

        int[][] expected = {
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4, 5},
            {1, 1, 2, 3, 3},
            {7},
            {2, 3, 4, 5, 8}
        };
        
        for(int i = 0; i < tests.length; i++){
            insertionSort(tests[i]);
            System.out.print("Test " + (i+1) + ": ");
            System.out.print("Output = ");
            for (int x : tests[i]) System.out.print(x + " ");
            System.out.print("| Expected = ");
            for (int x : expected[i]) System.out.print(x + " ");
            System.out.println();
        
        }
	}
	
}