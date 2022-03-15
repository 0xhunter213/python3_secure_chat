from binascii import hexlify


def key_init(key):
    s = []
    for i in range(256):
        s.append(i)
    j = 0
    for i in range(256):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        s[i], s[j] = s[j], s[i]
    return s


def enc(msg, key):
    s = key_init(key)
    i = 0
    j = 0
    res = []
    for c in msg:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        oct_enc = s[(s[i]+s[j]) % 256]
        res.append(chr(oct_enc ^ ord(c)))
    return ''.join(res)


def dec(enc, key):
    s = key_init(key)
    i = 0
    j = 0
    res = []
    for c in enc:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        oct_enc = s[(s[i]+s[j]) % 256]
        res.append(chr(oct_enc ^ ord(c)))
    return ''.join(res)


def main():
    while True:
        msg = input("Enter a message:")
        key = input("Enter a key:")
        enc_msg = enc(msg, key)
        print(f"Encrypted msg:{enc_msg}")
        print(f"Encrypted msg in hex:{hexlify(enc_msg.encode()).decode()}")
        dec_msg = dec(enc_msg, key)
        print(f"Decrypted msg:{dec_msg}")


if __name__ == "__main__":
    main()
