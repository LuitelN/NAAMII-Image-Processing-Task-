#File Objects 

# While opening a file we can specify whether we are opening the file for 'reading', 'writing', 'reading & writing' or 'appending'
# If we don't specify anything, it defaults to 'reading'
# f = open('text.txt', 'w')  # Opens a file for writing
# f = open('text.txt', 'r+')  # Opens a file for reading & writing
# f = open('text.txt', 'a')  # Opens a file for appending
# Opens a file for reading

f = open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r')


print(f.name)  # Returns the name of the open file
print(f.closed)  # Returns whether the file associated with the variable is closed
print(f.mode)  # Returns the mode in which it was opened i.e. 'r', 'w', 'r+', 'a'


# All files opened using an open() command need to be closed explicitly after their use is complete. If this is not done , we can end up with leaks that cause us to run over the maximum allowed file descriptors on the system and our app can throw an error.
f.close()

# We can avoid this problem with a context manager as below

# The below 'with open()' command will close the file as soon as the code has finished running or an error is thrown
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:

    # Code goes here
    pass

# This produces the error "ValueError: I/O operation on closed file.""
# print(f.read())


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    # This just reads all lines in the file
    text_file_contents = text_file.read()
    print(text_file_contents)



with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    # This returns a list that contains all lines in the file
    text_file_contents = text_file.readlines()
    print(text_file_contents)


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    # This returns a line of text (not a list) at a time
    # The first time we print .readline() it returns the first line
    text_file_contents = text_file.readline()
    print(text_file_contents)
    # The second time we print .readline() it returns the second line
    text_file_contents = text_file.readline()
    print(text_file_contents)



with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    # This returns a line of text (not a list) at a time
    # The first time we print .readline() it returns the first line
    # Putting an 'end = '' in the return or print statement removes the newline between each result
    text_file_contents = text_file.readline()
    print(text_file_contents, end='')
    # The second time we print .readline() it returns the second line
    # Putting an 'end = '' in the return or print statement removes the newline between each result
    text_file_contents = text_file.readline()
    print(text_file_contents, end='')


# The above methods take a lot of storage as lines get stored in memory
# Iterating over lines in a file avoid this
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    for line in text_file:
        print(line, end='')


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    # Passing a number to the .read() command preads just that number of characters
    # The first time this is run, a 10 characters will be read and printed
    text_file_contents = text_file.read(10)
    print(text_file_contents, end='')  # It returns '#1) This is'
    # The second time this is run, the next 10 characters will be read and printed
    text_file_contents = text_file.read(10)
    print(text_file_contents, end='')  # '1) This is a test fi'
    # The same line is extended (without introducing a new line or a new returned value)
    # When we reach the end of the file, read just reads what is left and returns an empty string for the rest of it
    text_file_contents = text_file.read(1000)
    print(text_file_contents, end='')

# The below code will print out the entire code

with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    size_to_read = 10
    text_file_contents = text_file.read(size_to_read)
    while len(text_file_contents) > 0:
        print(text_file_contents, end='')
        text_file_contents = text_file.read(size_to_read)


#
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    size_to_read = 10
    text_file_contents = text_file.read(size_to_read)
    while len(text_file_contents) > 0:
        # The '#' symbol in the output marks the chunks that were printed in each iteration
        print(text_file_contents, end='#')
        text_file_contents = text_file.read(size_to_read)


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    size_to_read = 10
    text_file_contents = text_file.read(size_to_read)
    # The 'filename.tell()' returns the position of the file till where we've read until now
    # This returns 10, since we've read 10 characters
    print(text_file.tell())
    text_file_contents = text_file.read(size_to_read)
    # This returns 20, since we've read 10 more characters (10+10=20)
    print(text_file.tell())


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    size_to_read = 10
    # Reads the first 10 characters. Read position set to 10
    text_file_contents = text_file.read(size_to_read)
    print(text_file.tell())  # Prints 10

    # Reads the next 10 characters. Read position set to 10+10=20
    text_file_contents = text_file.read(size_to_read)
    print(text_file.tell())  # Prints 20

    # filename.seek() sets the read position to whatever character we set it to. Here set to 0.
    text_file.seek(0)  # Sets the read position to 0
    print(text_file.tell())  # Prints 0

    # Reads the first 10 characters. Read position set to 10
    text_file_contents = text_file.read(size_to_read)
    print(text_file.tell())  # Prints 10
    

# If we try to write to a file that is opened for reading. An error is produced.
# Error = 'io.UnsupportedOperation: not writable'
# with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
#     text_file.write('Test')

# If a file with this name doesn't already exist. It will be created.
# If a file does exist, it will be overwritten
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text2.txt', 'w') as text_file:
    text_file.write('Test')



# If you don't want to overwrite a file, use an 'append' setting by passing a lowercase a
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text2.txt', 'a') as text_file:
    text_file.write('Test')


with open('C:/#Personal/Coding Projects/Proj1/Py edn/text2.txt', 'w') as text_file:
    text_file.write('Test')  # File contains: 'Test'
    # filename.seek(position) sets the write position to the number we pass in
    text_file.seek(0)
    # If we now write something. It will be written from the newly set position.
    # It will overwrite anything in its path for as many characters it need to overwrite
    text_file.write('LN')  # File contains: 'LNst'.
    # The first 2 characters from position 0 were overwritten because it was required



# Copying from one file to another, line by line
# This can't be done for image files. It shows an error. Invalid start byte. Copying an image file would require opening it in binary mode. We would be reading/writing bytes instead of text.
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'w') as copy_file:
        for line in text_file:
            copy_file.write(line)


# To read binary we change open(filename,'r') to open(filename, 'rb')
# To read binary we change open(filename,'w') to open(filename, 'wb')
# The below code with these changes, can copy an image file
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'rb') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'wb') as copy_file:
        for line in text_file:
            copy_file.write(line)



# Copying a file using chunks instead of line by line is better. This can be done by using the .read function we've studied above
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'w') as copy_file:
        chunk_size = 10
        chunk = text_file.read(chunk_size)
        while len(chunk) > 0:
            copy_file.write(chunk)
            chunk = text_file.read(chunk_size)

