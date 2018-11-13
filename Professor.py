from Person import Person
from BabsonPerson import BabsonPerson

class Professor(BabsonPerson):

    def __init__(self, name, course):
        BabsonPerson.__init__(self, name)
        self.course = course

    def get_title(self):
        return self.title

    def speak(self, utterance):
        new_utterance = 'In course ' + self.course + ' we say '
        BabsonPerson.speak(self, new_utterance + utterance)

zi = Professor('Zi', "Professor")
print(zi.speak('hello there'))