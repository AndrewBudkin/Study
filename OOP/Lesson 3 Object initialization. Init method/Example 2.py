class SoccerPlayer():
    def __init__(self, name, surname, goals=0, assists=0):
        self.name = name
        self.surname = surname
        self.goals = goals
        self.assist = assists

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=0):
        self.assist += assists

    def statistics(self):
        return f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assist}'


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
print(leo.statistics())
