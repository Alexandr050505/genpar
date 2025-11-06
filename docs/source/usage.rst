Usage Guide
===========

Command Line Arguments
----------------------

Генерация пароля
~~~~~~~~~~~~~~~~

.. code-block:: bash

   python main.py --generate --length 16 --uppercase --digits --special

Сохранение пароля
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python main.py --generate --save --service gmail --login user@gmail.com

Поиск пароля
~~~~~~~~~~~~

.. code-block:: bash

   python main.py --find gmail

Примеры использования
---------------------

Пример 1: Простая генерация
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python main.py --generate

Пример 2: Генерация и сохранение
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   python main.py -g -l 16 -u -d -s --save --service github --login myuser