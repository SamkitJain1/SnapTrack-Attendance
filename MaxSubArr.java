package CLRS_Book;
public class MaxSubArr {
    public static void main(String[] args) {
        int[] arr = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
        System.out.println(bruteForce(arr));
        System.out.println(divideConquer(arr, 0, arr.length-1));
        System.out.println(kadenAlgo(arr));
    }

    static int kadenAlgo(int[] arr) {
        int max_sum = Integer.MIN_VALUE;
        int csum = 0;
        for (int j : arr) {
            if (j + csum < j)
                csum = Math.max(csum, j);
            else
                csum += j;
            max_sum = Math.max(csum, max_sum);
        }
        return max_sum;
    }

    static int divideConquer(int[] arr, int l, int r){
        if (l==r)
            return arr[l];
        else {
            int m = l + (r-l)/2;
            int lmax = divideConquer(arr, l, m);
            int rmax = divideConquer(arr, m+1, r);

            int crossmax = crossMid(arr, l, m, r);

            return Math.max(crossmax, Math.max(lmax, rmax));
        }
    }

    static int crossMid(int[] arr, int l, int m, int r){
        int lmax = Integer.MIN_VALUE;
        int rmax = Integer.MIN_VALUE;
        int rsum = 0;
        int lsum = 0;
        for (int i=m; i>=l; i--){
            lsum += arr[i];
            lmax = Math.max(lmax, lsum);
        }
        for (int i=m+1; i<=r; i++){
            rsum += arr[i];
            rmax = Math.max(rmax, rsum);
        }
        return rmax + lmax;
    }

    static int bruteForce(int[] arr){
        int n = arr.length;
        int maxsum = Integer.MIN_VALUE;
        int csum;
        for (int i=0; i<n; i++){
            csum = 0;
            for (int j=i; j<n; j++){
                csum += arr[j];
                maxsum = Integer.max(maxsum, csum);
            }
        }
        return maxsum;
    }
}