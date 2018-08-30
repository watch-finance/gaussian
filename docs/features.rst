Features
========


제공 기능
~~~~~~~~~~~~~~~~~~~~~

* 백테스트
* 실시간 매매 및 모의 투자 기능 : API Key 등록을 통한 매매
* 6곳의 거래소와 94종의 암호화폐 지원 : 암호화폐 24시간 트레이딩 서비스 워치봇이 연동한 6곳의 거래소와 94종의 암호화폐를 지원합니다.
  워치봇은 거래소의 Open API를 연동하여 실제로 발생한 암호화폐 매매 기록을 수집하여 다양한 시간대를 지원하는 캔들 차트 데이터를 제공합니다.
    * 지원 거래소 : Bithumb, Upbit, Coinone, Poloniex, Binance, Huobi.
* 수수료, 슬리피지 적용
* MacOS, Linux 그리고 Windows 설치
* 파이썬 3 지원

 .. _naming:

네이밍 컨벤션
~~~~~~~~~~~~~~~~~

Gaussian은 암호화폐 네이밍 컨벤션을 아래와 같이 정했습니다.

    **{coin_symbol}_{fiat_currency}**

coin_symbobl은 암호화폐의 축약형 이름을 이용하며 fiat_currency는 암호화폐 거래 단위를 이용합니다.
예로들어 이더리움(ETH) 코인의 거래 수단이 테더화(USDT)라면 coin_symbol은 eth, fiat_currency는 usdt가 됩니다.

coin_symbol과 fiat_currency는 소문자를 사용하며 언더스코어('_') 문자로 이들을 연결하여 암호화폐 이름을 완성합니다.

.. code-block:: bash

   eth_usdt
