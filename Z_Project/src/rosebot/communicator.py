import abc


class Communicator(abc.ABC):
    """
    Abstract class that has:
      send_command
      receive_response
      send_message [abstract]
      receive_message [abstract]
      [maybe] receive_sensor_data [does so in a loop in a thread...]

    What else should a Communicator be able to do???

    A RoseBot proper constructs one of these to do all the actual
    communication with the RoseBot -- things we don't usually
    want students to have to bother with.

    It has:
    LowLevelCommunicator that (extends Communictor?) and can take a
    HighLevelCommand and encode it into something the Arduino
    understands and sent it to the Arduino (and get back stuff from
    the Arduino).

    The object that allows the RoseBot and its Arduino
    to talk to each other.
    Constructs and has a LowLevelCommunicator, which it uses to send
    Commands to the Arduino.

    Methods to:
      -- Connect to the Arduino.
      -- Send a Command to the Arduino.
      -- Get a Command's result from the Arduino.
      -- Sleep safely (while any concurrent processes are running).
      -- Return the type of connection.
      -- ??

    """
    def __init__(self):
        pass

    def __repr(self):
        pass

    @abc.abstractmethod
    def connect(self):
        """
        Does whatever is needed to establish a connection
        to the Arduino.
        """
        # Subclass must implement this method.

    @abc.abstractmethod
    def disconnect(self):
        """ Does whatever is needed to close the connection cleanly. """
        # Subclass must implement this method.

    @abc.abstractmethod
    def send_message(self, message):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        # Subclass must implement this method.

    @abc.abstractmethod
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
        # Subclass must implement this method.


    def send_command(self, command, data=None):
        """
        Encodes and then sends to the Arduino the given command
        with the given data. Returns the number of bytes sent.
          :type command: Command
          :type data: CommandData
          :rtype int
        """
        return self.send_message(command.to_bytes(data))

    def receive_command_data(self, command):
        """
        Receives whatever data the given Command expects back from
        the Arduino.  Returns it in whatever form that Command expects.
          :type data: CommandData
        """
        num_bytes = command.number_of_bytes_to_receive
        bytes_received = self.receive_message(num_bytes)

        return command.value_of(bytes_received)

