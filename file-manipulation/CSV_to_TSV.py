#----------------------------------------------------------------------#
#                  Multi-Core CSV to TSV Converter                     #
#----------------------------------------------------------------------#

# Author: Monty Perrotti

# In this program there will be use of as many cores as possible to
# convert Comma Seperated Value files to Tab Seperated Value files.

from time import perf_counter

class csv_tsv:
    input_path = ""
    output_path = ""


    def __init__(this, in_path, out_path):
        this.input_path = in_path
        this.output_path = out_path


    def run(this):
        print("Opening input file!") 
        file_csv = open(this.input_path, "rt")

        try:    # Check to see if file exists
            print("Creating output file in text mode!") 
            file_tsv = open(this.output_path, "xt")
        except:
            print("File exists! Opening output file in text write mode!") 
            file_tsv = open(this.output_path, "wt")

        for l in file_csv:
            # print(l)  # Debug
            l = l.replace(',', '\t')
            file_tsv.write(l)

        # Clean up memory
        file_csv.close()
        file_tsv.close()

tStart = perf_counter() # Used to time this program

converter = csv_tsv("defenderParts-Full.csv", "defenderParts-full.tsv")
converter.run()
tEnd = perf_counter()
execution_time = (tEnd - tStart)
print(f'Took {execution_time} seconds to run!')