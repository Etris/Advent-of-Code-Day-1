from pathlib import Path


test_files_part_1 = ('input_test_1', 'input_test_2', 'input_test_3', 'input_test_4', 'input_main')
test_files_part_2 = ('input_test_5', 'input_test_6', 'input_test_7', 'input_test_8', 'input_main')
expected_out_part_1 = (3, 3, 0, -6)
expected_out_part_2 = (0, 10, 5, 14)


class CompareException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def parse(tmp):
    return int(tmp)


def compare_output(expected, output):
    if expected == output:
        return True
    else:
        return False


def part_1():
    try:
        iterator_file = 0
        for test_file in test_files_part_1:
            with open(test_file, "r") as file:
                output = 0
                for line in file:
                    output += parse(line)
                if iterator_file < len(expected_out_part_1 ):
                    if not compare_output(expected_out_part_1 [iterator_file], output):
                        raise CompareException('Wrong score at {}! {} != {}'
                                               .format(test_file, output, expected_out_part_1[iterator_file]))
                    else:
                        print('{} positive!'.format(test_file))
                else:
                    print('Score for {}: {}'.format(test_file, output))
            iterator_file += 1
    except CompareException as err:
        print(err.value)


def part_2():
    try:
        iterator_file = 0
        for test_file in test_files_part_2:
            print("File: {}".format(test_file))
            with open(test_file, "r") as file:
                output = 0
                frequencies = list()
                frequencies.append(0)
                is_found = False
                data = file.readlines()
                iteration_id = 1
                while not is_found:
                    for line in data:
                        output += parse(line)
                        #print(*frequencies, sep=", ")
                        if output in frequencies:
                            print('Frequency found for {} : {}'.format(test_file, output))
                            frequencies.append(output)
                            is_found = True
                            break
                        else:
                            #print('Appending {} to {}'.format(parse(line), output))
                            frequencies.append(output)
                    print("Reiteration #{}, length of frequency list: {}".format(iteration_id, len(frequencies)))
                    iteration_id += 1
                if iterator_file < len(expected_out_part_1):
                    if not compare_output(expected_out_part_2[iterator_file], frequencies[len(frequencies)-1]):
                        raise CompareException('Wrong score at {}! {} != {}'
                                               .format(test_file, output, expected_out_part_2[iterator_file]))
                    else:
                        print('{} positive!'.format(test_file))
                else:
                    print('Score for {}: {}'.format(test_file, output))
            iterator_file += 1
    except CompareException as err:
        print(err.value)


part_2()