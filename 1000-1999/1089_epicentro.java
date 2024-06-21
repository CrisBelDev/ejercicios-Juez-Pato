import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.nextLine(); 
        for (int i = 0; i < n; i++) {
            String num = scanner.nextLine().trim();
            String resultado = encontrarEpicentro(num);
            System.out.println(resultado);
        }
 
        scanner.close();
    }
    public static String encontrarEpicentro(String num) {
        int longitud = num.length();
        if (longitud % 2 == 0) {
            return "*";
        } else {
            int medio = longitud / 2;
            return String.valueOf(num.charAt(medio));
        }
    }
}