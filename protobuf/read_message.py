import voiceactressdata_pb2
import sys

# Iterate through all people in the data and prints info about them.
def ListPeople(voiceactressdata):
    for person in voiceactressdata.people:
        print("Person ID:{}".format(person.id))
        #print("Person ID:", person.id)
        print(" Name:{}".format(person.name))
        if person.HasField('most_famous_character'):
            print(" info:{}".format(person.most_famous_character))

        for contact in person.contacts:
            if contact.type == voiceactressdata_pb2.Person.PRIVATE:
                print(" private info: {} {}".format(contact.info, contact.address))
            elif contact.type == voiceactressdata_pb2.Person.COMPANY:
                print(" company info: {} {}".format(contact.info, contact.address))

# main procedure: reads the entire data from a file and prints all
if len(sys.argv) != 2:
    print("Usage: {} voice_actress_data_file".format(sys.argv[0]))
    sys.exit(-1)

voiceactressdata = voiceactressdata_pb2.VoiceActressBook()

# read the existing data
f = open(sys.argv[1], "rb")
voiceactressdata.ParseFromString(f.read())
f.close()

ListPeople(voiceactressdata)
