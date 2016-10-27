import rosebot.communicator
import socket

class SocketCommunicator(rosebot.communicator.Communicator):
    """Uses a socket to send and receive messages to/from the robot
    """
    def __init__(self, rnum=-1):
        """
        Does whatever initialization is needed.
        May call  connect  below to establish the actual connection.
        """
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rnum = rnum

    def connect(self, addr=-1):
        """
        Does whatever is needed to establish a connection
        to the Arduino.
        """
        if addr != -1:
            self.rnum = addr
        addr = "r" + str(self.rnum) + ".wlan.rose-hulman.edu"
        try:
            self.connection.connect((addr, 2000))
        except:
            raise "Could not connect to robot " + str(addr)

    def disconnect(self):
        """ Does whatever is needed to close the connection cleanly. """
        return self.connection.shutdown(socket.SHUT_RDWR)

    def send_message(self, message):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        attempts = 3
        while(attempts > 0):
            try:
                self.connection.sendall(message)
                return True
            except:
                self.connect()
        return False

    def receive_message(self, length_of_message_in_bytes=1):
        """
        Receives from the Arduino the given number of bytes.
        Returns a byte (integer between 0 and 255) if the given
        number of bytes is 1, otherwise returns a bytearray
        containing the bytes.

        Blocking behavior is determined by
          TIMEOUT_FOR_READ_IN_SECONDS
        which was set when this object was constructed.
          :rtype byte or bytearray
        """
        return self.connection.recv(length_of_message_in_bytes)
