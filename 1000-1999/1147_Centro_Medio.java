import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

	Scanner leer = new 	Scanner(System.in);
	int n;
	while (leer.hasNext()) {
		n=leer.nextInt();
		int a=0, b=n;
		
		while (b-a>1) {
			int mid = (a+b)/2;
			 long sumiz = f(mid-1);
			long sumder = f(n) - f(mid);
			if (sumiz >= sumder) {
				b=mid;
			}
			else{
				a=mid;
			}
		}
		long totaliz = f(b-1);
		long totalder = f(n) - f(b);
		
		if (totaliz != totalder) {
			System.out.println("NO");
		}
		else{
			System.out.println(b);
		}
	}
	}
	public static long f(long n){
		return n*(n+1)/2;
	}
}