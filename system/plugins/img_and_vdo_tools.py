# # Copyright (C) 2021 KeinShin@Github.

# import os

# from system.Config.utils import Variable
# import face_recognition
# from PIL import Image
# import cv2

# import numpy as np
# from system import app


# async def face(client, message):
#  if not message.media:
#      await message.edit("**Are you sure this is image or video?**")
#      return
#  download=await message.download()
#  img = cv2.cvtColor(download, cv2.COLOR_BGR2RGB)
#  encode = face_recognition.face_encodings(img)[0]

#  if "img" in message.text:

#    ok = face_recognition.load_image_file(download)
#    rgb_img = cv2.cvtColor(ok, cv2.COLOR_BGR2RGB)
#    face_loc = face_recognition.face_locations(rgb_img)[0]
#    encode = face_recognition.face_encodings(ok)[0]
#    cv2.rectangle(ok, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2], (255,0,255), 2))
#    cv2.imwrite("rgb.png", cv2.putText(rgb_img))
#    img1 = Image.open(ok)
#    img2 = Image.open(ok)
#    await app.send_message('rgb.png', rgb_img)
   
#    os.remove("rgb.png")
   
#  elif "media" in message.text:
#      cap = cv2.VideoCapture(download)
#      while True:
#         sucesss, read = cap.read()
#         imgs = cv2.resize(img, (0,0), None, 0.25, 0.25) # to reduce time :p
#         imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
#         face_current_frm = face_recognition.face_locations(imgs)[0] # if multiple faces in video.

#         encode = face_recognition.face_encodings(imgs, face_current_frm)
#         for encode_face, face_loc in zip(encode, face_current_frm):
#             matches = face_recognition.compare_faces()

