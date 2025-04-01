import create_all

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter name of the parent directory:\n1. Backend or 2. Frontend: ")

            if user_input not in ["1", "2", "backend", "frontend"]:
                raise ValueError("Invalid input! Please choose '1', as 'backend' or '2', 'frontend'.")

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