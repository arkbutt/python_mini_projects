import sys

def wordcount(paragraph):
    bow = paragraph.split()
    return bow

    
tempo=""
def acronym(name):
    acro = ""
    words=wordcount(name)
    #['Ayub' , 'Tahir' , 'germany']
    for i in range(len(words)):
        #temp=Ayub
        #temp=Tahir
        #temp=germany
        temp=words[i]
        #acro=A
        #acro=AT
        #acro=ATg
        acro += temp[0]
    return acro.upper()
    #acro=ATG

if (len(sys.argv)>1 ):
    print(acronym(sys.argv[1]))
else:
    x= raw_input()
    print(acronym(x))