# app.py - intentionally includes some security issues for demonstration
from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    # Add some sample data
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description) VALUES (1, 'Laptop', 'A portable computer')")
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description) VALUES (2, 'Phone', 'A mobile device')")
    cursor.execute("INSERT OR IGNORE INTO items (id, name, description) VALUES (3, 'Tablet', 'A touchscreen device')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Secure DevOps Demo App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                }
                h1 { color: #333; }
                form {
                    margin: 20px 0;
                    padding: 20px;
                    background: #f5f5f5;
                    border-radius: 8px;
                }
                input[type="text"] {
                    padding: 10px;
                    width: 300px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                button {
                    padding: 10px 20px;
                    background: #007bff;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                }
                button:hover { background: #0056b3; }
            </style>
        </head>
        <body>
            <h1>Secure DevOps Demo App</h1>
            <p>Welcome! This is a demo application for learning DevSecOps practices.</p>
            
            <form action="/search" method="get">
                <h3>Search Items</h3>
                <input type="text" name="query" placeholder="Search for items...">
                <button type="submit">Search</button>
            </form>
            
            <h3>Available Endpoints:</h3>
            <ul>
                <li><a href="/">/</a> - This home page</li>
                <li><a href="/search?query=laptop">/search?query=laptop</a> - Search for items</li>
                <li><a href="/health">/health</a> - Health check endpoint</li>
            </ul>
        </body>
        </html>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    
    # INTENTIONAL VULNERABILITY: SQL Injection
    # This is deliberately insecure for demonstration purposes
    # The security scanner (Bandit) should flag this!
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    
    # BAD: String formatting in SQL query (vulnerable to SQL injection)
    cursor.execute(f"SELECT * FROM items WHERE name LIKE '%{query}%' OR description LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    
    # INTENTIONAL VULNERABILITY: XSS (Cross-Site Scripting)
    # The query is rendered without escaping
    results_html = ""
    for row in results:
        results_html += f"<li><strong>{row[1]}</strong>: {row[2]}</li>"
    
    if not results:
        results_html = "<li>No items found</li>"
    
    # BAD: Using render_template_string with user input
    return f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Search Results</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                }}
                a {{ color: #007bff; }}
            </style>
        </head>
        <body>
            <h1>Search Results for: {query}</h1>
            <ul>{results_html}</ul>
            <p><a href="/">← Back to Home</a></p>
        </body>
        </html>
    '''

@app.route('/health')
def health():
    """Health check endpoint for container orchestration"""
    return {'status': 'healthy', 'app': 'devsecops-demo'}, 200

# Initialize database when app starts
init_db()

if __name__ == '__main__':
    # BAD: Debug mode enabled and binding to all interfaces
    # Another issue for the security scanner to catch
    app.run(host='0.0.0.0', port=5000, debug=True)
