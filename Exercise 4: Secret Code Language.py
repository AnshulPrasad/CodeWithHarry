inp = input("Enter message: ")

s = "abc"
e = "123"


def encode(text):
    if len(text) > 3:
        text = text[1:] + text[0]
        text = s + text + e
        return text
    else:
        return text[::-1]


def decode(text):
    if len(text) <= 3:
        return text[::-1]
    else:
        text = text[3:-3]
        text = text[-1] + text[:-1]
        return text


print("1 for encoding, 2 for decoding.")
option = int(input("Enter mode: "))

if option == 1:
    enc = " ".join(encode(i) for i in inp.split())
    print(f"Encoded {inp}: {enc}")
elif option == 2:
    dec = " ".join(decode(i) for i in inp.split())
    print(f"Decoded {inp}: {dec}")
