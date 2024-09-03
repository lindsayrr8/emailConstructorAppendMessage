

# This program creates:
#
# --- a constructor that takes sender & recipient for an email;
# --- addLine() appends a line of text to message body;
# --- toString() that makes the message into one long string;
# --- createMessage() makes the message and prints it.



# Creates class of functions to design email message.
class Message :

    # Creates constructor for email message.
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
        self.messageBody = []

    # Creates function to append objects in Message class.
    def addLine(self, line):
        self.messageBody.append(line)

    # Adds strings to message body template.
    def toString(self):
        messageStr = f"From: {self.sender}\nTo: {self.recipient}\n"
        messageStr += "\n".join(self.messageBody)
        return messageStr




# Combines specific functions from Message class to create final email message.
def createMessage():
    
    # Creates a message object.
    myMessage = Message(sender="Harry Morgan", recipient="Rudolf Reindeer")

    # Appends to the message.
    myMessage.addLine("Dear Rudolf, ")
    myMessage.addLine("Wishing you a Merry Christmas! ")
    myMessage.addLine("Best regards, ")
    myMessage.addLine("- Harry ")

    # Prints message to user.
    print(myMessage.toString())



createMessage()
