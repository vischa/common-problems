'''
Question Source: LeetCode (leetcode.com)
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
It is possible that several messages arrive roughly at the same time.
'''

class Logger:

    def __init__(self):
        """
        Initializing structure here
        """
        self.message_buffer = dict()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.message_buffer:
            if timestamp - self.message_buffer[message] >= 10:
                self.message_buffer[message]=timestamp
                return True
            else:
                return False
        else:
            self.message_buffer[message] = timestamp
            return True


#test code
object = Logger()
for incoming_stream in [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]:
    shouldPrintMessage = object.shouldPrintMessage(incoming_stream[0], incoming_stream[1])
    print(shouldPrintMessage)
