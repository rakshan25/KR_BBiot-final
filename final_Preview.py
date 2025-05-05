#rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101
# cap1 = cv2.VideoCapture("rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101")
# cap2 = cv2.VideoCapture("rtsp://admin:Vit@12345@192.168.1.65:554/Streaming/Channels/101")

#ONVIF for IP cameras also the another procedure to get it



                                     #CODE - 2A1
#Image format detects the class name centering sheet alone and updates the image and csv in to aws
#
# import cv2
# import os
# import time
# import pandas as pd
# from ultralytics import YOLO
# from datetime import datetime
# import threading
# import boto3
#
# # Load the YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")
#
# # === Input Image Path (placed right after model load) ===
# image_path = "C:\\Users\\kulas\\Downloads\\centering5.jpg"  # Replace with your image
#
# # Class names
# class_names = ['centering sheet']
#
# # Directory to save output logs
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # S3 setup
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# BUCKET_NAME = 'ubuntu20'
#
# s3 = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
#
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
#
# def detect_from_image(image_path):
#     # Read image
#     frame = cv2.imread(image_path)
#     if frame is None:
#         print("Error: Could not read image.")
#         return
#
#     # Inference
#     results = model(frame)
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     frame_class_counts = {name: 0 for name in class_names}
#     total_count = 0
#
#     for result in results:
#         for box in result.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])
#             class_index = int(box.cls.tolist()[0])
#
#             if class_index < len(class_names):
#                 class_name = class_names[class_index]
#                 confidence_score = f"{box.conf.item():.2f}"
#
#                 # Draw bounding box
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame, f'{class_name} {confidence_score}',
#                             (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
#                             (0, 255, 0), 2)
#
#                 frame_class_counts[class_name] += 1
#                 total_count += 1
#
#     # Overlay counts
#     cv2.putText(frame, f'Total Count: {total_count}', (10, 30),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
#
#     y_offset = 60
#     for cls, count in frame_class_counts.items():
#         cv2.putText(frame, f'{cls}: {count}', (10, y_offset),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#         y_offset += 25
#
#     # Save detection result image
#     image_name = os.path.basename(image_path)
#     save_path = os.path.join(output_directory, f"detected_{image_name}")
#     cv2.imwrite(save_path, frame)
#
#     # Upload image to S3
#     upload_to_s3(save_path, BUCKET_NAME, f"detected_{image_name}")
#
#     # Save metadata to CSV
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     row = {
#         'Timestamp': current_time,
#         'Image': image_name,
#         'Total Count': total_count,
#         'Class Counts': frame_class_counts
#     }
#
#     # Append or create CSV
#     if os.path.exists(csv_filename):
#         df = pd.read_csv(csv_filename)
#         df = df._append(row, ignore_index=True)
#     else:
#         df = pd.DataFrame([row])
#
#     df.to_csv(csv_filename, index=False)
#
#     # Upload CSV
#     upload_to_s3(csv_filename, BUCKET_NAME, 'detection_log.csv')
#
#     print("Detection complete.")
#     cv2.imshow("Detection Result", frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# # ======= Call the Function ========
# detect_from_image(image_path)





                                    #CODE- 2A4
# This is seperate code and image update to aws for PROPS with send the image results as CSV and image format

# import cv2
# import pandas as pd
# import os
# from ultralytics import YOLO
# from datetime import datetime
# import boto3
#
# # Load YOLO ONNX model
# model_path = "C:\\Users\\kulas\\Downloads\\BBIOT project\\bestOPR.onnx"
# model = YOLO(model_path)
#
# # Input image path
# image_path = ("C:\\Users\\kulas\\Downloads\\samples for testing\\props1.jpg")
# frame = cv2.imread(image_path)
# if frame is None:
#     print("Error: Could not read the image.")
#     exit()
#
# # Detection class
# target_class = "props"
#
# # Output directory for logs and results
# output_dir = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_dir, exist_ok=True)
#
# # AWS S3 Configuration - use environment variables for safety
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# BUCKET_NAME = 'ubuntu20'
#
# # Initialize boto3 S3 client
# s3 = boto3.client('s3',
#                   aws_access_key_id=AWS_ACCESS_KEY,
#                   aws_secret_access_key=AWS_SECRET_KEY)
#
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"[S3 Upload] Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"[S3 Upload] Failed to upload {file_path}: {e}")
#
#
# # Run YOLO detection
# results = model(frame)[0]
#
# detections = []
# frame_count = 1
# class_counts = {target_class: 0}
#
# for box in results.boxes:
#     cls_id = int(box.cls[0])
#     confidence = float(box.conf[0])
#     label = model.names[cls_id]
#
#     if label == target_class:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         # Draw bounding box
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#
#         # Count and store detection info
#         class_counts[label] += 1
#         detections.append({
#             'Class': label,
#             'Confidence': round(confidence, 2),
#             'X1': x1,
#             'Y1': y1,
#             'X2': x2,
#             'Y2': y2,
#             'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         })
#
# # Draw total count and class count on image
# y_offset = 30
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 0.8
# color = (0, 255, 255)
# thickness = 2
#
# total_count = sum(class_counts.values())
# cv2.putText(frame, f"Total props count: {total_count}", (10, y_offset), font, font_scale, color, thickness)
#
# for cls, count in class_counts.items():
#     y_offset += 30
#     cv2.putText(frame, f"{cls}: {count}", (10, y_offset), font, font_scale, color, thickness)
#
# # Save image with bounding boxes and count
# output_image_path = os.path.join(output_dir, f"final_detection_{frame_count}.jpg")
# cv2.imwrite(output_image_path, frame)
# upload_to_s3(output_image_path, BUCKET_NAME, f"final_detection_{frame_count}.jpg")
#
# # Save detection data to CSV
# if detections:
#     csv_path = os.path.join(output_dir, 'detection_log.csv')
#     df = pd.DataFrame(detections)
#     df.to_csv(csv_path, index=False)
#     upload_to_s3(csv_path, BUCKET_NAME, 'detection_log.csv')
# else:
#     print("[INFO] No 'props' class detected.")
#
# print("[DONE] Detection, annotation, and upload complete.")
#
# # Display the image with detections
# cv2.imshow("YOLO Detection", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()















                                     #CODE - 2A3
# This is seperate code and image update to aws for span model

# import cv2
# import pandas as pd
# import os
# from ultralytics import YOLO
# from datetime import datetime
# import boto3
#
# # Load YOLO ONNX model
# model_path = "C:\\Users\\kulas\\Downloads\\BBIOT project\\best4SP.onnx"
# model = YOLO(model_path)
#
# # Input image path
# image_path = "C:\\Users\\kulas\\Downloads\\samples for testing\\span02.jpg"
# frame = cv2.imread(image_path)
# if frame is None:
#     print("Error: Could not read the image.")
#     exit()
#
# # Detection class
# target_class = "span"
#
# # Output directory for logs and results
# output_dir = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_dir, exist_ok=True)
#
# # AWS S3 Configuration - use environment variables for safety
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# BUCKET_NAME = 'ubuntu20'
#
# # Initialize boto3 S3 client
# s3 = boto3.client('s3',
#                   aws_access_key_id=AWS_ACCESS_KEY,
#                   aws_secret_access_key=AWS_SECRET_KEY)
#
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"[S3 Upload] Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"[S3 Upload] Failed to upload {file_path}: {e}")
#
#
# # Run YOLO detection
# results = model(frame)[0]
#
# detections = []
# frame_count = 1
# class_counts = {target_class: 0}
#
# for box in results.boxes:
#     cls_id = int(box.cls[0])
#     confidence = float(box.conf[0])
#     label = model.names[cls_id]
#
#     if label == target_class:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         # Draw bounding box
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#
#         # Count and store detection info
#         class_counts[label] += 1
#         detections.append({
#             'Class': label,
#             'Confidence': round(confidence, 2),
#             'X1': x1,
#             'Y1': y1,
#             'X2': x2,
#             'Y2': y2,
#             'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         })
#
# # Draw total count and class count on image
# y_offset = 30
# font = cv2.FONT_HERSHEY_SIMPLEX
# font_scale = 0.8
# color = (0, 255, 255)
# thickness = 2
#
# total_count = sum(class_counts.values())
# cv2.putText(frame, f"Total span count: {total_count}", (10, y_offset), font, font_scale, color, thickness)
#
# for cls, count in class_counts.items():
#     y_offset += 30
#     cv2.putText(frame, f"{cls}: {count}", (10, y_offset), font, font_scale, color, thickness)
#
# # Save image with bounding boxes and count
# output_image_path = os.path.join(output_dir, f"final_detection_{frame_count}.jpg")
# cv2.imwrite(output_image_path, frame)
# upload_to_s3(output_image_path, BUCKET_NAME, f"final_detection_{frame_count}.jpg")
#
# # Save detection data to CSV
# if detections:
#     csv_path = os.path.join(output_dir, 'detection_log.csv')
#     df = pd.DataFrame(detections)
#     df.to_csv(csv_path, index=False)
#     upload_to_s3(csv_path, BUCKET_NAME, 'detection_log.csv')
# else:
#     print("[INFO] No 'span' class detected.")
#
# print("[DONE] Detection, annotation, and upload complete.")
#
# # Display the image with detections
# cv2.imshow("YOLO Detection", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


                                                #Code- 3A1
#for the code i have implemented the deepsort algorithm to implement the seperate detection for the centering sheet
# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Load the YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")
#
# # Initialize DeepSORT Tracker
# tracker = DeepSort(max_age=30)
#
# # Create a VideoCapture object for the camera
# cap = cv2.VideoCapture("rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101")
# if not cap.isOpened():
#     print("Error: Could not access the camera.")
#     exit()
#
# # Class names
# class_names = ['centering sheet']
#
# # Directory to save output logs
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # S3 client initialization
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# BUCKET_NAME = 'ubuntu20'
#
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
# CAPTURE_INTERVAL = 3  # Capture a frame every 3 seconds
# CSV_UPLOAD_INTERVAL = 5  # Upload CSV data every 5 seconds
#
# data = []
# last_capture_time = time.time()
# last_csv_upload_time = time.time()
#
# tracked_ids = set()
# class_counts = {name: 0 for name in class_names}
# total_count = 0
#
# def save_and_upload(frame, frame_count):
#     capture_filename = os.path.join(output_directory, f"frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     threading.Thread(target=upload_to_s3, args=(capture_filename, BUCKET_NAME, f"frame_{frame_count}.jpg")).start()
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv')).start()
#
# try:
#     frame_count = 1
#     while True:
#         current_time_seconds = time.time()
#
#         ret, frame = cap.read()
#         if not ret:
#             print("Frame capture failed. Attempting to recover...")
#             time.sleep(1)
#             continue
#
#         results = model(frame, save=False)
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         frame_class_counts = {name: 0 for name in class_names}
#
#         detections = []
#         for result in results:
#             for box in result.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])
#                 class_index = int(box.cls.tolist()[0])
#                 confidence_score = float(box.conf.tolist()[0])
#                 class_name = class_names[class_index]
#                 detections.append([[x1, y1, x2, y2], confidence_score, class_name])
#
#         # Use DeepSORT to track objects
#         tracked_objects = tracker.update_tracks(detections, frame=frame)
#         for track in tracked_objects:
#             if not track.is_confirmed():
#                 continue
#             track_id = track.track_id
#             if track_id not in tracked_ids:
#                 tracked_ids.add(track_id)
#                 class_name = track.get_det_class()
#                 class_counts[class_name] += 1
#                 total_count += 1
#
#             ltrb = track.to_ltrb()
#             x1, y1, x2, y2 = map(int, ltrb)
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f'ID: {track_id} {class_name}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#         data.append({
#             'Timestamp': current_time,
#             'Frame': frame_count,
#             'Total Count': total_count,
#             'Class Counts': class_counts.copy(),
#         })
#
#         cv2.putText(frame, f'Total Count: {total_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#         cv2.putText(frame, f'centering sheet: {class_counts["centering sheet"]}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#         if current_time_seconds - last_capture_time >= CAPTURE_INTERVAL:
#             save_and_upload(frame, frame_count)
#             last_capture_time = current_time_seconds
#             frame_count += 1
#
#         if current_time_seconds - last_csv_upload_time >= CSV_UPLOAD_INTERVAL:
#             save_csv(data)
#             last_csv_upload_time = current_time_seconds
#
#         cv2.imshow("Real-Time Object Detection", frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     print("Video capture and object detection have been terminated.")











                                            #code- 3A2
#In this code i have implemented the Deepsort algorithm with the above code when will mark the seperate id for each tracking and maintain this for
#Props and span in this
#
# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Load the YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestPS.onnx")
#
# # Initialize DeepSORT Tracker
# tracker = DeepSort(max_age=30)
#
# # Create a VideoCapture object for the camera
# cap = cv2.VideoCapture("rtsp://admin:Kulass123@192.168.1.65:554/Streaming/Channels/101")
# if not cap.isOpened():
#     print("Error: Could not access the camera.")
#     exit()
#
# # Class names
# class_names = ['prop', 'span']
#
# # Directory to save output logs
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # S3 client initialization
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# BUCKET_NAME = 'ubuntu20'
#
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
#
# CAPTURE_INTERVAL = 3  # Capture a frame every 3 seconds
# CSV_UPLOAD_INTERVAL = 5  # Upload CSV data every 5 seconds
#
# data = []
# last_capture_time = time.time()
# last_csv_upload_time = time.time()
#
# tracked_ids = set()
# class_counts = {name: 0 for name in class_names}
# total_count = 0
#
#
# def save_and_upload(frame, frame_count):
#     capture_filename = os.path.join(output_directory, f"frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     threading.Thread(target=upload_to_s3, args=(capture_filename, BUCKET_NAME, f"frame_{frame_count}.jpg")).start()
#
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv')).start()
#
#
# try:
#     frame_count = 1
#     while True:
#         current_time_seconds = time.time()
#
#         ret, frame = cap.read()
#         if not ret:
#             print("Frame capture failed. Attempting to recover...")
#             time.sleep(1)
#             continue
#
#         results = model(frame, save=False)
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         frame_class_counts = {name: 0 for name in class_names}
#
#         detections = []
#         for result in results:
#             for box in result.boxes:
#                 x1, y1, x2, y2 = map(int, box.xyxy.tolist()[0])
#                 class_index = int(box.cls.tolist()[0])
#                 confidence_score = float(box.conf.tolist()[0])
#                 class_name = class_names[class_index]
#                 detections.append([[x1, y1, x2, y2], confidence_score, class_name])
#
#         # Use DeepSORT to track objects
#         tracked_objects = tracker.update_tracks(detections, frame=frame)
#         for track in tracked_objects:
#             if not track.is_confirmed():
#                 continue
#             track_id = track.track_id
#             if track_id not in tracked_ids:
#                 tracked_ids.add(track_id)
#                 class_name = track.get_det_class()
#                 class_counts[class_name] += 1
#                 total_count += 1
#
#             ltrb = track.to_ltrb()
#             x1, y1, x2, y2 = map(int, ltrb)
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#             cv2.putText(frame, f'ID: {track_id} {class_name}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
#                         (0, 255, 0), 2)
#
#         data.append({
#             'Timestamp': current_time,
#             'Frame': frame_count,
#             'Total Count': total_count,
#             'Class Counts': class_counts.copy(),
#         })
#
#         cv2.putText(frame, f'Total Count: {total_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#         cv2.putText(frame, f'prop: {class_counts["prop"]}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#         cv2.putText(frame, f'span: {class_counts["span"]}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
#
#         if current_time_seconds - last_capture_time >= CAPTURE_INTERVAL:
#             save_and_upload(frame, frame_count)
#             last_capture_time = current_time_seconds
#             frame_count += 1
#
#         if current_time_seconds - last_csv_upload_time >= CSV_UPLOAD_INTERVAL:
#             save_csv(data)
#             last_csv_upload_time = current_time_seconds
#
#         cv2.imshow("Real-Time Object Detection", frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     print("Video capture and object detection have been terminated.")










# username -admin
# password for cp cp plus - Vit@12345
# cap1 = cv2.VideoCapture("rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101")
# cap2 = cv2.VideoCapture("rtsp://admin:Vit@12345@192.168.1.65:554/Streaming/Channels/101")




          #                                    CODE-4A
# Here i used the DUAL camera with deepsort algorithm detecting different classes of objects in the seperate and
#send to the AWS

#
#
# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Initialize DeepSORT trackers
# tracker1 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)
# tracker2 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)
#
# # Load YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")
#
# # Initialize video captures
# cap1 = cv2.VideoCapture("rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101")
# cap2 = cv2.VideoCapture("rtsp://admin:Kulass123@192.168.1.65:554/Streaming/Channels/101")
#
# if not cap1.isOpened():
#     print("Error: Could not access the first camera.")
#     exit()
# if not cap2.isOpened():
#     print("Error: Could not access the second camera.")
#     exit()
#
# class_names = ['centering_sheet', 'prop', 'span']
#
# # Output directory
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # AWS S3
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
# BUCKET_NAME = 'ubuntu20'
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
# cy1 = 322
# crossed_ids1 = set()
# crossed_ids2 = set()
# cumulative_total_count1 = 0
# cumulative_total_count2 = 0
# data = []
# last_capture_time = time.time()
# last_csv_save_time = time.time()
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
# def save_and_upload(frame, frame_count, camera_num):
#     capture_filename = os.path.join(output_directory, f"cam{camera_num}_frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     thread = threading.Thread(target=upload_to_s3,
#                               args=(capture_filename, BUCKET_NAME, f"cam{camera_num}_frame_{frame_count}.jpg"))
#     thread.start()
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     thread_csv = threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv'))
#     thread_csv.start()
#
# try:
#     frame_count = 1
#     while True:
#         ret1, frame1 = cap1.read()
#         ret2, frame2 = cap2.read()
#
#         if not ret1 or not ret2:
#             print("Failed to grab frame from camera.")
#             break
#
#         # Process Camera 1
#         results1 = model(frame1, save=False)
#         detections1 = []
#         counts1 = {name: 0 for name in class_names}
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         if results1:
#             for result in results1:
#                 boxes = result.boxes
#                 for box in boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                     conf = float(box.conf[0])
#                     cls_id = int(box.cls[0])
#                     class_name = class_names[cls_id]
#                     detections1.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#             tracks1 = tracker1.update_tracks(detections1, frame=frame1)
#
#             for track in tracks1:
#                 if not track.is_confirmed():
#                     continue
#                 track_id = track.track_id
#                 ltrb = track.to_ltrb()
#                 x1, y1, x2, y2 = map(int, ltrb)
#                 class_name = track.det_class
#
#                 cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame1, f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                 bottom_center_y = (y1 + y2) / 2
#                 if track_id not in crossed_ids1:
#                     counts1[class_name] += 1
#                     cumulative_total_count1 += 1
#                     crossed_ids1.add(track_id)
#
#         # Process Camera 2
#         results2 = model(frame2, save=False)
#         detections2 = []
#         counts2 = {name: 0 for name in class_names}
#
#         if results2:
#             for result in results2:
#                 boxes = result.boxes
#                 for box in boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                     conf = float(box.conf[0])
#                     cls_id = int(box.cls[0])
#                     class_name = class_names[cls_id]
#                     detections2.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#             tracks2 = tracker2.update_tracks(detections2, frame=frame2)
#
#             for track in tracks2:
#                 if not track.is_confirmed():
#                     continue
#                 track_id = track.track_id
#                 ltrb = track.to_ltrb()
#                 x1, y1, x2, y2 = map(int, ltrb)
#                 class_name = track.det_class
#
#                 cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame2, f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                 bottom_center_y = (y1 + y2) / 2
#                 if track_id not in crossed_ids2:
#                     counts2[class_name] += 1
#                     cumulative_total_count2 += 1
#                     crossed_ids2.add(track_id)
#
#         # Remove cv2.line (line detection removed completely)
#
#         data.append({
#             'Timestamp': current_time,
#             'Frame': frame_count,
#             'Camera1_Total': cumulative_total_count1,
#             'Camera1_Counts': counts1,
#             'Camera2_Total': cumulative_total_count2,
#             'Camera2_Counts': counts2
#         })
#
#         count_str1 = f"Total: {cumulative_total_count1} | " + ", ".join([f"{k}:{v}" for k, v in counts1.items()])
#         count_str2 = f"Total: {cumulative_total_count2} | " + ", ".join([f"{k}:{v}" for k, v in counts2.items()])
#
#         cv2.putText(frame1, count_str1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#         cv2.putText(frame2, count_str2, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#
#         # === UPDATED TIMERS BELOW ===
#         current_time_sec = time.time()
#
#         # Send frame to AWS every 3 seconds
#         if current_time_sec - last_capture_time >= 3:
#             save_and_upload(frame1, frame_count, 1)
#             save_and_upload(frame2, frame_count, 2)
#             last_capture_time = current_time_sec
#
#         # Save and upload CSV every 2 seconds
#         if current_time_sec - last_csv_save_time >= 2:
#             save_csv(data)
#             last_csv_save_time = current_time_sec
#
#         cv2.imshow("Camera 1 Tracking", frame1)
#         cv2.imshow("Camera 2 Tracking", frame2)
#
#         frame_count += 1
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"Error: {str(e)}")
#
# finally:
#     cap1.release()
#     cap2.release()
#     cv2.destroyAllWindows()
#     for thread in threading.enumerate():
#         if thread != threading.current_thread():
#             thread.join()
#     print("Processing stopped.")








                                       # Code- 4B
