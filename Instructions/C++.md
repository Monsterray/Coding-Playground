"Visual Studio Code" as VSC



install C/C++ Extension for VSC
install MinGW at https://sourceforge.net/projects/mingw/
add gcc bin to PATH
config VSC using https://code.visualstudio.com/docs/cpp/config-mingw


Notes:
--**Variables Reference**--
A file located at /home/your-username/your-project/folder/file.ext opened in your editor;
The directory /home/your-username/your-project opened as your root workspace.

So you will have the following values for each variable:

    ${workspaceFolder} - /home/your-username/your-project
    ${workspaceFolderBasename} - your-project
    ${file} - /home/your-username/your-project/folder/file.ext
    ${fileWorkspaceFolder} - /home/your-username/your-project
    ${relativeFile} - folder/file.ext
    ${relativeFileDirname} - folder
    ${fileBasename} - file.ext
    ${fileBasenameNoExtension} - file
    ${fileDirname} - /home/your-username/your-project/folder
    ${fileExtname} - .ext
    ${lineNumber} - line number of the cursor
    ${selectedText} - text selected in your code editor
    ${execPath} - location of Code.exe
    ${pathSeparator} - / on macOS or linux, \\ on Windows
