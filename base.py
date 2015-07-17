__author__ = 'deepak'

class Notification():

    def __init__(self, detail, *topics):
        self.detail = detail
        self.topics =[]
        for topic in topics:
            self.topics.append(topic)

    def addTopics(self, topic):
        self.topics.append(topic)


    def getDescription(self):
        return self.detail

    def getTopics(self):
        return self.topics