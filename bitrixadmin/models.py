from django.db import models


"""Типы инфоблоков"""
class b_iblock_type(models.Model):
    """ Флаг (Y/N). Разделяются ли элементы блока этого типа по разделам. Обязателен. По умолчанию - "Y"."""
    #sections = models.CharField(blank=False, default="Y", max_length=1)
    sections = models.BooleanField(default=True)
    """Порядок сортировки типа"""
    sort = models.IntegerField(blank=False, default=500)
    """Название типа информационных блоков."""
    name = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Типы инфоблоков'


"""Инфоблоки"""
class b_iblock(models.Model):
    """Символьный идентификатор."""
    code = models.CharField(blank=True, max_length=50)
    """Внешний код."""
    xml_id = models.CharField(blank=True, max_length=255)
    """Код типа информационных блоков."""
    iblock_type_id = models.CharField(blank=False, max_length=50)
    """Дата последнего изменения параметров блока."""
    timestamp_x = models.DateTimeField(auto_now=True)
    """Дата создания"""
    time_create = models.DateTimeField(auto_now_add=True)
    """Дата последнего изменения"""
    time_update = models.DateTimeField(auto_now=True)
    """Название"""
    name = models.CharField(blank=False, max_length=255)
    """Флаг активности (Y|N)"""
    active = models.CharField(blank=False, default="Y", max_length=1)
    """Индекс сортировки."""
    sort = models.IntegerField(blank=False, default=500)
    """Шаблон URL-а к странице для публичного просмотра списка элементов информационного блока."""
    list_page_url = models.CharField(blank=True, max_length=255)
    """Шаблон URL-а к странице для просмотра раздела."""
    section_page_url = models.CharField(blank=True, max_length=255)
    """Шаблон URL-а странице для детального просмотра элемента."""
    detail_page_url = models.CharField(blank=True, max_length=255)
    """Код картинки в таблице файлов."""
    picture = models.CharField(blank=True, max_length=255)
    """Описание."""
    description = models.TextField(blank=True)
    """Тип описания (text/html)"""
    description_type = models.CharField(blank=True, max_length=4, default='text')
    """Признак наличия привязки свойств к разделам (Y|N)."""
    section_property = models.CharField(blank=True, max_length=1)

    def __str__(self):
        return self.name


"""Элементы"""
class b_iblock_element(models.Model):
    """Символьный идентификатор."""
    code = models.CharField(blank=True, max_length=255)
    """Внешний код."""
    xml_id = models.CharField(blank=False, max_length=255)
    """Название элемента."""
    name = models.CharField(blank=False, max_length=255)
    """ID информационного блока."""
    iblock_id = models.IntegerField(blank=False)
    """ID группы. Если не задан, то элемент не привязан к группе. 
    Если элемент привязан к нескольким группам, то в этом поле ID одной из них. 
    Эта группа будет основной для элемента, то есть её код или ID будет стоять в URL страницы элемента. 
    По умолчанию содержит привязку к разделу с минимальным ID из массива идентификаторов поля IBLOCK_SECTION."""
    iblock_section_id = models.IntegerField(blank=True)
    """Массив идентификаторов групп, к которым относится элемент."""
    iblock_section = models.IntegerField(blank=True)
    """Символический код инфоблока."""
    iblock_code = models.CharField(blank=True, max_length=255)
    """Флаг активности (Y|N)"""
    active = models.CharField(blank=False, default="Y", max_length=1)
    """Дата начала действия элемента."""
    active_from = models.DateTimeField(blank=True)
    """Дата окончания действия элемента."""
    active_to = models.DateTimeField(blank=True)
    """Индекс сортировки."""
    sort = models.IntegerField(blank=False, default=500)
    """Код картинки в таблице файлов для предварительного просмотра (анонса)."""
    preview_pucture = models.IntegerField(blank=True)
    """Предварительное описание (анонс)."""
    preview_text = models.TextField(blank=True)
    """Тип предварительного описания (text/html)."""
    preview_text_type = models.CharField(blank=False, max_length=4, default='text')
    """Код картинки в таблице файлов для детального просмотра."""
    detail_pucture = models.IntegerField(blank=True)
    """Детальное описание"""
    detail_text = models.TextField(blank=True)
    """Тип детального описания (text/html)."""
    detail_text_type = models.CharField(blank=False, max_length=4, default='text')
    """Дата создания"""
    time_create = models.DateTimeField(auto_now_add=True)
    """Дата последнего изменения"""
    time_update = models.DateTimeField(auto_now=True)
    """Время последнего изменения полей элемента."""
    timestamp_x = models.DateTimeField(auto_now=True)
    """Имя пользователя, создавшего элемент."""
    created_user_name = models.IntegerField(blank=True)
    """Имя пользователя, в последний раз изменившего элемент."""
    user_name = models.IntegerField(blank=True)
    """Шаблон URL-а к странице для публичного просмотра списка элементов информационного блока."""
    list_page_url = models.CharField(blank=True, max_length=255)
    """Путь к папке сайта. Определяется из параметров информационного блока. Изменяется автоматически."""
    lang_dir = models.CharField(blank=True, max_length=255)
    """Шаблон URL-а к странице для детального просмотра элемента. Определяется из параметров информационного блока. """
    detail_page_url = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


