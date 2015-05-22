android-flasher
===============

.. image:: https://pypip.in/v/android-flasher/badge.svg
    :target: https://pypi.python.org/pypi/android-flasher/

Flasher is a shell script generator which helps you to flash the Android
factory image without removing user data.

You can use it instead of ``flash-all.sh`` or ``flash-all.bat``.


Installation
~~~~~~~~~~~~

You can install android-flasher with ``pip``

::

    $ pip install android-flasher


How to use
~~~~~~~~~~~~~~~~

1. Install.
2. Move to the unzipped factory image directory.
3. Execute ``android-flasher`` in terminal.
4. Now reboot and enter the bootloader.
5. Execute the ``flasher.sh`` script.

If you meet an error like ``fastboot: command not found``, add following line in
 your ``~/.bash_profile``.

::

    export PATH="/Users/mspark/Downloads/android-sdk-macosx/platform-tools:$PATH"


License
~~~~~~~

`The MIT License (MIT)`_

Copyright (c) 2015 Minsoo Park

.. _The MIT License (MIT): https://github.com/minsoopark/android-flasher/blob/master/LICENSE
