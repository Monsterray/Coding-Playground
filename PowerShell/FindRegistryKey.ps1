######################################################################
##
## Search-RegistryKeyValues.ps1
## Search the registry keys from the current location and down for a
## given key value.
##
######################################################################
param([string] $searchText = $(throw "Please specify text to search for."))

gci . -rec -ea SilentlyContinue | 
   % { 
      if((get-itemproperty -Path $_.PsPath) -match $searchText)
      { 
         $_.PsPath
      } 
   } 