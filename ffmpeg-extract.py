#!/usr/bin/env python3
import subprocess
import sys

def extract_segment(start_time, end_time, input_filename):
    """
    Extracts a video segment using ffmpeg.

    Args:
        start_time (str): The start time of the segment (e.g., "00:01:23").
        end_time (str): The end time of the segment (e.g., "00:02:45").
        input_filename (str): The path to the input video file.
    """
    if not input_filename:
        print("Error: Input filename cannot be empty.")
        sys.exit(1)

    output_filename = f"{input_filename}_extracted.mp4"

    command = [
        "ffmpeg",
        "-i", input_filename,
        "-ss", start_time,
        "-to", end_time,
        "-c:v", "libx264",
        "-c:a", "copy",
        output_filename
    ]

    print(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(command, check=True)
        print(f"Successfully extracted segment to {output_filename}")
    except FileNotFoundError:
        print("Error: ffmpeg not found. Please ensure it is installed and in your PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error during ffmpeg execution: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./extract.py <start_time> <end_time> <filename>")
        print("Example: ./extract.py 00:01:23 00:02:45 my_video.mp4")
        sys.exit(1)

    start = sys.argv[1]
    end = sys.argv[2]
    filename = sys.argv[3]
    
    extract_segment(start, end, filename)
