import java.util.Arrays;

class LinearSearch {
    public static int LinearSearch(int[]arr, int target){
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;
            }
        }
        return -1;
    }
}

class BinarySearch {

public static int BinarySearch(int[]arr, int target){
    Arrays.sort(arr);
    int left = 0;
    int right = arr.length - 1; 
    while (left <= right){
        int mid = (left + right) / 2;
        if (arr[mid] == target){
            return mid;
    }
        else if (arr[mid] < target){
            left = mid + 1;
        }
        else{
            right = mid - 1;
        }
    }
    return -1;
    
}
}


class Tests {
    public static void main(String[] args) {
        int[] lista = {3, 2, 5, 3, 6, 9, 1, 4, 8};
        System.out.println(LinearSearch.LinearSearch(lista, 5));  
        System.out.println(LinearSearch.LinearSearch(lista, 10));


    int[][] arrays = {
            {1, 3, 5, 7, 9},
            {2, 4, 6, 8, 10},
            {5},
            {}
        };
        int[] values = {7, 9, 5, 1};
        int[] expected = {3,-1,0,-1};
        for (int i = 0; i < arrays.length; i++) {
            int result = BinarySearch.BinarySearch(arrays[i], values[i]);
            System.out.println("Array: " + Arrays.toString(arrays[i]) + ", Value: " + values[i] + ", Result: " + result + ", Expected: " + expected[i]);
        }

    }
}






