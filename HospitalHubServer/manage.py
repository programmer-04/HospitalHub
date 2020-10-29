<<<<<<< HEAD
#!/usr/bin/env python3
=======
#!/usr/bin/env python
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
<<<<<<< HEAD
=======
    """Run administrative tasks."""
>>>>>>> 97969be225cfb49aa6da4c5e428ba1c8b9fd53dd
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HospitalHubServer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
