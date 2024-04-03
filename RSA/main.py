alphabet_e = {
    "a": "01",
    "b": "02",
    "c": "03",
    "d": "04",
    "e": "05",
    "f": "06",
    "g": "07",
    "h": "08",
    "i": "09",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26",
    " ": "32",
}

alphabet_d = {n: c for c, n in alphabet_e.items()}

def gcd (a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
    
def prepare_rsa(p, q):
    N = p * q
    
    N0 = (p-1) * (q-1)
    
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break

    for i in range(0, N0):
        if((e*i) % N0) == 1:
            d = i
            break
    return N, e ,d

N, e, d = prepare_rsa(3,11)

def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)

def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)

def split(word):
    return list(word)

def encrypt_msg(msg, N, e):
    text = split(msg.lower())
    encrypted = []
    
    for char in text:
        if char in alphabet_e:
            encrypted.append(encrypt(alphabet_e[char], N, e))
    
    return " ".join(encrypted)

def decrypt_msg(msg, N, d):
    encrypted = msg.split()
    decrypted = []
    text = []
    
    for char in encrypted:
        decrypted.append(decrypt(char, N , d))
    
    for char in decrypted:
        text.append(alphabet_d[char])
    
    text = ''.join(text)
    return text  

def option():
    print("Options: \n\
        0 - Gerar par de chaves \n\
        1 - Criptografar mensagem de um arquivo\n\
        2 - Descriptografar mensagem de um arquivo\n\
        3 - Criptografar mensagem no terminal\n\
        4 - Descriptografar mensagem no terminal\n\
        5 - Sair\n")



while True:
    option()
    
    selection = input()
    
    match selection:
        case '0':
            p = int(input("Selecione o primeiro numero primo: ")) 
            q = int(input("Selecione o segundo numero primo: ")) 
            print()

            N, e, d = prepare_rsa(p ,q)
            
            print(f"Chave publica: \nN: {N}\ne: {e}\n")
            print(f"Chave privada: \nN: {N}\nd: {d}\n")
        case '1':
            N = int(input("Insira a chave puvblic key N: "))
            e = int(input("Insira a chave puvblic key e: "))
            print()
            
            with open('input.txt', 'r') as fin:
                msg = fin.read()
                
            with open('encrypted.txt', 'w') as fout:
                fout.write(encrypt_msg(msg, N, e))
                
            print('Arquivo criptografado')
        case '2':
            N = int(input("Insira a chave privada N: "))
            d = int(input("Insira a chave privada d: "))
            print()
            
            with open('input.txt', 'r') as fin:
                msg = fin.read()
                
            with open('decrypted.txt', 'w') as fout:
                fout.write(decrypt_msg(msg, N, d))
                
            print('Arquivo descriptografado')
        case '3':
            N = int(input("Insira a chave puvblic key N: "))
            e = int(input("Insira a chave puvblic key e: "))
            print()
            msg = input('Insira a mensagem para criptografar: \n')
            
            print(f'\nmensagem criptografada: \n {encrypt_msg(msg, N, e)}\n')
        case '4':
            N = int(input("Insira a chave privada N: "))
            d = int(input("Insira a chave privada d: "))
            print()

            msg = input('Insira a mensagem para descriptgrafar: \n')
            
            print(f'\nmensagem descriptografada: \n {decrypt_msg(msg, N, d)}\n')
        case '5':
            sair = input("Deseja memso sair?: \n\
                'Y' para sim\n\
                'N' para nao\n\n").upper()
            
            if sair == 'Y':
                break
            elif sair == 'N':
                continue
            else:
                print('Opcao invalida')
                continue
        case _:
            print('Opcao invaldia')
