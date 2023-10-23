from flask import Flask, request, jsonify

app = Flask(__name__)

# Methods for API requests: GET, POST (create), PUT (update), DELETE
# Extend URLS with query parameters from the request method and GET with the url (get request url is in the form button click)

# GET request
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'Flask API',
        'email': 'hello@gmail.com'
    }

    req = request.args.get("req")
    if req:
        user_data['req'] = req
    
    return jsonify(user_data), 200 # response code 

# POST request
@app.route("/create-user",  methods=['POST']) # GET is default method, specifiy methods args for any other request
def create_user():
    # if request.method == "POST":
    #     print('updating!')
    data = request.get_json()

    # use POSTMAN to submit API requests to the server running via Python (e.g. submit JSON of user data)
    return jsonify(data), 201

#Default home route
@app.route('/')  # "/" = default route or url
def home():
    
    home_page = '''
<html>
    <div id="flask">
        <h1>
        <br><br>
        </h1>
        <h2 class="heading">Flask API</h2>
            <ul>
                <li>GET</li>
                <li>POST</li>
                <li>PUT</li>
                <li>DELETE</li>
                <li>Postman for submitting API requests</li>
                <li>Define functions through "route" decorators<br>that link to URLs</li>
                <li>Return response codes with requests</li>
                <li>Flask & APIs! 🤯</li>
            </ul>
    </div>

    <div id='req_div'>
        <form id=req_but action="http://127.0.0.1:5000/get-user/7177">
            <input type="submit" value="Request User ID" />
            <input type="hidden" name="req" value="hello world!" /> 
        </form>
    </div>
</html>

<style>
#flask {
    color: #fff;
    font-family: 'Segoe UI', sans-serif;
    box-sizing: border-box;
    scroll-behavior: smooth;
    font-size: 150%;
    min-height: 30%;
    display: flex;
    align-items: center;
    padding: 200px 0px 50px 100px;
    justify-content: center;
    vertical-align: middle;
}

html {
    background: #00000f;
    font-family: 'Segoe UI', sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    margin:0 auto;
}

#req_but {
    background-color: #00000f;
    font-family: 'Segoe UI', sans-serif;
    font-size: 150%;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    margin:0 auto;
}

#req_but a:hover {
	background-color: red;
}

input[type=submit] {
    color: white;
    background-color: #23005F;
    font-family: 'Segoe UI', sans-serif;
    font-size: 130%;
    display: flex;
    align-items: center;
    justify-content: center;
    vertical-align: middle;
    padding: 24px 24px 24px 24px;
    margin: 0 auto;
    border: none;
    border-radius: 25px;
}

input[type=submit]:hover {
    color: black;
    background-color: #f0f0f0;
}
</style>
'''

    return home_page

if __name__ == "__main__":
    app.run(debug=True)
