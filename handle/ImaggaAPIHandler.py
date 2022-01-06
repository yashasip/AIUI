import requests

API_KEY = "acc_bb1f59217fa4df8"
API_SECRET = "2f8013473730615cc2aa68d77b05e4ea"


class ImaggaAPIHandler:
    def __init__(self, imagePath, recognitionType) -> None:
        self.imagePath = imagePath
        self.recognitionType = recognitionType

        self.categorizerId = 'personal_photos'
        self.uploadId = None
        self.result = None

    def uploadImage(self):
        response = requests.post(
            "https://api.imagga.com/v2/uploads",
            auth=(API_KEY, API_SECRET),
            files={"image": open(self.imagePath, "rb")},
        )
        self.uploadId = response.json()["result"]["upload_id"]

    def imageTagging(self):
        response = requests.get(
            "https://api.imagga.com/v2/tags?image_upload_id=%s" % self.uploadId,
            auth=(API_KEY, API_SECRET)
        )
        self.resultJson = response.json()
        # print(self.resultJson)

    def imageCategorizer(self):
        response = requests.get(
        'https://api.imagga.com/v2/categories/%s?image_upload_id=%s' % (self.categorizerId, self.uploadId),
        auth=(API_KEY, API_SECRET))
        self.resultJson = response.json()
        # print(self.resultJson)

    def imageFacialDetection(self):
        response = requests.get(
        'https://api.imagga.com/v2/faces/detections?image_upload_id=%s&return_face_attributes=1' % (self.uploadId),
        auth=(API_KEY, API_SECRET))
        self.resultJson = response.json()
        # print(self.resultJson)

    def deleteUploadedImage(self):
        response = requests.delete(
        'https://api.imagga.com/v2/uploads/%s' % (self.uploadId),
        auth=(API_KEY, API_SECRET))

        # print(response.json())

    def jsonDataParser(self):
        if self.recognitionType == 'Tagging':
            parsedResultData = []
            for item in self.resultJson["result"]["tags"]:
                parsedData = {}
                parsedData["Accuracy"] = str(round(item['confidence'],2)) + '%'
                parsedData['Tag'] = item['tag']['en']

                parsedResultData.append(parsedData)

        elif self.recognitionType == 'Categorize':
            parsedResultData = []
            print(type(self.resultJson["result"]["categories"]))
            for item in self.resultJson["result"]["categories"]:
                parsedData = {}
                parsedData["Accuracy"] = str(round(item['confidence'],2)) + '%'
                parsedData['Category'] = item['name']['en']

                parsedResultData.append(parsedData)

        elif self.recognitionType == 'Facial Detection':
            parsedResultData = []

            for item in self.resultJson["result"]["faces"]:
                parsedData = {}
                parsedData["Accuracy"] = str(round((item['attributes'][0]['confidence'] + item['attributes'][1]['confidence'] + item['attributes'][2]['confidence'])/3,2)) + '%'
                parsedData['Age Group'] = item['attributes'][0]['label']
                parsedData['Gender'] = item['attributes'][1]['label']
                parsedData['Ethnicity'] = item['attributes'][2]['label']

                parsedResultData.append(parsedData)

        return parsedResultData
            

    def prettifyJson(self,jsonData):
        import json
        return json.loads(jsonData, indent=4, sort_keys=True)

    def APIHandle(self):
        self.uploadImage()
        if self.recognitionType == 'Tagging':
            self.imageTagging()
        elif self.recognitionType == 'Categorize':
            self.imageCategorizer()
        elif self.recognitionType == 'Facial Detection':
            self.imageFacialDetection()
        else:
            raise Exception('Invalid Recognition Option')

        if self.resultJson['status']['type'] == 'success':
            self.data = self.jsonDataParser()
            return self.data

        print('No result found')