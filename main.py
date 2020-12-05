from commenUtils import get_input_data


def simple_solution_part_1() -> int:
    passports = get_input_data("inputData.txt")
    valid: int = 0
    for passport in passports:
        valid += int(passport.valid())
    return valid


def simple_solution_part_2_tests(file_name: str) -> int:
    passports = get_input_data(file_name)
    valid: int = 0
    for passport in passports:
        valid += int(passport.valid_part_2())
    return valid


if __name__ == '__main__':
    print(simple_solution_part_1())
    print(simple_solution_part_2_tests("validExamples.txt"))
    print(simple_solution_part_2_tests("invalidExamples.txt"))
    print(simple_solution_part_2_tests("inputData.txt"))
