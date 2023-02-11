try:
    my_file = open("epl.txt", "r")

    teams = []

    for line in my_file:
        #data = line.split(":")
        teams.append(line)

finally:
    my_file.close()

class Epl:
    def __init__(self, teams, stadium, city):
        self.teams = teams
        self.stadium = stadium
        self.city = city

    def __repr__(self):
        return f"{self.teams}/{self.stadium}/{self.city}"

def parseEpl(s : str):
    data = s.split(":") [0].split("-")
    return Epl(data[0], data[1], data[2])

d = parseEpl("teams")
print(d)





