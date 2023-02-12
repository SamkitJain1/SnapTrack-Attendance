//import java.util.Arrays;
//
//public class MergeSort{
//    void sort(int[] A, int l, int r){
//        if (l < r) {
//            int m = l + (r-l)/2;
//            sort(A, l, m);
//            sort(A, m+1, r);
//
//            merge(A, l, m, r);
//        }
//    }
//
//    void merge(int[] A, int l, int m, int r){
//        int p1 = l;
//        int p2 = m+1;
//        int[] B = Arrays.copyOf(A, A.length);
//        int i = p1;
//
//        while(p1<=m && p2<=r){
//            if(B[p1] > B[p2]){
//                A[i++] = B[p2];
//                p2++;
//            }
//            else {
//                A[i++] = B[p1];
//                p1++;
//            }
//        }
//        while(p1<=m)
//            A[i++] = B[p1++];
//        while(p2<=r)
//            A[i++] = B[p2++];
//    }
//
//    public static void main(String[] args) {
//        int[] arr = {14, 1112, 311, 60, 7};
//        MergeSort object = new MergeSort();
//
//        object.sort(arr, 0, arr.length-1);
//
//        System.out.println(Arrays.toString(arr));
//    }
//}