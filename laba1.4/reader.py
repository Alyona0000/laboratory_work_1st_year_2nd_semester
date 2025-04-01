def read(filename):
    file = open(filename, "r")
    #content = file.read()
    lines = file.readlines() 
    file.close()
    return lines