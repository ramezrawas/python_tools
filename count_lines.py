def get_count(datei):
    data = open(datei, 'r')
    str = data.read()
    len = str.count('\n') + 1
    data.close()
    return len
