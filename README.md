# 🛠️ Counter Assistant System

A real-time multilingual voice translation system designed for railway counters and service desks. This application features a split-screen interface that enables seamless communication between counter staff and customers in different languages using advanced AI-powered translation via Bhashini API.

## ✨ Features

### **🔄 Split-Screen Interface**
- **👨‍💼 Staff Panel (Left)**: Dedicated interface for railway counter staff
- **👥 Customer Panel (Right)**: User-friendly interface for customers
- **📱 Real-Time Communication**: Instant voice-to-voice translation between both sides

### **🎤 Voice-Enabled Communication**
- **Large Recording Buttons**: WhatsApp-style voice message interface
- **One-Click Recording**: Simple tap-to-record functionality
- **Audio Playback**: Hear translated messages in preferred languages
- **Duration Display**: Shows recording length after completion

### **🌍 Advanced Translation**
- **12 Indian Languages**: Hindi, English, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Marathi, Punjabi, Urdu, and Maithili
- **Bidirectional Translation**: Staff ↔ Customer real-time translation
- **Speech-to-Speech**: Complete audio translation pipeline (ASR → Translation → TTS)
- **Text Display**: See both original and translated text for clarity

### **💬 Conversation Management**
- **Live Conversation History**: Track all exchanges between staff and customer
- **Color-Coded Messages**: Easy distinction between staff and customer messages
- **Audio Playback**: Replay any message in the conversation
- **Clear Conversation**: Reset chat when needed

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Bhashini API credentials (User ID and API Key)
- Microphone access for audio recording

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd counter_assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your Bhashini credentials:
```env
userID=your_bhashini_user_id
ulcaApiKey=your_bhashini_api_key
DefaultPipeLineId=64392f96daac500b55c543cd
```

### Running the Application

#### Streamlit Web Application
```bash
streamlit run app.py
```

#### Command Line Speech-to-Speech Translation
```bash
python main.py
```

## 📋 Use Cases

### **🚆 Railway Counter Communications**
**Perfect for helping with:**
- **Ticket Booking**: Language assistance for reservation process
- **Train Information**: Schedule, platform, and delay updates
- **Customer Queries**: PNR status, seat availability, cancellation
- **Emergency Communications**: Urgent announcements and assistance
- **General Inquiries**: Facilities, directions, and services

### **🏢 Service Desk Applications**
**Ideal for:**
- **Government Offices**: Citizen services in local languages
- **Banks**: Customer service and account assistance  
- **Hospitals**: Patient registration and information
- **Hotels**: Guest services and concierge assistance
- **Retail Stores**: Customer support and product information

### **🌍 Real-World Scenarios**
- **Tourist Assistance**: Help foreign visitors communicate
- **Elder Care**: Assist elderly customers with technology barriers
- **Rural Services**: Bridge urban-rural language gaps
- **Emergency Services**: Critical communication in crisis situations

## 🔧 Project Structure

```
counter_assistant/
│
├── 📱 app.py                   # Main split-screen Streamlit application
├── 🎤 main.py                  # Command-line speech-to-speech demo  
├── 📋 requirements.txt         # Python dependencies
├── 🔑 .env                     # Bhashini API credentials (create this)
├── 📖 README.md                # Project documentation
├── 🧪 test_bhashini.py         # API credentials testing tool
│
└── 🔧 bhashini_translator/     # Bhashini API integration module
    ├── __init__.py             # Package initialization
    ├── bhashini_translator.py  # Main translator class
    ├── config.py               # API endpoint configuration  
    ├── payloads.py             # Request payload generators
    └── pipeline_config.py      # Pipeline configuration handler
```

### **📁 Key Files:**
- **`app.py`**: Split-screen real-time translation interface
- **`test_bhashini.py`**: Verify your API credentials before running
- **`.env`**: Store your Bhashini API credentials securely
- **`bhashini_translator/`**: Core translation engine with Bhashini integration

## 🎯 How It Works

### **🔄 Simple 3-Step Process:**

