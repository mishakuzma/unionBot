class Union:
    """A union is a set of participants."""
    def __init__(self, firstUser):
        # list of people who cannot participate in the union (strings)
        self.blocklist = []

        # list of people who are participating in the union. Establishing union requires one person to start
        self.participants = [firstUser]

        # list of strings stating expectations in the union.
        self.rules = []

    def addRule(self, inputRule: str):
        self.rules += inputRule

    def addParticipant(self, inParticipant):
        #  Add a participant to the union
        if inParticipant is Participant:
            self.participants += inParticipant
        else:
            raise TypeError

    def removeParticipant(self, inParticipant):
        #  Remove a participant from the union
        if inParticipant in self.participants:
            self.participants.remove(inParticipant)
        else:
            raise ValueError

class Decision(Union):
    """A decision is a yes or no question that voting participants submit answers to."""

    def __init__(self):
        self.votedList = []
        self.voteCount = 0
        self.voterCount = 0
        self.finalDecision = False

    def addVoter(self, inParticipant):
        #  Add a participant to the list of people who votd
        self.votedList += inParticipant

    def checkVoter(self, inParticipant):
        # Check if the user is allowed to vote (ex. hasn't voted already)
        # If voted already, return False
        if inParticipant in self.votedList:
            return False
        else:
            return True

    def checkFinalResult(self):
        if self.voteCount > 0:
            self.finalDecision = True
        else:
            self.finalDecision = False

    def addVoter(self, inParticipant):
        if self.checkVoter(inParticipant):
            return ValueError # TODO: need error handling
        else:
            #checkVote
            self.voterCount += 1
            self.votedList += inParticipant

class Participant(Union):
    """A Participant is a person who is inside of a democratically managed room."""
    def __init__(self, inName: str):
        self.name = inName
        self.canTalk = False
        self.canVote = False

    def checkVote(self):
        # Wrapper to return whether this person can vote in the union or not.
        return self.canVote

    def checkIfCanTalk(self):
        # Wrapper to return whether this person is allowed to talk.
        return self.canTalk

    def allowVote(self):
        # Change participant's status to allowed to vote
        self.canVote = True

    def allowTalk(self):
        # Change participant's status to allowed to talk
        self.canTalk = True

    def restrictVote(self):
        # Change participant's status to not allowed to vote
        self.canVote = False

    def restrictTalk(self):
        # Change participant's status to not allowed to talk
        self.canTalk = False

"""

test1 = Participant('hi')
print(test1.checkVote())
"""