from compress import Compress

if __name__ == '__main__':
    with open('tdd.txt') as file:
        text_1 = file.read()
    compress = Compress()
    compressed, values = compress.compress(text_1)
    # print(compressed)
    # print(values)
    compress.uncompress(compressed, values)