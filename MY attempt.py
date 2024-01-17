"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import pandas as pd
import matplotlib.pyplot as plt

# Function to display title with dashes
def display_title(title):
    dash_line = '-' * len(title)
    print(dash_line)
    print(title)
    print(dash_line)

# Function to load data from CSV file or handle missing file
def load_data(csv_file_path):
    try:
        data = pd.read_csv(csv_file_path)
        print("Dataset loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found. Please provide the correct file path.")
        return None
csv_file_path = "C:\\Users\\iulia\\OneDrive\\Desktop\\project_template\\data\\disneyland_reviews.csv"
data = load_data(csv_file_path)

if data is None:
    exit()

# Print column names for verification
print("Columns in the dataset:", data.columns)

# Print column names for verification
print("Columns in the dataset:", data.columns)

# ... rest of your code ...


# Function to display a bar chart of the top 10 locations with the highest average rating for a park
def bar_chart_top_locations_for_park(data, park_name):
    # Filter data for the specified park
    park_data = data[data['Branch'] == park_name]

    if park_data.empty:
        print(f"No data found for {park_name}.")
        return

    # Calculate the average rating for each location
    location_avg_ratings = park_data.groupby('Reviewer_Location')['Rating'].mean().sort_values(ascending=False)

    # Select the top 10 locations
    top_10_locations = location_avg_ratings.head(10)

    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    top_10_locations.plot(kind='bar')
    plt.xlabel('Location')
    plt.ylabel('Average Rating')
    plt.title(f'Top 10 Locations with Highest Average Ratings for {park_name}')
    plt.xticks(rotation=45)
    plt.show()

# ... (rest of your code)


# Function to display a pie chart of the number of reviews for each park
def pie_chart_reviews_by_park(data):
    park_reviews_counts = data['Branch'].value_counts()
    plt.figure(figsize=(10, 6))
    plt.pie(park_reviews_counts, labels=park_reviews_counts.index, autopct='%1.1f%%')
    plt.title('Number of Reviews by Park')
    plt.axis('equal')
    plt.show()

# Function to display a bar chart of average review scores for each park
def bar_chart_average_scores_by_park(data):
    park_average_scores = data.groupby('Branch')['Rating'].mean()
    plt.figure(figsize=(12, 6))
    park_average_scores.plot(kind='bar')
    plt.xlabel('Park')
    plt.ylabel('Average Rating')
    plt.title('Average Review Scores by Park')
    plt.xticks(rotation=45)
    plt.show()

# Function to display a bar chart of the top 10 locations with the highest average rating for a park
# Function to display a bar chart of average ratings by month for a specific park
def bar_chart_average_ratings_by_month(data, park_name):
    # Filter out rows with invalid 'Year_Month' values and create a copy
    valid_data = data[(data['Year_Month'] != 'missing') & (data['Branch'] == park_name)].copy()

    # Convert 'Year_Month' to datetime and extract month name for the copy
    valid_data['Month'] = pd.to_datetime(valid_data['Year_Month'], format='%Y-%m').dt.month_name()

    # Group by month and calculate mean. Reindex to ensure months are in order.
    monthly_average_ratings = valid_data.groupby('Month')['Rating'].mean().reindex(
        ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Plotting
    plt.figure(figsize=(12, 6))
    monthly_average_ratings.plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title(f'Average Ratings by Month for {park_name}')
    plt.xticks(rotation=45)
    plt.show()

# Function to display a bar chart of average ratings by month for a specific park



# Load data from the CSV file
csv_file_path = "C:\\Users\\iulia\\OneDrive\\Desktop\\project_template\\data\\disneyland_reviews.csv"
data = load_data(csv_file_path)

if data is None:
    exit()

main_menu = "Please enter the letter which corresponds with your desired menu choice:\n[A] View Data\n[B] Visualise Data\n[X] Exit"

# ... (previous code)

while True:
    display_title("Disneyland Review Analyser")
    print(main_menu)
    user_choice = input("Enter your choice: ").strip().upper()

    if user_choice == "X":
        print("Exiting the program.")
        break

    if user_choice == "A":
        sub_menu_a = "Please enter the following options:\n[A] View Review by Park\n[B] Number of Reviews by Park and Reviewer Location\n[C] Average Score per year by Park\n[D] Average Score per Park by Reviewer Location\n[X] Return to Main Menu"
        while True:
            display_title("Sub-Menu A")
            print(sub_menu_a)
            sub_user_choice = input("Enter your choice: ").strip().upper()

            if sub_user_choice == "X":
                break

            if sub_user_choice == "A":
                # Option A: View Review by Park
                park_name = input("Enter the park name you wish to see reviews for: ")
                park_reviews = data[data['Branch'] == park_name]

                if not park_reviews.empty:
                    print(f"Reviews for {park_name}:")
                    for index, row in park_reviews.iterrows():
                        print(f"Reviewer Location: {row['Reviewer_Location']}, Rating: {row['Rating']}")
                else:
                    print(f"No reviews found for {park_name}.")


            elif sub_user_choice == "B":
                # Option B: Number of Reviews by Park and Reviewer Location
                park_name = input("Enter the park name: ")
                location = input("Enter the reviewer's location: ")
                filtered_data = data[(data['Branch'] == park_name) & (data['Reviewer_Location'] == location)]

                review_count = len(filtered_data)
                print(f"Number of reviews for {park_name} from {location}: {review_count}")

            elif sub_user_choice == "C":
                # Option C: Average Score per year by Park
                park_name = input("Enter the park name: ")
                year = input("Enter the year: ")
                year_reviews = data[(data['Branch'] == park_name) & (data['Year_Month'].str.startswith(year))]
                if not year_reviews.empty:
                    average_score = year_reviews['Rating'].mean()
                    print(f"Average score for {park_name} in {year}: {average_score:.2f}")
                else:
                    print(f"No reviews found for {park_name} in {year}.")

            elif sub_user_choice == "D":
                # Option D: Average Score per Park by Reviewer Location
                parks = data['Branch'].unique()
                for park_name in parks:
                    park_avg_by_location = data[data['Branch'] == park_name].groupby('Reviewer_Location')['Rating'].mean()
                    print(f"Average score for {park_name} by reviewer location:")
                    print(park_avg_by_location)

            else:
                print("Invalid choice. Please enter 'A', 'B', 'C', 'D', or 'X'.")

    # ... (continue with other options for sub-menu B)

    elif user_choice == "B":
        sub_menu_b = "Please enter the following options:\n[A] Pie Chart - Number of Reviews by Park\n[B] Bar Chart - Average Review Scores by Park\n[C] Bar Chart - Top 10 Locations for a Park\n[D] Bar Chart - Average Ratings by Month for a Park\n[X] Return to Main Menu"
        while True:
            display_title("Sub-Menu B")
            print(sub_menu_b)
            sub_user_choice = input("Enter your choice: ").strip().upper()

            if sub_user_choice == "X":
                break

            elif sub_user_choice == "A":
                pie_chart_reviews_by_park(data)

            elif sub_user_choice == "B":
                bar_chart_average_scores_by_park(data)

            elif sub_user_choice == "C":
                park_name = input("Enter the park name: ")
                bar_chart_top_locations_for_park(data, park_name)
            elif sub_user_choice == "D":
                park_name = input("Enter the park name: ")
                bar_chart_average_ratings_by_month(data, park_name)
    else:
        print("Invalid choice. Please enter 'A', 'B', or 'X'.")