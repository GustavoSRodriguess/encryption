from Crypto.Cipher import AES

def pad(entry):
    pdded = entry+(16-len(entry)%16) * '['
    return pdded

text = input('Digite texto para codificar: ')
text = pad(text)
text = text.encode('UTF-8')

key = '123'
key = pad(key)
key = key.encode('UTF-8')

cipher = AES.new(key, AES.MODE_ECB)
cipherText = cipher.encrypt(text)
print(cipherText)
