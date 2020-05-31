class SPIX:
    rows = ['url']
    input_address = None
    input_content = None
    input_type = 'txt'

    @classmethod
    def get_input(cls, ext='txt', address='data'):

        if ext == 'txt':
            SPIX.input_type = 'txt'

        else:
            raise ValueError("The extension " + ext + " is not supported for now")

        SPIX.input_address = address

        with open(address, 'r') as f:
            SPIX.input_content = f.read()


if __name__ == "__main__":
    SPIX.get_input(ext='txt', address='test.txt')
