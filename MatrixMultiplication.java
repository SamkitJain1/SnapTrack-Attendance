import java.util.Arrays;

//package CLRS_Book;
public class MatrixMultiplication {
    public static void main(String[] args) {

        int[][] A =
                {
                        {3, 1, 2, 4},
                        {4, 1, 3, 2},
                        {1, 4, 2, 3},
                        {1, 2, 3, 4}
                };
        int[][] B =
                {
                        {3, 1, 2, 4},
                        {2, 4, 1, 3},
                        {4, 3, 2, 1},
                        {3, 1, 4, 2}
                };

        int n = A.length;

        for (int[] row : bruteForce(A, B))
            System.out.println(Arrays.toString(row));

        System.out.println("\n\n\n");

        for (int[] row : divConquer(A, B, n))
            System.out.println(Arrays.toString(row));
    }

    static int[][] bruteForce(int[][] A, int[][] B){
        int n = A.length;
        int m = A[0].length;
        int p = B.length;
        int q = B[0].length;
        if(m == p){
            int[][] C = new int[n][q];

            for (int i=0; i<n; i++){
                for (int j=0; j<q; j++){
                    int x = 0;
                    for (int k=0; k<m; k++){
                        x += A[i][k] * B[k][j];
                    }
                    C[i][j] = x;
                }
            }

            return C;
        }
        else
            return new int[0][0];
    }

    static int[][] divConquer(int[][] a, int[][] b, int n){
        int[][] c = new int[n][n];
        if (n==2){
            c[0][0] = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0]);
            c[0][1] = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1]);
            c[1][0] = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0]);
            c[1][1] = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1]);
        }
        else {
            int[][] a1 = arrayCopy(a, n, 1);
            int[][] a2 = arrayCopy(a, n, 2);
            int[][] a3 = arrayCopy(a, n, 3);
            int[][] a4 = arrayCopy(a, n, 4);

            int[][] b1 = arrayCopy(b, n, 1);
            int[][] b2 = arrayCopy(b, n, 2);
            int[][] b3 = arrayCopy(b, n, 3);
            int[][] b4 = arrayCopy(b, n, 4);

            int[][] c1 = arrayAdd(divConquer(a1, b1, n/2), divConquer(a2, b3, n/2), n/2);
            int[][] c2 = arrayAdd(divConquer(a1, b2, n/2), divConquer(a2, b4, n/2), n/2);
            int[][] c3 = arrayAdd(divConquer(a3, b1, n/2), divConquer(a4, b3, n/2), n/2);
            int[][] c4 = arrayAdd(divConquer(a3, b2, n/2), divConquer(a4, b4, n/2), n/2);

            c = arrayCombine(c1, c2, c3, c4, n);

        }
        return c;
    }

    static int[][] arrayAdd(int[][] A, int[][] B, int n){
        int[][] C = new int[n][n];
        for (int i=0; i<n; i++){
            for (int j=0; j<C[0].length; j++){
                C[i][j] = A[i][j] + B[i][j];
            }
        }
        return C;
    }

    static int[][] arrayCombine(int[][] c1, int[][] c2, int[][] c3, int[][] c4, int n){
        int[][] C = new int[n][n];

        for (int j=0; j<n/2; j++){
            System.arraycopy(c1[j], 0, C[j], 0, n / 2);
            if (n - n / 2 >= 0) System.arraycopy(c2[j], n / 2 - 2, C[j], n / 2, n - n / 2);
        }
        for (int j=n/2; j<n; j++){
            System.arraycopy(c3[j - 2], 0, C[j], 0, n / 2);
            if (n - n / 2 >= 0) System.arraycopy(c4[j - 2], n / 2 - 2, C[j], n / 2, n - n / 2);
        }
        return C;
    }

    static int[][] arrayCopy(int[][] A, int n, int block){
        int[][] Acopy = new int[n/2][n/2];
        switch (block){
            case 1 -> {
                for (int i = 0; i < n/2; i++) {
                    Acopy[i] = Arrays.copyOfRange(A[i], 0, n/2);
                }
            }
            case 2 -> {
                for (int i = 0; i < n/2; i++) {
                    Acopy[i] = Arrays.copyOfRange(A[i], n/2, n);
                }
            }
            case 3 -> {
                for (int i = 0; i < n/2; i++) {
                    Acopy[i] = Arrays.copyOfRange(A[i + n/2], 0, n/2);
                }
            }
            case 4 -> {
                for (int i = 0; i < n/2; i++) {
                    Acopy[i] = Arrays.copyOfRange(A[i + n/2], n/2, n);
                }
            }
        }
        return Acopy;
    }
}
