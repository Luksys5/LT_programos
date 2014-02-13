
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
            int i = -1;    
            
                while((input = br.readLine()) != null){
                pilnas[i+1] = input;
                sc = new Scanner(input);    
                
                sakau = sc.next(); 
                     if(sakau.matches(".*\\d.*"))
                     {                        
                            i++;
                        sakau=sc.next();                       
                        kodas[i] = sakau;                       

                     }

                if(i>=1){ 
                    int z=i;
                    tikr = kodas[z].toCharArray();
                    int index = 0;                    
                    for(i = z - 1; i > 0;i--){   
                        index = 0;
                        temp = kodas[i].toCharArray();                       
                        for(int j=0; j<tikr.length;j++){                            
                            if(tikr[j]==temp[j])
                                index++;
                        }
                        if(index == tikr.length){
                             kodas[z] = "null";   
                             System.out.println(kodas[z]);
                        }
                    }

                    i=z;
                    
                }
                              
                }
                
                out.close();
    }
}

