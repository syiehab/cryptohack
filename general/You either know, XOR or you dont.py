from pwn import xor

e = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# if e ^ key = flag
# then key flag ^ e = key

key = xor(e[0:7], "crypto{") + xor(e[-1], "}") 
flag = xor(key, e)

print(f'Key: {key}') #myXORkey
print(f'Flag: {flag}') #flag
