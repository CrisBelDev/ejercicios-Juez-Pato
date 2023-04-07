import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner leer = new Scanner(System.in);
		int t = leer.nextInt();
		leer.nextLine();
		while (t-- > 0) {
			String cad = leer.nextLine().toUpperCase();
			
			String nn ="";
			boolean sw = true;
			for(int i = 0 ; i <cad.length() ;i++) {
                                if(cad.charAt(i) == ' '){
                                    nn = nn + cad.charAt(i);
                                }else{
                                    if(sw) {

                                            nn = nn + cad.charAt(i);
                                            sw = false;
                                    }else {
                                            nn = nn + cad.toLowerCase().charAt(i);
                                            sw = true;
                                    }
                                }
			}
			
			System.out.println(nn);
		}
	}
}
