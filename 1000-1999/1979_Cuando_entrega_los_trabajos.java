
import java.util.Scanner;

public class Main {

    static int sumatoria(int n, int v[]) {
        int s = 0;
        for (int i = 0; i < v.length; i++) {
            s = s + (n / v[i]);
        }
        return s;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int v[] = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = sc.nextInt();
        }
        int c = sc.nextInt();
        while (c-- > 0) {
            int k = sc.nextInt();
            System.out.println("Tiempo minimo para " + k + " trabajos es: " + busqueda(k, v));
        }
    }

    public static long busqueda(int n, int v[]) {
        int L = 0;
        int R = 10000;
        while (L + 1 < R) {
            int mitad = (L + R) / 2;
            if (sumatoria(mitad,v) < n) {
                L = mitad;
            } else {
                R = mitad;
            }
        }
        if (sumatoria(R,v) >= n) {
            
            return R;
        } else {
            
            return 0;
        }
    }
}