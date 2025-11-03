"""
🔧 Bhashini API Credential Helper
This script helps you get valid Bhashini API credentials step by step.
"""

import webbrowser
import sys
import os

print("=" * 80)
print("🚀 BHASHINI API CREDENTIAL SETUP HELPER")
print("=" * 80)

print("""
❌ CURRENT ISSUE: Your API key is invalid/expired
   Error: "ulcaApiKey does not exist. Please provide a valid one"

🎯 SOLUTION: Get new valid credentials from Bhashini
""")

print("\n" + "=" * 50)
print("STEP 1: ACCESS BHASHINI PLATFORM")
print("=" * 50)

print("""
I'll open the Bhashini website for you. You need to:

1️⃣ Sign up / Login to Bhashini platform
2️⃣ Navigate to API/Developer section  
3️⃣ Generate new API credentials
4️⃣ Copy your UserID and API Key
""")

choice = input("\n🌐 Open Bhashini website now? (y/n): ").lower().strip()

if choice == 'y':
    print("\n🔗 Opening https://bhashini.gov.in/ ...")
    webbrowser.open("https://bhashini.gov.in/")
    print("✅ Website opened in your browser")
else:
    print("📋 Manual link: https://bhashini.gov.in/")

print("\n" + "=" * 50)
print("STEP 2: ALTERNATIVE REGISTRATION METHODS")
print("=" * 50)

print("""
If the main website doesn't work, try these alternatives:

🔗 ULCA Platform: https://bhashini.gitbook.io/bhashini-apis/
🔗 Developer Docs: https://github.com/ULCA-IN/ulca/
🔗 API Documentation: https://meity-auth.ulcacontrib.org/

📧 Support Email: bhashini-support@bhashini.gov.in
""")

print("\n" + "=" * 50)
print("STEP 3: GET YOUR NEW CREDENTIALS")
print("=" * 50)

print("""
Once you're logged in to Bhashini:

1. Look for "API Access" or "Developer Console"
2. Find/Generate your credentials:
   - User ID (looks like: 69a7ad080e824bf3bb76be02a0cabfed)
   - API Key (looks like: 3iMBoHOeKdJg4hprFtlU...)
3. Copy both values

⚠️  IMPORTANT: Some accounts need manual approval for API access
   If you can't find API section, contact support for approval.
""")

print("\n" + "=" * 50) 
print("STEP 4: UPDATE YOUR .ENV FILE")
print("=" * 50)

print("""
Once you have new credentials, I'll help you update your .env file.

Your .env file should look like this:

userID=your_new_user_id_here
ulcaApiKey=your_new_api_key_here
DefaultPipeLineId=64392f96daac500b55c543cd

📝 The Pipeline ID (64392f96daac500b55c543cd) is correct, 
   only your userID and ulcaApiKey need to be updated.
""")

print("\n" + "=" * 50)
print("STEP 5: TEST YOUR NEW CREDENTIALS")
print("=" * 50)

print("""
After updating .env file, test your credentials:

📋 Run: python test_bhashini.py

This will verify if your new credentials work properly.
""")

credentials_ready = input("\n🔑 Do you have your new credentials ready? (y/n): ").lower().strip()

if credentials_ready == 'y':
    print("\n📝 Please provide your new credentials:")
    
    new_user_id = input("🆔 Enter your new UserID: ").strip()
    new_api_key = input("🔐 Enter your new API Key: ").strip()
    
    if new_user_id and new_api_key:
        # Update .env file
        env_content = f"""userID={new_user_id}
ulcaApiKey={new_api_key}
DefaultPipeLineId=64392f96daac500b55c543cd
"""
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n✅ .env file updated successfully!")
        print("\n🧪 Now run: python test_bhashini.py")
        print("   This will test your new credentials.")
        
    else:
        print("\n❌ Invalid input. Please run this script again when you have credentials.")
        
else:
    print("""
    
📋 SUMMARY - What you need to do:

1. Visit: https://bhashini.gov.in/
2. Sign up/Login 
3. Get API access (may need approval)
4. Generate UserID and API Key
5. Run this script again with: python get_credentials.py
6. Test with: python test_bhashini.py

💡 TIP: Keep your credentials private and never share them!
    """)

print("\n" + "=" * 80)
print("🎯 Need help? Email: bhashini-support@bhashini.gov.in")
print("=" * 80)