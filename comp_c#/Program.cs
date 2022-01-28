// See https://aka.ms/new-console-template for more information
using System;
using shavendra;

namespace  shavendra
{
    public class SimpleTest{

        public SimpleTest()
        {
            this.simplemethod();
        }

        private void simplemethod()
        {            
            Console.WriteLine("working"); 
        }
    }   
}



class Program{
    public static void Main(string[] args){
        var s = new SimpleTest();
      
        // Console.WriteLine(s.First_name);
    }
}
