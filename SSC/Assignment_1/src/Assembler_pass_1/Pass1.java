package Assembler_pass_1;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Pass1 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("../mlp.asm"));
        String thisLine;
        int lineNo = 0;
        while((thisLine = br.readLine()) != null) {
            System.out.print("line no "+ ++lineNo + ": - ");
            StringTokenizer st = new StringTokenizer(thisLine, " ,");
            while (st.hasMoreTokens()) {
                System.out.print (" "+st.nextToken());
            }
            System.out.print("\n");
        }
    }
}
