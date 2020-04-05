import cv2 

def get_video_frame_count(folder): 
    """Counts the number of frames of the video raw.avi in the specified folder
    
    :param folder: folder where the video is located
    :type folder: string
    """

    # Get count from video
    count=0
    cap=cv2.VideoCapture(str(folder) + '/raw.avi')
    while (cap.isOpened()):
        ret,img=cap.read()
        if ret ==True:
            count+=1
        else:
            break
    print('[INFO] video frame count: ' + str(count))


def get_txt_frame_count(folder): 
    """Counts the number of lines in the txt name 'RFID_data_all.txt', and deduce the number of captured frames 
    
    :param folder: folder where the txt is located
    :type folder: string
    """
    # Get frame count from txt
    count = 0
    with open(str(folder) + '/RFID_data_all.txt', 'r') as f:
        for line in f:
            count+=1
    print('[INFO] logfile frame count: ' + str(count-1))



'''
Testing code
'''
if __name__ == '__main__':
    folder = input('What is the folder name? ')
    get_video_frame_count(folder)
    get_txt_frame_count(folder)
