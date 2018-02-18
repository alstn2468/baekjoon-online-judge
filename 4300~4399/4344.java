/*
 	*
 	* 문제
 	* 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
 	*
 	* 입력
 	* 첫째 줄에는 테스트케이스 C가 주어진다.
 	* 둘째 줄부터 각 테스트케이스 마다 첫 수로 정수 N(1 <= N <= 1000)명의 학생이 주어지고
 	* 그 다음으로 N명의 0부터 100 사이의 점수가 이어서 주어진다.
 	*
 	* 출력
 	* 각 케이스마다 한줄씩 평균을 넘는 학생들의 비율을 소수점 넷째자리에서 반올림하여 출력한다.
 	*
 */

import java.util.Scanner;

public class BOJ {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		int test_c = scan.nextInt();
		int std_num = 0, total, count = 0;
		double avg;

		int score[] = new int[1000];

		for(int i = 0; i < test_c; i++)
		{
			std_num = scan.nextInt();
			total = 0;
			count = 0;

			for(int j = 0; j < std_num; j++)
			{
				score[j] = scan.nextInt();
				total += score[j];
			}
			avg = (double)total / std_num;

			for(int j = 0; j < std_num; j++)
			{
				if(score[j] > avg)
					count++;
			}

			System.out.printf("%.3f", 100.0 * count / std_num);
			System.out.println("%");
		}

		scan.close();

	}

}
