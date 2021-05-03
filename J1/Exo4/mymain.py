from file_handling import file_handling

my_class = file_handling()

opened = my_class.creator("sample.txt")
written = my_class.writer(opened, ["a lot", " of", " data"])
my_class.closer(opened)

print(written)