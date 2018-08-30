Install
=======

Gaussian은 conda 패키지 매니저를 이용하여 설치합니다.
miniconda를 설치하는 것을 추천드리며 ``miniconda`` 설치 방법은
`Miniconda 링크 <https://conda.io/miniconda.html>`_
를 참고하시기 바랍니다.

python3 환경을 지원하며 python3.6-environment.yml 파일을 이용하여 독립된 conda 환경을 생성하실 수 있습니다.

.. code-block:: bash

    $ cd ${PROJECT_HOME}/gaussian/etc/
    $ conda env create -f python3.6-environment.yml
