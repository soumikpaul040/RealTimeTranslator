"""
Test script to verify Bhashini API credentials and Pipeline ID
"""
import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials
userID = os.environ.get("userID")
ulcaApiKey = os.environ.get("ulcaApiKey")
pipelineId = os.environ.get("DefaultPipeLineId")
endpoint = "https://meity-auth.ulcacontrib.org/ulca/apis/v0/model/getModelsPipeline"

print("=" * 60)
print("🔍 TESTING BHASHINI API CREDENTIALS")
print("=" * 60)

# Step 1: Check if credentials exist
print("\n1️⃣ Checking credentials in .env file...")
if not userID:
    print("   ❌ ERROR: userID not found in .env file")
else:
    print(f"   ✅ userID found: {userID[:10]}...")

if not ulcaApiKey:
    print("   ❌ ERROR: ulcaApiKey not found in .env file")
else:
    print(f"   ✅ ulcaApiKey found: {ulcaApiKey[:20]}...")

if not pipelineId:
    print("   ❌ ERROR: DefaultPipeLineId not found in .env file")
else:
    print(f"   ✅ Pipeline ID found: {pipelineId}")

if not all([userID, ulcaApiKey, pipelineId]):
    print("\n❌ Missing credentials! Please check your .env file")
    exit(1)

# Step 2: Test Translation Pipeline
print("\n2️⃣ Testing Translation Pipeline (English to Hindi)...")
payload = {
    "pipelineTasks": [
        {
            "taskType": "translation",
            "config": {
                "language": {
                    "sourceLanguage": "en",
                    "targetLanguage": "hi"
                }
            }
        }
    ],
    "pipelineRequestConfig": {
        "pipelineId": pipelineId
    }
}

headers = {
    "ulcaApiKey": ulcaApiKey,
    "userID": userID,
    "Content-Type": "application/json"
}

try:
    response = requests.post(endpoint, json=payload, headers=headers)
    
    print(f"\n   📡 Response Status Code: {response.status_code}")
    
    if response.status_code == 200:
        print("   ✅ SUCCESS! Translation pipeline is working!")
        data = response.json()
        print(f"\n   Pipeline Response Preview:")
        print(f"   {json.dumps(data, indent=2)[:500]}...")
        
    elif response.status_code == 401:
        print("   ❌ AUTHENTICATION FAILED!")
        print("   → Your userID or ulcaApiKey is incorrect")
        print("   → Please verify your credentials at https://bhashini.gov.in/")
        
    elif response.status_code == 400:
        print("   ❌ BAD REQUEST!")
        print(f"   Response: {response.text}")
        print("   → Your Pipeline ID might be incorrect")
        print("   → Or the language pair is not supported")
        
    elif response.status_code == 403:
        print("   ❌ ACCESS FORBIDDEN!")
        print("   → Your account may not have API access approved")
        print("   → Contact Bhashini support for API access")
        
    else:
        print(f"   ❌ ERROR: {response.status_code}")
        print(f"   Response: {response.text}")
        
except Exception as e:
    print(f"   ❌ EXCEPTION: {str(e)}")
    print("   → Check your internet connection")
    print("   → Verify the API endpoint is accessible")

# Step 3: Test ASR Pipeline
print("\n3️⃣ Testing ASR (Speech Recognition) Pipeline...")
asr_payload = {
    "pipelineTasks": [
        {
            "taskType": "asr",
            "config": {
                "language": {
                    "sourceLanguage": "hi"
                }
            }
        }
    ],
    "pipelineRequestConfig": {
        "pipelineId": pipelineId
    }
}

try:
    response = requests.post(endpoint, json=asr_payload, headers=headers)
    
    if response.status_code == 200:
        print("   ✅ ASR pipeline is working!")
    else:
        print(f"   ⚠️ ASR failed with status: {response.status_code}")
        
except Exception as e:
    print(f"   ❌ ASR test failed: {str(e)}")

# Step 4: Test TTS Pipeline
print("\n4️⃣ Testing TTS (Text-to-Speech) Pipeline...")
tts_payload = {
    "pipelineTasks": [
        {
            "taskType": "tts",
            "config": {
                "language": {
                    "sourceLanguage": "hi"
                },
                "gender": "female"
            }
        }
    ],
    "pipelineRequestConfig": {
        "pipelineId": pipelineId
    }
}

try:
    response = requests.post(endpoint, json=tts_payload, headers=headers)
    
    if response.status_code == 200:
        print("   ✅ TTS pipeline is working!")
    else:
        print(f"   ⚠️ TTS failed with status: {response.status_code}")
        
except Exception as e:
    print(f"   ❌ TTS test failed: {str(e)}")

print("\n" + "=" * 60)
print("✨ TEST COMPLETE")
print("=" * 60)
print("\n💡 Next Steps:")
print("   - If all tests passed: Your setup is correct! ✅")
print("   - If authentication failed: Check your credentials at https://bhashini.gov.in/")
print("   - If pipeline failed: You may need a different Pipeline ID")
print("   - If access forbidden: Request API access from Bhashini support")
print("\n")
