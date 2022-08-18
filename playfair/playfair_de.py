import string
from pydoc import plain, plaintext
def decryption(key,plain_text):
    atoz=string.ascii_lowercase.replace("j",".")
    #print(atoz)
    key_mat=["" for i in range(5)]
    i=0
    j=0
    for c in key:
        if c in atoz:
            key_mat[i]+=c 
            
            atoz=atoz.replace(c,".")
            j+=1
        if j>4:
            i+=1
            j=0
    
    for c in atoz:
        if c!=".":
            key_mat[i]+=c
            atoz.replace(c,".")
            j+=1
        if j>4:
            i+=1
            j=0
            
    #print(key_mat)
    
    ciper_text_pair=[]
    i=0
    #pre-processing of plain text according to the rule of playfair
    while i<len(plain_text):
        a=plain_text[i]
        
        b=plain_text[i+1]
        
        ciper_text_pair.append(a+b)
        i+=2
        
    #print(plain_text_pair)
    
    plain_text_pair=[]
    
    for pair in ciper_text_pair:
        applied=False
        #Rule 1
        for row in key_mat:
            if pair[0] in row and pair[1] in row:
                j0=row.find(pair[0])
                j1=row.find(pair[1])
                plaintextpair=row[(j0+4)%5]+row[(j1+4)%5]
                plain_text_pair.append(plaintextpair)
                applied=True
        
        if applied:
            continue
        
        #Rule 2
        for j in range(5):
            col="".join([key_mat[i][j] for i in range(5)])
            if pair[0] in col and pair[1] in col:
                i0=col.find(pair[0])
                i1=col.find(pair[1])
                
                plaintextpair=col[(i0+4)%5]+col[(i1+4)%5]
                plain_text_pair.append(plaintextpair)
                applied=True
        if applied:
            continue
        
        #rule 3
        i0=0 #row
        i1=0
        j0=0 #col
        j1=0
        for i in range(5):
            row=key_mat[i]
            if pair[0] in row:
                i0=i 
                j0=row.find(pair[0])
            
            if pair[1] in row:
                i1=i 
                j1=row.find(pair[1])
        
        plaintextpair=key_mat[i0][j1] +key_mat[i1][j0]
        plain_text_pair.append(plaintextpair)
        
    
    return "".join(plain_text_pair)


    