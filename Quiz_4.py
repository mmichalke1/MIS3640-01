ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=[], votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name= name
        self.winning_states = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        if len(self.winning_states) == 0:
            return "The Candidate, {}, has won no states.".format(self.name)
        else:
            self.votes = 0
            for state in self.winning_states:
                self.votes +=  ELECTORS.get(state)
            states = ', '.join(self.winning_states)
            return "The Candidate, {}, has won {} and has {} votes.".format(self.name, states, self.votes)

    def win_state(self, state):
        """Adds a tate to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)

    def __gt__(self, other):
        if self.votes > other.votes:
            dif = self.votes - other.votes
            return "{} has won the election by {} vote(s).".format(self.name, dif)
        elif self.votes < other.votes:
            dif = other.votes - other.votes
            return "{} has won the election by {} vote(s).".format(other.name, dif)
        else:
            return "{} and {} have tied".format(self.name, other.name)


def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA'])
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()