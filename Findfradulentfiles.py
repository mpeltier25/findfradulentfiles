import os
import os.path
import magic
import shutil
def searchingfiles():
    """In order to run searching files, simply run the .py program, and pick your directory. For example: /home/name/Desktop/test folder. Once the program is running, it will search whatever directory you choose for the appropriate files with various extensions, such as .txt files and more. then specify the folder that you wish to output to and the folder you wish to read."""
    directory=input("Enter the directory you wish to search ex. /home/name/Desktop/test folder\n")
    badfolderfile=input("Please specify a directory in which you want files that do not namech to be stored in: ex. badfilefolder (Please note, if you specify a directory in which python 3 does not have the appropriate permissions, this will not work!)\n")
    #Create the folder if you need to
    if os.path.exists(badfolderfile):
        shutil.rmtree(badfolderfile)
        os.makedirs(badfolderfile)
    else:
        os.makedirs(badfolderfile)
#search the directories and subdirectories
    for currentdir, alldirs, allfiles in os.walk(directory):
        for filename in allfiles:
#Now, look for each filetype using magic.
            if filename.endswith(".gif"):
                if (b'GIF')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a GIF\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".jpg"):
                if (b'JPEG')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a JPEG\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".docx"):
                if (b'Zip archive data, at least v2.0 to extract')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a docx\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".pdf"):
                if (b'PDF')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a pdf\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".zip"):
                if (b'Zip archive data')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a zip\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".apple"):
                if (b'AppleDouble')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a apple\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".txt"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a txt\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".png"):
                if (b'PNG')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a png\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".jpeg"):
                if (b'JPEG')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a JPEG\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".doc"):
                if (b'Composite Document')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a doc\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xlsx"):
                if (b'Zip archive data, at least v2.0 to extract')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xlsx\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".py"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a py\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".sql"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a sql\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".sqllite"):
                if (b'sql')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a sqllite\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".mp3"):
                if (b'MPEG')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a mp3\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".bz2"):
                if (b'bz2')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a bz2\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".tgz"):
                if (b'tgz')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a tgz\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".jar"):
                if (b'Zip archive data')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a jar\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".tar"):
                if (b'POSIX tar archive')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a tar\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".exe"):
                if (b'executable')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a exe\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".deb"):
                if (b'Debian')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a deb\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".odp"):
                if (b'OpenDocument Presentation')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a odp\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".pptx"):
                if (b'Zip archive data, at least v2.0 to extract')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a pptx\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".ppt"):
                if (b'Composite Document')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a ppt\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".odt"):
                if (b'OpenDocument Text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a odt\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".odg"):
                if (b'odg')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a odg\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".ods"):
                if (b'OpenDocument Spreadsheet')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a ods\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".l"):
                if (b'l')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a l\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".pch"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a pch\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".m"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a m\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".pbxproj"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a pbxproj\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xcworkspacedata"):
                if (b'XML')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xcworkspacedata\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xcuserstate"):
                if (b'Apple binary property list')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xcuserstate\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xscheme"):
                if (b'xscheme')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xscheme\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".plist"):
                if (b'XML document text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a plist\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xml"):
                if (b'XML')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xml\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".java"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a java\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".blarg"):
                if (b'blarg')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a blarg\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".ap_"):
                if (b'ap')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a ap_\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".dex"):
                if (b'dex')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a dex\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".cache"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a cache\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".class"):
                if (b'class')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a class\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".h"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a h\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".strings"):
                if (b'ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a strings\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xib"):
                if (b'XML document text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xib\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".xschscheme"):
                if (b'xschscheme')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a xscscheme\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".HTML"):
                if (b'HTML')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a HTML\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".sb"):
                if (b'data')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a sb\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".bmp"):
                if (b'bitmap')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a bitmap\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".wav"):
                if (b'WAVE')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a wav\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".db"):
                if (b'data')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a db\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".sprite"):
                if (b'data')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a sprite\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            if filename.endswith(".c"):
                if (b'C source, ASCII text')not in magic.from_file(os.path.join(currentdir,filename)):
                    print ("This is not a c\n", magic.from_file(os.path.join(currentdir,filename)))
                    src_file = os.path.join(currentdir, filename)
                    shutil.copy2(src_file, badfolderfile)
            
searchingfiles()
