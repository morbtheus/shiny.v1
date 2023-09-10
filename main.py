import subprocess


def install_colorama():
    try:
        subprocess.run(["pip", "install", "colorama"])
    except Exception as e:
        print(f"Error installing Colorama: {e}")


def print_ascii_art():
    try:
        import colorama
        colorama.init()  # Initialize Colorama
        from colorama import Fore, Style

        ascii_art = r"""
                                                       ,::::.._
                                                   ,':::::::::.
                                               _,-'`:::,::(o)::`-,.._
                                            _.', ', `:::::::::;'-..__`.
                                       _.-'' ' ,' ,' ,\:::,'::-`'''
                                   _.-'' , ' , ,'  ' ,' `:::/
                             _..-'' , ' , ' ,' , ,' ',' '/::
                     _...:::'`-..'_, ' , ,'  , ' ,'' , ,'::|
                  _`.:::::,':::::,'::`-:..'_',_'_,'..-'::,'|
          _..-:::'::,':::::::,':::,':,'::,':::,'::::::,':::;
            `':,'::::::,:,':::::::::::::::::':::,'::_:::,'/
            __..:'::,':::::::--''' `-:,':,':::'::-' ,':::/
       _.::::::,:::.-''-`-`..'_,'. ,',  , ' , ,'  ', `','
     ,::SSt:''''`                 \:. . ,' '  ,',' '_,'
                                   ``::._,'_'_,',.-'
                                       \\ \\
                                        \\_\\
                                         \\`-`.-'_
                                      .`-.\\__`. ``
                                         ``-.-._
                                             `
        """
        colored_ascii_art = (
            f"{Fore.MAGENTA}{ascii_art}{Style.RESET_ALL}"
        )
        print("This tool made by @metheus")
        print(colored_ascii_art)
        print("This tool made by @metheus")

    except ImportError:
        print("Colorama is not installed. Installing it now...")
        install_colorama()
        print("Colorama installed. Please run the script again.")


def function_1():
    print("Function 1 activated!")


def function_2():
    import requests
    import uuid

    def check_username_snapchat(username):
        url = "https://app.snapchat.com/loq/suggest_username_v3"
        user_agent = str(uuid.uuid4())  # Generate a UUID version 4
        headers = {
            "User-Agent": user_agent,
            "allow-recycled-username": "true"
        }
        data = {"requested_username": username}

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200 and "available" in response.text:
            return f"The username '{username}' is available on Snapchat! (Response Code: {response.status_code})"
        elif response.status_code == 200 and "unavailable" in response.text:
            return f"The username '{username}' is already taken on Snapchat. (Response Code: {response.status_code})"
        else:
            return f"An error occurred while checking the username on Snapchat. (Response Code: {response.status_code})"

    def check_usernames_from_file(filename):
        try:
            with open(filename, 'r') as file:
                usernames = file.read().splitlines()
                for username in usernames:
                    result = check_username_snapchat(username)
                    print(result)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    if __name__ == "__main__":
        print("Select an option:")
        print("1. Input username")
        print("2. Take usernames from a text file")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            username = input("Enter the Snapchat username you want to check: ")
            result = check_username_snapchat(username)
            print(result)
        elif choice == '2':
            filename = input("Enter the name of the text file containing usernames: ")
            check_usernames_from_file(filename)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def function_3():
    import requests

    def check_username(username):
        url = f"https://www.tiktok.com/@{username}"
        response = requests.get(url)

        if response.status_code == 404:
            return f"The username '@{username}' is available!"
        elif response.status_code == 200:
            return f"The username '@{username}' is already taken."
        else:
            return f"An error occurred while checking the username."

    def check_usernames_from_file(filename):
        try:
            with open(filename, 'r') as file:
                usernames = file.read().splitlines()
                for username in usernames:
                    result = check_username(username)
                    print(result)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    if __name__ == "__main__":
        print("Select an option:")
        print("1. Input username")
        print("2. Take usernames from a text file")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            username = input("Enter the TikTok username you want to check: ")
            result = check_username(username)
            print(result)
        elif choice == '2':
            filename = input("Enter the name of the text file containing usernames: ")
            check_usernames_from_file(filename)
        else:
            print("Invalid choice. Please enter 1 or 2.")


