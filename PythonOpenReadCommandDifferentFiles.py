employeefile = open("employees.txt", "r")
#r stands for read, w = write/new file, a = append =adds info to end of file, r+ = read+write
employeefile.close()
#print(employeefile.readable()) = checks if file is readable
#print(employeefile.read()) =opens file in read mode
#print(employeefile.readline()) =reads line, can be spammed for lines
#print(employeefile.readlines()) creates a []List
#best practice close a file after opening
