# Open Names.txt
with open("Names.txt", "r") as name_file:
    # Open Message.txt
    with open("Message.txt", "r") as message_file:
        # Variable ~ Body of text = read contents of message_file variable.
        body = message_file.read()
        # Loop through name_file for names.
        for name in name_file:
            # Variable ~ Mail = "hello " + name var + body var
            mail = "Hello " + name + body
            # Open /Write new file for each name
            with open(name.strip()+".txt", "w") as message_file:
                message_file.write(mail)
