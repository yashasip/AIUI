import requests
import json

# ENTER YOUR IMAGGA API KEY AND API SECRET KEY TO GET STARTED!
API_KEY = ""
API_SECRET = ""


class ImaggaAPIHandler:
    '''Handles the API takes path to image, type of image recognition'''
    def __init__(self, imagePath, recognitionType) -> None:
        self.imagePath = imagePath
        self.recognitionType = recognitionType

        self.categorizerId = 'personal_photos'
        self.uploadId = None
        self.result = None

    def uploadImage(self): # uploads image to the api for Imagga server for recognition
        response = requests.post(
            "https://api.imagga.com/v2/uploads",
            auth=(API_KEY, API_SECRET),
            files={"image": open(self.imagePath, "rb")},
        )
        self.uploadId = response.json()["result"]["upload_id"]

    def imageTagging(self): # finds tags related to image
        response = requests.get(
            "https://api.imagga.com/v2/tags?image_upload_id=%s" % self.uploadId,
            auth=(API_KEY, API_SECRET)
        )
        self.resultJson = response.json()

    def imageCategorizer(self): # categories related to image
        response = requests.get(
        'https://api.imagga.com/v2/categories/%s?image_upload_id=%s' % (self.categorizerId, self.uploadId),
        auth=(API_KEY, API_SECRET))
        self.resultJson = response.json()

    def imageFacialDetection(self): # detects faces in the image and sends determines Age & Group and Ethnicity
        response = requests.get(
        'https://api.imagga.com/v2/faces/detections?image_upload_id=%s&return_face_attributes=1' % (self.uploadId),
        auth=(API_KEY, API_SECRET))
        self.resultJson = response.json()

    def deleteUploadedImage(self): # deleted the uploaded image
        response = requests.delete(
        'https://api.imagga.com/v2/uploads/%s' % (self.uploadId),
        auth=(API_KEY, API_SECRET))

    def jsonDataParser(self): # parses json data according to the recognition type
        if self.recognitionType == 'Tagging':
            parsedResultData = []
            for item in self.resultJson["result"]["tags"]:
                parsedData = {}
                parsedData["Accuracy"] = str(round(item['confidence'],2)) + '%'
                parsedData['Tag'] = item['tag']['en']

                parsedResultData.append(parsedData)

        elif self.recognitionType == 'Categorize':
            parsedResultData = []

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
                # merges two result values to single value
                parsedData['Age Group & Gender'] = item['attributes'][0]['label'] + ' ' +item['attributes'][1]['label']
                parsedData['Ethnicity'] = item['attributes'][2]['label']

                parsedResultData.append(parsedData)

        return parsedResultData
            

    def getJsonResult(self): # returns json result in pretty format
        return json.dumps(self.resultJson, indent=4, sort_keys=True)

    def APIHandle(self): # Executes all Image recognition related methods returns output
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
        else: # in case of failure
            return []