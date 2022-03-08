#----------------------------------------------------------------------#
#                         MX Device Changer                            #
#----------------------------------------------------------------------#
# Version: 1.8

# Author: Monty Perrotti

# Program used to quickly change GUI skin in MESARE.

from time import perf_counter
import os
import fileinput
import sys

class MXDeviceChanger:
    pickedDevice = 0
    deviceNames = ''


    def __init__(this, choice, names):
        this.pickedDevice = choice -1
        this.deviceNames = names


    def run(this):
        print("Opening API server config file!")
        configFile = 'C:/MES/Server/MobileExperienceApiServer.exe.Config'

        for line in fileinput.input(configFile, inplace=1):
            if line.__contains__('DeviceAssemblyFileName'):
                line = '    <add key="DeviceAssemblyFileName" value="./plugins/' + this.deviceNames[this.pickedDevice] + '"/>\n'

            #     <add key="regulated_battery_voltage" value="4.8"/>
            if line.__contains__('regulated_battery_voltage'):
                if this.deviceNames[this.pickedDevice].__contains__('iPHONE_12'):
                    line = '    <add key="regulated_battery_voltage" value="4.8"/>\n'   # Higher is lower voltage
                else:
                    line = '    <add key="regulated_battery_voltage" value="4.15"/>\n'

            
            sys.stdout.write(line)



        # for l in configFile:
        #     # print(l)  # Debug
        #     if l.__contains__('plugins/MX.Device.'):
        #         l = '    <add key="DeviceAssemblyFileName" value="./plugins/MX.Device.' + this.deviceNames[this.pickedDevice] + '"/>'
        #         configFile.write(l)
        #         break
        
        print("Opening MESARE config file!") 
        configFile = 'C:/MES/MESARE/MESARE.exe.Config'

        for line in fileinput.input(configFile, inplace=1):
            if line.__contains__('DeviceAssemblyFileName'):
                line = '    <add key="DeviceAssemblyFileName" value="./plugins/' + this.deviceNames[this.pickedDevice] + '"/>\n'
            
            sys.stdout.write(line)
        

# Grab available .dll skins from plugins
path = 'C:/MES/Server/plugins'

files = os.listdir(path)
i = 1

for fName in files:
    if fName.__contains__('config'):
        # print(f'Removing {fName}')
        files.remove(fName)


for fName in files:
    print(f'{i}: {fName}')
    i += 1

choice = input("Pick a device: ")


tStart = perf_counter() # Used to time this program

converter = MXDeviceChanger( int(choice), files)
converter.run()
tEnd = perf_counter()
execution_time = (tEnd - tStart)

print('~~~~~  Completed without errors!  ~~~~~\n')

print('Modified MESARE.exe.Config and MobileExperienceApiServer.exe.Config')
print(f'Changed MX Device to {files[choice-1]}\n')

print(f'Which took {execution_time} seconds to run!')
