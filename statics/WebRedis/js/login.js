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
    var uname = getElmtById('input-login-username').value;
    var pwd = getElmtById('input-login-passwd').value;
    var verify_in = getElmtById('input-login-verify').value;
    $.ajax({
        type: 'post',
        url: '/login/',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            username: uname,
            passwd: pwd,
            verify: verify_in
        },
        cache: false,
        success: function (reval) {
            return false;
            if (reval.data == 'ok') {
                return true;
                e.submit();
            } else {
                refreshVerify('img-login-verify');
                return false;
            }
        }
    })
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
function refreshVerify(id, src) {
    id = id || 'img-login-verify';
    src = src || (media_uri + "WebRedis/verify/verify.png?");
    getElmtById(id).onclick = function () {
        $.ajax({
            type: 'get',
            url: '/verify/',
            success: function () {
                document.getElementById(id).setAttribute('src', src + Math.random());
            }
        })
    }
}

/**
 * 页面加载完后执行
 */
$(document).ready(function () {
    // 显示遮罩和登录窗口
    showFormBox('form-box-login');
    // 验证码刷新
    refreshVerify('img-login-verify');
})