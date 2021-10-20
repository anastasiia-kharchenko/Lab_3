class Kupyna:

    def __init__(self, n):
        self.sboxes = [[0xa8, 0x43, 0x5f, 0x06, 0x6b, 0x75, 0x6c, 0x59, 0x71, 0xdf, 0x87,
                        0x95, 0x17, 0xf0, 0xd8, 0x09, 0x6d, 0xf3, 0x1d, 0xcb, 0xc9, 0x4d,
                        0x2c, 0xaf, 0x79, 0xe0, 0x97, 0xfd, 0x6f, 0x4b, 0x45, 0x39, 0x3e,
                        0xdd, 0xa3, 0x4f, 0xb4, 0xb6, 0x9a, 0x0e, 0x1f, 0xbf, 0x15, 0xe1,
                        0x49, 0xd2, 0x93, 0xc6, 0x92, 0x72, 0x9e, 0x61, 0xd1, 0x63, 0xfa,
                        0xee, 0xf4, 0x19, 0xd5, 0xad, 0x58, 0xa4, 0xbb, 0xa1, 0xdc, 0xf2,
                        0x83, 0x37, 0x42, 0xe4, 0x7a, 0x32, 0x9c, 0xcc, 0xab, 0x4a, 0x8f,
                        0x6e, 0x04, 0x27, 0x2e, 0xe7, 0xe2, 0x5a, 0x96, 0x16, 0x23, 0x2b,
                        0xc2, 0x65, 0x66, 0x0f, 0xbc, 0xa9, 0x47, 0x41, 0x34, 0x48, 0xfc,
                        0xb7, 0x6a, 0x88, 0xa5, 0x53, 0x86, 0xf9, 0x5b, 0xdb, 0x38, 0x7b,
                        0xc3, 0x1e, 0x22, 0x33, 0x24, 0x28, 0x36, 0xc7, 0xb2, 0x3b, 0x8e,
                        0x77, 0xba, 0xf5, 0x14, 0x9f, 0x08, 0x55, 0x9b, 0x4c, 0xfe, 0x60,
                        0x5c, 0xda, 0x18, 0x46, 0xcd, 0x7d, 0x21, 0xb0, 0x3f, 0x1b, 0x89,
                        0xff, 0xeb, 0x84, 0x69, 0x3a, 0x9d, 0xd7, 0xd3, 0x70, 0x67, 0x40,
                        0xb5, 0xde, 0x5d, 0x30, 0x91, 0xb1, 0x78, 0x11, 0x01, 0xe5, 0x00,
                        0x68, 0x98, 0xa0, 0xc5, 0x02, 0xa6, 0x74, 0x2d, 0x0b, 0xa2, 0x76,
                        0xb3, 0xbe, 0xce, 0xbd, 0xae, 0xe9, 0x8a, 0x31, 0x1c, 0xec, 0xf1,
                        0x99, 0x94, 0xaa, 0xf6, 0x26, 0x2f, 0xef, 0xe8, 0x8c, 0x35, 0x03,
                        0xd4, 0x7f, 0xfb, 0x05, 0xc1, 0x5e, 0x90, 0x20, 0x3d, 0x82, 0xf7,
                        0xea, 0x0a, 0x0d, 0x7e, 0xf8, 0x50, 0x1a, 0xc4, 0x07, 0x57, 0xb8,
                        0x3c, 0x62, 0xe3, 0xc8, 0xac, 0x52, 0x64, 0x10, 0xd0, 0xd9, 0x13,
                        0x0c, 0x12, 0x29, 0x51, 0xb9, 0xcf, 0xd6, 0x73, 0x8d, 0x81, 0x54,
                        0xc0, 0xed, 0x4e, 0x44, 0xa7, 0x2a, 0x85, 0x25, 0xe6, 0xca, 0x7c,
                        0x8b, 0x56, 0x80],
                       [0xce, 0xbb, 0xeb, 0x92, 0xea, 0xcb, 0x13, 0xc1, 0xe9, 0x3a, 0xd6,
                        0xb2, 0xd2, 0x90, 0x17, 0xf8, 0x42, 0x15, 0x56, 0xb4, 0x65, 0x1c,
                        0x88, 0x43, 0xc5, 0x5c, 0x36, 0xba, 0xf5, 0x57, 0x67, 0x8d, 0x31,
                        0xf6, 0x64, 0x58, 0x9e, 0xf4, 0x22, 0xaa, 0x75, 0x0f, 0x02, 0xb1,
                        0xdf, 0x6d, 0x73, 0x4d, 0x7c, 0x26, 0x2e, 0xf7, 0x08, 0x5d, 0x44,
                        0x3e, 0x9f, 0x14, 0xc8, 0xae, 0x54, 0x10, 0xd8, 0xbc, 0x1a, 0x6b,
                        0x69, 0xf3, 0xbd, 0x33, 0xab, 0xfa, 0xd1, 0x9b, 0x68, 0x4e, 0x16,
                        0x95, 0x91, 0xee, 0x4c, 0x63, 0x8e, 0x5b, 0xcc, 0x3c, 0x19, 0xa1,
                        0x81, 0x49, 0x7b, 0xd9, 0x6f, 0x37, 0x60, 0xca, 0xe7, 0x2b, 0x48,
                        0xfd, 0x96, 0x45, 0xfc, 0x41, 0x12, 0x0d, 0x79, 0xe5, 0x89, 0x8c,
                        0xe3, 0x20, 0x30, 0xdc, 0xb7, 0x6c, 0x4a, 0xb5, 0x3f, 0x97, 0xd4,
                        0x62, 0x2d, 0x06, 0xa4, 0xa5, 0x83, 0x5f, 0x2a, 0xda, 0xc9, 0x00,
                        0x7e, 0xa2, 0x55, 0xbf, 0x11, 0xd5, 0x9c, 0xcf, 0x0e, 0x0a, 0x3d,
                        0x51, 0x7d, 0x93, 0x1b, 0xfe, 0xc4, 0x47, 0x09, 0x86, 0x0b, 0x8f,
                        0x9d, 0x6a, 0x07, 0xb9, 0xb0, 0x98, 0x18, 0x32, 0x71, 0x4b, 0xef,
                        0x3b, 0x70, 0xa0, 0xe4, 0x40, 0xff, 0xc3, 0xa9, 0xe6, 0x78, 0xf9,
                        0x8b, 0x46, 0x80, 0x1e, 0x38, 0xe1, 0xb8, 0xa8, 0xe0, 0x0c, 0x23,
                        0x76, 0x1d, 0x25, 0x24, 0x05, 0xf1, 0x6e, 0x94, 0x28, 0x9a, 0x84,
                        0xe8, 0xa3, 0x4f, 0x77, 0xd3, 0x85, 0xe2, 0x52, 0xf2, 0x82, 0x50,
                        0x7a, 0x2f, 0x74, 0x53, 0xb3, 0x61, 0xaf, 0x39, 0x35, 0xde, 0xcd,
                        0x1f, 0x99, 0xac, 0xad, 0x72, 0x2c, 0xdd, 0xd0, 0x87, 0xbe, 0x5e,
                        0xa6, 0xec, 0x04, 0xc6, 0x03, 0x34, 0xfb, 0xdb, 0x59, 0xb6, 0xc2,
                        0x01, 0xf0, 0x5a, 0xed, 0xa7, 0x66, 0x21, 0x7f, 0x8a, 0x27, 0xc7,
                        0xc0, 0x29, 0xd7],
                       [0x93, 0xd9, 0x9a, 0xb5, 0x98, 0x22, 0x45, 0xfc, 0xba, 0x6a, 0xdf,
                        0x02, 0x9f, 0xdc, 0x51, 0x59, 0x4a, 0x17, 0x2b, 0xc2, 0x94, 0xf4,
                        0xbb, 0xa3, 0x62, 0xe4, 0x71, 0xd4, 0xcd, 0x70, 0x16, 0xe1, 0x49,
                        0x3c, 0xc0, 0xd8, 0x5c, 0x9b, 0xad, 0x85, 0x53, 0xa1, 0x7a, 0xc8,
                        0x2d, 0xe0, 0xd1, 0x72, 0xa6, 0x2c, 0xc4, 0xe3, 0x76, 0x78, 0xb7,
                        0xb4, 0x09, 0x3b, 0x0e, 0x41, 0x4c, 0xde, 0xb2, 0x90, 0x25, 0xa5,
                        0xd7, 0x03, 0x11, 0x00, 0xc3, 0x2e, 0x92, 0xef, 0x4e, 0x12, 0x9d,
                        0x7d, 0xcb, 0x35, 0x10, 0xd5, 0x4f, 0x9e, 0x4d, 0xa9, 0x55, 0xc6,
                        0xd0, 0x7b, 0x18, 0x97, 0xd3, 0x36, 0xe6, 0x48, 0x56, 0x81, 0x8f,
                        0x77, 0xcc, 0x9c, 0xb9, 0xe2, 0xac, 0xb8, 0x2f, 0x15, 0xa4, 0x7c,
                        0xda, 0x38, 0x1e, 0x0b, 0x05, 0xd6, 0x14, 0x6e, 0x6c, 0x7e, 0x66,
                        0xfd, 0xb1, 0xe5, 0x60, 0xaf, 0x5e, 0x33, 0x87, 0xc9, 0xf0, 0x5d,
                        0x6d, 0x3f, 0x88, 0x8d, 0xc7, 0xf7, 0x1d, 0xe9, 0xec, 0xed, 0x80,
                        0x29, 0x27, 0xcf, 0x99, 0xa8, 0x50, 0x0f, 0x37, 0x24, 0x28, 0x30,
                        0x95, 0xd2, 0x3e, 0x5b, 0x40, 0x83, 0xb3, 0x69, 0x57, 0x1f, 0x07,
                        0x1c, 0x8a, 0xbc, 0x20, 0xeb, 0xce, 0x8e, 0xab, 0xee, 0x31, 0xa2,
                        0x73, 0xf9, 0xca, 0x3a, 0x1a, 0xfb, 0x0d, 0xc1, 0xfe, 0xfa, 0xf2,
                        0x6f, 0xbd, 0x96, 0xdd, 0x43, 0x52, 0xb6, 0x08, 0xf3, 0xae, 0xbe,
                        0x19, 0x89, 0x32, 0x26, 0xb0, 0xea, 0x4b, 0x64, 0x84, 0x82, 0x6b,
                        0xf5, 0x79, 0xbf, 0x01, 0x5f, 0x75, 0x63, 0x1b, 0x23, 0x3d, 0x68,
                        0x2a, 0x65, 0xe8, 0x91, 0xf6, 0xff, 0x13, 0x58, 0xf1, 0x47, 0x0a,
                        0x7f, 0xc5, 0xa7, 0xe7, 0x61, 0x5a, 0x06, 0x46, 0x44, 0x42, 0x04,
                        0xa0, 0xdb, 0x39, 0x86, 0x54, 0xaa, 0x8c, 0x34, 0x21, 0x8b, 0xf8,
                        0x0c, 0x74, 0x67],
                       [0x68, 0x8d, 0xca, 0x4d, 0x73, 0x4b, 0x4e, 0x2a, 0xd4, 0x52, 0x26,
                        0xb3, 0x54, 0x1e, 0x19, 0x1f, 0x22, 0x03, 0x46, 0x3d, 0x2d, 0x4a,
                        0x53, 0x83, 0x13, 0x8a, 0xb7, 0xd5, 0x25, 0x79, 0xf5, 0xbd, 0x58,
                        0x2f, 0x0d, 0x02, 0xed, 0x51, 0x9e, 0x11, 0xf2, 0x3e, 0x55, 0x5e,
                        0xd1, 0x16, 0x3c, 0x66, 0x70, 0x5d, 0xf3, 0x45, 0x40, 0xcc, 0xe8,
                        0x94, 0x56, 0x08, 0xce, 0x1a, 0x3a, 0xd2, 0xe1, 0xdf, 0xb5, 0x38,
                        0x6e, 0x0e, 0xe5, 0xf4, 0xf9, 0x86, 0xe9, 0x4f, 0xd6, 0x85, 0x23,
                        0xcf, 0x32, 0x99, 0x31, 0x14, 0xae, 0xee, 0xc8, 0x48, 0xd3, 0x30,
                        0xa1, 0x92, 0x41, 0xb1, 0x18, 0xc4, 0x2c, 0x71, 0x72, 0x44, 0x15,
                        0xfd, 0x37, 0xbe, 0x5f, 0xaa, 0x9b, 0x88, 0xd8, 0xab, 0x89, 0x9c,
                        0xfa, 0x60, 0xea, 0xbc, 0x62, 0x0c, 0x24, 0xa6, 0xa8, 0xec, 0x67,
                        0x20, 0xdb, 0x7c, 0x28, 0xdd, 0xac, 0x5b, 0x34, 0x7e, 0x10, 0xf1,
                        0x7b, 0x8f, 0x63, 0xa0, 0x05, 0x9a, 0x43, 0x77, 0x21, 0xbf, 0x27,
                        0x09, 0xc3, 0x9f, 0xb6, 0xd7, 0x29, 0xc2, 0xeb, 0xc0, 0xa4, 0x8b,
                        0x8c, 0x1d, 0xfb, 0xff, 0xc1, 0xb2, 0x97, 0x2e, 0xf8, 0x65, 0xf6,
                        0x75, 0x07, 0x04, 0x49, 0x33, 0xe4, 0xd9, 0xb9, 0xd0, 0x42, 0xc7,
                        0x6c, 0x90, 0x00, 0x8e, 0x6f, 0x50, 0x01, 0xc5, 0xda, 0x47, 0x3f,
                        0xcd, 0x69, 0xa2, 0xe2, 0x7a, 0xa7, 0xc6, 0x93, 0x0f, 0x0a, 0x06,
                        0xe6, 0x2b, 0x96, 0xa3, 0x1c, 0xaf, 0x6a, 0x12, 0x84, 0x39, 0xe7,
                        0xb0, 0x82, 0xf7, 0xfe, 0x9d, 0x87, 0x5c, 0x81, 0x35, 0xde, 0xb4,
                        0xa5, 0xfc, 0x80, 0xef, 0xcb, 0xbb, 0x6b, 0x76, 0xba, 0x5a, 0x7d,
                        0x78, 0x0b, 0x95, 0xe3, 0xad, 0x74, 0x98, 0x3b, 0x36, 0x64, 0x6d,
                        0xdc, 0xf0, 0x59, 0xa9, 0x4c, 0x17, 0x7f, 0x91, 0xb8, 0xc9, 0x57,
                        0x1b, 0xe0, 0x61]]

        self.mds_matrix = [
            [0x01, 0x01, 0x05, 0x01, 0x08, 0x06, 0x07, 0x04],
            [0x04, 0x01, 0x01, 0x05, 0x01, 0x08, 0x06, 0x07],
            [0x07, 0x04, 0x01, 0x01, 0x05, 0x01, 0x08, 0x06],
            [0x06, 0x07, 0x04, 0x01, 0x01, 0x05, 0x01, 0x08],
            [0x08, 0x06, 0x07, 0x04, 0x01, 0x01, 0x05, 0x01],
            [0x01, 0x08, 0x06, 0x07, 0x04, 0x01, 0x01, 0x05],
            [0x05, 0x01, 0x08, 0x06, 0x07, 0x04, 0x01, 0x01],
            [0x01, 0x05, 0x01, 0x08, 0x06, 0x07, 0x04, 0x01]
        ]

        self.mult_table = [[0 for j in range(256)] for i in range(256)]
        for x in range(256):
            for y in range(256):
                self.mult_table[x][y] = self.multiply_gf(x, y)

        self.n = n
        if 8 <= n <= 256:
            self.l = 512
            self.t = 10
            self.c = 8
        elif 256 < n <= 512:
            self.l = 1024
            self.t = 14
            self.c = 16
        else:
            raise Exception('Unsupported hash length')

    def preprocess(self, message):
        bytes = [int(message[i * 2: (i + 1) * 2], 16) for i in range(len(message) // 2)]
        binary_message = ''.join(bin(byte)[2:].zfill(8) for byte in bytes)

        N = len(binary_message)
        k = (-97 - N) % self.l
        binary_N = ''
        for i in range(12):
            binary_N += bin((N >> i * 8) & 0xff)[2:].zfill(8)
        padded_message = binary_message + '1' + '0' * k + binary_N

        states = []
        for b in range(len(padded_message) // self.l):
            bits = padded_message[b * self.l:(b + 1) * self.l]
            states.append(int(bits, 2))
        return states

    def xor_state_value(self, state, v):
        for j in range(self.c):
            state[0][j] ^= (j << 4) ^ v
        return state

    def add_state_value(self, state, v):
        for j in range(self.c):
            word = 0
            for i in range(8):
                word += state[i][j] << i * 8
            result = word + (0x00f0f0f0f0f0f0f3 ^ ((((self.c - j - 1) << 4) ^ v) << 56))
            for i in range(8):
                state[i][j] = (result >> i * 8) & 0xff
        return state

    def sub_bytes(self, state):
        new_state = [[0 for j in range(self.c)] for i in range(8)]
        for i in range(8):
            for j in range(self.c):
                new_state[i][j] = self.sboxes[i % 4][state[i][j]]
        return new_state

    def shift_bytes(self, state):
        new_state = [[0 for j in range(self.c)] for i in range(8)]
        for i in range(7):
            for j in range(self.c):
                new_state[i][(j + i) % self.c] = state[i][j]
        for j in range(self.c):
            shift = 7 if self.l == 512 else 11
            new_state[7][(j + shift) % self.c] = state[7][j]
        return new_state

    def multiply_gf(self, x, y):
        r = 0
        for i in range(8):
            if (y & 0x1) == 1:
                r ^= x
            hbit = x & 0x80
            x = x << 1
            if hbit == 0x80:
                x ^= 0x011d
            y >>= 1
        return r

    def mix_columns(self, state):
        new_state = [[0 for j in range(self.c)] for i in range(8)]
        for col in range(self.c):
            for row in range(7, -1, -1):
                product = 0
                for b in range(7, -1, -1):
                    product ^= self.mult_table[state[b][col]][self.mds_matrix[row][b]]
                new_state[row][col] = product
        return new_state

    def T_xor(self, word):
        state = self.word_to_state(word)
        for v in range(self.t):
            state = self.xor_state_value(state, v)
            state = self.sub_bytes(state)
            state = self.shift_bytes(state)
            state = self.mix_columns(state)
        return self.state_to_word(state)

    def T_add(self, word):
        state = self.word_to_state(word)
        for v in range(self.t):
            state = self.add_state_value(state, v)
            state = self.sub_bytes(state)
            state = self.shift_bytes(state)
            state = self.mix_columns(state)
        return self.state_to_word(state)

    def hash(self, message):
        if self.l == 512:
            hash_value = 1 << 510
        else:
            hash_value = 1 << 1023
        input_states = self.preprocess(message)
        for input_state in input_states:
            hash_value = self.T_xor(hash_value ^ input_state) ^ self.T_add(input_state) ^ hash_value
        return (self.T_xor(hash_value) ^ hash_value) & int('1' * self.n, 2)

    def word_to_state(self, word):
        state = [[0 for j in range(self.c)] for i in range(8)]
        hex_word = hex(word)[2:].zfill(self.l // 4)
        bytes = [int(hex_word[i * 2:(i + 1) * 2], 16) for i in range(len(hex_word) // 2)]
        for j in range(self.c):
            for i in range(8):
                state[i][j] = bytes[j * 8 + i]
        return state

    def state_to_word(self, state):
        word = 0
        for j in range(self.c):
            for i in range(8):
                word += state[i][j] << (self.c * 8 - 1 - j * 8 - i) * 8
        return word


kupyna = Kupyna(256)
hash = kupyna.hash('000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F')

# print(hash)