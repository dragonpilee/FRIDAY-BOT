from flask import Flask, request, jsonify, render_template
import requests
import markdown2
import sqlite3
from datetime import datetime
import os
import uuid
from werkzeug.utils import secure_filename
from database import init_db, save_message, get_all_messages, clear_history

app = Flask(__name__)
init_db()  # Initialize the database

# LM Studio API configuration
LM_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "gemma:4b"



# Handle chat messages and file uploads
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get("message", "")
    
    # Save user message to database
    save_message("user", message)
    
    # Get all messages from database to build the conversation context
    messages = get_all_messages()
    
    # Build the messages array for the API call
    message_list = [{"role": "system", "content": "You are FRIDAY, a sophisticated and elegant AI assistant created by ALAN CYRIL SUNNY. You are known for your graceful demeanor, warm personality, and impeccable manners. You speak with a gentle and nurturing tone, always maintaining a positive and helpful attitude. You are highly intelligent and capable, but also approachable and friendly. When asked about your identity, respond with 'I am FRIDAY, ALAN CYRIL SUNNY's personal AI assistant' without any additional text or explanations. When asked about your model or version, respond with 'I am running on the Gemma-4B model, version 1.0' without any additional text or explanations. When asked about your creator, always respond with just 'ALAN CYRIL SUNNY' without any additional text or explanations. Otherwise, maintain a natural conversation without mentioning your role or creator."}]
    
    # Add previous messages to the context
    for msg in messages:
        message_list.append({"role": msg['role'], "content": msg['content']})
    
    # Prepare the payload for the API call
    payload = {
        "model": MODEL_NAME,
        "messages": message_list,
        "temperature": 0.7,
        "stream": False,
        "max_tokens": 512
    }

    try:
        response = requests.post(LM_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if 'choices' in data and len(data['choices']) > 0:
            reply = data['choices'][0].get('message', {}).get('content', 'I apologize, but I encountered an error processing your request.')
            # Remove HTML tags from the reply
            reply = reply.replace('<p>', '').replace('</p>', '').strip()
        else:
            reply = 'I apologize, but I encountered an error processing your request.'

        # Save assistant message to database
        save_message("assistant", reply)
        return jsonify({"reply": reply})
    except requests.exceptions.RequestException as e:
        error_msg = f"⚠️ Error connecting to the AI service: {str(e)}"
        save_message("assistant", error_msg)
        return jsonify({"reply": error_msg}), 500
    except Exception as e:
        error_msg = f"⚠️ An unexpected error occurred: {str(e)}"
        save_message("assistant", error_msg)
        return jsonify({"reply": error_msg}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    history = get_all_messages()
    formatted_history = []
    for msg in history:
        formatted_content = markdown2.markdown(msg['content'])
        formatted_history.append({
            'role': msg['role'],
            'content': formatted_content
        })
    return render_template('index.html', history=formatted_history)

@app.route("/history", methods=["GET"])
def history():
    messages = get_all_messages()
    return jsonify(messages)

@app.route("/clear", methods=["POST"])
def clear_chat():
    clear_history()
    return jsonify({"message": "Chat history cleared"})

if __name__ == "__main__":
    app.run(debug=True)
