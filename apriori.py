"""
Author: Dhananjay Shettigar (Roll No. 8702)
Program written for TEIT DMBI practical on frequent itemset association rule generations
"""

from apriori_python import apriori

# Terminal highlight colors
class fontcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# Replace above class with below if color terminal not supported

# class fontcolors:
#     HEADER = ''
#     OKBLUE = ''
#     OKCYAN = ''
#     OKGREEN = ''
#     WARNING = ''
#     FAIL = ''
#     ENDC = ''
#     BOLD = ''
#     UNDERLINE = ''

# Check whether subarray exists in super array


def checkExists(sub, sup):
    exists = True
    for item in sub:
        if not item in sup:
            exists = False
            break
    return exists


# Return unique items from current list of itemsets of certain size


def uniqueItemsets(itemset):
    unique_items = []

    for arr in itemset:
        for item in arr:
            if not item in unique_items:
                unique_items.append(item)

    return unique_items


# Print confidence rules with appropriate highlighting


def printRule(left, right, conf):
    print(
        f"{fontcolors.FAIL}|{fontcolors.ENDC} {left} -> {right} = {conf}",
        end=f" {fontcolors.FAIL}|{fontcolors.ENDC}",
    )


# Generate association rules using minimum confidence


def ruleGen(itemset):
    combo = [itemset, []]
    print(f"{fontcolors.OKBLUE}Confidence rules:{fontcolors.ENDC}", end=" ")
    ruleExists = False
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            temp = [itemset[i], itemset[j]]
            combo[1].append(temp)
            confidence = mainset[str(temp)] / unique_items[itemset[i]]
            if confidence >= min_conf:
                ruleExists = True
                printRule(itemset[i], itemset[j], confidence)
            confidence = mainset[str(temp)] / unique_items[itemset[j]]
            if confidence >= min_conf:
                ruleExists = True
                printRule(itemset[j], itemset[i], confidence)

    if not ruleExists:
        print(f"{fontcolors.FAIL}None{fontcolors.ENDC}\n")
        return

    for i in range(2, len(itemset) - 1):
        combo.append([])
        for item in combo[0]:
            for iset in combo[i - 1]:
                if not item in iset:
                    temp = iset.copy()
                    temp.append(item)
                    temp.sort()
                    combo[i].append(temp)

    for i in range(len(combo)):
        if i != 0 and 2 * i + 2 <= len(itemset):
            for j in range(len(combo[i])):
                for k in range(j + 1, len(combo[i])):
                    exists = False
                    for item in combo[i][j]:
                        if item in combo[i][k]:
                            exists = True
                            break
                    if not exists:
                        temp = combo[i][j].copy()
                        temp.extend(combo[i][k])
                        temp.sort()

                        confidence = mainset[str(temp)] / mainset[str(combo[i][j])]
                        if confidence >= min_conf:
                            printRule(combo[i][j], combo[i][k], confidence)

                        confidence = mainset[str(temp)] / mainset[str(combo[i][k])]
                        if confidence >= min_conf:
                            printRule(combo[i][k], combo[i][j], confidence)

        for j in range(i + 1, len(combo)):
            if i + j + 2 <= len(itemset):
                if i == 0:
                    for iset in combo[j]:
                        for item in combo[i]:
                            if item in iset:
                                continue

                            temp = iset.copy()
                            temp.append(item)
                            temp.sort()
                            confidence = mainset[str(temp)] / unique_items[item]
                            if confidence >= min_conf:
                                printRule(item, iset, confidence)

                            iset.sort()
                            confidence = mainset[str(temp)] / mainset[str(iset)]
                            if confidence >= min_conf:
                                printRule(iset, item, confidence)

                else:
                    for iset in combo[j]:
                        for iset1 in combo[i]:
                            exists = False
                            for item in iset1:
                                if item in iset:
                                    exists = True
                                    break
                            if not exists:
                                temp = iset.copy()
                                temp.extend(iset1)
                                temp.sort()
                                confidence = mainset[str(temp)] / mainset[str(iset1)]
                                if confidence >= min_conf:
                                    printRule(iset1, iset, confidence)

                                iset.sort()
                                confidence = mainset[str(temp)] / mainset[str(iset)]
                                if confidence >= min_conf:
                                    printRule(iset, iset1, confidence)
    print("\n")


