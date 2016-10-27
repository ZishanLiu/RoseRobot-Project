import rosebot.communicator
import rosebot.command
import sys
import serial
import time


class SerialCommunicator(rosebot.communicator.Communicator):
    """ Uses a serial connection to send and receive messages. """

    BAUDRATE = 57600  # 57600  # Serial can go at 115200, but wifly only 57600
    READ_TIMEOUT = None  # in seconds. None means never timeout.
    SECONDS_AFTER_CONNECTING = 5  # TODO Tune this.
    TIME_BETWEEN_SENDS = 0.05  # TODO Tune this.

    def __init__(self, port, connect=False, simulate=False,
                 acknowledge=True):
        # TODO Allow the port to be specified via connect, too.
        # TODO Allow search for port.
        self.port = port
        self.simulate = simulate
        self.acknowledge = acknowledge

        self.is_connected = False
        if connect:
            self.connect()

    # TODO implement a __repr__ and/or __str__

    def connect(self, simulate=False):
        if simulate or self.simulate:
            self.reader_writer = sys.stdout
        else:
            try:
                # TODO Confirm that the remaining parameters in the
                # following statement are not going to change no matter
                # what hardware we use (within reason).
                # Otherwise, make variables herein for those parameters.
                self.reader_writer = \
                serial.Serial(self.port,
                              baudrate=SerialCommunicator.BAUDRATE,
                              timeout=SerialCommunicator.READ_TIMEOUT)
                time.sleep(SerialCommunicator.SECONDS_AFTER_CONNECTING)
            except:
                # TODO Add error-handling.
                raise

        self.is_connected = True

    def disconnect(self):
        # TODO Does this need to do anything?
        pass

    def send_message(self, message):
        """
        Sends the given message to the Arduino.
        Returns the number of bytes actually sent.
          :type message: bytes or bytearray
          :rtype int
        """
        if self.simulate:
            new_message = ''
            for byte in message:
                new_message = new_message + hex(byte) + ' '
            message = new_message + '\n'

#         print(message)  # TODO Make happen only in DEBUG mode

        # TODO Calulate the following.
        time_since_previous_send = 0
        first_sleep = max(0, SerialCommunicator.TIME_BETWEEN_SENDS
                          - time_since_previous_send)

        # TODO The following does writes one byte at a time,
        # with a short pause in between each.  Would it be more
        # or less reliable to do a single multi-byte write?

        total_bytes_sent = 0
        # Send the first byte of the message:
        time.sleep(first_sleep)
        total_bytes_sent += self.write_byte(message[0])

        # Send the rest of the message:
        for byte in message[1:]:
            time.sleep(SerialCommunicator.TIME_BETWEEN_SENDS)
            total_bytes_sent += self.write_byte(byte)

        # TODO Make the acknowledgement less hard-coded
        #   and better at error detection and handling.
        # TODO Allow for different encodings?
        # FIXME The ValueError below does not seem to fire
        #   when running from the unittest.  Why?
        if self.acknowledge:
            ack = self.receive_message(4)
#             for k in range(4):
#                 print(str(ack[k]), end=' ')
#             print()
            # TODO Check the acknowledge
#             if ...
#                 msg = 'Wrong acknowledgement.\n'
#                 msg += 'Expected: ackX  where X is a digit.\n'
# #                 msg += 'Got: ' + ack
#                 raise ValueError(msg)

        return total_bytes_sent

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
        if self.simulate:
            print('Receiving messages is unimplemented in the simulator')
            return
        # TODO Should this be a loop with a sleep?  I think not, but ...
        # TODO Deal with timeouts other than None.
        bytes_object = self.reader_writer.read(length_of_message_in_bytes)
        if len(bytes_object) == 1:
#             print('Returning a single byte')
            return int(bytes_object[0])
        else:
            return bytes_object

    def write_byte(self, byte_or_character):
        if self.simulate:
            self.reader_writer.write(byte_or_character)
            return 1
        else:
            return self.reader_writer.write([byte_or_character])


########################################################################
# The rest of this module is for testing.
########################################################################

def main():
    port = '/dev/cu.usbserial-A9048GND'
    sc = SerialCommunicator(port, connect=True, simulate=False)
    test_send_command(sc)
    test_send_message(sc)
    test_receive_message(sc)
    test_receive_command(sc)
    test_analog_receive(sc)


def test_send_message(sc):
    """ Blink. """
    for _ in range(2):
        time.sleep(1)
        print('off')
        sc.send_message(bytes([0x03, 0x0d, 0x00]))
        time.sleep(1)
        print('on')
        sc.send_message(bytes([0x03, 0x0d, 0x01]))


def test_send_command(sc):
    """ Blink. """
    command = rosebot.command.DigitalWriteCommand(13)
    for _ in range(2):
        time.sleep(1)
        print('off')
        sc.send_command(command, 0)
        time.sleep(1)
        print('on')
        sc.send_command(command, 1)


def test_receive_message(sc):
    """ Get status of the button, pause and repeat. """
    print('Release the button')
    sc.send_message(bytes([0x02, 0x0c]))
    print('Should be 1 (not pressed): ', sc.receive_message())
    print('Press the button')
    time.sleep(2)
    sc.send_message(bytes([0x02, 0x0c]))
    print('Should be 0 (pressed): ', sc.receive_message())


def test_receive_command(sc):
    """ Get status of the button, pause and repeat. """
    command = rosebot.command.DigitalReadCommand(12)
    print('Release the button')
    sc.send_command(command)
    print('Should be 1 (not pressed): ', sc.receive_command_data(command))
    print('Press the button')
    time.sleep(2)
    sc.send_command(command)
    print('Should be 0 (pressed): ', sc.receive_command_data(command))

def test_analog_receive(sc):
    command = rosebot.command.AnalogReadCommand(0)
    for _ in range(10):
        sc.send_command(command)
        print('Value is: ', sc.receive_command_data(command))
        time.sleep(1)


if __name__ == '__main__':
    main()
