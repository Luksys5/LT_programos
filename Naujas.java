import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;


public class Delimiter {
    static String sakau = null;
    static String input = null;
    static Scanner sc = null;
    static String[] pilnas = new String[10000];
    static String[] kodas =  new String[10000]; 
    
    public static void main(String[] args) throws   IOException{
            BufferedReader br = new BufferedReader(new FileReader("1seka.txt"));  
            PrintWriter out = new PrintWriter("Baigta.txt");
            
            int i = 0;    
                
                while((input = br.readLine()) != null){
                pilnas[i] = input;
                sc = new Scanner(input);    
                int ivykis = 1;
                sakau = sc.next(); 
                     if(sakau.matches(".*\\d.*"))
                     {                        
                        ivykis=0; 
                        sakau=sc.next();                       
                        kodas[i] = sakau;                       

                     }

                    if(i > 0 && ivykis == 0){                         
                        String naujas = kodas[i];                             
                        for(int j = 1; j <= i ;j++){  
                            String senas = kodas[i-j];
                            if(naujas.equals(senas))
                                kodas[i]= "null" ;                 
                        }   
                     }
                //    if(kodas[i]!= "null")
                  //      out.println(input);
                     if(ivykis==0)
                         i++;
                    
            }
                for(int j =0; j < i ,j++)
                    if(kodas[j] != "null")
                        out.println(pilnas[j]);
                out.close();
    
}

