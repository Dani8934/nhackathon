from pathlib import Path
from datetime import datetime

def parking_fee(entry, exit):
    entry = datetime.strptime(entry, "%Y-%m-%d %H:%M:%S")
    exit = datetime.strptime(exit, "%Y-%m-%d %H:%M:%S")
    
    if entry > exit:
        return "Exit earlier than entry, blud 😅✌️✌️"

    time = (exit - entry).total_seconds() / 60

    if time <= 30:
        return 0

    days = time // (60 * 24)
    if days >= 1:
        payment = time % (60 * 24) - 30
    else:
        payment = time - 30

    finalcost = 0
    if payment <= 0:
        return int(days * 10000)
    else:
        while payment > (3 * 60):
            finalcost += 500
            payment -= 60        
        while payment > 0:
            finalcost += 300
            payment -= 60
    
    if finalcost > 10000:
        finalcost = 10000

    return int(finalcost + days * 10000)

    



def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines()[2:]:
        line = line.split("\t\t")
        print(str(parking_fee(line[1], line[2])) + " forint", end="\n")


if __name__ == "__main__":
    main()
