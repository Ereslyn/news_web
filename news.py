#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import  Flask,render_template
app=Flask(__name__)


@app.route('/news')   #增加一个news页面
def newspage():
    newsContent="全国上下一心支持武汉，武汉加油！"
    return render_template("news.html",data=newsContent)


                           
if __name__=="__main__":
    app.run(port=2020,host="127.0.0.1",debug=True)