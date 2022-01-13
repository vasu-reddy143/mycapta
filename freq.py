word="Mississippi"
freq={}
for i in word:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
for i in freq:
    print(f"{i}:{freq[i]}")
