#!/usr/bin/python3
'''utf-8 VALIDATOR script;
determines if a given data set represents a valid UTF-8 encoding.
'''


def validUTF8(data):
    '''validUTF8():
    Determines if a given data set represents a valid UTF-8 encoding.

    check if the most significant bit of the byte is set to 0
    (a single-byte character)
    ELSE if the two MSB of the byte are 10 (a following byte)

    Return: True if data is a valid UTF-8 encoding, else return False
    '''

    seq_bytes = 0

    for number in data:
        bin_sequence = format(number, '#010b')[-8:]

        if seq_bytes == 0:
            for bit in bin_sequence:
                if bit == '0':
                    break
                seq_bytes += 1

            if seq_bytes == 0:
                continue

            if seq_bytes == 1 or seq_bytes > 4 == 0b1110:
                return False
        else:
            if not (bin_sequence[0] == '1' and bin_sequence[1] == '0'):
                return False

        seq_bytes -= 1

    return seq_bytes == 0

    # seq_bytes = 0
    # for num in data:
    #     if seq_bytes == 0:
    #         if num >> 7 == 0b0:
    #             continue
    #         elif num >> 5 == 0b110:
    #             seq_bytes = 1
    #         elif num >> 4 == 0b1110:
    #             seq_bytes = 2
    #         elif num >> 3 == 0b11110:
    #             seq_bytes = 3
    #         else:
    #             return False
    #     else:
    #         if num >> 6 == 0b10:
    #             seq_bytes -= 1
    #         else:
    #             return False

    # return seq_bytes == 0
