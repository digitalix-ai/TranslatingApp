from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode='w', encoding='utf-8') as my_file1:
            my_file1.write(translation)

except FileNotFoundError:
    print('check your file path')