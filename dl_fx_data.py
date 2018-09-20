if __name__ == '__main__':
  from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
  market = Market(market_data_generator=MarketDataGenerator())
  md_request = MarketDataRequest(start_date='14 Jun 2016', finish_date='15 Jun 2016', fields=['bid'], vendor_fields=['bid'], freq='tick', data_source='dukascopy', tickers=['EURUSD'], vendor_tickers=['EURUSD'])
  df = market.fetch_market(md_request)
  print(df.tail(n=10))