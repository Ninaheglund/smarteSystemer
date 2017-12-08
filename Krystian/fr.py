import cv2, sys, numpy, os
size = 2
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'att_faces'

def Facerec():
    #Oppretter fisherRecognizer
    print('Training...')

    #Oppretter en liste med bilder og en liste med tilsvarende navn
    (images, lables, names, id) = ([], [], {}, 0)

    # Får tak i folderen som inneholder training dataen
    for (subdirs, dirs, files) in os.walk(fn_dir):

        #Looper igjennom hver folder oppkalt etter subjektet i bildene
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(fn_dir, subdir)

            # Looper igjennom hvert bilde i folderen
            for filename in os.listdir(subjectpath):

                #Skiper ikke-bilde formater
                f_name, f_extension = os.path.splitext(filename)
                if(f_extension.lower() not in
                        ['.png','.jpg','.jpeg','.gif','.pgm']):
                    print("Skipping "+filename+", wrong file type")
                    continue
                path = subjectpath + '/' + filename
                lable = id

                #Legger til trenings dataen
                images.append(cv2.imread(path, 0))
                lables.append(int(lable))
            id += 1
    (im_width, im_height) = (112, 92)

    #Oppretter en Numpy array fra de 2 listene ovenfor
    (images, lables) = [numpy.array(lis) for lis in [images, lables]]

    #Opencv trener en model fra bildene
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, lables)

    #Bruker fisherRecognizer på kamera streamen
    haar_cascade = cv2.CascadeClassifier(fn_haar)
    webcam = cv2.VideoCapture(0)
    while True:

        #Her looper den til kamera funker
        rval = False
        while(not rval):
            #Putter bilde fra webcamera inni en ramme
            (rval, frame) = webcam.read()
            if(not rval):
                print("Failed to open webcam. Trying again...")

        # Flip the image (optional) #Her flippes bilde (valgfritt)
        frame=cv2.flip(frame,1,0)

        #Konverterer til gråtone
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #Skalerer for å øke gjennkjenningen (også valgfrit, endre verdien ovenfor)
        mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

        # Detekterer fjes og looper gjennom hvert enkel et
        faces = haar_cascade.detectMultiScale(mini)
        for i in range(len(faces)):
            face_i = faces[i]

            # Koordinatene til ansiktet etter å ha skaleret tilbake av 'size'
            (x, y, w, h) = [v * size for v in face_i]
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (im_width, im_height))

            #Prøver å gjennkjenne ansiktet
            prediction = model.predict(face_resize)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)


            #Skriver navnet til det gjennkjente ansiktet
            if prediction[1] < 100:
                print(prediction[0])
                return prediction[0]
                cv2.putText(frame,
               '%s - %.0f' % (names[prediction[0]],prediction[1]),
               (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

            else:
                cv2.putText(frame, 'Unknown', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

        #Fremviser bilde og sjekker etter at esc blir presset.
        #cv2.imshow('OpenCV', frame)
        key = cv2.waitKey(10)
        if key == 27:
            break

