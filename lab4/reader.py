def read(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content