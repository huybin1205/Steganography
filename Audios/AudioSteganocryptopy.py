import wave

def encryptAudio(pathAudio, secretMessage, pathOutput):
    try:
        waveaudio = wave.open(pathAudio, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        string = secretMessage + int((len(frame_bytes) - (len(secretMessage) * 8 * 8)) / 8) * '#'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string])))
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
        frame_modified = bytes(frame_bytes)
        with wave.open(pathOutput, 'wb') as fd:
            fd.setparams(waveaudio.getparams())
            fd.writeframes(frame_modified)
        waveaudio.close()
        return 1
    except:
        return -1

def decryptAudio(pathAudio):
    try:
        waveaudio = wave.open(pathAudio, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
        msg = string.split("###")[0]
        waveaudio.close()
        return msg
    except:
        return -1

if __name__ == '__main__':
    pathAudio = "01.wav"
    message = 'Ahihi do ngoc'
    pathOutput = '1_en.wav'
    encryptAudio(pathAudio, message, pathOutput)
    print(decryptAudio(pathOutput))
