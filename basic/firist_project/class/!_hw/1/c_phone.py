# def parse_phone(phone: str) -> str:
#     phone = phone.replace('+', '').replace('(', '').replace(')', '').replace('-', '')
#     if len(phone) == 11:
#         phone = phone[1:]
#     if len(phone) == 7:
#         phone = '495' + phone
#     return phone
#
#
# def is_exist(phones: list[str]):
#     example = parse_phone(phones[0])
#     for i in range(1, len(phones)):
#         print('YES') if example == parse_phone(phones[i]) else print('NO')
#
#
# phones = []
# phone = input()
# while phone:
#     phones.append(parse_phone(phone))
#     phone = input()
# is_exist(phones)


def parse_phone(phone: str) -> str:
    phone = phone.replace('+', '').replace('(', '').replace(')', '').replace('-', '')
    if len(phone) == 11:
        phone = phone[1:]
    if len(phone) == 7:
        phone = '495' + phone
    return phone


phone = input()
example = parse_phone(phone)

for i in range(3):
    phone = input()
    print('YES') if example == parse_phone(phone) else print('NO')