

def RLE(data):
    enc = ''
    prev_char = ''
    count = 1

    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                enc += str(count) + prev_char
            count = 1
            prev_char = char
        else: count += 1
    else:
        enc += str(count) + prev_char
        return enc

def UNRLE(data): 
    unrle = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            unrle += char * int(count) 
            count = '' 
    return unrle


ex1 = open("Python_5_3_1.txt", "r")
str1 = ex1.read()
ex1.close()

str2=RLE(str1)

file1 = open("Python_5_3_2.txt", "w")
file1.write(str2)
file1.close()

file2 = open("Python_5_3_2.txt", "r")
str3 = file2.read()
file2.close()

str4=UNRLE(str3)

file3 = open("Python_5_3_3.txt", "w")
file3.write(str4)
file3.close()