import json
from flask import Flask, jsonify, request, send_from_directory
from flask.templating import render_template
from sql_connection import sql_connection
import blogs_dao


app = Flask(__name__)

connection = sql_connection()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/getBlogs", methods=['GET'])
def get_blogs():
    result = blogs_dao.get_all_blogs(connection)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin' , '*')

    return response

@app.route('/deleteBlog/<id>', methods=['DELETE'])
def delete_blog(id):
    return_id = blogs_dao.delete_blog(connection, id)
    response = jsonify({
        'blog_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/addBlog', methods=['POST'])
def add_blog():
    request_payload = json.loads(request.get_data())
    result = blogs_dao.insert_new_blog(connection, request_payload)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route("/editBlog", methods=['PATCH'])
def edit_blog():
    request_payload = json.loads(request.get_data())
    result = blogs_dao.update_blog_by_id(connection,request_payload)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin' , '*')
    return response

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('./templates/js', path)



if __name__ == "__main__":
    app.run(debug=True)