# Procedurę dopisującą przekazany ciąg znaków jako nową linijkę do pliku 
'''
read string
add to file
'''
def write_line(file_path):
    text = input('Write : ')
    f = open(file_path,"a")
    f.readline
    f.write("\n" + text)
    f.close

write_line('test.txt')