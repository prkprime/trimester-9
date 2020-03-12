//package Assembler_pass_1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Pass1 {
    public static void main(String[] args) throws IOException {
        String[][] optab = {
          {"stop", "IS 00"},
          {"add","IS 01"},
          {"sub","IS 02"},
          {"mul","IS 03"},
          {"mover","IS 04"},
          {"moves","IS 05"},
          {"comp","IS 06"},
          {"bc","IS 07"},
          {"div","IS 08"},
          {"read","IS 09"},
          {"print","IS 10"},
          {"dc","DL 01"},
          {"ds","DL 02"},
          {"start","AD 01"},
          {"end","AD 02"},
          {"origin","AD 03"},
          {"equ","AD 04"},
          {"ltorg","AD 05"}
        };
        String[][] regtab = {
          {"areg", "01"},
          {"breg", "02"},
          {"creg", "03"},
          {"dreg", "04"}
        };
        BufferedReader br = new BufferedReader(new FileReader("../mlp.asm"));
        String thisLine;
        int lineNo = 0;
        while((thisLine = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(thisLine, " ,");
	    int isStart = 0;
            while (st.hasMoreTokens()) {
                String token = st.nextToken();
                for (String[] element : optab) {
                  if (token.toLowerCase().equals(element[0])) {
                    System.out.print(element[1]);
                  }
		}
                for (String[] element : regtab) {
                  if (token.toLowerCase().equals(element[0])) {
                    System.out.print(" "+element[1]);
                  }
                }
            }
	    System.out.print("\n");
        }
    }
}
