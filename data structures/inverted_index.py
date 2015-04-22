# Retrieve relative/absolute file path
filepath = raw_input('Please enter filepath to be indexed: ')

try:
    data = open(filepath).read().split('\n')
    index = {}
    # chop by line
    for line in xrange(len(data)):
        # chop by word
        for word in data[line].split():
            if word not in index:
                index[word] = [line]
            else:
                if line not in index[word]:
                    index[word].append(line)

    # print created index
    print 'Index: '

    for word in index:
        print word + ': ' + str(index[word])
except:
    print 'File not found!'
