# HelloWorld python script for the scripting framework

def HelloWorldPython( ):
    """Prints the string 'Hello World(in Python)' into the current document"""
    #get the doc from the scripting context which is made available to all scripts
    model = XSCRIPTCONTEXT.getDocument()
    #get the XText interface
    text = model.Text
    #create an XTextCursor
    cursor = text.createTextCursor()
    #and insert the string
    text.insertString( cursor, "this is the uno pkg python script", 0 )
    return None


g_exportedScripts = HelloWorldPython,


# --- faked component, dummy to allow registration with unopkg, no functionality expected
import unohelper
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation( None, "org.openoffice.script.DummyImplementationForPythonScripts", \
    ("org.openoffice.script.DummyServiceForPythonScripts",),)

