from translate import Translator
def get_supported_languages():
    supported_languages = [
        ("af", "Afrikaans"),
        ("sq", "Albanian"),
        ("am", "Amharic"),
        ("ar", "Arabic"),
        ("hy", "Armenian"),
        ("az", "Azerbaijani"),
        ("eu", "Basque"),
        ("be", "Belarusian"),
        ("bn", "Bengali"),
        ("bs", "Bosnian"),
        ("bg", "Bulgarian"),
        ("ca", "Catalan"),
        ("ceb", "Cebuano"),
        ("ny", "Chichewa"),
        ("zh-cn", "Chinese (Simplified)"),
        ("zh-tw", "Chinese (Traditional)"),
        ("co", "Corsican"),
        ("hr", "Croatian"),
        ("cs", "Czech"),
        ("da", "Danish"),
        ("nl", "Dutch"),
        ("en", "English"),
        ("eo", "Esperanto"),
        ("et", "Estonian"),
        ("tl", "Filipino"),
        ("fi", "Finnish"),
        ("fr", "French"),
        ("fy", "Frisian"),
        ("gl", "Galician"),
        ("ka", "Georgian"),
        ("de", "German"),
        ("el", "Greek"),
        ("gu", "Gujarati"),
        ("ht", "Haitian Creole"),
        ("ha", "Hausa"),
        ("haw", "Hawaiian"),
        ("iw", "Hebrew"),
        ("hi", "Hindi"),
        ("hmn", "Hmong"),
        ("hu", "Hungarian"),
        ("is", "Icelandic"),
        ("ig", "Igbo"),
        ("id", "Indonesian"),
        ("ga", "Irish"),
        ("it", "Italian"),
        ("ja", "Japanese"),
        ("jw", "Javanese"),
        ("kn", "Kannada"),
        ("kk", "Kazakh"),
        ("km", "Khmer"),
        ("ko", "Korean"),
        ("ku", "Kurdish (Kurmanji)"),
        ("ky", "Kyrgyz"),
        ("lo", "Lao"),
        ("la", "Latin"),
        ("lv", "Latvian"),
        ("lt", "Lithuanian"),
        ("lb", "Luxembourgish"),
        ("mk", "Macedonian"),
        ("mg", "Malagasy"),
        ("ms", "Malay"),
        ("ml", "Malayalam"),
        ("mt", "Maltese"),
        ("mi", "Maori"),
        ("mr", "Marathi"),
        ("mn", "Mongolian"),
        ("my", "Myanmar (Burmese)"),
        ("ne", "Nepali"),
        ("no", "Norwegian"),
        ("ps", "Pashto"),
        ("fa", "Persian"),
        ("pl", "Polish"),
        ("pt", "Portuguese"),
        ("pa", "Punjabi"),
        ("ro", "Romanian"),
        ("ru", "Russian"),
        ("sm", "Samoan"),
        ("gd", "Scots Gaelic"),
        ("sr", "Serbian"),
        ("st", "Sesotho"),
        ("sn", "Shona"),
        ("sd", "Sindhi"),
        ("si", "Sinhala"),
        ("sk", "Slovak"),
        ("sl", "Slovenian"),
        ("so", "Somali"),
        ("es", "Spanish"),
        ("su", "Sundanese"),
        ("sw", "Swahili"),
        ("sv", "Swedish"),
        ("tg", "Tajik"),
        ("ta", "Tamil"),
        ("te", "Telugu"),
        ("th", "Thai"),
        ("tr", "Turkish"),
        ("uk", "Ukrainian"),
        ("ur", "Urdu"),
        ("ug", "Uyghur"),
        ("uz", "Uzbek"),
        ("vi", "Vietnamese"),
        ("cy", "Welsh"),
        ("xh", "Xhosa"),
        ("yi", "Yiddish"),
        ("yo", "Yoruba"),
        ("zu", "Zulu"),
    ]
    return supported_languages


def translate_arb_file(arb_file, input_locale, output_locales):
    # Read the uploaded ARB file from the request
    content = arb_file.read().decode('ISO-8859-1')

    translations = {}

    lines = content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if line == '{' or line == '}':
            i += 1
            continue

        if ': ' in line:
            key, value = line.split(': ', 1)
            to_translate = value.strip().strip('"')
            translations[key.strip('"')] = {input_locale: to_translate}

        i += 1

    for supported_locale in output_locales:
        translator = Translator(from_lang=input_locale, to_lang=supported_locale)
        for key, values in translations.items():
            to_translate = values[input_locale]
            translation = translator.translate(to_translate)
            translations[key][supported_locale] = translation

    return translations


# def rreplace(s, old, new, occurrence):
#     li = s.rsplit(old, occurrence)
#     return new.join(li)

# def translate_arb_file(arb_file, input_locale, output_locales):
#     translator = Translator()

#     # Read the uploaded ARB file from the request
#     content = arb_file.read().decode('ISO-8859-1')

#     translations = {}

#     for line in content.splitlines():
#         # Ignore empty lines and brackets
#         if (line == '{' or line == '}' or not line.strip()):
#             continue

#         # Skip lines that don't have a colon and a space
#         if ': ' not in line:
#             continue

#         to_translate = line.split('": ')[1][1:]
#         to_translate = to_translate.split('"')[0]

#         for supported_locale in output_locales:
#             translation = translator.translate(
#                 to_translate, src=input_locale, dest=supported_locale)
#             new_line = rreplace(line, to_translate, translation.text, 1)

#             if supported_locale in translations.keys():
#                 translations[supported_locale].append(new_line)
#             else:
#                 translations[supported_locale] = [new_line]

#     return translations


# from googletrans import Translator

# def rreplace(s, old, new, occurrence):
#     li = s.rsplit(old, occurrence)
#     return new.join(li)

# def translate_arb_file(input_locale, output_locales):
#     translator = Translator()
#     file = open("input.arb", "r", encoding="ISO-8859-1")

#     translations = {}

#     for line in file:
#         # Ignore empty lines and brackets
#         if (line == '{\n' or line == '}' or line == ''):
#             continue

#         # Skip lines that don't have a colon and a space
#         if ': ' not in line:
#             continue

#         to_translate = line.split('": ')[1][1:]
#         to_translate = to_translate.split('"')[0]

#         for supported_locale in output_locales:
#             translation = translator.translate(
#                 to_translate, src=input_locale, dest=supported_locale)
#             new_line = rreplace(line, to_translate, translation.text, 1)

#             if supported_locale in translations.keys():
#                 translations[supported_locale].append(new_line)
#             else:
#                 translations[supported_locale] = [new_line]

#     for key in translations.keys():
#         with open("result/app_" + key + ".arb", "w", encoding='utf-8') as f:
#             f.write('{\n')
#             for line in translations[key]:
#                 f.write(line)
#             f.write('}')
#             f.close()
