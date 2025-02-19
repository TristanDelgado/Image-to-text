import image_data

#Entry point
def main():
    file_to_convert = input("Input image location:")
    print(image_data.get_rgb(file_to_convert))




if __name__ == "__main__":
    main()