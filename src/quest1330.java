import java.util.Scanner;

public class quest1330 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        // 백준 1330
        // 문제 정수 A, B 첫째줄에 주어진다. A와 B는 공백 한칸으로 구분됨.
        // -10000 <= A,B <= 10000 -> short = -32768~ 32767
        // A와 B를 비교하는 프로그램을 작성할것.
        // 첫째줄에 A > B 면 ">" 출력 or A < B면 "<" 출력 or A = B 면 "=="출력
        short A = myObj.nextShort(); short B = myObj.nextShort();
        if (A > B) {
            System.out.println(">");
        }
        if (A < B) {
            System.out.println("<");
        }
        if (A == B) {
            System.out.println("==");
        }

    }
}
