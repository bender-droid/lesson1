import xml.etree.ElementTree as ET

# file = ET.parse('./files/nschfdop.xml').getroot()
#
# xpath = file.find('Документ/СвСчФакт')
# xpath.set('НомерСчФ', '1')
#
# xpath = file.find('Документ/СвСчФакт/СвПрод/Адрес/АдрРФ')
# xpath.set('Индекс', '211023')
#
# xpath = file.find('Документ/СвСчФакт/ГрузПолуч/Адрес/АдрРФ')
# xpath.set('Город', 'Смоленск')
# # print(xpath.get('НомерСчФ'))
#
# file = ET.ElementTree(file)
# file.write('./files/new_nschfdop.xml', encoding='utf-8')


root = ET.Element('Страна')
appt = ET.Element('Город')
root.append(appt)

begin = ET.SubElement(appt, 'индекс')
begin.text = '213023'

name = ET.SubElement(appt, 'НазваниеГорода')
name.text = 'Смоленск'

street = ET.SubElement(appt, 'Улица')
street.text = 'Нарвская'

tree = ET.ElementTree(root)
ET.indent(tree)
tree.write('files/city.xml', encoding='utf-8')
