# Create "Names" Reference File
with open("Names.txt", "w") as names:
    # Create List of "Names"
    name_list = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
    # Loop through Names
    for i in name_list:
        # Write contents of iteration, + New line.
        names.write(f"{i} \n")

    # Create "Message" as Reference File
with open("Message.txt", "w") as message:
    # Write "xxx" as Text
    message.write(f"Welcome to the party! We hope you can make it, BYOB!")
