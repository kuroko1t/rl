import pickle

def pickle_write(df, name):
    with open(name, 'wb') as f:
        pickle.dump(df, f)

def pickle_read(name):
    with open(name, mode='rb') as f:
        return pickle.load(f)
