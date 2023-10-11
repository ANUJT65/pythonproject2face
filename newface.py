import cv2
from simple_facerec import SimpleFacerec
import time
from datetime import datetime, date
import pandas as pd

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

recognized_faces = {}  # Create a dictionary to store recognized faces and their entry time

def markAttendance(name, entry_time, verified_time):
    current_date = date.today().strftime('%Y-%m-%d')
    with open('Attendance.csv', 'a') as f:
        f.write(f'{name},{current_date},{entry_time},{verified_time}\n')

def saveAttendanceToExcel(data):
    df = pd.DataFrame(data, columns=["Name", "Date", "Entry Time", "Verified Time"])
    df.to_excel("Attendance.xlsx", index=False)

# Load the video file
video_file = "elon.mp4"

attendance_data = []

message = "Wait for 5-10 second to verify"

while True:
    ret, frame = cap.read()

    # Print message on screen
    cv2.putText(frame, message, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        # Draw red rectangle around the face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)


        # Print detected face name in terminal
        if name not in recognized_faces:
            recognized_faces[name] = {
                'entry_time': datetime.now(),
                'verified_time_recorded': False
            }
            current_time = recognized_faces[name]['entry_time'].strftime('%H:%M:%S')
            print("Detected your face")

            # Mark attendance
            markAttendance(name, current_time, "")

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

        else:
            entry_time = recognized_faces[name]['entry_time']
            verified_time_recorded = recognized_faces[name]['verified_time_recorded']

            if not verified_time_recorded:
                current_time = datetime.now()
                time_diff = (current_time - entry_time).total_seconds()

                if time_diff >= 20:
                    verified_time = current_time.strftime('%H:%M:%S')
                    recognized_faces[name]['verified_time_recorded'] = True
                    markAttendance(name, "", verified_time)
                    print("Verified time recorded for face: ", name)

                    attendance_data.append([name, date.today().strftime('%Y-%m-%d'), "", verified_time])

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

# Save attendance data to Excel
saveAttendanceToExcel(attendance_data)