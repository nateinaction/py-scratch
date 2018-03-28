import re


class funnyDates:
    dateDict = {}
    earliest = {
        'year': None,
        'month': None,
        'day': None,
    }

    def add(self, dates):
        for myDate in dates:
            year, month, day = self.parse(myDate)

            self.set_earliest(year, month, day)

            if not self.dateDict.get(year):
                self.dateDict[year] = {month: [day]}
            elif not self.dateDict[year].get(month):
                self.dateDict[year][month] = [day]
            else:
                self.dateDict[year][month].append(day)

        return self.dateDict

    def parse(self, date):
        pattern = '([0-9]+)/([0-9]+)/([0-9]+)'
        match = re.match(pattern, date)
        return int(match.group(1)), int(match.group(2)), int(match.group(3))

    def set_earliest(self, year, month, day):
        if not self.earliest['year'] or self.earliest['year'] > year:
            self.earliest['year'] = year
        elif not self.earliest['month'] or self.earliest['month'] > month:
            self.earliest['month'] = month
        elif not self.earliest['day'] or self.earliest['day'] > day:
            self.earliest['day'] = day

    def poke_earliest(self, thisDict):
        year = min(self.dateDict.keys())
        month = min(self.dateDict[year].keys())
        day = min(self.dateDict[year][month])
        return year, month, day


if __name__ == '__main__':
    poke = funnyDates()
    print(poke.parse("1989/05/02"))
    print(poke.add(["1989/05/02", "2010/02/40", "19/22222/5", "19/22222/2", "19/222252/2"]))
    print(poke.earliest)
