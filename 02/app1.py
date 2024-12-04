reports = []
result = 0

with open("02/input","r") as file:
    for row in file:
        row = list(map(int, row.split()))
        reports.append(row)

for report in reports:
    log = False
    valid = True
    report_sort = sorted(report)
    report_revsort = sorted(report,reverse=True)

    if(report == report_sort or report == report_revsort):
        if(report[0] < report[1]):
            for x in range(len(report)):
                if x < len(report)-1:
                    if report[x+1] - report[x] >3 or report[x+1] - report[x] < 1 or report[x] == report[x+1]:
                        valid = False
                        if(log == False):
                            print(report, "INVALID BECAUSE OF GAP ASC")
                            log = True

        if (report[0] > report[1]):
            for x in range(len(report)):
                if x < len(report)-1:
                    if report[x] - report[x+1] >3 or report[x] - report[x+1] < 1 or report[x] == report[x+1]:
                        valid = False
                        if (log == False):
                            print(report, "INVALID BECAUSE OF GAP DESC")
                            log = True

        if (report[0] == report[1]):
            valid = False
            print(report,"INVALID BECAUSE OF SAME DIGITS")

    else:
        valid = False
        if (log == False):
            print(report, "INVALID BECAUSE ARRAY")
            log = True

    if valid == True:
        result += 1
        print(report,"VALID")
print(result)
