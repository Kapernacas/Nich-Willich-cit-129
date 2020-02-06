# Nicholas Willich py2sp20 1-31-20
#icon project
raw = '0101001010101010101000110101010110100100101001001101011001101011010100101011011111011101000010111010'



print ('Enter name of file \n')
file=input(str())
open('file', 'w')
print('Enter Active character for icon')


variable = input(str())

'''
The conv function converts the binary into the
characters that will be displaying for the icon
'''
def conv(raw):
    con = ''
    for item in raw:
        if item == '0':
            con = con + ' '
        else:
            con = con + variable
    return (con)


'''
this function will split a 100 length string into a list of 10 strings
'''
def split(r):
    n=0
    clean = []
    while n<10:
        fin = r[0+n*10:10+n*10]
        clean.append(fin)
        n = n+1
    return(clean)
    
'''    
this function displays the list in a ten by ten grid
'''
def disp(clean):
    m=0
    while m<10:
        print (clean[m])
        m = m+1

disp(split(conv(raw)))