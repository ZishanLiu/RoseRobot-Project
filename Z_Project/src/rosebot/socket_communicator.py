import rosebot.communicator
import socket

class SocketCommunicator(rosebot.communicator.Communicator):
    """Uses a socket to send and receive messages to/from the robot
    """
    def __init__(self,
                 address,
                 connect=True,
                 wait_for_acknowledgement=True,
                 send_acknowledgement=False,
                 is_debug=True):
        self.address = address
        self.read_buffer_size = 4096
        self.bytes_read_but_not_yet_returned = bytearray()

        super().__init__(connect=connect,
                         wait_for_acknowledgement=wait_for_acknowledgement,
                         send_acknowledgement=send_acknowledgement,
                         is_debug=is_debug)

    # TODO implement a __repr__ and/or __str__

    def establish_connection(self):
        try:
            print(self.address)
            self.socket_connection = socket.socket(socket.AF_INET,
                                                   socket.SOCK_STREAM)
            self.socket_connection.connect((self.address, 2000))
        except:
            raise  # TODO Error handling.

        # At this point, the wifly sends to the Arduino:
        #  *HELLO**OPEN*
        # I don't know why.  To deal with it, the Communicator
        # will send a Startup Sequence.
        # FIXME  Investigate this!

    def disconnect(self):
        """ Does whatever is needed to close the connection cleanly. """
        return self.socket_connection.shutdown(socket.SHUT_RDWR)

    def send_bytes(self, bytes_to_send):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        self.socket_connection.sendall(bytes_to_send)
        return len(bytes_to_send)

    def receive_bytes(self, number_of_bytes_to_return=1):
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
        num_bytes = number_of_bytes_to_return
        while True:
            if self.is_debug:
                print('bytes in buffer:',
                      self.bytes_read_but_not_yet_returned)
            if len(self.bytes_read_but_not_yet_returned) >= num_bytes:
                result = self.bytes_read_but_not_yet_returned[:num_bytes]
                self.bytes_read_but_not_yet_returned = self.bytes_read_but_not_yet_returned[num_bytes:]
                break

            bytes_read = self.socket_connection.recv(self.read_buffer_size)
            if self.is_debug:
                print('bytes read:', bytes_read)
            self.bytes_read_but_not_yet_returned += bytes_read

        if self.is_debug:
            print('result:', result)

        if len(result) == 1:
            return int(result[0])
        else:
            return result
