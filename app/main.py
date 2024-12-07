#!/usr/bin/env python3

import argparse
from pathlib import Path

from PIL import Image

def shrink_image(file_path, shrink_percentage):
    if not (0 < shrink_percentage <= 100):
        raise ValueError("Shrink percentage must be between 0 and 100.")

    input_path = Path(file_path)
    output_path = input_path.with_name(f"{input_path.stem}.out{input_path.suffix}")
    
    with Image.open(input_path) as img:
        max_width = int(img.width * (shrink_percentage / 100))
        max_height = int(img.height * (shrink_percentage / 100))
        max_size = (max_width, max_height)
        
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        img.save(output_path)

        
def main():
    parser = argparse.ArgumentParser(description='Shrink an image by a specified percentage.')
    parser.add_argument('path', type=str, help='Path to the input image')
    parser.add_argument('--prop', type=float, required=True, help='Percentage to shrink the image')
    
    args = parser.parse_args()
    shrink_image(args.path, args.prop)
    
if __name__ == '__main__':
    main()

