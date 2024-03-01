import requests

URL = 'http://localhost:5000/get_frame'

def main():
    response = requests.get(URL)

    if response.status_code == 200:
        output_image_path = response.text 
        print("Output image saved at:", output_image_path)
    else:
        print("Inference failed. Error:", response.text)

if __name__ == "__main__":
    main()
