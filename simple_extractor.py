import cv2
import os

def extract_frames(video_path, output_folder, frame_skip=5):
    """
    Extract 1 frame per N frames from a video file.
    
    Parameters:
    - video_path: Path to the video file
    - output_folder: Folder to save extracted frames
    - frame_skip: Extract 1 frame every N frames (default: 5)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Check if video opened successfully
    if not video.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return
    
    # Process frames
    frame_count = 0
    saved_count = 0
    
    while True:
        # Read the next frame
        success, frame = video.read()
        
        # Break the loop if we've reached the end of the video
        if not success:
            break
        
        # Extract only every Nth frame (based on frame_skip)
        if frame_count % frame_skip == 0:
            # Create the output filename
            filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            
            # Save the frame
            cv2.imwrite(filename, frame)
            saved_count += 1
        
        frame_count += 1
    
    # Release the video
    video.release()
    
    print(f"Extraction complete! Extracted {saved_count} frames from {video_path}")
    print(f"Frames saved to {output_folder}")

# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python script.py video_path output_folder [frame_skip]")
        print("Example: python script.py river_video.mp4 ./frames 5")
        sys.exit(1)
    
    video_path = sys.argv[1]
    output_folder = sys.argv[2]
    
    # Use the third argument as frame_skip if provided, otherwise default to 5
    frame_skip = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    
    extract_frames(video_path, output_folder, frame_skip)