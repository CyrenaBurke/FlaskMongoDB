from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['note_app'] 
notes_collection = db['notes'] 

@app.route('/')
def index():
    notes = notes_collection.find()  
    return render_template('home.html', notes=notes) 

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        cwid = request.form['cwid']
        name = request.form['name']
        
        notes_collection.insert_one({
            'cwid': cwid,
            'name': name
        })
        return redirect(url_for('index')) 
    return render_template('add_note.html')  

@app.route('/delete/<note_id>')
def delete_note(note_id):
    notes_collection.delete_one({'_id': ObjectId(note_id)})
    return redirect(url_for('index'))  

if __name__ == '__main__':
    app.run(debug=True)
