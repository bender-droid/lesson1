import xml.etree.ElementTree as elemTree
import random


def update_book_template():
    file = elemTree.parse('./homework_files/book_template.xml').getroot()

    xpath = file.find('Book')
    xpath.set('id', str(random.randint(1, 10000)))

    xpath = file.find('Book/Author')
    xpath.text = 'Garghentini, Davide'

    xpath = file.find('Book/Title')
    xpath.text = "XML Developer's Guide"

    xpath = file.find('Book/Genre')
    xpath.text = 'Computer'

    xpath = file.find('Book/Price')
    xpath.text = '44.95'

    xpath = file.find('Book/PublishDate')
    xpath.text = '2000-10-01'

    xpath = file.find('Book/Description')
    xpath.text = 'An in-depth look at ' \
                 'creating applications with XML.'

    file = elemTree.ElementTree(file)
    file.write('./homework_files/updated_book.xml', encoding='utf-8')


update_book_template()
