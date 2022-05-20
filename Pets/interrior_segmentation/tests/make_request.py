import requests
import base64

image = '../data/processed/images/ADE_frame_00000101.jpg'

with open(image, "rb") as f:
    base64_fig = base64.b64encode(f.read())


def main():
    response = requests.get(
        'http://127.0.0.1:8000/predict',
        json={
            'image': base64_fig.decode('utf-8')
        }
    )
    print(response.status_code)
    print(response.json())


main()
