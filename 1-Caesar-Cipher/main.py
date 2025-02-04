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

#Alternative

print("\nImproved Cap Handlings")

class Caesar_2:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase

    def Encrypt(self, text, key):
        cipher_text = ""
        for char in text:
            if char in self.lowercase:
                new_index = (self.lowercase.index(char) + key) % 26
                cipher_text += self.lowercase[new_index]
            elif char in self.uppercase:
                new_index = (self.uppercase.index(char) + key) % 26
                cipher_text += self.uppercase[new_index]
            else:
                cipher_text += char  # Keep punctuation, spaces, and numbers unchanged
        return cipher_text

    def Decrypt(self, text, key):
        plain_text = ""
        for char in text:
            if char in self.lowercase:
                new_index = (self.lowercase.index(char) - key) % 26
                plain_text += self.lowercase[new_index]
            elif char in self.uppercase:
                new_index = (self.uppercase.index(char) - key) % 26
                plain_text += self.uppercase[new_index]
            else:
                plain_text += char
        return plain_text

Caesar_Cipher_2 = Caesar_2()
message_3 = Caesar_Cipher_2.Encrypt("Hello, I love Coding!", 25)
message_4 = Caesar_Cipher_2.Decrypt("gdkkn, h knud bnchmf!", 25)

print(message_3)
print(message_4)