#Dual camera for the classes props and span for detection and it will update the class count in seperate and
# total count will be also present in that


#
# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Initialize DeepSORT trackers
# tracker1 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)
# tracker2 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)
#
# # Load YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestPS.onnx")
#
# # Initialize video captures
# cap1 = cv2.VideoCapture("C:\\Users\\kulas\\Downloads\\samples for testing\\video03.mp4")
# cap2 = cv2.VideoCapture("C:\\Users\\kulas\\Downloads\\samples for testing\\video02.mp4")
#
# if not cap1.isOpened():
#     print("Error: Could not access the first camera.")
#     exit()
# if not cap2.isOpened():
#     print("Error: Could not access the second camera.")
#     exit()
#
# # Only keeping "prop" and "span"
# class_names = ['prop', 'span']
#
# # Output directory
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # AWS S3
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
# BUCKET_NAME = 'ubuntu20'
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
# crossed_ids1 = set()
# crossed_ids2 = set()
# cumulative_total_count1 = 0
# cumulative_total_count2 = 0
# cumulative_class_counts1 = {name: 0 for name in class_names}
# cumulative_class_counts2 = {name: 0 for name in class_names}
# data = []
# last_capture_time = time.time()
# last_csv_save_time = time.time()
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
# def save_and_upload(frame, frame_count, camera_num):
#     capture_filename = os.path.join(output_directory, f"cam{camera_num}_frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     thread = threading.Thread(target=upload_to_s3,
#                               args=(capture_filename, BUCKET_NAME, f"cam{camera_num}_frame_{frame_count}.jpg"))
#     thread.start()
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     thread_csv = threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv'))
#     thread_csv.start()
#
# try:
#     frame_count = 1
#     while True:
#         ret1, frame1 = cap1.read()
#         ret2, frame2 = cap2.read()
#
#         if not ret1 or not ret2:
#             print("Failed to grab frame from camera.")
#             break
#
#         results1 = model(frame1, save=False)
#         detections1 = []
#         counts1 = {name: 0 for name in class_names}
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#         if results1:
#             for result in results1:
#                 boxes = result.boxes
#                 for box in boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                     conf = float(box.conf[0])
#                     cls_id = int(box.cls[0])
#                     if cls_id >= len(class_names):
#                         continue
#                     class_name = class_names[cls_id]
#                     detections1.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#             tracks1 = tracker1.update_tracks(detections1, frame=frame1)
#
#             for track in tracks1:
#                 if not track.is_confirmed():
#                     continue
#                 track_id = track.track_id
#                 ltrb = track.to_ltrb()
#                 x1, y1, x2, y2 = map(int, ltrb)
#                 class_name = track.det_class
#
#                 if class_name not in class_names:
#                     continue
#
#                 cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame1, f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                 if track_id not in crossed_ids1:
#                     counts1[class_name] += 1
#                     cumulative_class_counts1[class_name] += 1
#                     cumulative_total_count1 += 1
#                     crossed_ids1.add(track_id)
#
#         # Camera 2
#         results2 = model(frame2, save=False)
#         detections2 = []
#         counts2 = {name: 0 for name in class_names}
#
#         if results2:
#             for result in results2:
#                 boxes = result.boxes
#                 for box in boxes:
#                     x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                     conf = float(box.conf[0])
#                     cls_id = int(box.cls[0])
#                     if cls_id >= len(class_names):
#                         continue
#                     class_name = class_names[cls_id]
#                     detections2.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#             tracks2 = tracker2.update_tracks(detections2, frame=frame2)
#
#             for track in tracks2:
#                 if not track.is_confirmed():
#                     continue
#                 track_id = track.track_id
#                 ltrb = track.to_ltrb()
#                 x1, y1, x2, y2 = map(int, ltrb)
#                 class_name = track.det_class
#
#                 if class_name not in class_names:
#                     continue
#
#                 cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                 cv2.putText(frame2, f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                 if track_id not in crossed_ids2:
#                     counts2[class_name] += 1
#                     cumulative_class_counts2[class_name] += 1
#                     cumulative_total_count2 += 1
#                     crossed_ids2.add(track_id)
#
#         data.append({
#             'Timestamp': current_time,
#             'Frame': frame_count,
#             'Camera1_Total': cumulative_total_count1,
#             'Camera1_Counts': counts1,
#             'Camera2_Total': cumulative_total_count2,
#             'Camera2_Counts': counts2
#         })
#
#         # Display Total Count
#         cv2.putText(frame1, f"Total: {cumulative_total_count1}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
#         y_offset = 60
#         for cls in class_names:
#             cv2.putText(frame1, f"{cls}: {cumulative_class_counts1[cls]}", (10, y_offset),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#             y_offset += 30
#
#         cv2.putText(frame2, f"Total: {cumulative_total_count2}", (10, 30),
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
#         y_offset = 60
#         for cls in class_names:
#             cv2.putText(frame2, f"{cls}: {cumulative_class_counts2[cls]}", (10, y_offset),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
#             y_offset += 30
#
#         current_time_sec = time.time()
#
#         if current_time_sec - last_capture_time >= 3:
#             save_and_upload(frame1, frame_count, 1)
#             save_and_upload(frame2, frame_count, 2)
#             last_capture_time = current_time_sec
#
#         if current_time_sec - last_csv_save_time >= 2:
#             save_csv(data)
#             last_csv_save_time = current_time_sec
#
#         cv2.imshow("Camera 1 Tracking", frame1)
#         cv2.imshow("Camera 2 Tracking", frame2)
#
#         frame_count += 1
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"Error: {str(e)}")
#
# finally:
#     cap1.release()
#     cap2.release()
#     cv2.destroyAllWindows()
#     for thread in threading.enumerate():
#         if thread != threading.current_thread():
#             thread.join()
#     print("Processing stopped.")










