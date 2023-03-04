# hezNom-encryption
A python program for text encryption.

This is a simple encryption code written in python.

To use it, clone or copy the code as a whole to your machine and power it up on your terminal as below:

   for windows systems:
   
       \Desktop> py <file-name.py>
       \Desktop> py HezNomCipher.py
       
   for linux systems
   
       ~: python3 <file-name.py>
       ~: python3 HezNomCipher.py
       
Choose what to do with the program as it dispalys on the ui screen.

For encryption, type in your plain text and provide a valid integer password of length six to encrypt your message. A cipher text will be dispalyed on your screen.

Take note of the password as this program doesn't store passwords or texts.

For decryption, type in the HezNom encrypted text and provide the valid corresponding password to decrypt. A plain text will be printed on the screen.


This is how the program looks like on windows: 
![2023-03-03](https://user-images.githubusercontent.com/115971663/222701858-9e47f495-5e3e-41ee-9a95-9b14cb49fdb8.png)

TO UNDERSTAND THE LOGICS BEHIND THE ENCRYPTION / DECRYPTION

      for char in input_text:
          output += chr(ord(char) ^ key)

- This is the major part of this program. I takes the user's inputed text as string and iterate it to find the integer coefficient of each character.
- This is achieved by ord() function in python.
- The operator (^) in python means XOR. XOR operation can only be done on binary values. This therefore means that the values of each character are converted into binary as well as the key. Note that the key value can only be an integer. This is to make it possible for binary conversion.
  
  For example:
    - Let's take 3 as the integer value of any character in the user's text. 
    - 2 to be the key of the user which is an integer.
            
             3 in binary is 00000011
             2 in binary is 00000010
             3 ^ 2 ==>>>>> 00000011 XOR 00000010 which gives 1 (00000001)
    
    - 1 is the resulting output after going through the encryption. chr() function then converts 1 into its coefficient ascii value and that becomes the cypher text.
    - Key points to note:
          1. The key must not be 0 otherwise the output will still be identical to the input.
          2. The length of the key ranges from 1 to 6, that means key can be 1 - 999999 past this the program generates an error.
          3. The output can still be encrypted using the same key and get back the plain text as XOR function reverts it back.
          4. To make it hard for an intruder to bruteforce your key, use bigger numbers in the range above.
