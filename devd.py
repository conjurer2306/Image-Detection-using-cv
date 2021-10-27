import io
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.client import GoogleCredentials
#identity card detection using Open CV
gauth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
client=vision.ImageAnnotatorClient()
file_name=os.path.join(
        os.path.dirname(__file__),
        'th.jpe')
with io.open(file_name,'rb') as image_file:
    content=image_file.read()
image=types.Image(content=content)
response=client.label_detection(image=image)
labels =response.label_annotations

print("LABELS;") 
a=[]
s=0
for label in labels:
    print(label.description)
    a.append(label.description)
for i in range (0,len(a)):
     ser1.write(a[i].encode())
     print(s)
     print(a[i])
     s=s+1
    


