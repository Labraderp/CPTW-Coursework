#linux has dictionaries in /usr/share/dict :D Thank you Google!

def generate_list():
    with open('/usr/share/dict/american-english', 'r') as english_dict:
        word_list = []

        line  = english_dict.readline()
        
        while line != '':           #go until EoF
            line = line[:-1]        #remove \n
            if not(line.isalpha()): #check for 's
                line = line[:-2]    #remove 's if true
            word_list.append(line)  #append word to word list
            line = english_dict.readline()  #read next line
    
    return word_list

def find_longest_substring(word, dictionary, pos=0, max=0):
    while current < len(word):
        current = pos
        if word[pos:current] in dictionary:
            len(word[pos:current])