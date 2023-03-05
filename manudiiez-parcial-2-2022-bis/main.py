from encoder import Encoder

if __name__ == '__main__':
    encoder = Encoder()
    result_dict = encoder.encode(
            'While The Python')
    print(result_dict)
    result_dict2 = encoder.decode({'W': [1], 'h': [2, 8, 14], 'i': [3], 'l': [4], 'e': [5, 9], ' ': [6, 10], 'T': [7], 'P': [11], 'y': [12], 't': [13], 'o': [15], 'n': [16]})
    print(result_dict2)
    