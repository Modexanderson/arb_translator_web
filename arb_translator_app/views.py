import os
import zipfile
from django.shortcuts import render
from django.http import HttpResponse
from .translate import translate_arb_file, get_supported_languages

def home_view(request):
    # Add any context data you want to pass to the template
    context = {
        # You can add any data you want to display on the home page here
    }
    return render(request, 'arb_translator_app/index.html', context)

def about_view(request):
    # Add any context data you want to pass to the template
    context = {
        # You can add any data you want to display on the home page here
    }
    return render(request, 'arb_translator_app/about.html', context)


def translation_view(request):
    if request.method == 'POST' and request.FILES.get('arb_file'):
        input_locale = request.POST.get('input_locale', 'en')
        output_locales = request.POST.getlist('output_locales[]', ['ar'])

        # Get the uploaded ARB file
        arb_file = request.FILES['arb_file']

        # Call the translation function
        translations = translate_arb_file(arb_file, input_locale, output_locales)

        # Get the supported languages for rendering in the template
        supported_languages = get_supported_languages()

        # Create a temporary directory to store the translated files
        temp_directory = 'temp_translation'
        os.makedirs(temp_directory, exist_ok=True)

        # Write the translated content to individual files
        for supported_locale in output_locales:
            os.makedirs(os.path.join(temp_directory, f'result'), exist_ok=True)
            with open(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'), 'w', encoding='utf-8') as f:
                for key, content in translations.items():
                    f.write(f'"{key}": "{content[supported_locale]}"\n')

        # Create a zip file containing all the translated files
        zip_file_path = 'translated_files.zip'
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            for supported_locale in output_locales:
                file_path = os.path.join(temp_directory, f'result/app_{supported_locale}.arb')
                zip_file.write(file_path, os.path.basename(file_path))

        # Clean up the temporary directory
        for supported_locale in output_locales:
            os.remove(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'))
        os.rmdir(os.path.join(temp_directory, 'result'))
        os.rmdir(temp_directory)

        # Serve the zip file for download
        with open(zip_file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=translated_files.zip'
            return response

    # If the request method is not POST, just render the template with supported languages
    supported_languages = get_supported_languages()
    return render(request, 'arb_translator_app/translate.html', {
        'supported_languages': supported_languages,
    })
# def translation_view(request):
#     if request.method == 'POST' and request.FILES.get('arb_file'):
#         input_locale = request.POST.get('input_locale', 'en')
#         output_locales = request.POST.getlist('output_locales', ['ar'])

#         # Get the uploaded ARB file
#         arb_file = request.FILES['arb_file']

#         # Call the translation function
#         translations = translate_arb_file(arb_file, input_locale, output_locales)


#         # Create a temporary directory to store the translated files
#         temp_directory = 'temp_translation'
#         os.makedirs(temp_directory, exist_ok=True)

#         # Write the translated content to individual files
#         for supported_locale in output_locales:
#             os.makedirs(os.path.join(temp_directory, f'result'), exist_ok=True)
#             with open(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'), 'w', encoding='utf-8') as f:
#                 for key, content in translations.items():
#                     f.write(f'"{key}": "{content[supported_locale]}"\n')

#         # Create a zip file containing all the translated files
#         zip_file_path = 'translated_files.zip'
#         with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
#             for supported_locale in output_locales:
#                 file_path = os.path.join(temp_directory, f'result/app_{supported_locale}.arb')
#                 zip_file.write(file_path, os.path.basename(file_path))

#         # Clean up the temporary directory
#         for supported_locale in output_locales:
#             os.remove(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'))
#         os.rmdir(os.path.join(temp_directory, 'result'))
#         os.rmdir(temp_directory)

#         # Serve the zip file for download
#         with open(zip_file_path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='application/zip')
#             response['Content-Disposition'] = 'attachment; filename=translated_files.zip'
#             return response

#     return render(request, 'arb_translator_app/translate.html')

# def translation_view(request):
#     if request.method == 'POST' and request.FILES.get('arb_file'):
#         input_locale = 'en'
#         output_locales = ['ar', 'bn', 'cs', 'de', 'es', 'fr', 'he', 'hi', 'id', 'it', 'ja', 'pt', 'ru', 'ta', 'tr', 'uk', 'ur', 'zh-cn']

#         # Get the uploaded ARB file
#         arb_file = request.FILES['arb_file']

#         # Call the translation function
#         translations = translate_arb_file(arb_file, input_locale, output_locales)

#         # Create a temporary directory to store the translated files
#         temp_directory = 'temp_translation'
#         os.makedirs(temp_directory, exist_ok=True)

#         # Write the translated content to individual files
#         for supported_locale in output_locales:
#             os.makedirs(os.path.join(temp_directory, f'result'), exist_ok=True)
#             with open(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'), 'w', encoding='utf-8') as f:
#                 for key, content in translations.items():
#                     f.write(f'"{key}": "{content[supported_locale]}"\n')

#         # Create a zip file containing all the translated files
#         zip_file_path = 'translated_files.zip'
#         with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
#             for supported_locale in output_locales:
#                 file_path = os.path.join(temp_directory, f'result/app_{supported_locale}.arb')
#                 zip_file.write(file_path, os.path.basename(file_path))

#         # Clean up the temporary directory
#         for supported_locale in output_locales:
#             os.remove(os.path.join(temp_directory, f'result/app_{supported_locale}.arb'))
#         os.rmdir(os.path.join(temp_directory, 'result'))
#         os.rmdir(temp_directory)

#         # Serve the zip file for download
#         with open(zip_file_path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='application/zip')
#             response['Content-Disposition'] = 'attachment; filename=translated_files.zip'
#             return response

#     return render(request, 'arb_translator_app/translate.html')

# def translation_view(request):
#     if request.method == 'POST':
#         input_locale = 'en'
#         output_locales = ['ar', 'bn', 'cs', 'de', 'es', 'fr', 'he', 'hi', 'id', 'it', 'ja', 'pt', 'ru', 'ta', 'tr', 'uk', 'ur', 'zh-cn']

#         # Call the translation function
#         translate_arb_file(input_locale, output_locales)

#         # Redirect to a success page or show a success message
#         return render(request, 'translator/success.html')

#     return render(request, 'translator/translate.html')
