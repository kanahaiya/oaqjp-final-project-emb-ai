import json, requests

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input= { "raw_document": { "text": text_to_analyse } }
    response=requests.post(url,json=input, headers=headers)
    formatted_response=json.loads(response.text)
    #print(formatted_response)
    if response.status_code == 400:
         return {'anger':None,'disgust':None,'fear':None,'joy':None,'sadness':None,'dominant_emotion':None}
    else :
        predictions=formatted_response['emotionPredictions'][0]['emotion']
        anger=predictions['anger']
        disgust=predictions['disgust']
        fear=predictions['fear']
        joy=predictions['joy']
        sadness=predictions['sadness']
        dominant_emotion = max(predictions, key=predictions.get)

        return {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness,'dominant_emotion':dominant_emotion}




