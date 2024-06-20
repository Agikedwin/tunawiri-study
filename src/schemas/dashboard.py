from collections import Counter


def serializeDict(item) -> list:
    phq9 = serializedCount(item['phq9'])
    gad7 = serializedCount(item['gad7'])
    harvard = serializedCount(item['harvard'])
    suicidal = serializedCount(item['suicidal'])
    trauma = serializedCount(item['trauma'])

    return_value = [
        {'phq9': phq9},
        {'gad7': gad7},
        {'harvard': harvard},
        {'suicidal': suicidal},
        {'trauma': trauma}
    ]
    print(return_value)

    return return_value


def serializeList(entity) -> list:
    return [serializeDict(item) for item in entity]


def serializedCount(entity) -> list:
    data = []
    values = {'Low': 0, 'Moderate': 0, 'Mild': 0, 'Severe': 0}
    signs = Counter(k['severity'] for k in entity if k.get('severity'))
    for severity, count in signs.most_common():
        values.update({severity: count})
    data.append(values)
    return data
