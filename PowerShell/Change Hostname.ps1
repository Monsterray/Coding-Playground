# Yesterday I faced a problem in which I needed to change the computer name using PowerShell. First I was looking for some cmdlet which can do this job for me but there is not any inbuilt cmdlet for it.
# Then I searched and finally find a way by which I can do this within the PowerShell. This method is using WMI to do the task.

Get-WmiObject Win32_ComputerSystem
# We are using Get-WMI to give us  all the value of Win32_ComputerSystem.
# You can see in the Output that the "Name value contain our Computer name "WINANAL-088y8gx" with mach with our above screenshot.



$computerName = Get-WmiObject Win32_ComputerSystem
# We are putting the command in to the $computerName variable.  And you can see that the output of $computerName is the same and above screenshot in which we run the command alone.



$name = Read-Host -Prompt "Please Enter the ComputerName you want to use."
# And if you want a GUI box to to open a Pop-UP to insert computer Name try this
# [System.Reflection.Assembly]::LoadWithPartialName('Microsoft.VisualBasic') | Out-Null
# $name = [Microsoft.VisualBasic.Interaction]::InputBox("Enter Desired Computer Name ")
# $name 
# In $name variables we are using Read-Host cmdlet with -Prompt argument with asking users to provide a computer name to be use.

# Whatever user provide to Read-Host, the value is stored in the  $name variable. In First example in below screenshot we didn't provide anything to Read-Host and you can see that output of $name is blank. In next example we provide "Test-Laptop" to Read-Host and you can see that now $name contains the value of "Test-Laptop"



$computername.Rename($name)
# The Win32_ComputerSystem WMI class contain the method of .Rename() in which we need to provide a desired computer name in brackets.

# Now check if you computer name get changed or not.
# Yes, it is changed..  now reboot your computer using  restart-Computer 

