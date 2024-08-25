from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group,User
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import os.path
import csv
import json
import logging
from usuarios.models import Cliente
from django.conf import settings
logger = logging.getLogger(__name__)

COMMAND_DIR = os.path.join(
    settings.BASE_DIR, 'projectcommands/management/commands')
tru_str_list = ['true', '1', 't', 'y', 'yes',
                'yeah', 'yup', 'certainly', 'uh-huh']


class Command(BaseCommand):
    help = 'Upload information to the database'

    def handle(self, *args, **options):
        try:
            group_data = read_csv(os.path.join(COMMAND_DIR, 'users/users.csv'))
            for group_d in group_data:
                createuser(group_d)
        except Exception as e:
            print('aqui no ',e)
            pass
def read_csv(file):
    f = open(file, 'r')
    reader = csv.DictReader(f)
    out = json.dumps([row for row in reader])
    return json.loads(out)
def createuser(user):
    try:
        print(user)
        username=user["username"]
        email=user["email"]
        password=user["password"]
        cedula=user["cedula"]
        telefono=user["telefono"]
        direccion=user["direccion"]
        usuario = User.objects.create(
                    username=username,
                    is_staff=True,
                    is_superuser=True,
                )
        usuario.set_password(password)
        usuario.save()
        logger.info("usuario creado")
    except IntegrityError:
        logger.info("el usuario ya existe")
    except Exception as e:
        logger.exception("error")