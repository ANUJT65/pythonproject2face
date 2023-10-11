import time
import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime, date
import pandas as pd

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

recognized_faces = {}  # Create a dictionary to store recognized faces and their entry time

def markAttendance(name, entry_time, exit_time):
    current_date = date.today().strftime('%Y-%m-%d')
    with open('Attendance.csv', 'a') as f:
        f.write(f'{name},{current_date},{entry_time},{exit_time}\n')

def saveAttendanceToExcel(data):
    df = pd.DataFrame(data, columns=["Name", "Date", "Entry Time", "Exit Time"])
    df.to_excel("Attendance.xlsx", index=False)

# Load the video file
video_file = "elon.mp4"

attendance_data = []

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    # Update recognized_faces dictionary
    for name in face_names:
        if name not in recognized_faces:
            recognized_faces[name] = {
                'entry_time': datetime.now(),
                'stable_timer': time.time()
            }
        else:
            recognized_faces[name]['stable_timer'] = time.time()

    # Print detected face name in terminal after 5-10 seconds
    for name in recognized_faces.keys():
        stable_timer = recognized_faces[name]['stable_timer']
        elapsed_time = time.time() - stable_timer
        if name in face_names and 10 <= elapsed_time <= 15:
            print("Detected face:", name)

    # Update recognized_faces dictionary
    for name in recognized_faces.keys():
        if name not in face_names:
            entry_time = recognized_faces[name]['entry_time']
            exit_time = datetime.now().strftime('%H:%M:%S')
            markAttendance(name, entry_time.strftime('%H:%M:%S'), exit_time)
            attendance_data.append([name, date.today().strftime('%Y-%m-%d'), entry_time.strftime('%H:%M:%S'), exit_time])
            del recognized_faces[name]

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        # Play video if Elon Musk is detected
        if name == "Elon Musk1":
            video_capture = cv2.VideoCapture(video_file)
            while True:
                ret, video_frame = video_capture.read()
                if not ret:
                    break

                cv2.imshow("Video", video_frame)
                if cv2.waitKey(1) == 27:
                    break

            video_capture.release()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Save attendance data to Excel
saveAttendanceToExcel(attendance_data)