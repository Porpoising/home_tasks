import requests

params = {
    'json': 'true'
}

with open('dataset_24476_3.txt', 'r') as numbers_file, open('numbers_answers.txt', 'w') as answers:
    for number in numbers_file:
        number = number.rstrip()
        result = requests.get(f'http://numbersapi.com/{number}/math', params=params)
        if result.json()['found']:
            answers.write('Interesting\n')
        else:
            answers.write('Boring\n')
