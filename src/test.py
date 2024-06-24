from flask import Flask
from sklearn.ensemble import RandomForest

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)

# Let's build a random forest regression with control of leaves
rf = RandomForest(n_estimators=100, max_depth=10, min_samples_leaf=50)

# We need to train the model with some data to make predictions
# Let's use a dataset from sklearn

