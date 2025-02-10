string1=input("Enter first string: ")
string2=input("Enter second string: ")
string3=string1+string2                 #combine the two strings
string4=["F","L","A","M","E","S"]
#unique_char=set(string3)
#print(unique_char)
s1={}
for c in string3:
    if c in s1:
        s1[c]+=1
    else:
        s1[c]=1
print(s1)                               #Adding each character into set
unduplicate=0
for c in s1:
    if s1[c]==1:
        unduplicate+=1
print(unduplicate)                      #Count the number of unduplicated charcters in the string1 and string2
index=0
while len(string4)>1:                   #check for the relationship
    index=(index+unduplicate-1)%len(string4)
    string4.pop(index)
    #print(string4)
print(string4)                          #print the relationship