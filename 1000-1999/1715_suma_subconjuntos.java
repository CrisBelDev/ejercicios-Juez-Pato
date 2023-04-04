import java.util.Scanner;

public class Main{
    static final int MAXN = 1000;
    static int[] V = new int[MAXN];
    static int con = 0;

    static void comb_rec(int i, int K, int N, int s, int sum, int bitmask) {
        if (K == 0) {
            if (sum == s) {
                con++;
            }
            return;
        }
        if (i >= N) {
            return;
        }
        comb_rec(i + 1, K - 1, N, s, sum + V[i], bitmask | (1 << i));
        comb_rec(i + 1, K, N, s, sum, bitmask);
    }

    static void comb(int N, int K, int s) {
        comb_rec(0, K, N, s, 0, 0);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int s, n;
        while (input.hasNextInt()) {
            s = input.nextInt();
            n = input.nextInt();
            for (int i = 0; i < n; i++) {
                V[i] = input.nextInt();
            }
            for (int i = 0; i <= n; i++) {
                comb(n, i, s);
            }
            System.out.println(con);
            con = 0;
        }
        input.close();
    }
}