class CaesarCipher:
    """ CaesarCipher class is intended to provide methods for encypting
        decrypting text input provided in the constructor, from the main
        program.
    """
    __text = ""
    __character_range = list(map(chr, range(97, 123)))

    
    def __init__(self, text):
        """ Sets the input text and operation to be performed defined in
            the 'mode' argument.
        """
        self.__text = text.lower()
    
    
    def encrypt(self, key) -> str:
        """ The method returns encrypted cipher text using caesar algorithm
            based on the 'key' passed in the argument's list.
        """
        keyed_indexes = [self.__character_range.index(character) + key for character in self.__text]
        encrypted_characters = [ self.__character_range[value] for value in keyed_indexes]
        return "".join(encrypted_characters)
    

    def decrypt(self, key) -> str:
        """ The method returns decrypted cipher text using caesar algorithm
            based on the 'key' passed in the argument's list.
        """
        keyed_indexes = [self.__character_range.index(character) - key for character in self.__text]
        encrypted_characters = [ self.__character_range[value] for value in keyed_indexes]
        return "".join(encrypted_characters)
