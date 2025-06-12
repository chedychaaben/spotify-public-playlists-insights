import os
import subprocess
import argparse
import sys

def convert_to_mp3(webm_path, mp3_path=None):
    if not os.path.isdir(webm_path):
        print(f'The input path "{webm_path}" does not exist.')
        sys.exit(1)
    if mp3_path is None:
        mp3_path = webm_path
    os.makedirs(mp3_path, exist_ok=True)
    for file in os.listdir(webm_path):
        if file.endswith(('.webm', '.mp4')):
            input_file = os.path.join(webm_path, file)
            output_file = os.path.join(mp3_path, os.path.splitext(file)[0] + '.mp3')
            command = [
                'ffmpeg', '-i', input_file, '-vn', '-ab', '128k', '-ar', '44100', '-y', output_file
            ]
            try:
                subprocess.run(command, check=True, shell=False)
                print(f"Converted {file} to MP3")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {file}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert audio files to MP3 using ffmpeg.')
    parser.add_argument('--webm_path', type=str, required=True, help='Path to input audio files')
    parser.add_argument('--mp3_path', type=str, help='Path for MP3 output files')
    args = parser.parse_args()
    convert_to_mp3(args.webm_path, args.mp3_path)