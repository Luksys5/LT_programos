import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;


public class Delimiter {
    static String sakau = null;
    static String input = null;
    static char[] temp = new char[10];
    static Scanner sc = null;
    static String[] pilnas = new String;
    static String[] kodas = new String;
    
    public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new FileReader("1seka.txt"));
            PrintWriter out = new PrintWriter("Baigta.txt");
            int i = 0;
                
                while((input = br.readLine()) != null){
                pilnas[i] = input;
                sc = new Scanner(input);
                int ivykis = 1;
                String nenaudingas = null;
                sakau = sc.next();
                     if(sakau.matches(".*\\d.*"))
                     {
                        ivykis=0;
                        sakau=sc.next();
                        temp = sakau.toCharArray();
                        
                        for(int j=0 ;j < temp.length;j++)
                            if(temp[j] == '-')
                                temp[j]= '_' ;
                        nenaudingas = new String(temp);
                                              
                     }
                    out.println(nenaudingas);

    
                } out.close();
      }
}
