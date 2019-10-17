import voiceactressdata_pb2
import sys

# This function fills in a Person message based on user input.
def PromptForInfo(person):
    person.id = int(raw_input("Enter person ID number:"))
    person.name = raw_input("Enter name:")

    most_famous_character = raw_input("Enter most famous character (blank for none):")
    if most_famous_character != "":
        person.most_famous_character = most_famous_character

    while True:
        contact_input = raw_input("Enter a contact related information:")
        if contact_input == "":
            break

        contact = person.contacts.add()
        contact.info = contact_input

        address_input = raw_input("Enter a contact address (blank for none):")
        if address_input == "":
            pass
        else:
            contact.address = address_input
    
        type_input = raw_input("Does this info relate to private or company ?:")
        if type_input == "private":
            contact.type = voiceactressdata_pb2.Person.PRIVATE
        elif type_input == "company":
            contact.type = voiceactressdata_pb2.Person.COMPANY
        else:
            print("Unknown working type; leaving ad default value.")


# main prcedure: reads the entire data from a file.
#   adds one person based on user input, then writes it back out to the same file.

if len(sys.argv) != 2:
    print("Usage:",sys.argv[0],"voice_actress_data_file")
    sys.exit(-1)

voiceactressdata = voiceactressdata_pb2.VoiceActressBook()

# read the existing address book
try:
    f = open(sys.argv[1], "rb")
    voiceactressdata.ParseFromString(f.read())
    f.close()
except IOError:
    print(sys.argv[1] + ": Could not open file. Creating new one.")

# add an adress
PromptForInfo(voiceactressdata.people.add())

# write the new voiceactressdata to disk.
f = open(sys.argv[1], "wb")
f.write(voiceactressdata.SerializeToString())
f.close()
