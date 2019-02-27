/**
 * Created by Administrator on 2018/4/26.
 */
/**
 * 显示表单盒子，并新建弹出遮罩
 * @param id
 * @returns {Element}
 */
function showFormBox(id) {
    var uiMask = document.body.ctElement("div", "id=mask", "class=ui-mask");
    var formBox = getElmtById(id);
    uiMask.fullScreen();
    uiMask.style.zIndex = 8000;
    formBox.autoCenter();
    formBox.style.zIndex = uiMask.style.zIndex + 1;
    return formBox
}

function submitForm(e) {
    var postData = new FormData(e);
    postData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    $.ajax({
        type: 'post',
        url: url_register,
        dataType: 'JSON',
        data: postData,
        processData: false,                // jQuery不要去处理发送的数据
        contentType: false,                 // 告诉jQuery不要去设置Content-Type请求头
        success: function (responseData) {
            if (responseData.is_ok) {
                // 弹窗遮罩
                var formMask = e.parentNode.parentNode.ctElement("div", "id=form-mask", "class=ui-mask");
                formMask.coverParent(e.parentNode.parentNode);
                formMask.style.zIndex = 9000;

                // 设置成功提示
                var alertNode = e.parentNode.ctElement('div', 'id=myAlert', 'class=close alert alert-success', 'data-dismiss=alert');
                alertNode.innerHTML = '<a href="#" class="close" data-dismiss="alert">&times;</a><strong>恭喜，注册成功！</strong>';
                alertNode.parentCenter();

                // 主页跳转
                alertNode.onclick = function () {
                    window.location.href = url_index;
                }
            } else {
                for (var name in responseData) {
                    var inputId = 'input-register-' + name;
                    var errorId = 'input-error-' + name;
                    var inputElement = getElmtById(inputId);

                    if (!inputElement) {
                        continue;
                    }
                    var errorElement = getElmtById(errorId);

                    if (errorElement) {
                        errorElement.innerHTML = responseData[name];
                    } else {
                        var newLable = document.createElement('lable');
                        //newLable.setAttribute('class', 'label label-warning clearfix');
                        newLable.setAttribute('id', errorId);
                        newLable.innerHTML = '* ' + responseData[name];

                        inputElement.parentNode.parentNode.insertBefore(newLable, inputElement.parentNode);
                    }
                }
                return false;
            }
        },
        error: function (responseData) {
            print((responseData));
        }
    });
    print('adfasdf')
    autofreshVerify()
    return false;
}

/**
 * 隐藏盒子
 * @param id
 */
function hideFormBox(id) {
    getElmtById('mask').style.display = 'none';
    getElmtById(id).style.display = 'none';
}

/**
 * 刷新验证码
 * @param id
 * @param src
 */
function refreshVerify(id) {
    var id = id || 'img-register-verify';
    var el = getElmtById(id);
    var src = el.getAttribute('src');
    el.onclick = function () {
        $.ajax({
            type: 'get',
            url: '/verify/',
            contentType: false,
            success: function () {
                el.setAttribute('src', src + '?' + Math.random());
            },
            error: function () {
                print('error');
            }
        })
    }
}

/**
 * 刷新验证码
 * @param id
 * @param src
 */
function autofreshVerify(id) {
    var id = id || 'img-register-verify';
    var el = getElmtById(id);
    var src = el.getAttribute('src');

        $.ajax({
            type: 'get',
            url: '/verify/',
            contentType: false,
            success: function () {
                el.setAttribute('src', src + '?' + Math.random());
            },
            error: function () {
                print('error');
            }
        })

}

/**
 * 页面加载完后执行
 */
$(document).ready(function () {
    // 显示遮罩和登录窗口
    showFormBox('form-box-register');
    // 验证码刷新
    refreshVerify('img-register-verify');
})