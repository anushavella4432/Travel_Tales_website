import pickle

def save_data(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        return data
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist
