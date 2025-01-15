def write_to_file(filename, text):
    with open(filename, 'w') as text_file:
        text_file.write(text + '\n')


write_to_file('test.txt', 'test text')


def append_to_file(filename, text):
    with open(filename, 'a') as text_file:
        text_file.write(text)


append_to_file('test.txt', 'test text2')


def read_from_file(filename):
    with open(filename) as text_file:
        text = text_file.read()
        print(text)


read_from_file('test.txt')