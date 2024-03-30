import cv2

def take_photo(user_id):
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_crop(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_cropped = img[y:y + h, x:x + w]
            return face_cropped

    capture = cv2.VideoCapture(0)
    img_id = 0

    while True:
        ret, frame = capture.read()
        if face_crop(frame) is not None:
            img_id += 1
            face = cv2.resize(face_crop(frame), (450, 450))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = "face_data/user." + str(user_id) + "." + str(img_id) + ".jpg"  # -------------- once the camera works, replace this line with "face_data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"............and comment out that "s_id" thing
            cv2.imwrite(file_name_path, face)  # chenge in video ???
            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)  # chenge in video ???
            cv2.imshow("Capturing, please wait...", face)

        if cv2.waitKey(1) == 13 or int(img_id) == 100:  # 13 is for <enter> key, the loop stops if you press enter or 100 samples are taken
            break

    capture.release()
    cv2.destroyAllWindows()
