import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner leer = new Scanner(System.in);
		String s = leer.next();

		String [] Sufijos = new String[s.length()];	
		String SufijoActual = "";

		for (int i = s.length()-1; i >=0; i--) {
			char c = s.charAt(i);
			SufijoActual = c + SufijoActual;
			Sufijos[i] = SufijoActual;
		}
		
		int n = s.length();

		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				if (esMenor(Sufijos[j], Sufijos[i])) {
					String aux = Sufijos[j];
					Sufijos[j] = Sufijos[i];
					Sufijos[i] = aux;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			System.out.println(Sufijos[i]);
		}
	}
	
	public static boolean esMenor(String a, String b){
		for (int i = 0; i <Math.min(a.length(), b.length()); i++) {
			char da=a.charAt(i);
			char db=b.charAt(i);
			if (da>db) {
				return false;
			}
			else{
				if (da<db) {
					return true;
				}
			}
		}
		return a.length() <= b.length();
	}
}