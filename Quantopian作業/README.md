# 交易策略
## Due: 2018/01/04 6:00pm

買進策略：現在的價格>1.008*MA7(7日均價)、7日均量>現在的量
賣出策略：現在的價格<7日均價、7日均價>35日均價

### 程式碼

def initialize(context):
    # In our example, we're looking at Apple.  If you re-type
    # this line you'll see the auto-complete popup after `sid(`.
    context.security = [sid(24),sid(5061)]

    # Specify that we want the 'rebalance' method to run once a day
    schedule_function(rebalance, date_rule=date_rules.every_day())

"""
Rebalance function scheduled to run once per day (at market open).
"""
def rebalance(context, data):
    # To make market decisions, we're calculating the stock's
    # moving average for the last 5 days.

    # We get the price history for the last 5 days.
    price_history = data.history(
        context.security,
        fields=["price", "volume"],
        bar_count=7,
        frequency='1d'
    )
    price_history2 = data.history(
        context.security,
        fields='price',
        bar_count=35,
        frequency='1d'
    )

    # Then we take an average of those 5 days.
    average_price = price_history["price"].mean()
    average_vol = price_history["volume"].mean()
    average_price2 = price_history2.mean()

    # We also get the stock's current price.
    current_price = data.current(context.security, 'price')
    current_vol = data.current(context.security, 'volume')
    #current_vol = data.current(context.security, 'volume')

    # If our stock is currently listed on a major exchange
    for s in context.security:
        if data.can_trade(s):
        # If the current price is 1% above the 5-day average price,
        # we open a long position. If the current price is below the
        # average price, then we want to close our position to 0 shares.
            if current_price[s] > (1.008 * average_price[s]) and (average_vol[s] > current_vol[s]):
            # Place the buy order (positive means buy, negative means sell)
                order_target_percent(s, 1)
                log.info("Buying %s" % (s.symbol))
            elif current_price[s] < average_price[s] and (average_price[s] > average_price2[s]):
            # Sell all of our shares by setting the target position to zero
                order_target_percent(s, 0)
                log.info("Selling %s" % (s.symbol))

    # Use the record() method to track up to five custom signals. 
    # Record Apple's current price and the average price over the last
    # five days.
        record(current_price=current_price[s], average_price=average_price[s])

### 連結：

* https://www.quantopian.com/algorithms/5a3b99f50623f317f758d827
