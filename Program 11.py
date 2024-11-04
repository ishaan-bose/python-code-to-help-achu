import pickle

def File_Create():
    with open("Player.dat", "ab") as file:
        player_id = input("Enter Player ID: ")
        player_name = input("Enter Player Name: ")
        player_game = input("Enter Player Game: ")
        record = {"Player_id": player_id, "Player_name": player_name, "Player_game": player_game}
        pickle.dump(record, file)

def File_Read():
    with open("Player.dat", "rb") as file:
        print("\nRecords in Player.dat:")
        while True:
            try:
                record = pickle.load(file)
                print(f"ID: {record['Player_id']}, Name: {record['Player_name']}, Game: {record['Player_game']}")
            except EOFError:
                break

def Search_Data():
    player_id = input("Enter Player ID to search: ")
    found = False
    with open("Player.dat", "rb") as file:
        while True:
            try:
                record = pickle.load(file)
                if record["Player_id"] == player_id:
                    print(f"Player found - ID: {record['Player_id']}, Name: {record['Player_name']}, Game: {record['Player_game']}")
                    found = True
                    break
            except EOFError:
                    break
        if not found:
            print("Player not found.")


print("Enter \'create\' to create new record")
print("Enter \'read\' to read record")
print("Enter \'search\' to search record")
print("Enter \'quit\' to quit")

while True:
    a = input("Enter choice: ")
    if a == "create":
        File_Create()
    elif a == "read":
        File_Read()
    elif a == "search":
        Search_Data()
    elif a == "quit":
        print("quitting..")
        break
    else:
        print("Invalid choice, please try again.")