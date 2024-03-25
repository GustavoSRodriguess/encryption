import hashlib

h = hashlib.new("SHA256")
correct_pwd = "123"
h.update(correct_pwd.encode())

pwd_hash = h.hexdigest()
print(pwd_hash)

"é bom comparar hashes em relacao a descriptografar a senha do bd, vc da hash no input e comparaas 2 hasehs"
user_input = input("Qual a sua senha?: ")
h = hashlib.new("SHA256")
h.update(user_input.encode())
input_hash = h.hexdigest()
if(pwd_hash == input_hash):
    print("teste1")
else:
    print("teste2")




"hex digest num geral ;e melhor"
