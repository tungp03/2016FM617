import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
    df = pd.read_csv(url)
    return df.to_html()

@app.route('/nyse/<symbol>')
def nyse_company(symbol):
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
    df = pd.read_csv(url)
    df2 = df[df['Symbol'].isin([symbol])]
    return df2.to_html()

@app.route('/nasdaq')
def nasdaq():
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
    df = pd.read_csv(url)
    return df.to_html()

@app.route('/nasdaq/<symbol>')
def nasdaq_company(symbol):
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download"
    df = pd.read_csv(url)
    df2 = df[df['Symbol'].isin([symbol])]
    return df2.to_html()

@app.route('/amex')
def amex():
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
    df = pd.read_csv(url)
    return df.to_html()

@app.route('/amex/<symbol>')
def amex_company(symbol):
    url = "http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download"
    df = pd.read_csv(url)
    df2 = df[df['Symbol'].isin([symbol])]
    return df2.to_html()


if __name__=="__main__":
    app.run()
