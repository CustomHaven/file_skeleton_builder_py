import delete_all
import create_all

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter name of the parent directory:\n1. Backend, 2. Frontend, or 0. End: ")

            if user_input.lower() in ["0", "end"]:
                delete_all.delete_directory_and_contents("__pycache__")
                break
            if user_input.lower() not in ["1", "2", "backend", "frontend"]:
                raise ValueError("Invalid input! Please choose '1', as 'backend' or '2', as 'frontend'. Or you can enter '0' or 'end' to exit.")

            if user_input == "1" or user_input == "2":
                create_all.src = ["backend", "frontend"][int(user_input) -1]
            else:
                create_all.src = user_input
            create_all.start()
            break
        except ValueError as e:
                print(e)
        except Exception as e:
            print(f"Error: {e}. Please try again.") 