from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = 'python'
favorite_languages["sarah"] = 'c'
favorite_languages["phil"] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "favorite " + language.title())


