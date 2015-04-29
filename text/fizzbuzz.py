if __name__ == '__main__':
    for x in xrange(101):
        q = ''
        if x % 3 == 0:
            q += 'Fizz'
        if x % 5 == 0:
            q += 'Buzz'

        print q if q else x
