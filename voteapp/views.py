
from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView

class VotesView(TemplateView):

    #初期変数定義
    def __init__(self):
        self.params = {"Message":"情報を入力してください。",
                        "vote":forms.Votes_Form(),
                    }

    #GET時の処理を記載
    def get(self,request):
        return render(request, "vote/votes.html",context=self.params)

    #POST時の処理を記載
    def post(self,request):
        if request.method == "POST":
            self.params["vote"] = forms.Votes_Form(request.POST)
            
            #フォーム入力が有効な場合
            if self.params["vote"].is_valid():
                #入力項目をデータベースに保存
                self.params["vote"].save(commit=True)
                self.params["Message"] = "入力情報が送信されました。"

        return render(request, "vote/votes.html",context=self.params)
