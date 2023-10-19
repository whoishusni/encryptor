class Encryption_Attributes:
    __salt = b'\x8e\xbf\xa4\xaa$\x8f9\x8eH\x9a\x1a~\xbd\\\x9f^g"\xe0UGV\x0b\x17\x0b\x8c\x04F\x85\x01\xbe\x10'
    __init_vector = b'q\xbd~{E\xca\xca\x1c\xf9\x89&]\xad0\xc8\xf0'
    
    def __init__(self):
        pass
    
    def get_salt(self):
        self.salt = self.__salt
        return self.salt
    
    def get_iv(self):
        self.iv = self.__init_vector
        return self.iv