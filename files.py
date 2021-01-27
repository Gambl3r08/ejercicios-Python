# Open a file in read/write mode
fo = open("abc.txt", "r+")
print ("Nombre del archivo: ", fo.name)

str = "This is 6th line"
# Write a line at the end of the file.
fo.seek(0, 2)
line = fo.write( str )

# Now read complete file from beginning.
fo.seek(0,0)
print(fo.read())
# Close opened file
fo.close()

if fo.closed:
    print("El archivo se ha cerrado correctamente")

else:
    print("El archivo sigue abierto")