def function_4():
    import requests
    import uuid

    def main():
        url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"

        headers = {
            "User-Agent": str(uuid.uuid4()),
        }

        print("Choose an input method:")
        print("1. Enter a username")
        print("2. Read usernames from a text file")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            username = input("Enter a username to check: ")
            check_username(url, headers, username)
        elif choice == "2":
            filename = input("Enter the name of the text file containing usernames: ")
            try:
                with open(filename, "r") as file:
                    for line in file:
                        username = line.strip()
                        check_username(url, headers, username)
            except FileNotFoundError:
                print("File not found.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

    def check_username(url, headers, username):
        data = {
            "username": username,
        }

        response = requests.post(url, json=data, headers=headers)

        print("Response Status Code:", response.status_code)

        if response.status_code == 200:
            response_data = response.json()
            if "taken" in response_data:
                if response_data["taken"]:
                    print(f" '{username}' is taken.")
                else:
                    print(f" '{username}' is available.")
            else:
                print("Unexpected response data format.")
        else:
            print("Error: Unable to check the username.")

    if __name__ == "__main__":
        main()


def function_5():
    import requests

    def check_youtube_handler(username):
        url = f"https://www.youtube.com/@{username}"
        response = requests.get(url)

        if response.status_code == 200:
            return f"The YouTube handler '{username}' is already taken."
        elif response.status_code == 404:
            return f"The YouTube handler '{username}' is available."
        else:
            return "An error occurred while checking the YouTube handler."

    def check_usernames_from_file(filename):
        try:
            with open(filename, 'r') as file:
                usernames = file.read().splitlines()
                for username in usernames:
                    result = check_youtube_handler(username)
                    print(result)
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def main():
        print("Select an option:")
        print("1. Input YouTube username")
        print("2. Take YouTube usernames from a text file")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            username = input("Enter the YouTube username you want to check: ")
            result = check_youtube_handler(username)
            print(result)
        elif choice == '2':
            filename = input("Enter the name of the text file containing YouTube usernames (e.g., 5.txt): ")
            check_usernames_from_file(filename)
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if __name__ == "__main__":
        main()


def function_6():
    import requests

    def main():
        url = "https://gql.twitch.tv/gql"

        headers = {
            "Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",
        }

        # Prompt the user to choose the input method
        print("Choose an input method:")
        print("1. Enter a username")
        print("2. Read usernames from a text file")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            username = input("Enter a username to check: ")
            check_username(url, headers, username)
        elif choice == "2":
            filename = input("Enter the name of the text file containing usernames: ")
            try:
                with open(filename, "r") as file:
                    for line in file:
                        username = line.strip()
                        check_username(url, headers, username)
            except FileNotFoundError:
                print("File not found.")
        else:
            print("Invalid choice. Please enter 1 or 2.")

    def check_username(url, headers, username):
        try:
            body = requests.post(url, json=[{
                'operationName': 'UsernameValidator_User',
                'variables': {
                    'username': username
                },
                'extensions': {
                    'persistedQuery': {
                        'version': 1,
                        'sha256Hash': 'fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660'
                    }
                }
            }], headers=headers).json()

            if not body or len(body) == 0:
                print("Error: Unable to check the username.")
                return

            if not body[0]['data']['isUsernameAvailable']:
                print(f"'{username}' is taken.")
            else:
                print(f"'{username}' is available.")
        except Exception as e:
            print("Error: Unable to check the username.")

    if __name__ == "__main__":
        main()


def function_7():
    print("Function 7 activated!")


def function_8():
    print("Function 8 activated!")


if __name__ == "__main__":
    print_ascii_art()

    while True:
        try:
            choice = int(input("Enter a number between 1 and 8 to activate a function (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= 8:
                function_name = f"function_{choice}"
                globals()[function_name]()
            else:
                print("Invalid input. Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a valid number between 1 and 8 or 0 to exit.")
