from flask import Flask, request, render_template_string
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': os.environ.get('DB_HOST', 'db'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', 'password'),
    'database': os.environ.get('DB_NAME', 'testdb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content VARCHAR(255) NOT NULL
        )
    ''')
    conn.commit()

    if request.method == 'POST':
        message = request.form['message']
        cursor.execute('INSERT INTO messages (content) VALUES (%s)', (message,))
        conn.commit()

    cursor.execute('SELECT content FROM messages ORDER BY id DESC')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>DevOps Demo App</title>
        <style>
            * { box-sizing: border-box; margin: 0; padding: 0; }
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            .container {
                background: #ffffff;
                border-radius: 16px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.3);
                padding: 40px;
                max-width: 500px;
                width: 100%;
            }
            h1 {
                color: #4c1d95;
                font-size: 26px;
                margin-bottom: 8px;
                text-align: center;
            }
            .subtitle {
                text-align: center;
                color: #6b7280;
                font-size: 13px;
                margin-bottom: 24px;
            }
            form {
                display: flex;
                gap: 10px;
                margin-bottom: 24px;
            }
            input[type="text"] {
                flex: 1;
                padding: 12px 16px;
                border: 2px solid #e5e7eb;
                border-radius: 8px;
                font-size: 14px;
                outline: none;
                transition: border-color 0.2s;
            }
            input[type="text"]:focus {
                border-color: #764ba2;
            }
            button {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.15s, box-shadow 0.15s;
            }
            button:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(118, 75, 162, 0.4);
            }
            h2 {
                color: #374151;
                font-size: 16px;
                margin-bottom: 12px;
                border-bottom: 2px solid #f3f4f6;
                padding-bottom: 8px;
            }
            ul { list-style: none; }
            li {
                background: #f9fafb;
                padding: 12px 16px;
                border-radius: 8px;
                margin-bottom: 8px;
                border-left: 4px solid #764ba2;
                color: #374151;
                font-size: 14px;
                animation: fadeIn 0.3s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(-5px); }
                to { opacity: 1; transform: translateY(0); }
            }
            .empty-msg {
                text-align: center;
                color: #9ca3af;
                font-size: 13px;
                padding: 20px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 DevOps Demo App</h1>
            <p class="subtitle">Flask + Docker + MySQL + Docker Compose</p>
            <form method="POST">
                <input type="text" name="message" placeholder="Type a message..." required>
                <button type="submit">Submit</button>
            </form>
            <h2>📋 Saved Messages</h2>
            <ul>
                {% for msg in messages %}
                    <li>{{ msg[0] }}</li>
                {% endfor %}
                {% if not messages %}
                    <p class="empty-msg">No messages yet — add one above!</p>
                {% endif %}
            </ul>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html, messages=messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
