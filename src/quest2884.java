import java.util.Scanner;
public class quest2884 {
    public static void main(String[] args) {
        //45분 일찍 알람 설정하기 -> 원래 설정되어있는 알람을 45분 일찍 설정하기 
        //입력 : 첫째 줄 = H, M 주어짐. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)
        //상근이가 설정한 시간 = H시 분
        //24시간 표현-하루 시작 0:0 (자정), 하루 끝 (23:59)(다음날 자정1분전)
        //만약 입력을 H10시 M10분입력하면 출력된 시간은 H9시 M25분
        //H= H -1 or H=0일땐 H+23, M = (M-45)+60 
        Scanner mytime= new Scanner (System.in);
        int myalarm = mytime.nextInt ();
        //return 0 ;

    }
}
