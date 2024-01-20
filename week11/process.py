import tui


def list_years(data):
    tui.started("Listing years...")
    years = set()

    for record in data:
        year = int(record[9])
        years.add(year)

    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tallying medals...")
    medal_count = {"Gold": 0, "Silver": 0, "Bronze": 0}

    for record in data:
        medal = record[14]
        if medal in medal_count:
            medal_count[medal] += 1

    tui.display_medal_tally(medal_count)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team.")
    team_medals = {}

    for record in data:
        team = record[6]
        medal = record[14]
        if team in team_medals:
            if medal in team_medals[team]:
                team_medals[team][medal] += 1
            else:
                team_medals[team][medal] = 1
        else:
            team_medals[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_medals[team][medal] = 1

    tui.display_team_medal_tally(team_medals)
    tui.completed()
