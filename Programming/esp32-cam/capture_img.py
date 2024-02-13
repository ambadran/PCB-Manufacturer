import camera

camera.init(0, format=camera.JPEG)

buf = camera.capture()

with open("test3.jpeg", "wb") as f:
    f.write(buf)

camera.deinit()
