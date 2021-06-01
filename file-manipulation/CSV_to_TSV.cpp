//----------------------------------------------------------------------#
//                  CSV to TSV Converter C++ Edition                    #
//----------------------------------------------------------------------#

// Author: Monty Perrotti


#include <iostream>
#include <fstream>

#include <chrono>   // Just for timing
class CSV_to_TSV{
    public:
        std::string inputFilePath;     // Path to the input file
        std::string outputFilePath;    // Path to the output file

        CSV_to_TSV(std::string inPath, std::string outPath)
            : inputFilePath(inPath), outputFilePath(outPath)
        {
        }

        CSV_to_TSV()    // Default contructor
        {
        }

        ~CSV_to_TSV()   // Default destructor
        {
        }

        /**
            Converts a CSV file to a TSV file
            @param inPath string of the path to the input file
            @param outPath string of the path to the output file
        */
        void convertFiles (std::string inPath, std::string outPath){
            std::ifstream inputFile;     // input CSV file
            std::ofstream outputFile;    // output TSV file

            inputFile.open(inPath, std::ios::in);
            outputFile.open(outPath, std::ios::out);
            if (!inputFile) {
                std::cout << "No such file" << std::endl;
            }
            else {
                if (!outputFile) {
                    std::cout << "File not created!" << std::endl;
                }
                else {
                    std::cout << "File created successfully!" << std::endl;
                }

                // Do replacement character by character
                char ch; // Temporarily holds character of the file
                
                while ( !inputFile.eof() ) {
                	// inputFile >> ch; // This way does not read new lines charachters

                    inputFile.get(ch);  // Trying to use different way to get new lines
                    if ( ch == ',' )
                        ch = '\t';

                    outputFile << ch;
                	// std::cout << ch;
                }

                // Do replacement line by line ( 2X slower then going character by character)
                // std::string line;    // Temporarily holds a file line
                // while (getline(inputFile, line)){
                //     replaceAll(line, ",", "\t");
                //     outputFile << line;
                // }

            }
            inputFile.close();
            outputFile.close();
        }


        /**
            Replaces all ocurances of toSearch to replaceStr in the data string.
            @param data string to be modified
            @param toSearch string to search for inside of data
            @param replaceStr string to replace toSearch inside of data
            @author Shubham Agrawal
        */
        void replaceAll(std::string &data, const std::string &toSearch, const std::string &replaceStr)
        {
            // Get the first occurrence
            size_t pos = data.find(toSearch);
            // Repeat till end is reached
            while( pos != std::string::npos)
            {
                // Replace this occurrence of Sub String
                data.replace(pos, toSearch.size(), replaceStr);
                // Get the next occurrence from the current position
                pos = data.find(toSearch, pos + replaceStr.size());
            }
        }

};

  
int main(int argc, char *argv[])
{
    // "defenderParts-Full.csv" "defenderParts-Full.tsv"
    CSV_to_TSV converter;
    auto t_Start = std::chrono::high_resolution_clock::now();
    converter.convertFiles(argv[1], argv[2]);
    auto t_End = std::chrono::high_resolution_clock::now();

    std::chrono::microseconds duration = std::chrono::duration_cast<std::chrono::microseconds>(t_End - t_Start);

    std::cout << "Took " << duration.count() << " microseconds to run!" << std::endl;
    return 0;   // Exit app with code 0
}
