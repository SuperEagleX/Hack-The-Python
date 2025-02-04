import string

# alphabets = string.ascii_lowercase

class Caesar:
    def __init__(self):
        self.alphabets = string.ascii_lowercase *2

    def Encrypt(self, text, key):
        cipher_text = ""
        for alpha in text.lower().strip(" "):
            if alpha not in self.alphabets:
                cipher_text += alpha
            else:
                cipher_text += self.alphabets[self.alphabets.index(alpha) + key]
        return cipher_text

    def Decrypt(self, text, key):
        plain_text = ""
        for alpha in text.lower().strip(" "):
            if alpha not in self.alphabets:
                plain_text += alpha
            else:
                plain_text += self.alphabets[self.alphabets.index(alpha) - key]
        return plain_text

Caesar_Cipher = Caesar()
message_1 = Caesar_Cipher.Encrypt("Hello, I love Coding!", 25)
message_2 = Caesar_Cipher.Decrypt("gdkkn, h knud bnchmf!", 25)

print(message_1)
print(message_2)
