inp = input("Enter message: ")


def encode(text):
    if len(text) > 3:
        text = text[1:] + text[0]
        text = "123" + text + "xyz"
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


enc = encode(inp)
dec = decode(enc)
print(f"Encoded {inp}: {enc}")
print(f"Decoded {enc}: {dec}")
