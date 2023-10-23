#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inventario_2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    

    if __name__ == '__main__':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inventario.settings')
        from django.core.management import execute_from_command_line

        # Cambia el número de puerto a tu elección
        ip = '192.168.0.8'
        
        port = 8080

        # Ejecuta el servidor Django en el nuevo puerto
        execute_from_command_line([f'{ip}:{port}'])

        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
