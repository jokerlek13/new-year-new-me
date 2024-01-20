def started(msg=""):
    LINE_WIDTH = 85
    print('-' * LINE_WIDTH)
    print(f"Operation started: {msg}...\n")


def completed():
    LINE_WIDTH = 85
    print("\nOperation completed.")
    print('-' * LINE_WIDTH)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("Please select one of the following options:")
    print(f"{'[years]':<10} List unique years")
    print(f"{'[tally]':<10} Tally up medals")
    print(f"{'[ctally]':<10} Tally up medals for each team")
    print(f"{'[exit]':<10} Exit the program")
    return input("Your selection: ")


def display_medal_tally(tally):
    print(f"| {'Medal':<10} | {'Count':<10} |")
    for medal, count in tally.items():
        print(f"| {medal:<10} | {count:<10} |")


def display_team_medal_tally(team_tally):
    for team, medals in team_tally.items():
        print(team)
        for medal, count in medals.items():
            print(f"\t{medal}: {count}")


def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)
