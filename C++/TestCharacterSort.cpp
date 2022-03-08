#include <iostream>
#include <fstream>
#include <string>
#include "ctype.h"

using std::cout; using std::ofstream;
using std::endl; using std::string;
using std::cerr;
using std::fstream;

using namespace std;


int main()
{

    string str;

    for (int k = 0; k <= 255; k++)
        //(char)k

        string filename((char)k + ".txt");
        fstream output_fstream;

        output_fstream.open(filename, std::ios_base::out);
        if (!output_fstream.is_open()) {
            cerr << "Failed to open " << filename << '\n';
        } else {
            output_fstream << "Maecenas accumsan purus id \norci gravida pellentesque." << endl;
            cerr << "Done Writing!" << endl;
        }
    }

    return EXIT_SUCCESS;
}
