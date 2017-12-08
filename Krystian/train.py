import cv2, sys, numpy, os
size = 4
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'
try:
    fn_name = sys.argv[1]
except:
    print("Navn ikke registrert..")
    sys.exit(0)
path = os.path.join(fn_dir, fn_name)
if not os.path.isdir(path):
    os.mkdir(path)
(im_width, im_height) = (112, 92)
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)

#Genererer navn for bilde filen
pin=sorted([int(n[:n.find('.')]) for n in os.listdir(path)
     if n[0]!='.' ]+[0])[-1] + 1

#Skriver ut melding
print("\n\033[94mThe program will save 20 samples. \
Move your head around to increase while it runs.\033[0m\n")

#Programmet looper til den har 20 bilder av ansiktet
count = 0
pause = 0
count_max = 20
while count < count_max:

    #looper inntil kameraet virker
    rval = False
    while(not rval):
        #Putter bildet fra webkamera inni ramme
        (rval, frame) = webcam.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")

    #Får bilde størrelse
    height, width, channels = frame.shape

    #Fliper rammen
    frame = cv2.flip(frame, 1, 0)

    #Konverterer til gråtone
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Scalerer ned for hastighet
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    #Gjennkjenner fjes
    faces = haar_cascade.detectMultiScale(mini)

    #Vi ser kun etter de største fjesene
    faces = sorted(faces, key=lambda x: x[3])
    if faces:
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        #Skaper en rektangel og skriver navn
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN,
            1,(0, 255, 0))

        #Fjerner falske positiver
        if(w * 6 < width or h * 6 < height):
            print("Face too small")
        else:

            # For å opprette mangfold, lagre bare alle femte oppdagede bilde
            if(pause == 0):

                print("Saving training sample "+str(count+1)+"/"+str(count_max))

                # Save image file
                cv2.imwrite('%s/%s.png' % (path, pin), face_resize)

                pin += 1
                count += 1

                pause = 1

    if(pause > 0):
        pause = (pause + 1) % 5
    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
