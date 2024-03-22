import rsa

""" publicKey, privateKey = rsa.newkeys(1024) """

with open("public.pem", "rb") as f:
    publicKey = rsa.PublicKey.load_pkcs1(f.read())
    
with open("private.pem", "rb") as f:
    privateKey = rsa.PrivateKey.load_pkcs1(f.read())
    
message = input("Digite a msg: ")

encrypt_message_cmd = rsa.encrypt(message.encode(), publicKey)
print("encrypted msg: ", encrypt_message_cmd)

with open("encrypted.message", "wb") as f:
    f.write(encrypt_message_cmd) 

encrypt_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypt_message, privateKey)
print("mensagem descriptografada: ", clear_message)

""" 
criar as chaves
with open("public.pem", "wb") as f:
    f.write(publicKey.save_pkcs1("PEM"))
    
with open("private.pem", "wb") as f:
    f.write(privateKey.save_pkcs1("PEM")) """
    

