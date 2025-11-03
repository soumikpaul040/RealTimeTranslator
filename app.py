import streamlit as st
from audio_recorder_streamlit import audio_recorder
from dotenv import load_dotenv
import base64
import time
import datetime
import threading
from bhashini_translator import Bhashini

load_dotenv()

LANGUAGES = {
    "Hindi (hi)": "hi",
    "English (en)": "en", 
    "Bengali (bn)": "bn",
    "Tamil (ta)": "ta",
    "Telugu (te)": "te",
    "Gujarati (gu)": "gu",
    "Kannada (kn)": "kn",
    "Malayalam (ml)": "ml",
    "Marathi (mr)": "mr",
    "Punjabi (pa)": "pa",
    "Urdu (ur)": "ur",
    "Maithili (mai)": "mai"
}

# Page configuration
st.set_page_config(page_title="🚆 Railway Counter Assistant", layout="wide")

# Custom CSS for vertical divider and styling
st.markdown("""
<style>
.main-container {
    display: flex;
    height: 100vh;
}
.left-panel {
    flex: 1;
    padding: 20px;
    border-right: 3px solid #e0e0e0;
    background-color: #f8f9fa;
}
.right-panel {
    flex: 1;
    padding: 20px;
    background-color: #fff8e1;
}
.staff-header {
    background: linear-gradient(135deg, #1e88e5, #1565c0);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
}
.customer-header {
    background: linear-gradient(135deg, #43a047, #2e7d32);
    color: white;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 20px;
}
.record-section {
    background: white;
    padding: 20px;
    border-radius: 10px;
    border: 2px solid #e0e0e0;
    margin: 10px 0;
}
.translation-output {
    background: #f0f8ff;
    padding: 15px;
    border-radius: 8px;
    border-left: 4px solid #2196f3;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 36px; font-weight: bold; color: #1565c0;'>� Railway Counter Real-Time Translation System</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 2px solid #1565c0;'>", unsafe_allow_html=True)

# Create two columns for staff and customer
left_col, right_col = st.columns([1, 1])

# Initialize session state for conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# LEFT SIDE - RAILWAY STAFF
with left_col:
    st.markdown("""
    <div class="staff-header">
        <h2>👨‍💼 Railway Staff Panel</h2>
        <p>Select your language and communicate with customers</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Staff language selection
    staff_lang_name = st.selectbox(
        "�️ Select Your Language", 
        list(LANGUAGES.keys()), 
        index=1,  # Default to English
        key="staff_lang"
    )
    staff_lang = LANGUAGES[staff_lang_name]
    
    # Center the recording section
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("### 🎤 Record Your Message")
    st.markdown("*Speak in your selected language. It will be translated for the customer.*")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Simple instruction text
    st.markdown("""
    <div style='text-align: center; padding: 10px; margin: 10px 0;'>
        <p style='color: #666; margin: 0; font-size: 14px;'>🎙️ Tap to record voice message</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Actual audio recorder - bigger and centered with custom styling
    st.markdown("""
    <div style='display: flex; justify-content: center; margin: 30px 0; padding: 20px;'>
    """, unsafe_allow_html=True)
    
    # Create centered columns for better positioning
    rec_col1, rec_col2, rec_col3 = st.columns([2, 1, 2])
    with rec_col2:
        staff_audio = audio_recorder(
            text="",
            recording_color="#e74c3c",
            neutral_color="#3498db",
            icon_name="microphone",
            icon_size="3x",
            key="staff_recorder"
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Simple audio handling for staff
    if staff_audio is not None:
        st.success("✅ Message recorded!")
        
        # Display audio with duration
        duration = len(staff_audio) / (16000 * 2)  # Approximate duration
        mins, secs = divmod(int(duration), 60)
        st.markdown(f"""
        <div style='background: #f8f9fa; padding: 10px; border-radius: 15px; border-left: 4px solid #2196f3;'>
            🎵 <strong>Voice Message</strong> - Duration: {mins:02d}:{secs:02d}
        </div>
        """, unsafe_allow_html=True)
        st.audio(staff_audio, format="audio/wav")
        
        # Process staff message button
        if st.button("🚀 Send to Customer", key="send_staff_msg", type="primary"):
            with st.spinner("🔄 Translating message..."):
                try:
                    # Get customer language for translation
                    if 'customer_lang' in st.session_state:
                        customer_lang = st.session_state.customer_lang
                        
                        # Convert audio to base64
                        audio_b64 = base64.b64encode(staff_audio).decode("utf-8")
                        
                        # Create translator (staff -> customer)
                        staff_translator = Bhashini(sourceLanguage=staff_lang, targetLanguage=customer_lang)
                        
                        # ASR: Convert staff speech to text
                        staff_translator.getPipeLineConfig("asr")
                        staff_text = staff_translator.asr(audio_b64)
                        
                        # Translate to customer language
                        staff_translator.getPipeLineConfig("translation")
                        translated_text = staff_translator.translate(staff_text)
                        
                        # TTS: Convert translation to audio
                        staff_translator.getPipeLineConfig("tts")
                        translated_audio_b64 = staff_translator.tts(translated_text)
                        
                        # Store in conversation history
                        st.session_state.conversation_history.append({
                            'speaker': 'staff',
                            'original_text': staff_text,
                            'translated_text': translated_text,
                            'audio_b64': translated_audio_b64,
                            'original_lang': staff_lang_name,
                            'target_lang': st.session_state.get('customer_lang_name', 'Hindi (hi)')
                        })
                        
                        st.success("✅ Message sent to customer!")
                        
                except Exception as e:
                    st.error(f"❌ Translation failed: {str(e)}")
    
    # Display conversation history (staff side)
    st.markdown("### 💬 Conversation History")
    for i, msg in enumerate(st.session_state.conversation_history):
        if msg['speaker'] == 'staff':
            st.markdown(f"""
            <div class="translation-output" style="color: #1a1a1a;">
                <strong style="color: #0d47a1;">🗣️ You said ({msg['original_lang']}):</strong><br>
                <span style="color: #212121;">{msg['original_text']}</span><br><br>
                <strong style="color: #0d47a1;">🌍 Translated to customer:</strong><br>
                <span style="color: #212121;">{msg['translated_text']}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div style="background: #fff3e0; padding: 15px; border-radius: 8px; border-left: 4px solid #ff9800; margin: 10px 0; color: #1a1a1a;">
                <strong style="color: #e65100;">👤 Customer said ({msg['original_lang']}):</strong><br>
                <span style="color: #212121;">{msg['original_text']}</span><br><br>
                <strong style="color: #e65100;">🌍 Translation for you:</strong><br>
                <span style="color: #212121;">{msg['translated_text']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Play translated audio for staff
            if msg.get('audio_b64'):
                st.markdown("🔊 **Listen to translation:**")
                audio_bytes = base64.b64decode(msg['audio_b64'])
                st.audio(audio_bytes, format="audio/wav")

# RIGHT SIDE - CUSTOMER  
with right_col:
    st.markdown("""
    <div class="customer-header">
        <h2>👥 Customer Panel</h2>
        <p>Select your preferred language and communicate</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Customer language selection
    customer_lang_name = st.selectbox(
        "🌍 Select Your Language", 
        list(LANGUAGES.keys()), 
        index=0,  # Default to Hindi
        key="customer_lang_select"
    )
    customer_lang = LANGUAGES[customer_lang_name]
    
    # Store in session state
    st.session_state.customer_lang = customer_lang
    st.session_state.customer_lang_name = customer_lang_name
    
    # Center the recording section
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("### 🎤 Record Your Response")
    st.markdown("*Speak in your selected language. It will be translated for the railway staff.*")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Simple instruction text
    st.markdown("""
    <div style='text-align: center; padding: 10px; margin: 10px 0;'>
        <p style='color: #666; margin: 0; font-size: 14px;'>🎙️ Tap to record voice message</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Actual audio recorder - bigger and centered with custom styling
    st.markdown("""
    <div style='display: flex; justify-content: center; margin: 30px 0; padding: 20px;'>
    """, unsafe_allow_html=True)
    
    # Create centered columns for better positioning
    rec_col1, rec_col2, rec_col3 = st.columns([2, 1, 2])
    with rec_col2:
        customer_audio = audio_recorder(
            text="",
            recording_color="#27ae60",
            neutral_color="#27ae60", 
            icon_name="microphone",
            icon_size="3x",
            key="customer_recorder"
        )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Simple audio handling for customer
    if customer_audio is not None:
        st.success("✅ Response recorded!")
        
        # Display audio with duration
        duration = len(customer_audio) / (16000 * 2)  # Approximate duration  
        mins, secs = divmod(int(duration), 60)
        st.markdown(f"""
        <div style='background: #f8f9fa; padding: 10px; border-radius: 15px; border-left: 4px solid #27ae60;'>
            🎵 <strong>Voice Message</strong> - Duration: {mins:02d}:{secs:02d}
        </div>
        """, unsafe_allow_html=True)
        st.audio(customer_audio, format="audio/wav")
        
        # Process customer response button
        if st.button("🚀 Send to Staff", key="send_customer_msg", type="primary"):
            with st.spinner("🔄 Translating response..."):
                try:
                    # Convert audio to base64
                    audio_b64 = base64.b64encode(customer_audio).decode("utf-8")
                    
                    # Create translator (customer -> staff)
                    customer_translator = Bhashini(sourceLanguage=customer_lang, targetLanguage=staff_lang)
                    
                    # ASR: Convert customer speech to text
                    customer_translator.getPipeLineConfig("asr")
                    customer_text = customer_translator.asr(audio_b64)
                    
                    # Translate to staff language
                    customer_translator.getPipeLineConfig("translation")
                    translated_text = customer_translator.translate(customer_text)
                    
                    # TTS: Convert translation to audio
                    customer_translator.getPipeLineConfig("tts")
                    translated_audio_b64 = customer_translator.tts(translated_text)
                    
                    # Store in conversation history
                    st.session_state.conversation_history.append({
                        'speaker': 'customer',
                        'original_text': customer_text,
                        'translated_text': translated_text,
                        'audio_b64': translated_audio_b64,
                        'original_lang': customer_lang_name,
                        'target_lang': staff_lang_name
                    })
                    
                    st.success("✅ Response sent to railway staff!")
                    
                except Exception as e:
                    st.error(f"❌ Translation failed: {str(e)}")
    
    # Display messages from staff (customer side)
    st.markdown("### 💬 Messages from Railway Staff")
    for i, msg in enumerate(st.session_state.conversation_history):
        if msg['speaker'] == 'staff':
            st.markdown(f"""
            <div style="background: #e3f2fd; padding: 15px; border-radius: 8px; border-left: 4px solid #2196f3; margin: 10px 0; color: #1a1a1a;">
                <strong style="color: #0d47a1;">👨‍💼 Railway Staff Message:</strong><br>
                <span style="color: #212121;">{msg['translated_text']}</span><br>
            </div>
            """, unsafe_allow_html=True)
            
            # Play audio for customer
            if msg.get('audio_b64'):
                st.markdown("🔊 **Listen to message:**")
                audio_bytes = base64.b64decode(msg['audio_b64'])
                st.audio(audio_bytes, format="audio/wav")
        else:
            st.markdown(f"""
            <div class="translation-output" style="color: #1a1a1a;">
                <strong style="color: #2e7d32;">🗣️ You said ({msg['original_lang']}):</strong><br>
                <span style="color: #212121;">{msg['original_text']}</span><br><br>
                <strong style="color: #2e7d32;">🌍 Translated to staff:</strong><br>
                <span style="color: #212121;">{msg['translated_text']}</span>
            </div>
            """, unsafe_allow_html=True)

# Bottom section - Clear conversation
st.markdown("<hr>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    if st.button("🗑️ Clear Conversation", type="secondary"):
        st.session_state.conversation_history = []
        st.success("Conversation cleared!")
        st.rerun()
