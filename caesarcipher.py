class CaesarCipher:
    def __init__(self, input_str, key):
        self.input = input_str
        self.key = key

    def encryptString(self):
        output = ''
        for c in self.input:
            if c.isalpha() and c.isupper():
                if ord(c) + self.key > 91:
                    output += chr(ord(c) + self.key - 26)
                else:
                    output += chr(ord(c) + self.key)
            elif c.isalpha() and c.islower():
                if ord(c) + self.key > 122:
                    output += chr(ord(c) + self.key - 26)
                else:
                    output += chr(ord(c) + self.key)
            else:
                output += c
        return output

    def descrypt_string(self, inp):
        self.input = inp
        n = 25
        answer = []
        while n:
            output = ''
            for c in self.input:
                if c.isalpha() and c.isupper():
                    if ord(c) - n < 65:
                        output += chr(ord(c) - n + 26)
                    else:
                        output += chr(ord(c) - n)

                elif c.isalpha() and c.islower():
                    if ord(c) - n < 97:
                        output += chr(ord(c) - n + 26)
                    else:
                        output += chr(ord(c) - n)
                else:
                    output += c
            answer.append(output)
            n -= 1
        return answer

inpStr = input("Enter your string to encrypt: ")
key = int(input("Enter your key: "))
c = CaesarCipher(inpStr, key)
x = c.encryptString()
print(x)
l = c.descrypt_string(x)
print(l, sep='\n')
