def count_words():
    fin = open("BeatlesSongs.dat")
    d = {}
    for line in fin:
        line = line[7:].lower.strip()
        words = line.split()
        for word in words:
            #d[word] = d.get(word, 0) + 1
            if word not in d:
                d[word] = 1
            else:
                d[word] = d[word] + 1
                #d[word] += 1
    fin.close()
    return d
