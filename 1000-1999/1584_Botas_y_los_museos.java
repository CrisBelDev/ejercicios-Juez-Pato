import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		 
		ArrayList<Integer> c = new ArrayList<>();
		Scanner leer = new Scanner(System.in);
		while (leer.hasNext()) {
			int x = leer.nextInt();
			leer.nextLine();
			String [] l = leer.nextLine().split(" ");
			for (int i = 0; i < l.length; i++) {
				c.add(Integer.parseInt(l[i]));
			}
			Collections.sort(c);
			int r = c.get(c.size()-1)-c.get(0);
			System.out.println(r);
			c.clear();
		}
	}
}