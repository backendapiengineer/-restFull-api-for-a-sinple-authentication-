from database import db, Users
from flasks_object import app
from flask import  jsonify, session, request  
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/signup", methods=["POST"])
def signup():
  
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
  
    existing_name = Users.query.filter_by(name=name).first()  # Changed to .first()
    existing_email = Users.query.filter_by(email=email).first()  # Fixed typo and changed to .first()
    
    if not name :
        return jsonify({"error": "User name cannot be empty"}), 400  # Added error key
    elif len(name) > 20 :
        return jsonify({"error": "Name cannot exceed 20 characters"}), 400
    elif existing_name :
        return jsonify({"error": "User already exist"}), 400
    elif not email :
        return jsonify({"error": "Email cannot be empty"}), 400  # Added error key
    elif len(email) > 50 :
         return jsonify({"error": "Email cannot exceed 50 characters"}), 400
    elif existing_email :
        return jsonify({"error": "Email already registered"}), 400  # More specific message
    elif not password :
         return jsonify({"error": "Password cannot be empty"}), 400
    elif len(password) > 150 :
         return jsonify({"error": "Password cannot exceed 150 characters"}), 400
    else:
        hashed_password = generate_password_hash(password)
         
        
        new_user = Users(name=name, email=email, password=hashed_password)
        db.session.add(new_user)  
        db.session.commit() 
         
        return jsonify({"message": "Signup Successful"}), 201  # Changed to message
     
@app.route("/login", methods=["POST"])
def login():
    
    data = request.get_json()
    email = data.get('email')  
    password = data.get('password')
    
    if not email:
        return jsonify({"error": "Email cannot be empty"}), 400
    elif not password:
        return jsonify({"error": "Password cannot be empty"}), 400
    
    
    user = Users.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({"error": "Invalid email or password"}), 400
    elif not check_password_hash(user.password, password):  # Fixed order of parameters
        return jsonify({"error": "Invalid email or password"}), 400
    else:
        
        session['user_id'] = user.id
        session['user_email'] = user.email
        return jsonify({"message": "Login successful"}), 200

if __name__ == "__main__":
    app.run()