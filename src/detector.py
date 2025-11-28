import cv2
import numpy as np
import time
import csv
import argparse
import os
from datetime import datetime

def run_detector(duration, threshold, output_file, camera_id):
    """
    Runs the CMOS Muon Detector.
    Args:
        duration (int): How long to run in seconds.
        threshold (int): Pixel brightness (0-255) to trigger a detection.
        output_file (str): Path to save the CSV log.
        camera_id (int): ID of the webcam (usually 0 or 1).
    """
    
    # 1. Initialize Camera
    cap = cv2.VideoCapture(camera_id)
    
    # Optimize for low light / scientific detection
    # Turn off auto-exposure to reduce thermal noise fluctuation
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) 
    cap.set(cv2.CAP_PROP_EXPOSURE, -10) # Max manual exposure usually
    
    if not cap.isOpened():
        print(f"Error: Could not open camera {camera_id}.")
        return

    # 2. Prepare Output File
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"--- STARTING DATA COLLECTION ---")
    print(f"Target Duration: {duration} seconds")
    print(f"Threshold: {threshold} / 255")
    print(f"Saving to: {output_file}")
    print("Press 'q' to stop manually.\n")

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Unix_Time", "Intensity_Pixels", "Comments"])

        start_time = time.time()
        event_count = 0

        while (time.time() - start_time) < duration:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # 3. Process Frame (The Physics)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply Threshold: Ignore everything darker than 'threshold'
            _, thresh_img = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

            # Count bright pixels (The "Event")
            bright_pixels = cv2.countNonZero(thresh_img)

            # 4. Filter Logic
            # > 0: Something hit the sensor.
            # < 100: Likely a particle. (Light leaks usually flood >1000 pixels)
            if 0 < bright_pixels < 100:
                now = datetime.now()
                timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
                unix_time = time.time()
                
                print(f"[{timestamp}] HIT DETECTED! Size: {bright_pixels} pixels")
                writer.writerow([timestamp, unix_time, bright_pixels, "Valid Event"])
                event_count += 1

            elif bright_pixels >= 100:
                # Optional: Log light leaks if debugging
                pass

            # 5. Display (Optional - turn off to save battery)
            cv2.imshow('Muon Detector View (Threshold)', thresh_img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    print(f"\n--- EXPERIMENT COMPLETE ---")
    print(f"Total Events: {event_count}")
    print(f"Average Flux: {event_count / (duration/60):.2f} CPM")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CMOS Muon Detector')
    parser.add_argument('--duration', type=int, default=3600, help='Duration in seconds')
    parser.add_argument('--threshold', type=int, default=30, help='Brightness threshold (0-255)')
    parser.add_argument('--output', type=str, default='data/raw_logs/data.csv', help='Output CSV file path')
    parser.add_argument('--camera', type=int, default=0, help='Camera ID')

    args = parser.parse_args()
    run_detector(args.duration, args.threshold, args.output, args.camera)
