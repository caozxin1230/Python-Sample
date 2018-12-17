from sys import argv
#open file by using argument
script, filename = argv

txt= open(filename)

print "Here's your file %r: " %filename
print txt.read()

#open file by using raw_input()
print "Type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()