#### **1️⃣ Setup**
- **Staff selects** their preferred communication language
- **Customer selects** their native language from 12 options
- **Split-screen interface** automatically configures for both users

#### **2️⃣ Communication**
- **Staff speaks** into left panel → **Customer hears** translation on right
- **Customer responds** into right panel → **Staff hears** translation on left
- **Real-time processing**: Voice → Text → Translation → Voice (under 5 seconds)

#### **3️⃣ Conversation Flow**
- **All messages saved** in conversation history with timestamps
- **Both audio and text** versions available for reference
- **Color-coded interface** makes it easy to follow the conversation
- **One-click clear** to start fresh conversation

### **🔧 Technical Process:**
```
🎤 Voice Input → 📝 Speech Recognition → 🌍 Translation → 🔊 Text-to-Speech → 🎧 Audio Output
```

## 🔌 Bhashini API Integration

The application uses Bhashini API for:
- **ASR** (Automatic Speech Recognition): Convert speech to text
- **NMT** (Neural Machine Translation): Translate text between languages
- **TTS** (Text-to-Speech): Convert text to speech audio

## 📦 Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `streamlit` | Web application framework | Latest |
| `audio-recorder-streamlit` | Voice recording interface | Latest |
| `python-dotenv` | Environment variable management | Latest |
| `requests` | HTTP library for Bhashini API calls | Latest |
| `speech_recognition` | Speech recognition (CLI demo) | Latest |
| `bhashini_translator` | Custom Bhashini API wrapper | Local |

### **🔧 Installation Command:**
```bash
pip install streamlit audio-recorder-streamlit python-dotenv requests speech_recognition
```

## 🌐 Supported Languages

| Language | Code |
|----------|------|
| Hindi | hi |
| English | en |
| Bengali | bn |
| Tamil | ta |
| Telugu | te |
| Gujarati | gu |
| Kannada | kn |
| Malayalam | ml |
| Marathi | mr |
| Punjabi | pa |
| Urdu | ur |
| Maithili | mai |

## 🚀 Quick Start Guide

### **⚡ Fast Setup (2 minutes):**
1. **Clone & Install**:
   ```bash
   git clone <repository-url>
   cd counter_assistant
   pip install -r requirements.txt
   ```

2. **Get Bhashini Credentials**:
   - Visit [Bhashini.gov.in](https://bhashini.gov.in/)
   - Register and get your `userID` and `ulcaApiKey`

3. **Test Credentials**:
   ```bash
   python test_bhashini.py
   ```

4. **Launch Application**:
   ```bash
   streamlit run app.py
   ```

5. **Open Browser**: Go to `http://localhost:8501`

## 🎯 Usage Tips

### **👨‍💼 For Counter Staff:**
- Use the **left panel** (blue theme)
- Select your working language
- Click the microphone to record messages
- View customer responses with translations

### **👥 For Customers:**  
- Use the **right panel** (green theme)
- Choose your preferred language
- Tap the microphone to respond
- Listen to staff messages in your language

### **🔧 Troubleshooting:**
- **No audio?** Check microphone permissions
- **Translation fails?** Run `python test_bhashini.py` 
- **App won't start?** Verify all dependencies installed
- **API errors?** Check your `.env` file credentials

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional language support
- Mobile responsiveness  
- Voice activity detection
- Integration with other translation services

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

- **Issues**: Open an issue in this repository
- **API Help**: Contact Bhashini support at bhashini-support@bhashini.gov.in
- **Feature Requests**: Submit a pull request or feature request

## 🙏 Acknowledgments

- **Bhashini/ULCA** for providing world-class multilingual AI services
- **Streamlit** for the intuitive web application framework
- **Indian Government** for promoting digital inclusion through language technology
- **Open Source Community** for continuous improvement and feedback

---

## ⚠️ Important Notes

- **API Credentials Required**: Get valid Bhashini credentials before use
- **Internet Required**: Application needs internet for translation services  
- **Microphone Access**: Browser needs microphone permissions for voice recording
- **Modern Browser**: Use Chrome, Firefox, or Safari for best experience

**🌟 Star this repository if it helps bridge language barriers in your community!**
