import cv2
import os
from moviepy.editor import VideoFileClip
import ffmpeg

def extractImageFromVideo(pathVideo):
    # Read the video from specified path
    cam = cv2.VideoCapture(pathVideo)
    fps = cam.get(cv2.CAP_PROP_FPS)
    print('fps = '+fps)
    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')
    # frame
    currentframe = 0
    while (True):
        # reading from frame
        ret, frame = cam.read()
        if ret:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            # writing the extracted images
            cv2.imwrite(name, frame)
            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()

def extractAudioFromVideo(pathVideo, pathOutput):
    clip = VideoFileClip(pathVideo)
    clip.audio.write_audiofile(pathOutput)

def createVideoFromImages(pathImages):
    img_array = []
    for filename in os.listdir(pathImages):
        img = cv2.imread(pathImages+'\\'+filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()

def test():
    input_video = ffmpeg.input(r"C:\Users\HuyBin\PycharmProjects\Steganography\Videos\project.mp4")
    input_audio = ffmpeg.input(r"C:\Users\HuyBin\PycharmProjects\Steganography\Videos\test.wav")
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('final.mp4').run()

if __name__ == '__main__':
    # extractImageFromVideo(r"C:\Users\HuyBin\Downloads\test.mp4")
    # extractAudioFromVideo(r"C:\Users\HuyBin\Downloads\test.mp4",'test.wav')
    # createVideoFromImages(r'C:\Users\HuyBin\PycharmProjects\Steganography\Videos\data')
    test()
