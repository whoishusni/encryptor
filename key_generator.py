from Crypto.Random import get_random_bytes

class Key_Gen:
    def __init__(self, bytes_16, bytes_32):
        self.bytes_16 = bytes_16
        self.bytes_32 = bytes_32
        
    def generate(self):
        gens = f'''
        16 bytes : {get_random_bytes(self.bytes_16)}
        32 bytes : {get_random_bytes(self.bytes_32)}
        '''
        return gens
