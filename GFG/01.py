arr="aabbcdde"
dictionary={}
for ch in arr:
    #dict[ch]=dict.get(ch,0)+1
    if ch in dictionary:
        dictionary[ch]+=1
    else:
        dictionary[ch]=1

found=False    
for k,v in dictionary.items():
    if v==1:
        found=True
        break
print(k,v)
print(found)