# Main function to run the TV show manager
def main():
    while True:
        shows_list = read_shows()  # Read the current list of shows from the file
        action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
''')
        if action == '1':
            add_show(shows_list)  # Add a new show
        elif action == '2':
            remove_show(shows_list)  # Remove a show
        elif action == '3':
            view(shows_list)  # View the list of shows
        elif action == '4':
            print("Thanks for using this app!")
            break

main()