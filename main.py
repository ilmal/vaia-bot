import requests
import json
import uuid

def main():

    link = input("Enter your referal link:")

    ref_id = link.split("=")[-1]

    for _ in range(2):
        url = "https://prod.studysmarter.de/users/?="

        payload = json.dumps({
        "email": f"{str(uuid.uuid4())}@lol.lol",
        "platform": "webapp",
        "language": "en",
        "ref_id_inviter": ref_id,
        "delayed_confirmation_possible": True,
        "university": None,
        "course_of_studies": None,
        "password": "hejsan1234",
        "target_market": "us",
        "amplitude_device_id": "fe970fc1-ab8e-45ec-be57-5390b745a11b"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)




if __name__ == "__main__":
    main()