#                                      CODE- 5A1
#FOUR CAMERA SUPPORT IS FOR PROPS AND SPAN , which will do the same thing which will send the data in csv and image to aws
# FOR USB

# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Initialize DeepSORT trackers for 4 cameras
# trackers = [DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0) for _ in range(4)]
#
# # Load YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")
#
# # Initialize USB cameras (change indices if required)
# caps = [cv2.VideoCapture(i) for i in range(4)]
# for idx, cap in enumerate(caps):
#     if not cap.isOpened():
#         print(f"Error: Could not access camera {idx + 1}.")
#         exit()
#
# # Class names: Only use 'prop' and 'span'
# class_names = ['prop', 'span']  # index 0: prop, 1: span
#
# # Output directory setup
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # AWS S3 configuration
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
# BUCKET_NAME = 'ubuntu20'
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
# # Tracking variables
# crossed_ids = [set() for _ in range(4)]
# cumulative_total_count = [0 for _ in range(4)]
# data = []
# last_capture_time = time.time()
# last_csv_save_time = time.time()
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
# def save_and_upload(frame, frame_count, camera_num):
#     capture_filename = os.path.join(output_directory, f"cam{camera_num}_frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     thread = threading.Thread(target=upload_to_s3,
#                               args=(capture_filename, BUCKET_NAME, f"cam{camera_num}_frame_{frame_count}.jpg"))
#     thread.start()
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     thread_csv = threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv'))
#     thread_csv.start()
#
# try:
#     frame_count = 1
#     while True:
#         frames = []
#         rets = []
#
#         for cap in caps:
#             ret, frame = cap.read()
#             rets.append(ret)
#             frames.append(frame)
#
#         if not all(rets):
#             print("Failed to grab frame from one or more cameras.")
#             break
#
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         current_time_sec = time.time()
#
#         log_row = {'Timestamp': current_time, 'Frame': frame_count}
#
#         for i in range(4):
#             results = model(frames[i], save=False)
#             detections = []
#             counts = {name: 0 for name in class_names}
#
#             if results:
#                 for result in results:
#                     boxes = result.boxes
#                     for box in boxes:
#                         x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                         conf = float(box.conf[0])
#                         cls_id = int(box.cls[0])
#                         if cls_id >= len(class_names):
#                             continue
#                         class_name = class_names[cls_id]
#                         detections.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#                 tracks = trackers[i].update_tracks(detections, frame=frames[i])
#
#                 for track in tracks:
#                     if not track.is_confirmed():
#                         continue
#                     track_id = track.track_id
#                     ltrb = track.to_ltrb()
#                     x1, y1, x2, y2 = map(int, ltrb)
#                     class_name = track.det_class
#
#                     cv2.rectangle(frames[i], (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.putText(frames[i], f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                     if track_id not in crossed_ids[i]:
#                         counts[class_name] += 1
#                         cumulative_total_count[i] += 1
#                         crossed_ids[i].add(track_id)
#
#             # Update log and draw total + per-class count
#             log_row[f"Camera{i + 1}_Total"] = cumulative_total_count[i]
#             log_row[f"Camera{i + 1}_Counts"] = counts
#
#             count_str = f"Total: {cumulative_total_count[i]} | " + ", ".join([f"{k}:{v}" for k, v in counts.items()])
#             y_offset = 30
#             for idx, (k, v) in enumerate(counts.items()):
#                 cv2.putText(frames[i], f"{k}: {v}", (10, y_offset + idx * 20),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#             cv2.putText(frames[i], count_str, (10, y_offset + len(counts) * 20),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#
#             # Show each camera
#             cv2.imshow(f"Camera {i + 1}", frames[i])
#
#             if current_time_sec - last_capture_time >= 3:
#                 save_and_upload(frames[i], frame_count, i + 1)
#
#         if current_time_sec - last_csv_save_time >= 10:
#             data.append(log_row)
#             save_csv(data)
#             last_csv_save_time = current_time_sec
#             data.clear()
#
#         frame_count += 1
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"Error: {str(e)}")
#
# finally:
#     for cap in caps:
#         cap.release()
#     cv2.destroyAllWindows()
#     for thread in threading.enumerate():
#         if thread != threading.current_thread():
#             thread.join()
#     print("Processing stopped.")


                                            #CODE- 5A2
           # Connecting the four cameras for the centering sheet in the Model with the same code structure
