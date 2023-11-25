def parse_file()->list:
    # Use a breakpoint in the code line below to debug your script.
    content = open('чеки.txt', 'r', encoding='utf-8')
    return content.readlines()

def parse_bills(bills: list[str], out):
    service_types = []
    cash = {'январь': [],
            'февраль': [],
            'март': [],
            'апрель': [],
            'май': [],
            'июнь': [],
            'июль': [],
            'август': [],
            'сентябрь': [],
            'октябрь': [],
            'ноябрь': [],
            'декабрь': []
            }
    # Разбиение чеков по месяцам
    for bill in bills:
        service, month = bill.split("_")
        month = month.split(".")[0]
        if month in cash:
            cash[month].append(bill.strip('\n'))
        if service not in service_types:
            service_types.append(service)
    for key in cash:
        # Сортировка типов чеков по алфавиту(как в примере решения)
        cash[key].sort(key=lambda x: x.lower())
        unpaid_service = []
        # Добавление чека в итоговый файл
        for item in cash[key]:
            out.write('/{0}/{1}\n'.format(key, item))
            unpaid_service = service_types
            # Учёт неоплаченных типов платежей по месяцам
            for ser in unpaid_service:
                if item.find(ser) != -1:
                    unpaid_service.remove(ser)
        cash[key].clear()
        cash[key] = unpaid_service.copy()
    out.write('не оплачены:\n')
    # Добавление неоплаченных типов платежей по месяцам
    for key in cash:
        if len(cash[key]) != 0:
            out.write(key + ':\n')
            for item in cash[key]:
                out.write(item + '\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    out = open('результат.txt', 'w', encoding='utf-8')
    bills = parse_file()
    parse_bills(bills, out)
    out.close()

