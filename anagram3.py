def anagram(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    for i in xrange(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] += 1
    for i in xrange(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] += 1
    if cmp(c1,c2)==0:
        return True
    else:
        return False

s1= raw_input()

s2 = raw_input()

print 'yes' if anagram(s1,s2) else 'No'

