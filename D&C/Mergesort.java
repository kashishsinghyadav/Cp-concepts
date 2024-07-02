import java.util.Arrays;

class HelloWorld {
    public static void merge(int mid, int l, int r, int[] arr) {
        int[] mer = new int[r - l + 1];
        int idx1 = l;
        int idx2 = mid + 1;
        int x = 0;
        
        while (idx1 <= mid && idx2 <= r) {
            if (arr[idx1] < arr[idx2])
                mer[x++] = arr[idx1++];
            else
                mer[x++] = arr[idx2++];
        }
        
        while (idx1 <= mid) {
            mer[x++] = arr[idx1++];
        }
        
        while (idx2 <= r) {
            mer[x++] = arr[idx2++];
        }
        
        for (int i = 0; i < mer.length; i++) {
            arr[l + i] = mer[i];
        }
    }
    
    public static void mergesort(int[] arr, int l, int r) {
        if (l < r) {
            int mid = l + (r - l) / 2; 
            mergesort(arr, l, mid);
            mergesort(arr, mid + 1, r);
            merge(mid, l, r, arr);
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {2, 1, 4, 3, 5, 8, 6};
        mergesort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    }
}