#
# import cv2
# import pandas as pd
# import time
# from ultralytics import YOLO
# import os
# from datetime import datetime
# import threading
# import boto3
# from deep_sort_realtime.deepsort_tracker import DeepSort
#
# # Initialize DeepSORT trackers for 4 cameras
# trackers = [DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0) for _ in range(4)]
#
# # Load YOLO model
# model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")
#
# # Initialize USB cameras (change indices if required)
# caps = [cv2.VideoCapture(i) for i in range(4)]
# for idx, cap in enumerate(caps):
#     if not cap.isOpened():
#         print(f"Error: Could not access camera {idx + 1}.")
#         exit()
#
# # Class names: only 'centering sheet'
# class_names = ['centering sheet']
#
# # Output directory setup
# output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
# os.makedirs(output_directory, exist_ok=True)
#
# # AWS S3 configuration
# AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
# AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
# BUCKET_NAME = 'ubuntu20'
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
#
# # Tracking variables
# crossed_ids = [set() for _ in range(4)]
# cumulative_total_count = [0 for _ in range(4)]
# data = []
# last_capture_time = time.time()
# last_csv_save_time = time.time()
#
# def upload_to_s3(file_path, bucket_name, s3_path):
#     try:
#         s3.upload_file(file_path, bucket_name, s3_path)
#         print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
#     except Exception as e:
#         print(f"Error uploading {file_path}: {e}")
#
# def save_and_upload(frame, frame_count, camera_num):
#     capture_filename = os.path.join(output_directory, f"cam{camera_num}_frame_{frame_count}.jpg")
#     cv2.imwrite(capture_filename, frame)
#     thread = threading.Thread(target=upload_to_s3,
#                               args=(capture_filename, BUCKET_NAME, f"cam{camera_num}_frame_{frame_count}.jpg"))
#     thread.start()
#
# def save_csv(data):
#     csv_filename = os.path.join(output_directory, 'detection_log.csv')
#     df = pd.DataFrame(data)
#     df.to_csv(csv_filename, index=False)
#     thread_csv = threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv'))
#     thread_csv.start()
#
# try:
#     frame_count = 1
#     while True:
#         frames = []
#         rets = []
#
#         for cap in caps:
#             ret, frame = cap.read()
#             rets.append(ret)
#             frames.append(frame)
#
#         if not all(rets):
#             print("Failed to grab frame from one or more cameras.")
#             break
#
#         current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         current_time_sec = time.time()
#
#         log_row = {'Timestamp': current_time, 'Frame': frame_count}
#
#         for i in range(4):
#             results = model(frames[i], save=False)
#             detections = []
#             counts = {name: 0 for name in class_names}
#
#             if results:
#                 for result in results:
#                     boxes = result.boxes
#                     for box in boxes:
#                         x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                         conf = float(box.conf[0])
#                         cls_id = int(box.cls[0])
#                         if cls_id >= len(class_names):
#                             continue
#                         class_name = class_names[cls_id]
#                         detections.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))
#
#                 tracks = trackers[i].update_tracks(detections, frame=frames[i])
#
#                 for track in tracks:
#                     if not track.is_confirmed():
#                         continue
#                     track_id = track.track_id
#                     ltrb = track.to_ltrb()
#                     x1, y1, x2, y2 = map(int, ltrb)
#                     class_name = track.det_class
#
#                     cv2.rectangle(frames[i], (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.putText(frames[i], f"{class_name} ID:{track_id}", (x1, y1 - 10),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#
#                     if track_id not in crossed_ids[i]:
#                         counts[class_name] += 1
#                         cumulative_total_count[i] += 1
#                         crossed_ids[i].add(track_id)
#
#             # Update log and draw total + per-class count
#             log_row[f"Camera{i + 1}_Total"] = cumulative_total_count[i]
#             log_row[f"Camera{i + 1}_Counts"] = counts
#
#             count_str = f"Total: {cumulative_total_count[i]} | " + ", ".join([f"{k}:{v}" for k, v in counts.items()])
#             y_offset = 30
#             for idx, (k, v) in enumerate(counts.items()):
#                 cv2.putText(frames[i], f"{k}: {v}", (10, y_offset + idx * 20),
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
#             cv2.putText(frames[i], count_str, (10, y_offset + len(counts) * 20),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#
#             # Show each camera
#             cv2.imshow(f"Camera {i + 1}", frames[i])
#
#             if current_time_sec - last_capture_time >= 3:
#                 save_and_upload(frames[i], frame_count, i + 1)
#
#         if current_time_sec - last_csv_save_time >= 10:
#             data.append(log_row)
#             save_csv(data)
#             last_csv_save_time = current_time_sec
#             data.clear()
#
#         frame_count += 1
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
# except Exception as e:
#     print(f"Error: {str(e)}")
#
# finally:
#     for cap in caps:
#         cap.release()
#     cv2.destroyAllWindows()
#     for thread in threading.enumerate():
#         if thread != threading.current_thread():
#             thread.join()
#     print("Processing stopped.")





                     #Double camera with the object detection less or more in that part



