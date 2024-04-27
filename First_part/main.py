import sys

from seed import connect
from models import Quotes, Authors

help_dict = {
    'name: <author name>': 'Find all quotes by given author name',
    'tag: <tag>': 'Find qoutes by giventag',
    'tags: <tag1>,<tag2>...': 'Find qoutes by few given tags',
    'exit:': 'Close program'
}

help_str = ''
for key, value in help_dict.items():
    help_str += '{} -> {}\n'.format(key, value)


def find_by_name(user_input: str):
    author_name = user_input.replace('name:', '').strip()
    author = Authors.objects(full_name=author_name).first()
    if author:
        quotes = Quotes.objects(author=author)
        for quote in quotes:
            print(f'{quote.quote}')
        return ''
    else:
        return 'Author not found'


def find_by_tag(user_input: str):
    tag = user_input.replace('tag:', '').strip()
    quotes = Quotes.objects(tags=tag)
    if quotes:
        for quote in quotes:
            print(f'{quote.quote}')
        return ''
    else:
        return 'Not quotes with such tag'


def find_by_tags(user_input: str):
    tag = user_input.replace('tags:', '').strip().split(',')
    quotes = Quotes.objects(tags__in=tag)
    if quotes:
        for quote in quotes:
            print(f'{quote.quote}')
        return ''
    else:
        return 'Not quotes with such tags'


def exit(user_input: str):
    print('Good bye')
    sys.exit()


commands = {
    'name': find_by_name,
    'tag': find_by_tag,
    'tags': find_by_tags,
    'exit': exit
}


def get_handler(user_input: str):
    user_input = user_input.split(':')
    for i in commands:
        if user_input[0] == i:
            return commands[i]


def main():
    print(help_str)
    while True:
        user_input = input('>> ')
        handler = get_handler(user_input)
        try:
            result = handler(user_input)
            print(result)
        except TypeError:
            print(f'Unknown command. Try again following the comands list: \n')
            print(help_str)


if __name__ == '__main__':
    main()