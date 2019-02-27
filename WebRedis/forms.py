from django import forms
from django.forms import ModelForm
from django.forms import widgets as wdgts
from django.forms import fields as flds

from .models import UserInfoHandler


class UserInfoHandlerForm(ModelForm):
    repwd = forms.CharField(label='确认密码', max_length=256,
                            widget=forms.PasswordInput(
                                    attrs={"id": "input-register-repwd",
                                           "class": "form-control input-lg",
                                           "name": "repwd",
                                           "type": "password",
                                           "autocomplete": "off",
                                           "requried": "requried",
                                           "oninvalid": "setCustomValidity('密码不能为空哟')",
                                           "oninput": "setCustomValidity('')",
                                           "placeholder": "请再次输入密码",
                                           }))

    verify = forms.CharField(label='验证码', max_length=8,
                            widget=forms.TextInput(
                                    attrs={"id": "input-register-verify",
                                           "class": "form-control input-lg",
                                           "name": "verify",
                                           "type": "text",
                                           "autocomplete": "off",
                                           "requried": "requried",
                                           "oninvalid": "setCustomValidity('请输入验证码')",
                                           "oninput": "setCustomValidity('')",
                                           "placeholder": "验证码",
                                           }))
    class Meta:
        # 对应数据模型
        model = UserInfoHandler
        # 自定义字段类型 （也可以自定义字段）
        field_classes = {
            "repwd": forms.CharField
        }
        # 显示字段， field= "__all__"表示展示所有
        fields = ["uid", "pwd", "repwd", "name", "phone", "email", "verify"]
        # exclude = [] # 排除字段
        # 提示信息，对model的verbose_name的重命名
        labels = {
            "uid": "用户名",
            "phone": "电话"
        }
        # 帮助提示信息
        # help_texts = None,
        # 自定义插件
        widgets = {'uid': wdgts.TextInput(attrs={"id": "input-register-uid",
                                                 "class": "form-control",
                                                 "name": "uid",
                                                 "requried": "requried",
                                                 "type": "text",
                                                 "autocomplete": "off",
                                                 "oninvalid": "setCustomValidity('用户名不能为空哟')",
                                                 "oninput": "setCustomValidity('')",
                                                 "placeholder": "请输入用户名",
                                                 "autofocus": "autofocus"
                                                 }),
                   'pwd': wdgts.PasswordInput(attrs={"id": "input-register-pwd",
                                                     "class": "form-control",
                                                     "name": "pwd",
                                                     "requried": "requried",
                                                     "type": "password",
                                                     "autocomplete": "off",
                                                     "oninvalid": "setCustomValidity('密码不能为空哟')",
                                                     "oninput": "setCustomValidity('')",
                                                     "placeholder": "请输入密码"
                                                     }),
                   'name': wdgts.TextInput(attrs={"id": "input-register-name",
                                                  "class": "form-control",
                                                  "name": "name",
                                                  "type": "text",
                                                  "autocomplete": "off",
                                                  "oninvalid": "setCustomValidity('姓名格式错误')",
                                                  "oninput": "setCustomValidity('')",
                                                  "placeholder": "请输入姓名"
                                                  }),
                   'phone': wdgts.NumberInput(attrs={"id": "input-register-phone",
                                                     "class": "form-control",
                                                     "name": "phone",
                                                     "type": "number",
                                                     "autocomplete": "off",
                                                     "oninvalid": "setCustomValidity('电话号码格式错误')",
                                                     "oninput": "setCustomValidity('')",
                                                     "placeholder": "请输入电话"
                                                     }),
                   'email': wdgts.EmailInput(attrs={"id": "input-register-email",
                                                    "class": "form-control",
                                                    "name": "email",
                                                    "type": "email",
                                                    "autocomplete": "off",
                                                    "oninvalid": "setCustomValidity('邮箱格式错误')",
                                                    "oninput": "setCustomValidity('')",
                                                    "placeholder": "请输入邮箱"
                                                    })
                   }
        # 自定义错误信息（整体错误信息from django.core.exceptions import NON_FIELD_ERRORS）

        error_messages = {
            # 定义整体错误信息
            'uid': {'unique': '该用户名已被注册！'},
            'phone': {'phone': '该电话号码已被注册！'},
            'email': {'unique': '该邮箱已被注册！'}
        }

        # 对哪些字段做本地化，如：根据不同时区显示数据
        localized_fields = ('ctime', 'mtime')
