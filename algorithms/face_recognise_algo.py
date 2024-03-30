import cv2
import mysql.connector
from datetime import datetime


n, s_id, r, d = None, None, None, None
def draw_boundary(img, classifier, scale_factor, min_neighbor, clf):  # change "clf" --> "trained_clf"

    global n, s_id, r, d

    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_image, scale_factor, min_neighbor)

    # coord = []

    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        id1, predict = clf.predict(gray_image[y:y + h, x:x + w])
        confidence = int(100 * (1 - predict / 300))

        if confidence >= 77:
            conn = mysql.connector.connect(host="localhost", username="root", password="Samkit!sqL20",
                                           database="attendence_system")
            cursor = conn.cursor()

            # Name
            cursor.execute("Select name from student where student_id=" + str(id1))
            n = cursor.fetchone()
            n = n[0]

            # ID
            cursor.execute("Select student_id from student where student_id=" + str(id1))
            s_id = cursor.fetchone()
            s_id = s_id[0]

            # Roll No
            cursor.execute("Select roll from student where student_id=" + str(id1))
            r = cursor.fetchone()
            r = r[0]

            # Department
            cursor.execute("Select department from student where student_id=" + str(id1))
            d = cursor.fetchone()
            d = d[0]

        #
            cv2.putText(img, f"Name: {n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
            cv2.putText(img, f"ID: {s_id}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
            cv2.putText(img, f"Roll No: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
            cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
            mark_attendance(n, s_id, r, d)

        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.putText(img, "(Unknown Face)", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

        # coord = [x, y, w, h]  # -------------not really using these coordinates anywhere

def recognize(img, clf, face_cascade):
    draw_boundary(img, face_cascade, 1.1, 10, clf)
    return img


def face_recogniser():
    face_cascade1 = cv2.CascadeClassifier(r"C:\Users\samki\PycharmProjects\pythonProject1\Attendance System\haarcascade_frontalface_default.xml")  # later on remove the full address
    clf1 = cv2.face.LBPHFaceRecognizer_create()  # try _create()
    clf1.read(r"C:\Users\samki\PycharmProjects\pythonProject1\Attendance System\Classifier.xml")  # later on remove the full address

    video_cap = cv2.VideoCapture(0)


    while True:
        ret, img1 = video_cap.read()
        img1 = recognize(img1, clf1, face_cascade1)
        cv2.imshow("Welcome to SnapTrack", img1)

        if cv2.waitKey(1) == 13:
            break
    video_cap.release()
    cv2.destroyAllWindows()


def mark_attendance(n1, s_id1, r1, d1):
    with open("attendance.csv", "r+", newline="\n") as f:
        my_data_list = f.readlines()

        now = datetime.now()
        date_string = now.strftime("%d/%m/%y")
        time_string = now.strftime("%H:%M:%S")
        if len(my_data_list) > 0:
            flag = 0
            for line in my_data_list:
                entry = line.split(",")
                if (str(s_id1) in entry) and entry[0] != '\n':  # should be: s_id1 not in entry...
                    flag = 1
                    break
            if flag != 1:
                f.writelines(f"\n{s_id1},{r1},{n1},{d1},{time_string},{date_string},Present")

        else:
            f.writelines(f"\n{s_id1},{r1},{n1},{d1},{time_string},{date_string},Present")
