from django import forms

class StockForm(forms.Form):

    stockCode = forms.CharField(max_length=100)
    companyName = forms.CharField(max_length=30)
    industry=forms.CharField(max_length=30)
    sector=forms.CharField(max_length=20)
    website=forms.CharField(max_length=100)
    about= forms.CharField(max_length=1000)
    singleLine=forms.CharField(max_length=300)
    upTrend=forms.CharField(max_length=300)
    downTrend=forms.CharField(max_length=300)
    lineTouch=forms.CharField(max_length=300)
    lineCross=forms.CharField(max_length=300)
    



