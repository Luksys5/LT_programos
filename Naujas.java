import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;


public class Delimiter {
    static String sakau = null;
    static String input = null;
    static Scanner sc = null;
    static char[] tikr = new char[5];
    static char[] temp = new char[5];
    static String[] pilnas = new String[1000];
    static String[] kodas =  new String[1000]; 
    
    public static void main(String[] args) throws   IOException{
            BufferedReader br = new BufferedReader(new FileReader("labas.txt"));  
            PrintWriter out = new PrintWriter("Baigta.txt");
            
        //   while((input = br.readLine()) != null){  
            int i = 0;    
            
                while((input = br.readLine()) != null){
                pilnas[i] = input;
                sc = new Scanner(input);    
                
                sakau = sc.next(); 
                     if(sakau.matches(".*\\d.*"))
                     {                        
                         
                        sakau=sc.next();                       
                        kodas[i] = sakau;                       

                     }

                 int index = 0; 
                     if(i>0){ 
                        tikr = kodas[i].toCharArray();                     
                        for(int j = 1; j <= i ;j++){  
                            index = 0;
                                temp = kodas[i-j].toCharArray();
                                System.out.println("i:"+i+"sk="+tikr.length);
                            for(int sk = 0; sk < tikr.length;sk++){
                                if(tikr[sk] == temp[sk])
                                    index++;}
                            if(index == tikr.length)
                                kodas[i] = "null";
                        }
                        }
                   //  for(int j = 0; j < i;j++)
                    //%     System.out.println(kodas[j]);
                     if(ivykis==0)
                         i++;
    }
}

