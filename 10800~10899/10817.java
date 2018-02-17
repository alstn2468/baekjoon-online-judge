/*
 	*
 	* 문제
 	* 세 정수 A, B, C가 주어진다. 이 때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
 	*
 	* 입력
 	* 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
 	*
 	* 출력
 	* 두 번째로 큰 정수를 출력한다.
 	*
 */

import java.util.Arrays;
import java.util.Scanner;

public class BOJ {

	public static void main(String[] args) {
		int[] num = new int[3];

		Scanner scan = new Scanner(System.in);

		for(int i = 0; i < 3; i++)
		{
			num[i] = scan.nextInt();
		}
		scan.close();

		Arrays.sort(num);
		System.out.println(num[1]);

	}

}
