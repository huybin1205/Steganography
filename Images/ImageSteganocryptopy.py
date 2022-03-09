from steganocryptopy.steganography import Steganography

def readContentFile(path):
    f = open('key','r')
    content = f.readlines()[0]
    f.close()
    return content

def encryptImage(pathImage, pathMessageFile, pathOutput):
    try:
        key = Steganography.generate_key('Images/key')
        encrypted = Steganography.encrypt('Images/key', pathImage, pathMessageFile)
        encrypted.save(pathOutput)
        return readContentFile('Images/key')
    except:
        return -1

def decryptImage(pathImage):
    try:
        return Steganography.decrypt('Images/key', pathImage)
    except:
        return -1

if __name__ == '__main__':
    pathImageEncrypt = r'images_test.png'
    pathImageDecrypt = r'test.png'
    pathMessageFile = r'secretMessage.txt'
    print(encryptImage(pathImageEncrypt, pathMessageFile, pathImageDecrypt))
    print(decryptImage(pathImageDecrypt))
