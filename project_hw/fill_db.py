# скрипт автозаполнения бд
from models import Shop

def fill_db(name):
    shop = Shop(name)         
    list_supplier = [
        ['reep', 'exemple_@gmail.com'],
        ['megacorp', 'qwertyu_@yahoo.com'],
        ['ajax', 'zxcvbnm_@agmail.com'],
        ['jungle', 'asdfgjh_@jungle.com'],
        ['gnom', 'gnoms@gnom.com'],
        ['qwerty', 'qwerty_sys@sys.com']]

    list_product = [
        ['автомобили', 122, 953, 4],
        ['авиатехника', 121, 755, 3],
        ['автомобили_грузовые', 8123, 56, 2],
        ['корабли', 125, 978, 1],
        ['одежда', 126, 877, 4],
        ['электроинструменты', 126, 777, 2],
        ['мотоциклы', 126, 677, 3],
        ['украшения', 126, 777, 1],
        ['мебель', 345, 889, 5],
        ['игрушки_авиамодели',324, 998, 6],
        ['drons', 234, 876, 3],
        ['книги_журналы', 324, 898, 5],
        ['робототехника', 567, 987, 6]]

    list_foodstaff = [
        ['бананы', 124, 23, 'аргентина', '11,09,17', 1],
        ['киви', 127, 234, 'chili', '12,09,17', 2],
        ['апельсины', 128, 73, 'египет', '13,09,17', 3],
        ['виноград', 120, 355, 'chili', '12,09,17', 4],
        ['манго', 128, 70, 'египет', '13,09,17', 3],
        ['яблоки', 528, 71, 'черногория', '13,09,17', 4],
        ['лимоны', 128, 70, 'марокко', '13,07,17', 5],
        ['сахар', 128, 70, 'куба', '13,09,17', 6],
        ['персики', 328, 77, 'армения', '23,11,17', 2]]

    for i in list_supplier:
        shop.add_supplier(i[0], i[1])

    for i in list_product:
        shop.add_product(i[0], i[1], i[2], i[3])

    for i in list_foodstaff:
        shop.add_foodstuff(i[0], i[1], i[2], i[3], i[4], i[5])
