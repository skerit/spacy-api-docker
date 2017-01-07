import spacy
from spacyapi import options
import pkg_resources


class Spacy(object):
    lang = options()['language']
    version = pkg_resources.get_distribution("spacy").version
    nlp = spacy.load(lang)

    def analyze(self, text: str, fields: list) -> dict:
        """
        Analyzes the given text and returns only the provided fields
        :param text: A text.
        :param fields: A list of fields to be returned like 'pos'.
        :return: The ling. analysis of the text.
        """
        doc = self.nlp(text)

        ret = {
            'numOfSentences': len(list(doc.sents)),
            'numOfTokens': len(list(doc)),
            'sentences': []
        }

        for sentence in doc.sents:
            sentence_analysis = [{
                'token': w.orth_,
                'lemma': w.lemma_,
                'tag': w.tag_,
                'ner': w.ent_type_,
                'offsets': {
                    'begin': w.idx,
                    'end': w.idx + len(w.orth_)
                },
                'oov': w.is_oov,
                'stop': w.is_stop,
                'url': w.like_url,
                'email': w.like_email,
                'num': w.like_num,
                'pos': w.pos_
            } for w in sentence]

            if fields:
                # Remove certain fields if requested
                sentence_analysis = [
                    dict([(k, v) for k, v in token.items() if k in fields])
                    for token in sentence_analysis
                ]
            ret['sentences'].append(sentence_analysis)
        return ret
