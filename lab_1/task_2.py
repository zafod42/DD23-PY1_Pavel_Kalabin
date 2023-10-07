# TODO Найдите количество книг, которое можно разместить на дискете


bytes_in_megabyte = 2**20

disk_volume = 1.44 * bytes_in_megabyte
lists = 100
count_lines = 50
char_in_line = 25

char_size = 4

chars_count = lists * count_lines * char_in_line

book_size = chars_count * char_size

book_number = int(disk_volume // book_size)

print("Количество книг, помещающихся на дискету:", book_number)
