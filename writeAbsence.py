import csv


def giveAbsenceFile(names):
    with open('absence.csv', mode='w') as absence:
        writer = csv.writer(absence, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for name in set(names):
            writer.writerow([name, 'P'])