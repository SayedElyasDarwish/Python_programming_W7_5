from dataclasses import dataclass

WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


@dataclass
class TIMESTAMP:
    weekday: str
    hour: str
    consumption: float
    price: float


@dataclass
class DAY_USAGE:
    weekday: str
    usage: float = 0.0
    cost: float = 0.0


def readTimestamps(PFilename: str, PTimestamps: list[TIMESTAMP]) -> None:
    print(f'Reading file "{PFilename}".')
    for line in open(PFilename, encoding="utf-8").read().splitlines()[1:]:
        if line:
            day, hour, consumption, price = line.split(";")
            PTimestamps.append(TIMESTAMP(day, hour, float(consumption), float(price)))


def analyseTimestamps(PTimestamps: list[TIMESTAMP], PDayUsages: list[DAY_USAGE], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    PDayUsages.extend(DAY_USAGE(name) for name in WEEKDAYS)
    for t in PTimestamps:
        for day in PDayUsages:
            if t.weekday.replace("Saturnday", "Saturday") == day.weekday:
                day.usage += t.consumption
                day.cost += t.consumption * t.price
    PResults.append("### Electricity consumption summary ###")
    PResults.extend(f" - {d.weekday} usage {d.usage:.2f} kWh, cost {d.cost:.2f} €" for d in PDayUsages)
    PResults.append("### Electricity consumption summary ###")


def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    for result in PResults:
        print(result)


def main() -> None:
    print("Program starting.")
    timestamps, dayUsages, results = [], [], []
    readTimestamps(input("Insert filename: "), timestamps)
    analyseTimestamps(timestamps, dayUsages, results)
    displayResults(results)
    print("Program ending.")


if __name__ == "__main__":
    main()