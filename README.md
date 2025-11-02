# 🛠️ Counter Assistant System

A multilingual voice-enabled assistant system designed for railway and airport enquiry counters. This application helps bridge language barriers between counter staff and customers by providing real-time speech-to-speech translation using Bhashini API.

## ✨ Features

- **🌍 Multilingual Support**: Supports 12 Indian languages including Hindi, English, Bengali, Tamil, Telugu, Gujarati, Kannada, Malayalam, Marathi, Punjabi, Urdu, and Maithili
- **🎤 Voice Recording**: Real-time audio recording for customer responses
- **🔊 Text-to-Speech**: Automatic audio playback of questions in customer's preferred language
- **📝 Speech-to-Text**: Convert customer's voice responses to text
- **🌐 Translation**: Seamless translation between counter staff and customer languages
- **🚆 Railway Enquiry**: Pre-defined questions for railway counter assistance
- **✈️ Airport Enquiry**: Pre-defined questions for airport counter assistance

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

### Railway Enquiry Counter
The system assists with:
- Passenger name and phone number collection
- PNR number verification
- Train number/name enquiry
- Boarding and destination station information
- Journey date confirmation
- Seat availability checking
- Train timing enquiries
- Train delay status
- Platform information
- Ticket cancellation and refund assistance

### Airport Enquiry Counter
The system assists with:
- Passenger identity verification
- Flight number confirmation
- Departure and destination city information
- Travel date verification
- Flight status checking
- Check-in counter information
- Boarding gate details
- Baggage allowance information
- Flight delays or cancellation updates
- Ticket rescheduling assistance

## 🔧 Project Structure

```
counter_assistant/
│
├── app.py                      # Main Streamlit web application
├── main.py                     # Command-line speech-to-speech demo
├── requirements.txt            # Python dependencies
│
└── bhashini_translator/        # Bhashini API integration module
    ├── __init__.py
    ├── bhashini_translator.py  # Main translator class
    ├── config.py               # API configuration
    ├── payloads.py             # API payload generators
    └── pipeline_config.py      # Pipeline configuration handler
```

## 🎯 How It Works

1. **Language Selection**: Counter staff selects their language and customer's language
2. **Service Type**: Choose between Railway or Airport enquiry
3. **Question Display**: Pre-defined questions are displayed and translated to customer's language
4. **Audio Playback**: Questions can be played in audio format for the customer
5. **Customer Response**: Customer records their answer in their native language
6. **Speech Recognition**: Audio is converted to text using ASR (Automatic Speech Recognition)
7. **Translation**: Customer's response is translated to counter staff's language
8. **Display**: Both original and translated text are displayed for the counter staff

## 🔌 Bhashini API Integration

The application uses Bhashini API for:
- **ASR** (Automatic Speech Recognition): Convert speech to text
- **NMT** (Neural Machine Translation): Translate text between languages
- **TTS** (Text-to-Speech): Convert text to speech audio

## 📦 Dependencies

- `streamlit`: Web application framework
- `audio-recorder-streamlit`: Audio recording component for Streamlit
- `python-dotenv`: Environment variable management
- `requests`: HTTP library for API calls
- `bhashini_translator`: Bhashini API wrapper
- `speech_recognition`: Speech recognition library (for main.py)

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

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

For issues and questions, please open an issue in the repository.

## 🙏 Acknowledgments

- Bhashini API for providing multilingual AI services
- Streamlit for the web application framework
- All contributors and users of this system

---

**Note**: Make sure to obtain valid Bhashini API credentials before using this application. Visit the [Bhashini platform](https://bhashini.gov.in/) for more information.
