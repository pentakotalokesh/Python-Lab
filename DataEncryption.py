plaintext=input("Enter one-word ,Lower case Message:")
distance=int(input("Enter Distance:"))
for ch in plaintext:
    ciphervalue=ord(ch)+distance
    if ciphervalue > ord('z'):
        ciphervalue=ord('a')+distance-1
print(chr(ciphervalue))
"""
ASCII values      97 98 99 100 101 
Plaintext         a  b   c  d   e
distance 3
Cipher text       d   e   f  g   h
ASCII values     100 101 102 103 104
"""