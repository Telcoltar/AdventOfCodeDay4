from typing import Optional
import re


class Passport:

    def __init__(self):
        self.byr: Optional[str] = None
        self.iyr: Optional[str] = None
        self.eyr: Optional[str] = None
        self.hgt: Optional[str] = None
        self.hcl: Optional[str] = None
        self.ecl: Optional[str] = None
        self.pid: Optional[str] = None
        self.cid: Optional[str] = None

    def valid(self) -> bool:
        return all([self.byr is not None,
                    self.iyr is not None,
                    self.eyr is not None,
                    self.hgt is not None,
                    self.hcl is not None,
                    self.ecl is not None,
                    self.pid is not None])

    def valid_byr(self) -> bool:
        if len(self.byr) != 4:
            return False
        if not (1920 <= int(self.byr) <= 2002):
            return False
        return True

    def valid_iyr(self) -> bool:
        if len(self.iyr) != 4:
            return False
        if not (2010 <= int(self.iyr) <= 2020):
            return False
        return True

    def valid_eyr(self) -> bool:
        if len(self.eyr) != 4:
            return False
        if not (2020 <= int(self.eyr) <= 2030):
            return False
        return True

    def valid_hgt(self) -> bool:
        matches_unit: list[str] = re.findall("[a-z]+", self.hgt)
        if len(matches_unit) != 1:
            return False
        unit: str = matches_unit[0]
        if unit != "in" and unit != "cm":
            return False
        matches_height_number: list[str] = re.findall("[0-9]+", self.hgt)
        if len(matches_height_number) != 1:
            return False
        height_number = int(matches_height_number[0])
        if unit == "cm":
            if not (150 <= height_number <= 193):
                return False
        if unit == "in":
            if not (59 <= height_number <= 76):
                return False
        return True

    def valid_hcl(self) -> bool:
        matches_hash: list[str] = re.findall("#", self.hcl)
        if len(matches_hash) != 1:
            return False
        matches_code: list[str] = re.findall("[0-9a-f]+", self.hcl)
        if len(matches_code) != 1:
            return False
        if len(matches_code[0]) != 6:
            return False
        return True

    def valid_ecl(self) -> bool:
        valid_eye_colors: list[str] = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.ecl in valid_eye_colors

    def valid_pid(self) -> bool:
        return len(self.pid) == 9

    def valid_part_2(self) -> bool:
        return self.valid() and all([self.valid_byr(),
                                     self.valid_iyr(),
                                     self.valid_eyr(),
                                     self.valid_hgt(),
                                     self.valid_hcl(),
                                     self.valid_ecl(),
                                     self.valid_pid()])


def get_input_data(input_file_name: str) -> list[Passport]:
    f = open(input_file_name, "r")
    passports: list[Passport] = []
    current_passport = Passport()
    for line in f:
        if line.strip() == "":
            passports.append(current_passport)
            current_passport = Passport()
            continue
        fields = line.strip().split(" ")
        for field_string in fields:
            field, value = field_string.split(":")
            setattr(current_passport, field, value)
    passports.append(current_passport)
    return passports
