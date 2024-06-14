from PIL import Image
import os
import argparse

def downsample_image(source_path, output_path, width, height):
    # Load the image
    image = Image.open(source_path)
    
    # Resize the image
    downsampled_image = image.resize((width, height), Image.LANCZOS)

    # Create the output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    # Save the downsampled image
    downsampled_image.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downsample an image to a specified size.")
    parser.add_argument("source_image_path", type=str, help="Path to the source image.")
    parser.add_argument("output_path", type=str, help="Path to save the downsampled image, including the new image name.")
    parser.add_argument("width", type=int, help="Expected width of the downsampled image.")
    parser.add_argument("height", type=int, help="Expected height of the downsampled image.")

    args = parser.parse_args()

    downsample_image(args.source_image_path, args.output_path, args.width, args.height)


# python downsample.py /home/zhiyundeng/aeroplan/dataset/source_image/aerial_view/DJI_0481_3013x3013.jpeg /home/zhiyundeng/aeroplan/dataset/source_image/aerial_view 3000 3000