#  I have created the code in a such a way that the total number of sheets will be counted added or subtracted
# based on the live detection

import cv2
import pandas as pd
import time
from ultralytics import YOLO
import os
from datetime import datetime
import threading
import boto3
from deep_sort_realtime.deepsort_tracker import DeepSort

# Initialize DeepSORT trackers
tracker1 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)
tracker2 = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0)

# Load YOLO model
model = YOLO("C:\\Users\\kulas\\Downloads\\BBIOT project\\bestST.onnx")

# Initialize video captures
cap1 = cv2.VideoCapture("rtsp://admin:vitcctv%40321@192.168.1.64:554/Streaming/Channels/101")
cap2 = cv2.VideoCapture("rtsp://admin:Kulass123@192.168.1.65:554/Streaming/Channels/101")
if not cap1.isOpened():
    print("Error: Could not access the first camera.")
    exit()
if not cap2.isOpened():
    print("Error: Could not access the second camera.")
    exit()

class_names = ['centering_sheet', 'prop', 'span']

# Output directory
output_directory = "C:\\Users\\kulas\\Downloads\\BBIOT project\\outputlogs"
os.makedirs(output_directory, exist_ok=True)

# AWS S3
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
BUCKET_NAME = 'ubuntu20'
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

# Initialize counters and state trackers
cumulative_total_count1 = 0
cumulative_total_count2 = 0
crossed_ids1 = set()
crossed_ids2 = set()
current_ids1 = set()
current_ids2 = set()

