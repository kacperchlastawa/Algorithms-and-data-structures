package CountingSort;

public class CountingSort {

	public static void countingSort(int [] arr) {
        if(arr.length == 0)
            return;	
            
        int max = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] > max)
                max = arr[i];
        }
        int[] counting = new int[max + 1];
        for(int j = 0; j < arr.length; j++){
            counting[arr[j]] += 1;	
            }
        for(int k = 1; k < counting.length; k++){
            counting[k] = counting[k] + counting[k-1];
        }
        int[] output = new int[arr.length];
        for(int l = arr.length - 1; l >= 0; l--){
            output[counting[arr[l]] - 1] = arr[l];
            counting[arr[l]] -= 1;
        }
        System.arraycopy(output, 0, arr, 0, arr.length);
}
public static void main(String[] args) {
        int[][] tests = {
            {1, 4, 1, 2, 7, 5, 2}, 
            {5, 4, 3, 2, 1},         
            {1, 2, 3, 4, 5},         
            {3, 3, 2, 1, 2, 1},      
            {7},                     
            {}                       
        };

        int[][] expected = {
            {1, 1, 2, 2, 4, 5, 7},
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4, 5},
            {1, 1, 2, 2, 3, 3},
            {7},
            {}
        };

        for (int i = 0; i < tests.length; i++) {
            CountingSort.countingSort(tests[i]);
            System.out.print("Test " + (i + 1) + ": Output = ");
            for (int x : tests[i]) System.out.print(x + " ");
            System.out.print("| Expected = ");
            for (int x : expected[i]) System.out.print(x + " ");
            System.out.println();
        }
    }


}
