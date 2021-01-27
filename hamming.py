def hamming(s1, s2):
    #assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))
    
      
x = "1010"
y = "1111"

print(hamming(x, y))