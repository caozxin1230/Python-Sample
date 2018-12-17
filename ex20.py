from sys import argv

script, input_file=argv # script and input_file are the arguments here

def print_all(f):
    print f.read()      #read the all file here

def rewind(f):
    f.seek(0)      # A seek() operation moves that pointer to some other
#part of the file so you can read or write at that place.

def print_a_line(line_count,f):
    print line_count, f.readline() # readline() reads each line

current_file=open(input_file)   #open the input file

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)   #goes back the the oth byte

print "Let's print three lines: "

current_line=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)

current_line+=1
print_a_line(current_line,current_file)
