import cv2

def check_cameras(max_cameras=10):
    print("🔍 Checking available camera indices...")
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ Camera index {i} is available.")
            cap.release()
        else:
            print(f"❌ Camera index {i} NOT available.")

check_cameras()
