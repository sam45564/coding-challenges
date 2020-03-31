from caesarCipher import CaesarCipher

class Validator:
    """ This class validates the inputs against the decrypted text to
        conclude the results.
    """

    __emblem_mappings = { "land": "panda", "water": "octopus", "ice": "mammoth", "air": "owl", "fire": "dragon" }
    __text = ""
    __kingdom = ""
    

    def __init__(self, kingdom, text):
        self.__kingdom = kingdom.lower()
        self.__text = text.lower()


    def process(self) -> bool:
        """ The methods process the text provided in the constructor and 
            maps with the relevant emblem after decrypting it using the key.
        """
        characters_found = 0
        emblem = self.__emblem_mappings.get(self.__kingdom)
        length_of_emblem_name = len(emblem)

        cipher = CaesarCipher(self.__text)
        decrypted_text = cipher.decrypt(length_of_emblem_name)

        for character in emblem:
            if character in decrypted_text:
                characters_found = characters_found + 1
        
        if characters_found == length_of_emblem_name:
            return True
        else:
            return False
