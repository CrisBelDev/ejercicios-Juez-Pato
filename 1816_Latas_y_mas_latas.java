import java.util.Scanner;

public class Main{

	public static long suma(long n)
	{
		return (n*(n+1))/2;
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		long m,j;
		m= sc.nextLong();
		j=sc.nextLong();
		long sum=suma(j-1)+suma(m-j);
		System.out.println(sum);
		
	}

}