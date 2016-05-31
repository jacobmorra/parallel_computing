import cgi
import cgitb; cgitb.enable()

print('Content-Type: text/html')
print('')
arguments = cgi.FieldStorage()
for i in arguments.keys():
    print(arguments[i].value)

cgi.test()
cgi.print_environ()
print "Hello"
