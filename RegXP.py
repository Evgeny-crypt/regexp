from pprint import pprint
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ


list_names = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"
list_names1 = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"
list_numbers = "(\+7|8)(\s*)\(*(\d\d\d)\)*\-*\s*(\d\d\d)\-*(\d\d)\-*(\d\d)\s*\(*(доб.)*\s*(\d*)(\)*)"

for contact in contacts_list:
    new_contact = re.sub(list_numbers, r"+7(\3)\4-\5-\6 \7\8", contact[5])
    contact[5] = new_contact

    if re.match(list_names, contact[0]):
        result = re.match(list_names, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)
        contact[2] = result.group(5)

    if re.match(list_names1, contact[0]):
        result = re.match(list_names1, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)

    if re.match(list_names1, contact[1]):
        result = re.match(list_names1, contact[1])
        contact[1] = result.group(1)
        contact[2] = result.group(3)

phone_books = {}
for contact in contacts_list:
    if contact[0] not in phone_books.keys():
        phone_books[contact[0]] = contact[1:]
    else:
        for e, item in enumerate(contact[1:]):
            if phone_books[contact[0]][e - 6] == '':
                phone_books[contact[0]][e - 6] = item

new_list = []
for key, value in phone_books.items():
    local_contact = [key]
    for i in value:
        local_contact.append(i)
    new_list.append(local_contact)

pprint(new_list)

with open("phonebook_out.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_list)
