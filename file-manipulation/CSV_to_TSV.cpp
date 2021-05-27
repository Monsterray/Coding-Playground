//----------------------------------------------------------------------#
//                  CSV to TSV Converter C++ Edition                    #
//----------------------------------------------------------------------#

// Author: Monty Perrotti


#include <iostream>
#include <fstream>

std::string inputFilePath("defenderParts-Partial.csv");     // Path to the input file
std::string outputFilePath("defenderParts-Partial.tsv");    // Path to the output file


int main()
{
    std::ifstream inputFile;     // input CSV file
    std::ofstream outputFile;    // output TSV file

    inputFile.open(inputFilePath, std::ios::in);
    outputFile.open(outputFilePath, std::ios::out);
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
        
        while (!inputFile.eof()) {
			inputFile >> ch;

			std::cout << ch;
		}

        // Do replacement line by line
		// std::string line;    // Temporarily holds a file line
		// while (getline(inputFile, line)){
        //     replaceAll(line, ",", "\n");
        // }

	}
    inputFile.close();
    outputFile.close();




    // Output some text to the console
    std::cout << "Hello Console" << std::endl;

    return 0;   // Exit app with code 0
    
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