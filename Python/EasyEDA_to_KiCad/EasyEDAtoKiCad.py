#----------------------------------------------------------------------#
#                    EasyEDA to KiPart Converter                       #
#----------------------------------------------------------------------#

# Author: Monty Perrotti

# This program is used to convert EasyEda part JSON Source files to be used
# with KiPart to convert CSV files to KiCad files.
 
 
import json
from dataclasses import dataclass

@dataclass
class PinPack:
    pinName: str
    pinNumber: str
    electricalType: str
    side: str
    inverted: bool
    clock: bool
    hidden: bool

class EasyEDAtoKiCad:
    filePath = ''
    fileOutputPath = ''

    partName = ''
    footprint = ''
    prefix = ''
    manufacturePartNum = ''
    datasheetLink = ''
    description = ''

    pins = []

    shapeKeys = {
        'R' : 'Rounded Box',
        'P' : 'Pin',
        'E' : 'Circle',
        'T' : 'Text',
        'PL' : 'Line'
    }
    pinTypes = [
        'unspecified',
        'input',
        'output',
        'bidirectional',
        'power_out'
    ]
    sideConversion = {
        0:'right',
        90:'bottom',
        180:'left',
        270:'top'
    }

    def __init__(this, inputPath, outputPath):   # Initializer
        this.filePath = inputPath
        this.fileOutputPath = outputPath


    def run(this):
        print("Opening EasyEDA JSON file!") 
        # Opening JSON file
        f = open(this.filePath)
 
        # returns JSON object as
        # a dictionary
        data = json.load(f)

        # "head": {
        #     "c_para": {
            #     "name": "M.2_E_Card",
            #     "package": "M.2-CARD-E-2222",
            #     "pre": "J?",
            #     "BOM_Manufacturer Part": "NA",
            #     "link": "",
        # },
        # "shape": {}
        this.partName = data['head']['c_para']['name']
        this.footprint = data['head']['c_para']['package']
        this.prefix = data['head']['c_para']['pre']
        this.manufacturePartNum = data['head']['c_para']['BOM_Manufacturer Part']
        this.datasheetLink = data['head']['c_para']['link']

        for i in data['shape']:
            # pinName: str
            # pinNumber: str
            # electricalType: str
            # side: str
            # inverted: bool
            # clock: bool
            # hidden: bool
            parts = i.split('~')
            tempType = ''
            

            if parts[0] == 'P':
                this.pins.append(PinPack(
                    parts[14].replace(' ', '_'),
                    parts[3],
                    this.pinTypes[ int(parts[2]) ],
                    this.sideConversion[ int(parts[6]) ],
                    False if parts[8][:1]=='0' else True,
                    False if parts[28][-1:]=='0' else True,
                    False if parts[1]=='show' else True
                ))
        # print(this.pins)

        # Closing input file
        f.close()

        print("Creating csv file for KiPart!") 
        f = open(this.fileOutputPath, 'w')
        
        # This is the top with all the part information
        topString = this.partName + ',' + this.prefix + ',' + this.footprint + ',' + this.manufacturePartNum + ',' + this.datasheetLink + ',' + this.description
        # print(topString)
        f.write( topString )
        f.write( '\n' )

        # Here we have all of the column titles
        f.write('Pin,Name,Type,Side,Style,Hidden')
        f.write( '\n' )

        # pinName: str
        # pinNumber: str
        # electricalType: str
        # side: str
        # inverted: bool
        # clock: bool
        # hidden: bool  
        
        # Now we go through all of the pins and print them to file
        for pack in this.pins:
            tempType = ''
            if pack.inverted and pack.clock:
                tempType = 'inverted_clock'
            elif pack.clock:
                tempType = 'clock'
            elif pack.inverted:
                tempType = 'inverted'
            concatStr = pack.pinNumber + ',' + pack.pinName + ',' + pack.electricalType + ',' + pack.side + ',' + tempType + ',' + str(pack.hidden)

            f.write( concatStr )
            f.write( '\n' )


# Main entry point
converter = EasyEDAtoKiCad('M.2_E_Card.json', 'output.csv')

converter.run()