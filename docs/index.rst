Gaussian
========

.. image:: gaussian.svg
    :width: 120px
    :alt: Viper logo
    :align: center


Gaussian은 백테스트와 실시간 거래를 지원하는 트레이딩 알고리즘 시뮬레이션 파이썬 프레임워크입니다.
여러 거래소의 매매 데이터와 워치봇 인프라를 이용하여 투자 전략을 개발하고 테스트하실 수 있습니다.

단 1회의 보안 사고도 없이 1조 1,600억원 이상의 암호화폐 거래를 성공적으로 수행한 워치봇 팀이 개발에 참여하고 있습니다.
`워치봇 <https://www.watchbot.co.kr>`_
은 보조지표를 활용하여 24시간 자동 매매를 수행하는 암호화폐 트레이딩 봇 서비스입니다.

Overview
========

- 높은 자유도: Gaussian은 매우 높은 자유도를 제공합니다. 암호화폐 시장에서 구현할 수 있는 전략을 상당 부분 구현 할 수 있으며, 기본적인 보조 지표 사용 부터 모든 트레이딩 로직을 구현 할 수 있습니다.
- 다양한 지원 거래소: Bithumb, Upbit, Coinone, Binance, Huobi, Poloniex
- 전략설계에 필요한 데이터: 모든 암호화폐에 대한 OHLCV, Orderbook, Slippage 데이터 제공.
- 다양한 테스트 모드 지원 및 실제 트레이딩: backtest, papertest, live
- PyData eco-system: Pandas DataFrames 에 기반한 아웃풋 값을 가지며, PyData eco-system 과 연동이 쉽다.
- 빠른 백테스팅: zipline, catalyst 대비 5배 정도 빠른 백테스팅 속도

Contents
========

.. toctree::
   :maxdepth: 1

   install.rst
   features.rst
   example-algorithms.rst
   api-reference.rst


활발히 개발 중인 알고리즘 트레이딩 라이브러리
`Zipline <https://github.com/quantopian/zipline>`_
과
`Catalyst <https://github.com/enigmampc/catalyst>`_
를 참고하여 프레임워크를 개발하고 있습니다.
