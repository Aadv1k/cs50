import sys
from PIL import Image, ImageOps

def overlay_shirt(input_path, output_path, shirt_path="shirt.png"):
    try:
        input_image = Image.open(input_path)
        shirt_image = Image.open(shirt_path)

        input_extension = input_path.lower().split('.')[-1]
        output_extension = output_path.lower().split('.')[-1]

        if input_extension != output_extension:
            sys.exit("Input and output must have the same extension.")

        # https://www.reddit.com/r/cs50/comments/uvqiz0/cs50p_project6_shirtpy_image_does_not_match/
        input_image = ImageOps.fit(input_image, shirt_image.size)

        input_image.paste(shirt_image, (0, 0), shirt_image)
        input_image.save(output_path)

        print(f"Virtual shirt overlay complete! Check {output_path} for the result.")
    except FileNotFoundError:
        sys.exit(f"Input image {input_path} does not exist.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = ('.jpg', '.jpeg', '.png')
    if not input_path.lower().endswith(valid_extensions) or not output_path.lower().endswith(valid_extensions):
        sys.exit("Invalid input or output format. Use .jpg, .jpeg, or .png.")

    overlay_shirt(input_path, output_path)

if __name__ == "__main__":
    main()
