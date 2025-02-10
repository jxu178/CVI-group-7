import cv2
import os

# Initialize webcam (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a directory to save images if it doesn't exist
save_dir = "snapshots"
os.makedirs(save_dir, exist_ok=True)

# Initialize image counter
image_counter = len([f for f in os.listdir(save_dir) if f.startswith("image") and f.endswith(".jpg")]) + 1

print("Press 's' to take a snapshot and 'q' to exit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    # Display the frame
    cv2.imshow("Webcam Live Feed", frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save snapshot
        img_filename = os.path.join(save_dir, f"image{image_counter}.jpg")
        cv2.imwrite(img_filename, frame)
        print(f"Snapshot saved as {img_filename}")
        image_counter += 1  # Increment image counter
    elif key == ord('q'):
        print("Exiting...")
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
