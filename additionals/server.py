from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='./') 

@app.route('/') 
def send_index_file(): 
    return send_from_directory(app.static_folder, 'retrieve_webapi.html') 

if __name__ == '__main__': 
    app.run(host='0.0.0.0')