"""Разделы"""
class b_iblock_section(models.Model):
    """Символьный идентификатор."""
    code = models.CharField(blank=True, max_length=255)
    """Внешний код."""
    xml_id = models.CharField(blank=True, max_length=255)
    """Название элемента."""
    name = models.CharField(blank=False, max_length=255)
    """ID информационного блока."""
    iblock_id = models.IntegerField(blank=False)
    """ID группы родителя, если не задан то группа корневая."""
    iblock_section_id = models.IntegerField(blank=True)
    """Дата создания"""
    time_create = models.DateTimeField(auto_now_add=True)
    """Дата последнего изменения"""
    time_update = models.DateTimeField(auto_now=True)
    """Время последнего изменения полей элемента."""
    timestamp_x = models.DateTimeField(auto_now=True)
    """Индекс сортировки."""
    sort = models.IntegerField(blank=False, default=500)
    """Флаг активности (Y|N)"""
    active = models.CharField(blank=False, default="Y", max_length=1)
    """Флаг активности, учитывая активность вышележащих (родительских) групп (Y|N). 
    Вычисляется автоматически (не может быть изменен вручную)."""
    global_active = models.CharField(blank=True, max_length=1)
    """Код картинки в таблице файлов."""
    picture = models.IntegerField(blank=True)
    """Описание."""
    description = models.TextField(blank=True)
    """Тип описания (text/html)"""
    description_type = models.CharField(blank=True, max_length=4, default='text')
    """Левая граница группы. Вычисляется автоматически (не устанавливается вручную)."""
    left_margin = models.IntegerField(blank=True)
    """Правая граница группы. Вычисляется автоматически (не устанавливается вручную)."""
    right_margin = models.IntegerField(blank=True)
    """Уровень вложенности группы. Вычисляется автоматически (не устанавливается вручную)."""
    depth_level = models.IntegerField(blank=True)
    """Шаблон URL-а к странице для детального просмотра раздела. 
    Определяется из параметров информационного блока. Изменяется автоматически."""
    section_page_url = models.CharField(blank=True, max_length=255)
    """Код картинки в таблице файлов для детального просмотра."""
    detail_pucture = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


"""Свойства элементов """
class b_iblock_property(models.Model):
    """Символьный идентификатор."""
    code = models.CharField(blank=True, max_length=255)
    """Внешний код."""
    xml_id = models.CharField(blank=True, max_length=255)
    """Название элемента."""
    name = models.CharField(blank=False, max_length=255)
    """ID информационного блока."""
    iblock_id = models.IntegerField(blank=False)
    """Индекс сортировки."""
    sort = models.IntegerField(blank=False, default=500)
    """Флаг активности (Y|N)"""
    active = models.CharField(blank=False, default="Y", max_length=1)
    """Обязательное (Y|N)."""
    is_required = models.CharField(blank=True, max_length=1)
    """Тип свойства. Возможные значения: 
    S - строка, N - число, F - файл, L - список, E - привязка к элементам, G - привязка к группам."""
    property_type = models.CharField(blank=False, default="S", max_length=1)
    """Множественность (Y|N)."""
    multiple = models.CharField(blank=False, default="N", max_length=1)
    """Время последнего изменения полей элемента."""
    timestamp_x = models.DateTimeField(auto_now=True)
    """Значение свойства по умолчанию (кроме свойства типа список L)."""
    default_value = models.CharField(blank=True, max_length=255)
    """Количество строк в ячейке ввода значения свойства."""
    row_count = models.IntegerField(blank=False, default=1, max_length=1)
    """Количество столбцов в ячейке ввода значения свойства."""
    col_count = models.IntegerField(blank=False, default=1, max_length=1)
    """Тип для свойства список (L). Может быть "L" - выпадающий список или "C" - флажки."""
    list_type = models.CharField(blank=False, default="L", max_length=1)
    """Количество строк в выпадающем списке для свойств типа "список"."""
    multiple_cnt = models.IntegerField(blank=True)
    """Список допустимых расширений для свойств файл "F"(через запятую)."""
    file_type = models.CharField(blank=True, max_length=200)
    """Подсказка"""
    hint = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.name


class b_iblock_element_property(models.Model):
    """Код свойства."""
    iblock_property_id = models.IntegerField(blank=False)
    """Код элемента."""
    iblock_pelement_id = models.IntegerField(blank=False)
    """Значение свойства."""
    value = models.TextField(blank=False)
    """Тип значения свойства (text/html)."""
    value_type = models.CharField(blank=False, max_length=4, default='text')
    """Представление значения свойства в виде целого числа."""
    value_enum = models.IntegerField(blank=True)
    """Представление значения свойства в виде числа с плавающей точкой."""
    value_num = models.FloatField(blank=True)
    """Дополнительное поле описания"""
    description = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.iblock_property_id

class b_iblock_section_property(models.Model):
    """ID информационного блока."""
    iblock_id = models.IntegerField(blank=False)
    """ID раздела."""
    section_id = models.IntegerField(blank=False)
    """ID свойства."""
    property_id = models.IntegerField(blank=False)