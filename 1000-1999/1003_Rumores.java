import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] arg)
    {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int n = in.nextInt(); // numero de personas numeradas
            int m = in.nextInt(); // numero de relaciones de amistar
            int matris[][] = new int[2][m];
            for (int j = 0; j < m; j++) {
                int u = in.nextInt();
                int v = in.nextInt();
                matris[0][j]=u;
                matris[1][j]=v;
            }
            int x = in.nextInt();
            int y = in.nextInt();
            funcion(m,x,y,matris);
        }
        
    }

    private static void funcion(int m, int x, int y, int[][] matris) {
        List lista = new ArrayList();
        for (int j = 0; j < m; j++) {
            for (int i = 0; i < m; i++) {
                if(x==matris[0][i])
                {
                    lista.add(matris[1][i]);
                }
            }
            int num = lista.size();
            x = (int) lista.get(num-1);
        }
        int num = lista.size();
        for (int i = 0; i < num; i++) {
            int var = (int) lista.get(i);
            if(var==y)
            {
                System.out.println("SI");
                return;
            }
        }
        System.out.println("NO");
        return;
    }
}