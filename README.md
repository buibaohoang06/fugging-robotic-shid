# fugging-robotic-shid
some fuggin robotic shid i gotta do at 3am

# How to use:
Step 1: Upload Firmata to Arduino
![Image of the Firmata File](https://downloader.disk.yandex.ru/preview/a77a15b4d2364010407fcaf98c27e1cb6a7f522f54806e4bf5ebfd299fb8bd42/625a0a69/zpb4LN24rSUaNft-IJhyIwVIbFkC0vx4RITXQDmj753dAOLsHXFplmrITGqp__WjIOlTCqYLZoyo1AgP2Zh7bA%3D%3D?uid=0&filename=Screen%20Shot%202022-04-16%20at%2003.14.12.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048)
- Upload the firmata.ino file to the Arduino (DO NOT CHANGE SERIAL PORT NUMBER - DEFAULT AT 57600)

Step 2: Download pyFirmata module
- Download pyFirmata with PyPi using pip install pyFirmata or python3 -m pip install pyFirmata
- ![Image of installing pyFirmata](https://4.downloader.disk.yandex.com/preview/ec2403eb5c27052c76000dd1a50b047b0db49f15909ada30c5096b9325aa93ac/inf/ymq7rHYIQkVrOpYACXzJ7f0L5eeB4BYUngKszgGDqlgxnprlWUn8yAlohzI3G1_xOQqI5-2l80iNm5pd1HDh2w%3D%3D?uid=1613175372&filename=Screen%20Shot%202022-04-16%20at%2003.17.38.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1613175372&tknv=v2&size=1920x970)

Step 3: Configure the files
- Install FastAPI (pip install FastAPI / python3 -m pip install FastAPI) and install uvicorn to host API server (pip install 'uvicorn[standard]' / python3 -m pip install 'uvicorn[standard]')
- Run the main.py file to host API with command uvicorn main:app --reload | python3 -m uvicorn main:app --reload (This will host the FastAPI on your local computer)

Step 4: Start Facial Recognition software
- Install dependencies: opencv-python and face_recognition with PyPi
- Run the cum.py file with python3 cum.py

# Make sure the shid.json file is empty before starting the program for best performance
