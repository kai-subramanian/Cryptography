#a simple function to check if a number is prime or not; we will be using this later.
def prime(x):
        if (x<=1):
                return False
        for i in range (2,x):
                if(x%i==0):
                        return False
        return True

#another function to find gcd of two numbers x and y
def gcd(x,y):
        while(y!=0):
                x,y = y,x%y
        return x

#get the input
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
rsa_arr = list()
for i in range (0,len(arr)):
        rsa_arr.insert(i,int(str(arr[i][0])+str(arr[i][1])))
print("Concatenated Values")
print(rsa_arr)
#rsa implementation
p=int(input("Enter first prime p"))
q=int(input("Enter second prime q"))
if (p==q or prime(p)==False or prime(q)==False):
        print("Invalid primes; please retry")
else:
        n=p*q
        print("N value is : ",n)
        z=(p-1)*(q-1)
        print("Z value is : ",z)
        for i in range (2,z):
                if(gcd(i,z)==1):
                        e=i
                        break
        print("e value is : ",e)
        #now, find multiplicative inverse
        for i in range (1,z):
                d = ((z*i)+1)/e
                if(d.is_integer()):
                        break
        d=int(d)        
        print("d value is : ",d)
        print("Public key pair (e,n) : (",e,",",n,")")
        print("Private key pair (d,n) : (",d,",",n,")")
        #start encryption and decryption process
        encrypted = list()
        decrypted = list()
        for i in rsa_arr:
                encrypted.append((i**e)%n)
        print("Encrypted stream is : ")
        print(encrypted)
        for i in encrypted:
                decrypted.append((i**d)%n)
        print("Decrypted stream is : ")
        print(decrypted)
        #now, let's convert the ASCII numbers back to letters
        string = ''.join(map(str,decrypted))
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