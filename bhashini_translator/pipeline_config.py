import requests
import json

class PipelineConfig:
    def getTaskTypeConfig(self, taskType):
        taskTypeConfig = {
            "translation": {
                "taskType": "translation",
                "config": {
                    "language": {
                        "sourceLanguage": self.sourceLanguage,
                        "targetLanguage": self.targetLanguage,
                    },
                },
            },
            "tts": {
                "taskType": "tts",
                "config": {
                    "language": {"sourceLanguage": self.sourceLanguage},
                    "gender": "female",
                },
            },
            "asr": {
                "taskType": "asr",
                "config": {"language": {"sourceLanguage": self.sourceLanguage}},
            },
        }
        try:
            return taskTypeConfig[taskType]
        except KeyError:
            raise KeyError("Invalid task type.")
    
    def getPipeLineConfig(self, taskType):
        taskTypeConfig = self.getTaskTypeConfig(taskType)
        payload = json.dumps(
            {
                "pipelineTasks": [taskTypeConfig],
                "pipelineRequestConfig": {
                    "pipelineId": self.pipeLineId,
                },
            }
        )
        response = requests.post(
            self.ulcaEndPoint,
            data=payload,
            headers={
                "ulcaApiKey": self.ulcaApiKey,
                "userID": self.ulcaUserId,
                "Content-Type": "application/json",
            },
        )
        if response.status_code != 200:
            error_details = f"""
            ❌ Bhashini API Error:
            - Status Code: {response.status_code}
            - Response: {response.text}
            - Endpoint: {self.ulcaEndPoint}
            - Pipeline ID: {self.pipeLineId}
            
            Please check:
            1. Your API credentials in .env file
            2. Your Bhashini account has API access approved
            3. The Pipeline ID is correct
            """
            print(error_details)
            raise ValueError(error_details)
        serviceId = (
            response.json()["pipelineResponseConfig"][0]
            .get("config")[0]
            .get("serviceId")
        )
        taskTypeConfig["config"]["serviceId"] = serviceId
        self.pipeLineData = response.json()
        return taskTypeConfig
