from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



# quotes= {
#     "happy":["hy -vishnu", "hello -jeno"],
# }

# print(quotes["happy"][0].split('-')[1])