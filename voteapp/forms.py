from django import forms
#モデルクラスを呼出
from .models import People

#フォームクラス作成
class Votes_Form(forms.ModelForm):

    class Meta():

        model = People

        fields = ('MyName','GoodPerson','comment')


        labels = {'MyName':"名前",
                    'GoodPerson':"素敵さん",
                    'comment':"コメント",
        }
