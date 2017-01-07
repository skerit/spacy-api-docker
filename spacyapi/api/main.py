from spacyapi.common.spacy import Spacy
from spacyapi import options
import time

analyzer = Spacy()
print("SpaCy loaded for '%s'!" % analyzer.lang)


def post(request: dict):
    t0 = time.time()
    ret = {
        'version': analyzer.version,
        'lang': analyzer.lang
    }

    if options().get('apiKeys'):
        if request.get('key') not in options().get('apiKeys'):
            return {"message": "An API key is required."}, 403

    if request.get('text'):
        # Analyze only a single text
        ret['analysis'] = [
            analyzer.analyze(request.get('text'), request.get('fields'))]
        ret['numOfTexts'] = 1
    elif request.get('texts'):
        ret['analysis'] = [
            analyzer.analyze(text, request.get('fields'))
            for text in request.get('texts')]
        ret['numOfTexts'] = len(request.get('texts'))

    ret['performance'] = time.time() - t0

    return ret, 200
