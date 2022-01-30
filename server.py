from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def default():
  return "Hello World!"
@app.route('/dojo')
def dojo():
  return "Dojo!"
@app.route('/say/<name>')
def say_hi(name): 
  return (f"Hi {name}!")
@app.route('/repeat/<int:repeat_num>/<name>')
def repeat(repeat_num, name):
  array = ""
  for x in range(0,repeat_num):
    array += f"{name}\n"
  return array

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
  app.run(debug=True)    # Run the app in debug mode.