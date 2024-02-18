from PIL import Image
import os

def encrypt_image(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Iterate through each pixel and apply encryption
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            r, g, b = img.getpixel((x, y))
            
            # Example encryption: swap red and blue components
            encrypted_pixel = (b, g, r)
            
            # Set the new pixel value
            img.putpixel((x, y), encrypted_pixel)
    
    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted and saved successfully.")

def decrypt_image(encrypted_path, output_path):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    
    # Get image dimensions
    width, height = img.size
    
    # Iterate through each pixel and apply decryption (reverse the encryption process)
    for y in range(height):
        for x in range(width):
            # Get the RGB values of the current pixel
            r, g, b = img.getpixel((x, y))
            
            # Example decryption: swap red and blue components back to original
            decrypted_pixel = (b, g, r)
            
            # Set the new pixel value
            img.putpixel((x, y), decrypted_pixel)
    
    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted and saved successfully.")

def main():
    image_path = input("Enter the path to the image: ")

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print("Error: The specified image file does not exist.")
        return

    encrypted_path = "encrypted_image.jpg"
    decrypted_path = "decrypted_image.jpg"
    
    # Encrypt the image
    encrypt_image(image_path, encrypted_path)
    
    # Decrypt the image
    decrypt_image(encrypted_path, decrypted_path)

if __name__ == "__main__":
    main()
