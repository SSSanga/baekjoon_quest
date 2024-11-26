import java.util.Scanner;

public class quest2753 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        //백준 2753번
        //윤년이면 1, 아니면 0 을 출력
        //윤년 조건 : 4의 배수이면서 100의 배수가 아닌것, 400의 배수인것
        //첫째줄에 연도 주어짐. 연도는 1 < = year <= 4000 자연수 

        short A = myObj.nextShort(); 
        if ( A % 4 == 0 && A % 100 != 0) {
            System.out.println( 1);
        }
        else if (A % 400 == 0) {
            System.out.println(1);
        }
        else {
            System.out.println (0);
        }
    }
}
