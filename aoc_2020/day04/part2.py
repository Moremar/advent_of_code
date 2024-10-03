import re
from part1 import REQUIRED_FIELDS


class Passport:
    def __init__(self, fields):
        self.fields = fields

    def valid_required(self):
        return all([x in self.fields for x in REQUIRED_FIELDS])

    def valid_byr(self):
        m = re.match('^([0-9]{4})$', self.fields['byr'])
        return m and 1920 <= int(m.group(0)) <= 2002

    def valid_iyr(self):
        m = re.match('^([0-9]{4})$', self.fields['iyr'])
        return m and 2010 <= int(m.group(0)) <= 2020

    def valid_eyr(self):
        m = re.match('^([0-9]{4})$', self.fields['eyr'])
        return m and 2020 <= int(m.group(0)) <= 2030

    def valid_hgt(self):
        m = re.match('^([0-9]+)(cm|in)$', self.fields['hgt'])
        if not m:
            return False
        valid_cm = m.group(2) == 'cm' and 150 <= int(m.group(1)) <= 193
        valid_in = m.group(2) == 'in' and 59 <= int(m.group(1)) <= 76
        return valid_cm or valid_in

    def valid_hcl(self):
        return re.match(r'^#[0-9a-f]{6}$', self.fields['hcl'])

    def valid_ecl(self):
        return re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', self.fields['ecl'])

    def valid_pid(self):
        return re.match('^([0-9]{9})$', self.fields['pid'])

    def is_valid(self):
        return self.valid_required() \
           and self.valid_byr() \
           and self.valid_iyr() \
           and self.valid_eyr() \
           and self.valid_hgt() \
           and self.valid_hcl() \
           and self.valid_ecl() \
           and self.valid_pid()


def solve(passports):
    return len([p for p in passports if p.is_valid()])


def parse(file_name):
    passports = []
    with open(file_name, 'r') as f:
        for passport in f.read().split('\n\n'):
            fields = {}
            for field in passport.replace('\n', ' ').split(' '):
                key, val = field.split(':')
                fields[key] = val
            passports.append(Passport(fields))
        return passports


if __name__ == '__main__':
    print(solve(parse('data.txt')))
