Python Files I/O:

File is a named location on disk to store related information. 

It is used to permanently store data in a non-volatile memory (e.g. hard disk). 

Since, random access memory (RAM) is volatile which loses its data when computer is turned off, we use files for future use of the data.

When we want to read from or write to a file we need to open it first. 

When we are done, it needs to be closed, so that resources that are tied with the file are freed. 

Hence, in Python, a file operation takes place in the following order.

1. Open a file
2. Read or write (perform operation)
3. Close the file

********************************************************************
Opening a File:

Python has a built-in function open() to open a file. 

This function returns a file object, also called a handle, 
as it is used to read or modify the file accordingly.

>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python33/README.txt")  # specifying full path

We can specify the mode while opening a file. 
In mode, we specify whether we want to read 'r', write 'w' or append 'a' to the file. 
We also specify if we want to open the file in text mode or binary mode. The default is reading in text mode. 
In this mode, we get strings when reading from the file. 
On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like image or exe files.

Python File Modes:
------------------
Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not 
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation. If the file already exists, the operation fails.
'a'		Open for appending at the end of the file without truncating it. 
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)


f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode


Since the version 3.x, Python has made a clear distinction between str (text) and bytes (8-bits). 
Unlike other languages, the character 'a' does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings). 
Hence, when working with files in text mode, it is recommended to specify the encoding type. 
Files are stored in bytes in the disk, we need to decode them into str when we read into Python. Similarly, encoding is performed while writing texts to the file.

The default encoding is platform dependent. 
In windows, it is 'cp1252' but 'utf-8' in Linux. 
Hence, we must not rely on the default encoding otherwise, 
our code will behave differently in different platforms. 
Thus, this is the preferred way to open a file for reading in text mode.

f = open("test.txt",mode = 'r',encoding = 'utf-8')
********************************************************************
Closing a File:
---------------

When we are done with operations to the file, we need to properly close it. 
Python has a garbage collector to clean up unreferenced objects. 

But we must not rely on it to close the file. 

Closing a file will free up the resources that were tied with the file and
is done using the close() method.

f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()

Note: This method is not entirely safe. 

# try...finally method:

If an exception occurs when we are performing some operation with the file, 
the code exits without closing the file. 
A safer way is to use a try...finally block.


try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
Note: This way, we are guaranteed that the file is properly closed even if
an exception is raised, causing program flow to stop.

# with statement :
The best way to do this is using the "with" statement. 
This ensures that the file is closed when the block inside with is exited. 
We dont need to explicitly call the close() method. It is done internally.


with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations


Writing to a File:
------------------
In order to write into a file we need to open it in write 'w', append 'a' or exclusive creation 'x' mode. 
We need to be careful with the 'w' mode as it will overwrite into the file if it already exists. 
All previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using write() method. 
This method returns the number of characters written to the file.


with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

Note: This program will create a new file named 'test.txt' if it does not exist. 
If it does exist, it is overwritten. 
We must include the newline characters ourselves to distinguish different lines.
********************************************************************
Reading From a File:
********************
To read the content of a file, we must open the file in reading mode. 
There are various methods available for this purpose. 
We can use the read(size) method to read in size number of data. 
If size parameter is not specified, it reads and returns up to the end of the file.

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''

We can see, that read() method returns newline as '\n'. 
Once the end of file is reached, we get empty string on further reading. 
We can change our current file cursor (position) using the seek() method. 
Similarly, the tell() method returns our current position (in number of bytes).

>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines
********************************************************************
We can read a file line-by-line using a for loop. 
This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines

Note: The lines in file itself has a newline character '\n'.
Moreover,the print() function also appends a newline by default.
Hence, we specify the end parameter to avoid two newlines when printing.
********************************************************************
Alternately, we can use readline() method to read individual lines of a file.
This method reads a file till the newline, including the newline character.

>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''

Lastly, the readlines() method returns a list of remaining lines of the entire file. 
All these reading method return empty values when end of file (EOF) is reached.

>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
********************************************************************
Python File Methods:
********************

There are various methods available with the file object. 
Some of them have been used in above examples. 
Here is the complete list of methods in text mode with a brief description.

Python File Methods:
********************
Method		Description
close()		Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()		Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)		Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()		Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.

******************************************************************

Printing to the Screen:
***********************

The simplest way to produce output is using the print statement where you can pass zero or more expressions separated by commas. 

This function converts the expressions you pass into a string and writes the result to standard output as follows −

#!/usr/bin/python

print "Python is really a great language,", "isn't it?"
This produces the following result on your standard screen −

Python is really a great language, isn't it?
---------------------------------------------------------
Reading Keyboard Input:
***********************

Python provides two built-in functions to read a line of text from standard input, 
which by default comes from the keyboard. 

These functions are :

1. raw_input
2. input

The raw_input Function:
***********************

The raw_input([prompt]) function reads one line from standard input 
and returns it as a string (removing the trailing newline).

#!/usr/bin/python

str = input("Enter your input: ");
print "Received input is : ", str

This prompts you to enter any string and it would display same string on the screen. 
When I typed "Hello Python!", its output is like this −

Enter your input: Hello Python
Received input is :  Hello Python

---------------------------------------------------------
The input Function:
*******************
The input([prompt]) function is equivalent to raw_input, except that it assumes the input is a valid Python expression and returns the evaluated result to you.

#!/usr/bin/python

str = input("Enter your input: ");
print "Received input is : ", str

Output:
Enter your input: [x*5 for x in range(2,10,2)]
Recieved input is :  [10, 20, 30, 40]

---------------------------------------------------------------
Opening and Closing Files:
**************************

Until now, you have been reading and writing to the standard input and output. 
Now, we will see how to use actual data files.

