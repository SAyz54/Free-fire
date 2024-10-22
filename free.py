import pyautogui
import cv2
import numpy as np
import time

# Function to capture the screen
def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    return screenshot

# Function to detect enemy heads
def detect_heads(image):
    # Load the pre-trained Haar Cascade classifier for head detection
    head_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    heads = head_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return heads

# Function to perform auto headshot
def auto_headshot():
    while True:
        # Capture the screen
        screen = capture_screen()

        # Detect enemy heads
        heads = detect_heads(screen)

        # Perform headshot if heads are detected
        if len(heads) > 0:
            # Get the first detected head
            (x, y, w, h) = heads[0]

            # Calculate the center of the head
            center_x = x + w // 2
            center_y = y + h // 2

            # Move the mouse to the center of the head
            pyautogui.moveTo(center_x, center_y)

            # Simulate a mouse click
            pyautogui.click()

            # Wait for a short period before the next detection
            time.sleep(0.5)

# Main function
def main():
    auto_headshot()

# Execute the main function
if __name__ == "__main__":
    main()