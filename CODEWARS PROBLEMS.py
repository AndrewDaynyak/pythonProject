str1="I really hope it works this time"
str2=str1.split()
should_be_reversed=[]
for i, b in enumerate(str2):
    if i!=0 and i%2!=0:
       str2[i]=str2[i][::-1]
result=''
for word in str2:
    result+=word+" "
print(result)








