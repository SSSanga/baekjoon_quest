import java.util.Scanner;

public class quest14681 {
    public static void main(String[] args) {
        // 백준 14681 번
        // 사분면 고르기
        // 1사분면 x, y 둘다 양수(0 < x, 0 < y )
        // 2사분면 x는 음수, y는 양수 (0>x, 0< y)
        // 3사분면 x, y 둘다 음수 (0>x, 0>y)
        // 4사분면 x는 양수, y는 음수 (0<x, 0>y)
        // 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0)
        // 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)
        Scanner mynumber = new Scanner(System.in);
        short x = mynumber.nextShort();        short y = mynumber.nextShort();
        if (0 < x && 0 < y) {
            System.out.println(1);
        } else if (0 > x && 0 < y) {
            System.out.println(2);
        } else if (0 > x && 0 > y) {
            System.out.println(3);
        } else if (0 < x && 0 > y) {
            System.out.println(4);
        }
        System.out.println();
        // return 0 ;
    }
}