data = []
last_capture_time = time.time()
last_csv_save_time = time.time()

def upload_to_s3(file_path, bucket_name, s3_path):
    try:
        s3.upload_file(file_path, bucket_name, s3_path)
        print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_path}")
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")

def save_and_upload(frame, frame_count, camera_num):
    capture_filename = os.path.join(output_directory, f"cam{camera_num}_frame_{frame_count}.jpg")
    cv2.imwrite(capture_filename, frame)
    thread = threading.Thread(target=upload_to_s3,
                              args=(capture_filename, BUCKET_NAME, f"cam{camera_num}_frame_{frame_count}.jpg"))
    thread.start()

def save_csv(data):
    csv_filename = os.path.join(output_directory, 'detection_log.csv')
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False)
    thread_csv = threading.Thread(target=upload_to_s3, args=(csv_filename, BUCKET_NAME, 'detection_log.csv'))
    thread_csv.start()

try:
    frame_count = 1
    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            print("Failed to grab frame from camera.")
            break

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --- Camera 1 ---
        results1 = model(frame1, save=False)
        detections1 = []
        counts1 = {name: 0 for name in class_names}
        new_ids1 = set()

        if results1:
            for result in results1:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    conf = float(box.conf[0])
                    cls_id = int(box.cls[0])
                    class_name = class_names[cls_id]
                    detections1.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))

            tracks1 = tracker1.update_tracks(detections1, frame=frame1)

            for track in tracks1:
                if not track.is_confirmed():
                    continue
                track_id = track.track_id
                new_ids1.add(track_id)

                ltrb = track.to_ltrb()
                x1, y1, x2, y2 = map(int, ltrb)
                class_name = track.det_class

                cv2.rectangle(frame1, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame1, f"{class_name} ID:{track_id}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                counts1[class_name] += 1

        # Update cumulative count for Camera 1
        newly_entered_ids1 = new_ids1 - current_ids1
        exited_ids1 = current_ids1 - new_ids1
        cumulative_total_count1 += len(newly_entered_ids1) - len(exited_ids1)
        current_ids1 = new_ids1

        # --- Camera 2 ---
        results2 = model(frame2, save=False)
        detections2 = []
        counts2 = {name: 0 for name in class_names}
        new_ids2 = set()

        if results2:
            for result in results2:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                    conf = float(box.conf[0])
                    cls_id = int(box.cls[0])
                    class_name = class_names[cls_id]
                    detections2.append(([x1, y1, x2 - x1, y2 - y1], conf, class_name))

            tracks2 = tracker2.update_tracks(detections2, frame=frame2)

            for track in tracks2:
                if not track.is_confirmed():
                    continue
                track_id = track.track_id
                new_ids2.add(track_id)

                ltrb = track.to_ltrb()
                x1, y1, x2, y2 = map(int, ltrb)
                class_name = track.det_class

                cv2.rectangle(frame2, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame2, f"{class_name} ID:{track_id}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                counts2[class_name] += 1

        # Update cumulative count for Camera 2
        newly_entered_ids2 = new_ids2 - current_ids2
        exited_ids2 = current_ids2 - new_ids2
        cumulative_total_count2 += len(newly_entered_ids2) - len(exited_ids2)
        current_ids2 = new_ids2

        data.append({
            'Timestamp': current_time,
            'Frame': frame_count,
            'Camera1_Total': cumulative_total_count1,
            'Camera1_Counts': counts1,
            'Camera2_Total': cumulative_total_count2,
            'Camera2_Counts': counts2
        })

        count_str1 = f"Total: {cumulative_total_count1} | " + ", ".join([f"{k}:{v}" for k, v in counts1.items()])
        count_str2 = f"Total: {cumulative_total_count2} | " + ", ".join([f"{k}:{v}" for k, v in counts2.items()])

        cv2.putText(frame1, count_str1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame2, count_str2, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        current_time_sec = time.time()

        if current_time_sec - last_capture_time >= 3:
            save_and_upload(frame1, frame_count, 1)
            save_and_upload(frame2, frame_count, 2)
            last_capture_time = current_time_sec

        if current_time_sec - last_csv_save_time >= 2:
            save_csv(data)
            last_csv_save_time = current_time_sec

        cv2.imshow("Camera 1 Tracking", frame1)
        cv2.imshow("Camera 2 Tracking", frame2)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    print("Processing stopped.")