Python provides basic functions and methods necessary to manipulate files by default. 
You can do most of the file manipulation using a file object.

The open Function:
******************

Before you can read or write a file, you have to open it using Python's built-in open() function. 
This function creates a file object, which would be utilized to call other support methods associated with it.

Syntax:
file object = open(file_name [, access_mode][, buffering])

Here are parameter details:
+++++++++++++++++++++++++++

file_name: The file_name argument is a string value that contains the name of the file that you want to access.

access_mode: The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is optional parameter and the default file access mode is read (r).

buffering: If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).

----------------------------------------------------------
The file Object Attributes:
***************************

Once a file is opened and you have one file object, 
you can get various information related to that file.

Here is a list of all attributes related to file object:

Attribute		Description
file.closed		Returns true if file is closed, false otherwise.
file.mode		Returns access mode with which file was opened.
file.name		Returns name of the file.
file.softspace	Returns false if space explicitly required with print, true otherwise.

Example
#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

Output:
Name of the file:  foo.txt
Closed or not :  False
Opening mode :  wb
Softspace flag :  0
---------------------------------------------------
The close() Method:

The close() method of a file object flushes any unwritten information 
and closes the file object, after which no more writing can be done.

Python automatically closes a file when the reference object of a file is reassigned to another file. 
It is a good practice to use the close() method to close a file.

Syntax: fileObject.close();

Example:
#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print "Name of the file: ", fo.name

# Close opend file
fo.close()

Output:
Name of the file:  foo.txt
------------------------------------------------
Reading and Writing Files:
**************************

The file object provides a set of access methods to make our lives easier. 
We would see how to use read() and write() methods to read and write files.

The write() Method:
-------------------

The write() method writes any string to an open file. 
It is important to note that Python strings can have binary data and not just text.

The write() method does not add a newline character ('\n') to the end of the string −

Syntax: fileObject.write(string);
Here, passed parameter is the content to be written into the opened file.

Example
#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

Note: The above method would create foo.txt file and would write given content in that file and finally it would close that file. 

Python is a great language.
Yeah its great!!

----------------------------------------------------------
The read() Method:
******************

The read() method reads a string from an open file. 
It is important to note that Python strings can have binary data. apart from text data.

Syntax : fileObject.read([count]);

Here, passed parameter is the number of bytes to be read from the opened file. This method starts reading from the beginning of the file and if count is missing, then it tries to read as much as possible, maybe until the end of file.

Example:
Let's take a file foo.txt, which we created above.

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()

Output:
Read String is :  Python is

------------------------------------------------------------
File Positions:
***************

The tell() method tells you the current position within the file; in other words, the next read or write will occur at that many bytes from the beginning of the file.

The seek(offset[, from]) method changes the current file position. The offset argument indicates the number of bytes to be moved. The from argument specifies the reference position from where the bytes are to be moved.

If from is set to 0, it means use the beginning of the file as the reference position and 1 means use the current position as the reference position and if it is set to 2 then the end of the file would be taken as the reference position.

Example
Let us take a file foo.txt, which we created above.

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()

Output:
Read String is :  Python is
Current file position :  10
Again read String is :  Python is
-----------------------------------------------
Renaming and Deleting Files:
****************************

Python os module provides methods that help you perform file-processing operations, 
such as renaming and deleting files.

To use this module you need to import it first and then you can call any related functions.

The rename() Method:
********************
The rename() method takes two arguments, the current filename and the new filename.

Syntax: os.rename(current_file_name, new_file_name)

Example:
Following is the example to rename an existing file test1.txt:

#!/usr/bin/python
import os

# Rename a file from test1.txt to test2.txt
os.rename( "test1.txt", "test2.txt" )

The remove() Method:
--------------------
You can use the remove() method to delete files by supplying the name of the file to be deleted as the argument.

Syntax : os.remove(file_name)

Example: 
Following is the example to delete an existing file test2.txt −

#!/usr/bin/python
import os

# Delete file test2.txt
os.remove("text2.txt")
-----------------------------------------------------
Directories in Python:
**********************

All files are contained within various directories, 
and Python has no problem handling these too. 
The os module has several methods that help you create, remove, and change directories.

The mkdir() Method:
-------------------
You can use the mkdir() method of the os module to create directories in the current directory. 
You need to supply an argument to this method which contains the name of the directory to be created.

Syntax : os.mkdir("newdir")

Example:
#!/usr/bin/python
import os

# Create a directory "test"
os.mkdir("test")

-----------------------------------------------------
The chdir() Method:
*******************
You can use the chdir() method to change the current directory. The chdir() method takes an argument, which is the name of the directory that you want to make the current directory.

Syntax: os.chdir("newdir")

Example:
#!/usr/bin/python
import os

# Changing a directory to "/home/newdir"
os.chdir("/home/newdir")

--------------------------------------------------------
The getcwd() Method:
********************

The getcwd() method displays the current working directory.

Syntax: os.getcwd()

Example:
#!/usr/bin/python
import os

# This would give location of the current directory
os.getcwd()
------------------------------------------------------

The rmdir() Method:
*******************
The rmdir() method deletes the directory, which is passed as an argument in the method.

Before removing a directory, all the contents in it should be removed.

Syntax: : os.rmdir('dirname')

Example: 
Following is the example to remove "/tmp/test" directory. 
It is required to give fully qualified name of the directory, 
otherwise it would search for that directory in the current directory.

#!/usr/bin/python
import os

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )

----------------------------------------------------
File & Directory Related Methods:
*********************************

There are three important sources, which provide a wide range of utility methods to handle and manipulate files & directories on Windows and Unix operating systems. 

They are as follows :

File Object Methods: The file object provides functions to manipulate files.

OS Object Methods: This provides methods to process files as well as directories.
-------------------------------------------------------------------
