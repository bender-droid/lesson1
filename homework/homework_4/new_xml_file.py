import xml.etree.ElementTree as elemTree


def create_book_xml_template():
    root = elemTree.Element('Catalog')
    book = elemTree.Element('Book')

    root.append(book)

    author = elemTree.SubElement(book, 'Author')
    author.text = 'Lastname, Firstname'

    title = elemTree.SubElement(book, 'Title')
    title.text = 'Book name'

    genre = elemTree.SubElement(book, 'Genre')
    genre.text = 'Book genre'

    price = elemTree.SubElement(book, 'Price')
    price.text = 'Price'

    publ_date = elemTree.SubElement(book, 'PublishDate')
    publ_date.text = 'YYYY-MM-DD'

    description = elemTree.SubElement(book, 'Description')
    description.text = 'Book description'

    file = elemTree.ElementTree(root)
    elemTree.indent(file, space='    ')

    file.write('./homework_files/book_template.xml', encoding='utf-8')


create_book_xml_template()
