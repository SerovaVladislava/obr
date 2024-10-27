from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import os
import openpyxl
from django.conf import settings

# Настройки для загрузки файлов
MEDIA_ROOT = settings.MEDIA_ROOT
fs = FileSystemStorage(location=MEDIA_ROOT)

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        # Получаем загруженный файл
        uploaded_file = request.FILES['file']
        
        # Проверяем тип файла
        if not uploaded_file.name.endswith('.xlsx'):
            return JsonResponse({'error': 'Неверный тип файла. Допустимо только xlsx.'}, status=400)

        # Сохраняем файл в папку MEDIA_ROOT
        filename = fs.save(uploaded_file.name, uploaded_file)
        filepath = os.path.join(MEDIA_ROOT, filename)

        # Обработка файла с помощью openpyxl
        try:
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            
            # Добавьте код для обработки данных из файла
            import h5py
            from keras.models import load_model

            model = load_model('gov_neural-main\models\weights_config_3.weights.h5') 

            
            return JsonResponse({'message': 'Файл успешно загружен и обработан.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': f'Ошибка обработки файла: {e}'}, status=500)

    return JsonResponse({'error': 'Неверный метод запроса.'}, status=405)