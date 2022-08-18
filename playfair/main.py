from playfair import playfair_en
from playfair import playfair_de

def post_processing(ans):
    s=""
    for i in range(len(ans)):
        if ans[i]!="x":
            s+=ans[i]
    return s
def switch(N):
        if N==1:
            K=input("Enter the key: ")
            P=input("Enter the Text: ")
            playfair_en.encryption(K, P)
        elif N==2:
            K=input("Enter the Key: ")
            P=input("Enter the CiperText: ")
            ans=playfair_de.decryption(K,P)
            p_ans=post_processing(ans)
            print("with padding: "+ans+"\n")
            print("without padding: "+p_ans+"\n")
        else:
            print("enter an valid option")   
while True:
    print("Enter 1 for encryption")
    print("Enter 2 for decryption")
    print("Enter 3 to stop the program")
    N=int(input("Enter your option: "))
    if N==3:
        print("exiting the program")
        break
    switch(N)
    
    
            
    


