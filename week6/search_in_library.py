def search(file_name):

    print("Searching...")

    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(f"Looked in {line.strip()}.")

        print("...Done!")

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if 'file' in locals() and not file.closed:
            file.close()

def run_task3():

    search("data.txt")

run_task3()
