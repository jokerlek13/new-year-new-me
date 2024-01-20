import csv
import tui
import process

def read_data(file_path):
    tui.started(f"Reading data from {file_path}")
    data = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        tui.error(f"File not found: {file_path}")

    tui.completed()
    return data


def run():
    file_path = "C:\\Users\\iulia\\Downloads\\athlete_events.csv"
    athlete_data = read_data(file_path)

    while True:
        selection = tui.menu()
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "ctally":
            process.tally_team_medals(athlete_data)
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")

if __name__ == "__main__":
    run()

