import pandas as pd
import talib
import ta
import matplotlib.pyplot as plt


def classic_EMA(df, window):
# ЕМА classic calc using {window} amount of data    

    # Cutting just {window} last closes
    close_prices = df['close'].values[-1*window:]

    alpha = 2 / (window + 1) 
    ema = close_prices[0]  # initial EMA that's the key of difference between normal function, TA and TaLib

    for price in close_prices[1:]:
        ema = alpha * price + (1 - alpha) * ema

    return ema


def EMA_check(df, window):
    
    df_test = pd.DataFrame()
    
    for i in range(window, len(df_70_values)):
        df = df_70_values.tail(i)

        row = pd.DataFrame({
            'Data frame': [i],
            'EMA classic': [round(classic_EMA(df, window), 6)],
            'EMA TaLib': [round(talib.EMA(df['close'].values, timeperiod=window)[-1], 6)],
            'EMA TA': [round(ta.trend.EMAIndicator(df['close'], window=window, fillna=False).ema_indicator().iloc[-1], 6)]
        })

        df_test = pd.concat([df_test, row], ignore_index=True)

    # Построение графиков
    plt.figure(figsize=(12, 6))
    
    plt.plot(df_test['Data frame'], df_test['EMA classic'], label='EMA classic')
    plt.plot(df_test['Data frame'], df_test['EMA TaLib'], label='EMA TaLib')
    plt.plot(df_test['Data frame'], df_test['EMA TA'], label='EMA TA')

    plt.xlabel('Length of used data frame ie amount of closes')
    plt.ylabel('Stock close price')
    plt.title(f'EMA\'s Comparison Window = {window}')
    plt.legend()
    plt.grid(True)
    plt.show()

    display(df_test)

# Test data set of stock closes
df_70_values = pd.DataFrame({"close": [284.41,282.17,283.5,287.28,287.07,289.06,290.24,288.33,288.93,283.9,282.0,284.77,291.25,292.52,291.75,292.19,295.38,299.17,298.4,297.71,300.4,299.79,300.9,298.85,295.83,298.3,298.87,295.2,295.4,295.62,292.99,293.9,294.11,295.1,299.0,298.72,300.43,300.38,306.72,304.61,306.1,307.75,306.76,306.48,306.95,307.1,307.99,308.29,306.59,307.99,307.38,314.99,307.39,307.94,308.41,309.0,308.98,308.97,308.24,307.37,307.53,306.01,308.22,311.21,313.49,314.85,318.12,319.7,322.91,323.16]})

EMA_check(df_70_values, window = 10)


    
