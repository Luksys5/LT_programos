
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Delimiter {
    static String sakau = null;
    static String[] newput = new String[2];
    public static void main(String[] args) throws   IOException{
            Scanner sc = new Scanner(new FileReader("labas.txt"));
            sc.useDelimiter("kuo");

                System.out.println(sc.next());
                sakau = sc.next();
                
                newput = sakau.split("\\s+\\d+");

                System.out.println(newput[1]);
          
    }
    
}
