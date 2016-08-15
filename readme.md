Este programa executa algumas tarefas de manipulação de matrizes.

Para executá-lo, é necessário a instalação de alguns requisitos:

* Python 3.4+
* Pacotes do arquivo requirements.txt

Caso esteja com alguma complicação para rodá-lo, seguem algumas dicas:

1) Verifique se o pip está instalado e se é a versão para o python3:

    $ pip3 --version
    pip 1.5.4 from /usr/lib/python3/dist-packages (python 3.4)

    Se precisar instalar o pip para o python3, é só seguir os passos:

    $ sudo apt-get install python3-pip
    $ sudo apt-get update


2) Se o erro persistir, tente instalar esses pacotes python development headers:

    $ sudo apt-get install python3-dev
    $ sudo apt-get install libevent-dev
    $ pip3 install --upgrade setuptools
    $ sudo apt-get install build-essential


Se desejar, entre em contato por email: julianaskubs@gmail.com