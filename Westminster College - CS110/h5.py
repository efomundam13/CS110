#Name: Manny Fomundam
#Date: February 19, 2023
#Professor: John Bonomo

#Problem 1a
#Write code which takes a string fname representing a file name and adds
#the suffix ’.txt’ to the end of it if it does not already end with that suffix

#def add_suffix(fname):
    #if(fname.endswith('.txt'):
       #print('FileName is already .txt')
    #else:
        #fname += '.txt'
    #return fname

#Problem 1b
#Write code that strips off a suffix from fname and replaces it with ’.txt. We define a
#suffix as a substring of 3 to 5 characters starting with a ’.’ found at the end of a string.
#If fname has no such suffix you should just add ’.txt’ to the end of it.

#def suffix_change(fname):
    #if(fname.endswith('.txt') == False):
        #fname = fname[:-4]
        #fname += '.txt'
    #else:
        #print('FileName is already .txt')
        #return fname
    #return fname
  
#Problem 2
#In class we wrote a function that searched for words in titles of Beatles’ songs.
#Unfortunately it would match a search string like ’me’ with words like ’time’ and ’mean’
#and ’something’. Modify this code so that it searches for the exact word. We’ll define an
#exact word match for a string s as satisfying two criteria
    #(a) It either starts the beginning of a line or is preceded by a non-alphabetic character
    #(b) It either ends a line or is followed by a non-alphabetic character

def beatlesSearch():
    fin = open("BeatlesSongs.dat")
    searchWord = input("enter the word to search for---> ")
    searchWord = searchWord.lower().strip()
    for line in fin:
        line = line[7:].rstrip()
        if exact_match(line, searchWord) == True:
            print(line)
    fin.close()

def exact_match(line, s):
    #If line starst or end with a specific word
    if line.startswith(s) or line.endswith(s):
        return True
    #If word in line is preceded by a non-alphabetic characte
        if (line.find(' ' + s) != -1 or not line[line.find(' ' + s) - 1].isalpha()):
            return True
        #If word in line is allowed by a non-alphabetic character
            if(line.find(s + ' ') != -1 and not line[line.find(s + ' ') + len(s)].isalpha()):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#Problem 3
#Write a function is_word_ladder(fname) which opens up the text file fname and checks
#if it contains a word ladder. A word ladder is a series of words where each word differs
#from the previous by one letter.
def is_word_ladder(fname):
  try:
    with open(fname, 'r') as f:
      lines = f.readlines()
      if len(lines) > 1:
          #for the range of the length of the words
        for i in range(len(lines)-1):
            #if the letters of one specific place are equal, the words are the same
          if len(lines[i]) == len(lines[i+1]):
            diff_count = 0
            for j in range(len(lines[i])):
                #if the letters of one specific place are not equal, the words are not the same
              if lines[i][j] != lines[i+1][j]:
                diff_count += 1
            if diff_count != 1:
              return False
            #return true if word ladder eists
        return True
      else:
        return False
    #If file isn 't found then return false
  except FileNotFoundError:
    return False
