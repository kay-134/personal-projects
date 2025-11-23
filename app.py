"""
PCOS Buddy - Web Application
A friendly chatbot web interface for PCOS information and support.
"""

from flask import Flask, render_template, request, jsonify, session
from chatbot import PCOSChatbot
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Store chatbot instances for each session
chatbots = {}

def get_chatbot():
    """Get or create a chatbot instance for the current session."""
    session_id = session.get('session_id')
    if not session_id:
        session_id = secrets.token_hex(8)
        session['session_id'] = session_id

    if session_id not in chatbots:
        chatbots[session_id] = PCOSChatbot()

    return chatbots[session_id]

@app.route('/')
def home():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/api/start', methods=['POST'])
def start_chat():
    """Start a new chat and return the greeting."""
    chatbot = get_chatbot()
    greeting = chatbot.get_initial_greeting()
    return jsonify({'response': greeting})

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    data = request.get_json()
    message = data.get('message', '').strip()

    if not message:
        return jsonify({'error': 'No message provided'}), 400

    chatbot = get_chatbot()
    response = chatbot.generate_response(message)

    return jsonify({'response': response})

@app.route('/api/tips', methods=['GET'])
def get_tips():
    """Get quick tips for new PCOS patients."""
    chatbot = get_chatbot()
    tips = chatbot.get_quick_tips()
    return jsonify({'tips': tips})

@app.route('/api/reset', methods=['POST'])
def reset_chat():
    """Reset the chat conversation."""
    session_id = session.get('session_id')
    if session_id and session_id in chatbots:
        del chatbots[session_id]

    session['session_id'] = secrets.token_hex(8)
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
