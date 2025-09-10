package Bubblesort;
class Tests{
    public static void main(String[] args){
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

        for (int i = 0; i < tests.length; i++) {
            BubbleSort.bubblesort(tests[i]);
            System.out.print("Test " + (i+1) + ": ");
            System.out.print("Output = ");
            for (int x : tests[i]) System.out.print(x + " ");
            System.out.print("| Expected = ");
            for (int x : expected[i]) System.out.print(x + " ");
            System.out.println();
        }

    }
}
class BubbleSort {
    public static void bubblesort(int [] arr){
    for(int i = 0; i < arr.length - 1; i ++){
    for(int j = 0; j < arr.length - 1 - i; j++){
    int temp;
    if(arr[j] > arr[j+1]){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp	;
}
}
}

}
}


