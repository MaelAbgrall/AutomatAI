import json


def create_folder(path):
    pass


def save_model(model, path):
    """save a keras model

    Arguments:
        model {keras.model} -- a keras model
        path {string} -- /path/to/file.h5
    """
    model.save_weights(path)


def save_architecture(model, path):
    """save the architecture of a model

    Arguments:
        model {keras.model} -- a keras model
        path {string} -- /path/to/file.json
    """
    with open(path, 'w+') as json_file:
        json_file.write(model.to_json())


def load_architecture(path):
    """load a model's architecture from a json file

    Arguments:
        path {string} -- /path/to/file/json

    Returns:
        keras.model -- a keras model
    """
    from keras.models import model_from_json  # if this module is imported in global, keras can't be used in multiprocessing
    with open(path, 'r') as json_file:
        architecture = model_from_json(json_file.read())
    return architecture


def load_weights(model, path):
    """load weights for a model

    Arguments:
        model {keras.model} -- a keras model
        path {string} -- /path/to/file.h5

    Returns:
        keras.model -- 
    """
    model.load_weights(path)
    return model

def read_json(path):
    """read a json file and return an oject

    Arguments:
        path {string} -- /path/to/file.json

    Returns:
        datastructure -- data structure defined at write
    """

    with open(path, 'r') as json_file:
        data_structure = json.load(json_file)
    return data_structure

def write_json(data, path):
    """write an object in a json file
    
    Arguments:
        data {object} -- 
        path {string} -- /path/to/file.json
    """
    with open(path, 'w+') as json_file:
        json.dump(data, json_file)