import cv2
import face_recognition

img = cv2.imread("images/Anuj.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

cv2.imshow("Img",img)



img2 = cv2.imread("images/2_Anushka_Waghmare.jpeg")
rgb_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

cv2.imshow("Img2",img2)



img3 = cv2.imread("images/3_Arya_Lokhande.jpeg")
rgb_img3 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

cv2.imshow("Img3",img3)



img4 = cv2.imread("images/7_Ishwar_Borade.jpeg")
rgb_img4 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]




img5 = cv2.imread("images/8_Tanmay_Bora.jpeg")
rgb_img5 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]

cv2.imshow("Img5",img5)



img6 = cv2.imread("images/14_Subodh_Deogade.jpeg")
rgb_img6 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding6 = face_recognition.face_encodings(rgb_img6)[0]

cv2.imshow("Img6",img6)



img7 = cv2.imread("images/21_Purva_Golegaonkar.jpeg")
rgb_img7 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding7 = face_recognition.face_encodings(rgb_img7)[0]

cv2.imshow("Img7",img7)






img9 = cv2.imread("images/42_Mithali_Patil.jpeg")
rgb_img9 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding9 = face_recognition.face_encodings(rgb_img9)[0]

cv2.imshow("Img9",img9)



img10 = cv2.imread("images/52_Pradnyesh_Ravane.jpeg")
rgb_img10 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding10 = face_recognition.face_encodings(rgb_img10)[0]

cv2.imshow("Img10",img10)



img11 = cv2.imread("images/54_Prajyot_Borikar.jpeg")
rgb_img11 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding11 = face_recognition.face_encodings(rgb_img11)[0]

cv2.imshow("Img11",img11)

img12 = cv2.imread("images/55_Pranav_Ratnalikar.jpeg")
rgb_img12 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding12 = face_recognition.face_encodings(rgb_img12)[0]

cv2.imshow("Img12",img12)

img13 = cv2.imread("images/56_Vedant_Rawale.jpeg")
rgb_img13 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding13 = face_recognition.face_encodings(rgb_img13)[0]

cv2.imshow("Img13",img13)


img15 = cv2.imread("images/61_Unnati_Shendge.jpeg")
rgb_img15 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding15 = face_recognition.face_encodings(rgb_img15)[0]

cv2.imshow("Img15",img15)

img16 = cv2.imread("images/66_Tanmay_Mali.jpeg")
rgb_img16 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding16 = face_recognition.face_encodings(rgb_img16)[0]

cv2.imshow("Img16",img16)

img17 = cv2.imread("images/54_Prajyot_Borikar.jpeg")
rgb_img17 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding17 = face_recognition.face_encodings(rgb_img17)[0]

cv2.imshow("Img17",img17)

result= face_recognition.compare_faces([img_encoding],img_encoding2)
print("Result",result)





