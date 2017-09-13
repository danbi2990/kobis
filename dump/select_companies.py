if __name__ == '__main__':
    import sys
    sys.path.insert(0, "/home/jake/Dev/kobis")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.db.utils import IntegrityError
from json_file import JsonFile
from settings import DATA_DIR
from kobis.models import Companies


first = Companies.objects.get(pk=1)
# print(dir(first))
# ['CompanyDetails_ceoNm', 'CompanyDetails_companyCd', 'CompanyDetails_companyNm', 'CompanyDetails_companyNmEn', 'DoesNotExist', 'Movies_company', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'ceoNm', 'check', 'clean', 'clean_fields', 'companyCd', 'companyNm', 'companyNmEn', 'companyPartNames', 'date_error_message', 'delete', 'filmoNames', 'from_db', 'full_clean', 'get_deferred_fields', 'id', 'objects', 'pk', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']

# print(first.companyNm)
print(type(first))
