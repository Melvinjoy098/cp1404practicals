"""
Word Occurrences Counter
Estimate: 45 minutes
Actual: 60 minutes
"""

import csv


def read_wimbledon_data(filename):
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)  # Skipping the header row
        for row in csv_reader:
            year, champion_country, champion, _, _, _ = row
            champions.append((champion, champion_country))
    return champions


def get_champion_counts(champions):
    champion_counts = {}
    for champion, _ in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def get_sorted_countries(champions):
    countries = set()
    for _, country in champions:
        countries.add(country)
    sorted_countries = sorted(countries)
    return sorted_countries


def main():
    filename = 'wimbledon.csv'
    champions = read_wimbledon_data(filename)

    champion_counts = get_champion_counts(champions)
    sorted_countries = get_sorted_countries(champions)

    print("Wimbledon Champions:")
    for champion, count in sorted(champion_counts.items()):
        print(f"{champion} {count}")

    print("\nThese countries have won Wimbledon:")
    countries_str = ', '.join(sorted_countries)
    print(countries_str)


main()
