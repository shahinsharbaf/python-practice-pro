import re


class Parser:
    def __init__(self) -> None:
        pass

    def email_parser(self, text):
        my_reg = re.compile(r'\w+@\w+.\w+')
        result = my_reg.findall(text)
        return result

    def phone_number(self, text):
        my_reg = re.compile(r'\d{3}-\d{3}-\d{4}')
        result = my_reg.findall(text)
        return result


class Ukparser(Parser):
    def __init__(self) -> None:
        super().__init__()

    def phone_number(self, text):
        my_reg = re.compile(r'\+\d{1}-\d{3}-\d{3}-\d{4}')
        result = my_reg.findall(text)
        return result


my_parser = Parser()
my_text = "sfvsd ali@vdf.vsdf  ecfsdfcsd sh@gmail.com r15"
print(my_parser.email_parser(my_text))

my_number = "srdfvfd 444-555-7777 dfvfd +4-555-777-4578"
print(my_parser.phone_number(my_number))

my_ukparser = Ukparser()
print(my_ukparser.phone_number(my_number))
