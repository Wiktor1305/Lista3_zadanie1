# Lista3_zadanie1:
1. Create a new project "Hello_world"
2. Click on Settings>Project: Hello_world>Python interpreter>Install(plus symbol)>search "Flask"> Install Package>close
3. Create a new file "aplikacja.py"
4. Code for "aplikacja.py":
 
  from flask import Flask

  aplikacja = Flask(__name__)

  @aplikacja.route("/")
  def index():
      return "<p>Hello, World!</p>"

  if __name__ == "__main__":
     aplikacja.run(debug=True)
     
5. Open a terminal and write:
...\Hello_world\Scripts\activate.bat
6. Write: python aplikacja.py
7. Open a browser and write: http://localhost:5000/
