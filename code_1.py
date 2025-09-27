import json

with open("file.json", "r") as file:
    data = json.load(file)
comand = ""
while comand != "exit":
    comand = input("")
    if comand == "add":
        new_chore = input("Enter a new chore: ")
        #saves the new chore to the list
        data['chores'].append(new_chore)
        #saves the changes to the json file
        with open("file.json", "w") as file:
            json.dump(data, file, indent=4)
    if comand == "show":
        for chore in data['chores']:
            print(chore)
    if comand == "completed":
        chore_done = input("Enter the chore you completed: ")
        if chore_done in data['chores']:
            data['chores'].remove(chore_done)
            with open("file.json", "w") as file:
                json.dump(data, file, indent=4)
            print(f"Chore '{chore_done}' marked as completed and removed from the list.")
        else:
            print(f"Chore '{chore_done}' not found in the list.")
