import pandas as pd
from logbook import Logger

from gaussian.framework import algorithm
from gaussian.assets.assets import Asset, CoinCurrency
from gaussian.framework import run_algo
from gaussian.account.account import Account


def initialize(context: algorithm.TradingAlgorithm, args: dict):
    context.btc_asset = Asset(CoinCurrency("btc", "usdt"), "binance")
    context.add_asset(context.btc_asset)
    context.account = Account(context=context,
                              capital_base=10000,
                              exchange='binance',
                              support_credit=True)
    context.position = 'buy'


def handle_data(context):
    current_dt = context.current_dt
    coin_market_holder = context.coin_market_holder
    short_moving_data = coin_market_holder.get_history_data(asset=context.btc_asset,
                                                            end_dt=current_dt,
                                                            bar_count=18,
                                                            fields="close"
                                                            )
    long_moving_data = coin_market_holder.get_history_data(asset=context.btc_asset,
                                                           end_dt=current_dt,
                                                           bar_count=26,
                                                           fields="close")
    short_moving = short_moving_data.values.mean()
    long_moving = long_moving_data.values.mean()

    if short_moving > long_moving and context.position is 'sell':
        context.account.order(asset=context.btc_asset,
                              trade_method='market',
                              order_percent=100,
                              credit_position='long',
                              direction='entry',
                              slippage=0.5
                              )
        context.position = 'buy'
    elif short_moving < long_moving and context.position is 'buy':
        context.account.order(asset=context.btc_asset,
                              trade_method='market',
                              order_percent=100,
                              credit_position='long',
                              direction='exit',
                              slippage=0.5
                              )
        context.position = 'sell'


def analyze(context):
    context.account.analyze_backtest()
    context.account.print_backtest_result()


if __name__ == '__main__':
    start = pd.Timestamp('2018-07-26')
    end = pd.Timestamp('2018-08-05')

    run_algo.run_algorithm(
        frequency='15m',
        initialize=initialize,
        handle_data=handle_data,
        analyze=analyze,
        quote_currency='usdt',
        start=start,
        end=end
    )
