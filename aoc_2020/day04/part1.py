REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


class Passport:
    def __init__(self, fields):
        self.fields = fields

    def is_valid(self):
        return all([x in self.fields for x in REQUIRED_FIELDS])


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
