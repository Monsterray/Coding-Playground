using System;
using System.IO;

namespace C__tutorial
{
    /// <summary>
    /// MicroStopwatch class
    /// </summary>
    public class MicroStopwatch : System.Diagnostics.Stopwatch
    {
        readonly double _microSecPerTick =
            1000000D / System.Diagnostics.Stopwatch.Frequency;

        public MicroStopwatch()
        {
            if (!System.Diagnostics.Stopwatch.IsHighResolution)
            {
                throw new Exception("On this system the high-resolution " +
                                    "performance counter is not available");
            }
        }

        public long ElapsedMicroseconds
        {
            get
            {
                return (long)(ElapsedTicks * _microSecPerTick);
            }
        }
    }
    public class CSVConverter
    {
        public void convert(string inPath, string outPath){
            String line;
            try
            {
                StreamReader inS = new StreamReader(inPath);
                StreamWriter outS = new StreamWriter(outPath);

                //Read the first line of text
                line = inS.ReadLine();
                //Continue to read until you reach end of file
                while (line != null)
                {
                    line = line.Replace(',', '\t');
                    //Write a line of text
                    outS.WriteLine(line);
                    //Read the next line
                    line = inS.ReadLine();
                }
                //close the file
                inS.Close();
                outS.Close();
            }
            catch(Exception e)
            {
                Console.WriteLine("Exception: " + e.Message);
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MicroStopwatch uWatch = new MicroStopwatch();      // Stopwatch in the us range to time the code
            uWatch.Start();
            // var watch = new System.Diagnostics.Stopwatch(); // Stopwatch in the ms range to time the code
            // watch.Start();

            CSVConverter csc = new CSVConverter();
            csc.convert("defenderParts-Full.csv", "defenderParts-Full.tsv");
            
            uWatch.Stop();
            // watch.Stop();
            Console.WriteLine($"Execution Time: {uWatch.ElapsedMicroseconds} us");
            Console.WriteLine($"CSV Formated:C#(Windows),{uWatch.ElapsedMicroseconds} microseconds");

            Console.Write($"{Environment.NewLine}Press any key to exit...");
            Console.ReadKey(true);
        }
    }
}
