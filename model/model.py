from tensorflow.keras.models import load_model

model = load_model("./model/model_dir.keras")

def predict(data):
    return model.predict(data)

