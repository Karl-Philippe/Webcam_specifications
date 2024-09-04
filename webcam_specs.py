import cv2

def get_webcam_specs():
    # Open the first webcam available
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Could not open webcam")
        return
    
    # Get the width and height of the frame
    w_video = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h_video = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Calculate megapixels and aspect ratio
    pixels_vid = (w_video * h_video * 10e-7)
    aspect_ratio_video = w_video / h_video
    
    # Get the frame rate
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Calculate the approximate bitrate
    bitrate = frame_rate * pixels_vid

    # Display the specs
    print(f"Test de webcam\n")
    print(f"Specifications")
    print(f"Spatial resolution: {w_video} x {h_video}")
    print(f"Frame rate: {frame_rate} FPS")
    print(f"Pixel density: {pixels_vid:.2f} MP")
    print(f"Data rate: {bitrate:.2f} MB/s (approx.)")
    print(f"Aspect ratio: {aspect_ratio_video:.2f}")

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    get_webcam_specs()
