def beatlesSearch():
    fin = open("BeatlesSongs.dat")
    searchWord = input("enter the word to search for---> ")
    searchWord = searchWord.lower().strip()
    count = 0
    for line in fin:
        line2 = line.lower()
        if searchWord in line2:
            count += 1
            print(line[7:].rstrip())
    fin.close()
    print(f'Total # of songs: {count}')

def beatlesSearch_2(outputFileName):
    fin = open("BeatlesSongs.dat")
    fout = open(outputFileName, 'w')
    searchWord = input("enter the word to search for---> ")
    searchWord = searchWord.lower().strip()
    count = 0
    for line in fin:
        line2 = line.lower()
        if searchWord in line2:
            count += 1
            print(line[7:].rstrip())
    fin.close()
    fout.write(f'Total # of songs: {count}')
    fout.close()

def beatlesSearch_3(outputFileName = None):
    fin = open("BeatlesSongs.dat")
    if !outputFileName != None
        fout = open(outputFileName, 'w')
    else:
        fout = None
    searchWord = input("enter the word to search for---> ")
    searchWord = searchWord.lower().strip()
    count = 0
    for line in fin:
        line2 = line.lower()
        if searchWord in line2:
            count += 1
            if fout:
                print(line[7:])
            else:
                print(line[7:].rstrip)
    fin.close()
    if fout:
        fout.write(f'Total # of songs: {count}')
        fout.close()
    else:
        fout.write(f'Total # of songs: {count}')
