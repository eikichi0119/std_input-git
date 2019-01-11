import sys

print (sys.version)

if sys.version_info.major >= 3:
    a = input()
    print (a)
    print (type(a))
else:
    a = raw_input()
    print (a)
    print (type (a))

