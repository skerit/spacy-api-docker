from spacyapi.common.spacy import Spacy


def get():
    if not Spacy().nlp:
        return {
           "health": "red",
           "message": "Models are not loaded."
         }, 503

    return {
        "health": "green"
    }, 200
