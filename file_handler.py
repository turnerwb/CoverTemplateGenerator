def read_in(style):
    file = open(style, 'r')
    roughsplit = file.read().splitlines()
    file.close()
    roughsplit = [i.split(':')[1] for i in roughsplit]
    rough_field_block = roughsplit[0]
    return [formatter(rough_field_block),
            interpreter(roughsplit[1]),
            eval(roughsplit[2]),
            interpreter(roughsplit[3]),
            interpreter(roughsplit[4]),
            interpreter(roughsplit[5]),
            roughsplit[6]]


def formatter(unformatted):
    return unformatted.split(',')


def interpreter(uninterpreted):
    if uninterpreted == 'True':
        return True
    else:
        return False