# Print the itemset array along with all satisfying association rules for the itemset


def dataPrint(itemsets):
    for itemset in itemsets:
        print(
            f"{fontcolors.OKGREEN}{itemset}:{fontcolors.ENDC} {mainset[str(itemset)]}"
        )
        ruleGen(itemset)


# Import external csv data
"""
import csv
dataset = []
with open('transactions.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        dataset.append(row)
"""

dataset = [
    ["Milk", "Bread", "Biscuit"],
    ["Bread", "Milk", "Biscuit", "Cornflakes"],
    ["Bread", "Tea", "Bournvita"],
    ["Jam", "Maggi", "Bread", "Milk"],
    ["Maggi", "Tea", "Biscuit"],
    ["Bread", "Tea", "Bournvita"],
    ["Maggi", "Tea", "Cornflakes"],
    ["Maggi", "Bread", "Tea", "Biscuit"],
    ["Jam", "Maggi", "Bread", "Tea"],
    ["Bread", "Milk"],
    ["Coffee", "Cock", "Biscuit", "Cornflakes"],
    ["Coffee", "Cock", "Biscuit", "Cornflakes"],
    ["Coffee", "Sugar", "Bournvita"],
    ["Bread", "Coffee", "Cock"],
    ["Bread", "Sugar", "Biscuit"],
    ["Coffee", "Sugar", "Cornflakes"],
    ["Bread", "Sugar", "Bournvita"],
    ["Bread", "Coffee", "Sugar"],
    ["Bread", "Coffee", "Sugar"],
    ["Tea", "Milk", "Coffee", "Cornflakes"],
]

unique_items = {}

for arr in dataset:
    for item in arr:
        if not item in unique_items.keys():
            unique_items[item] = 1
        else:
            unique_items[item] = unique_items[item] + 1

min_sup = 999
unique_items_list = []
for item in unique_items:
    unique_items_list.append(item)
    if unique_items[item] < min_sup:
        min_sup = unique_items[item]

min_sup_ratio = min_sup / len(dataset)

print("Minimum Support Count: ", min_sup)
print("Minimum Support: ", min_sup_ratio, "\n")

min_conf = float(input("Enter minimum confidence: "))
print("\n")


itemset_size = 1
itemsets = {1: unique_items_list}
mainset = {}
while True:
    itemset_size += 1
    itemsets[itemset_size] = []
    base_itemset = []

    if itemset_size == 2:
        current_unique = unique_items_list
    else:
        current_unique = uniqueItemsets(itemsets[itemset_size - 1])

    for item in itemsets[itemset_size - 1]:
        if type(item) == str:
            base_itemset = [item]
        else:
            base_itemset = item

        last_item = base_itemset[len(base_itemset) - 1]
        last_item_index = current_unique.index(last_item)

        for i in range(last_item_index, len(current_unique)):
            if current_unique[i] in base_itemset:
                continue

            current_itemset_count = 0
            current_itemset = base_itemset.copy()
            current_itemset.append(current_unique[i])

            for curr_set in dataset:
                exists = True

                for item in current_itemset:
                    if not item in curr_set:
                        exists = False
                        break

                if exists:
                    current_itemset_count += 1

            current_itemset.sort()

            if str(current_itemset) in mainset.keys():
                continue

            if current_itemset_count >= min_sup:
                mainset[str(current_itemset)] = current_itemset_count
                itemsets[itemset_size].append(current_itemset)

    if len(itemsets[itemset_size]) == 0:
        break

    print(
        f"{fontcolors.HEADER}Current size of itemset:{fontcolors.ENDC} ", itemset_size
    )
    dataPrint(itemsets[itemset_size])
