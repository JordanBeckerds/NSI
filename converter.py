class Converter:
    @staticmethod
    def sort_dict_keys_alphabetically(d):
        sorted_keys = []
        for key in d:
            sorted_keys.append(key)
        sorted_keys.sort()
        sorted_dict = {}
        for key in sorted_keys:
            sorted_dict[key] = d[key]
        return sorted_dict

    @staticmethod
    def sort_list_alphabetically(lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    @staticmethod
    def dec_to_bin(decimal):
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary

    @staticmethod
    def bin_to_hex(binary):
        decimal = 0
        power = 0
        for digit in binary[::-1]:
            decimal += int(digit) * (2 ** power)
            power += 1
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(remainder + 55) + hexadecimal
            decimal //= 16
        return hexadecimal

    @staticmethod
    def hex_to_dec(hexadecimal):
        decimal = 0
        power = 0
        for digit in hexadecimal[::-1]:
            if '0' <= digit <= '9':
                decimal += int(digit) * (16 ** power)
            else:
                decimal += (ord(digit.upper()) - 55) * (16 ** power)
            power += 1
        return decimal

    @staticmethod
    def dec_to_hex(decimal):
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            if remainder < 10:
                hexadecimal = str(remainder) + hexadecimal
            else:
                hexadecimal = chr(remainder + 55) + hexadecimal
            decimal //= 16
        return hexadecimal

    @staticmethod
    def hex_to_bin(hexadecimal):
        decimal = Converter.hex_to_dec(hexadecimal)
        return Converter.dec_to_bin(decimal)

    @staticmethod
    def bin_to_dec(binary):
        decimal = 0
        power = 0
        for digit in binary[::-1]:
            decimal += int(digit) * (2 ** power)
            power += 1
        return decimal
