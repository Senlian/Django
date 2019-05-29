$('.article-action').on('click', function (event) {
    //window.event 兼容IE
    var e = event || window.event;
    var target = e.target || e.srcElement;
    var data;
    while (target !== this) {
        if (target.getAttribute('data-method')) {
            break;
        }

        target = target.parentNode;
    }
    if (target === this || target.disabled || target.className.indexOf('disabled') > -1) {
        return;
    }
    data = {
        // 方法
        method: target.getAttribute('data-method'),
        // 参数1
        option: target.getAttribute('data-option') || undefined,
        // 参数2
        secondOption: target.getAttribute('data-second-option') || undefined
    };

    switch (data.method) {
        case 'setTop':
            console.log('setTop');
            break;
        case 'setAllowreply':
            console.log('setAllowreply');
            break;
        case 'edit':
            console.log('edit');
            break;
        case 'delete':
            console.log('delete');
            break;
        case 'unfollow':
            console.log('unfollow');
            break;
        case 'focus':
            console.log('focus');
            break;
        default:
    }
})
