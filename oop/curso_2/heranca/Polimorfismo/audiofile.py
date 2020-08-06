class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Formato invalido')

        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print('Tocando arquivo MP3')


class WavFile(AudioFile):
    ext = 'wav'

    def play(self):
        print('Tocando arquivo WAV')


class OggFile(AudioFile):
    ext = 'ogg'

    def play(self):
        print('Tocando arquivo Ogg')


try:
    """ 
    Validação da extensão do arquivo é feito na Classe AudioFile
    """
    mp3 = MP3File('musica.mp3')
    mp3.play()

except Exception as err:
    print(err)
