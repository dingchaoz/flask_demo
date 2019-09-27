
from nltk.chunk import ChunkParserI
from nltk.corpus import names


class PersonChunker(ChunkParserI):
    def __init__(self):
        self.name_set = set(names.words())

    def parse(self, tagged_sent):

        iobs = []
        in_person = False
        for word in tagged_sent:
            if word in self.name_set and in_person:
                iobs.append((word, 'I-PERSON'))
            elif word in self.name_set:
                iobs.append((word, 'B-PERSON'))
                in_person = True
            else:
                iobs.append((word, 'O'))
                in_person = False

        return iobs


chunker = PersonChunker()


def return_names(chunker, sentence='hello David and Lily Smith'):
    print("Person name  : ",
          chunker.parse(sentence.split(' ')))


return_names(chunker)
