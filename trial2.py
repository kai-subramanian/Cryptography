import random
#this is the code to demonstrate elliptic curve cryptography.
#it has been coded out as a hybrid with diffie hellman 
plaintext = input("Enter plaintext\n")
if(len(plaintext)%2!=0):
        plaintext=plaintext+' '
#the ord() function is used to convert to ASCII
numbers = [ord(letter) for letter in plaintext] 
pairs=[plaintext[i:i+2] for i in range (0,len(plaintext),2)]
print("Letter pairs:")
print(pairs)
arr = list()
for i in range(0,len(numbers)-1,2):
    arr.insert(i,[numbers[i],numbers[i+1]])
print("ASCII value pairs")
print(arr)
pair = list()
for i in range (0,len(arr)):
        pair.insert(i,int(str(arr[i][0])+str(arr[i][1])))
print("Concatenated Values")
print(pair)

#some diffie-hellman stuff

print("Enter the value of n")
n=int(input())
#the curve is a weierstrass equation, of the form y^2=x^3+ax+b, where a,b are curve parameters
print("Enter the curve parameter a")
a=int(input())
print("Enter the curve parameter b")
b=int(input())
#now, lets parse the polynomial using 2 2d lists - lhs and rhs for left hand side and right hand side of the equation
lhs=[[]]
rhs=[[]]
lhs.append([])
rhs.append([])
for i in range(0,n):
    lhs[0].append(i)
    rhs[0].append(i)
    lhs[1].append((i**3+a*i+b)%n)
    rhs[1].append((i**2)%n)
x=[]
y=[]
count=0
for i in range (0,n):
        for j in range (0,n):
                if(lhs[1][i]==rhs[1][j]):
                        count+=1
                        x.append(lhs[0][i])
                        y.append(rhs[0][j])
#print nG values
for i in range(0,count):
        print(i+1,"(",x[i],",",y[i],")")
bx=x[0]
by=y[0]
print("Initial point is :",bx,",",by)
#now, lets generate a random integer 'd',the private key of sender
d=random.randint(0,n)
qx=d*bx
qy=b*by
print("Public key of sender : ",qx,",",qy)
#generate another random integer 'k'
k=random.randint(0,n)
c1xarr=list()
c1yarr=list()
c2xarr=list()
c2yarr=list()
#encryption process
final_ans=list()
for i in pair:
        c1x=k*bx
        c1y=k*by
        print("Value of ciphertext 1 is ",c1x,",",c1y)
        c1xarr.append(c1x)
        c1yarr.append(c1y)
        c2x=k*qx+i
        c2y=k*qy+i
        print("Value of ciphertext2 is ",c2x,",",c2y)
        c2xarr.append(c2x)
        c2yarr.append(c2y)
        mx=c2x-i*c1x
        my=c2y-i*c2x
        print("Decrypted sentence is : ",mx)
        final_ans.append(mx)

print(final_ans)

#now, convert the ascii back to human-readable letters
string = ''.join(map(str,final_ans))
char_num = 0
op = list()
for i in range(len(string)):
        char_num=char_num*10 + (ord(string[i])-ord('0'))
        if(char_num>=32 and char_num <=122):
                ch = chr(char_num)
                op.append(ch)
                char_num=0
print("Letter character stream : ")
print(op)
print("Decrypted sentence : ")
opstring = ''.join(map(str,op))
print(opstring)




