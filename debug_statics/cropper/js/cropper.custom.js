window.onload = function () {
    // 严格模式
    'use strict';
    // 提示框方式显示title
    $('[data-toggle="tooltip"]').tooltip();
    var URL = window.URL || window.webkitURL;
    // 获得头像元素
    var protrait = document.getElementById('id_protrait');
    // 获得actions按钮容器
    var actions = document.getElementById('actions');
    // 实例化cropper
    var options = {
        // 视图模式
        ViewMode: 2,
        // 拖拽模式
        dragMode: 'crop',
        // 裁剪框初始化比例
        // initialAspectRatio:3/1,
        // 裁剪框固定比例
        aspectRatio: 1 / 1,
        // 预览容器
        preview: '.img-preview',
        // 宽口尺寸变化重新渲染裁剪区
        responsive: true,
        // 宽口尺寸变化保留裁剪区
        restore: true,
        // 显示遮罩
        modal: true,
        // 裁剪框虚线显示
        guides: true,
        // 裁剪框位于画布中间
        center: true,
        // 裁剪区高亮显示
        highlight: true,
        // 容器马赛克是否显示
        background: true,
        // 画布加载后是否自动显示裁剪框
        autoCrop: true,
        // 自定义裁剪框占画布的比例
        autoCropArea: 0.8,
        // 画布可移动
        movable: true,
        // 画布缩放比例
        wheelZoomRatio: 0.1,
        // 裁剪框是否可以拖动
        cropBoxMovable: true,
        // 裁剪框是否可以通过拖动改变大小
        cropBoxResizable: true,
    };
    var cropper = new Cropper(protrait, options);
    var originalImageURL = protrait.src;
    var uploadedImageType = 'image/jpeg';
    var uploadedImageName = 'cropped.jpg';
    var uploadedImageURL;

    // 按钮点击事件
    actions.querySelector('.docs-buttons').onclick = function (event) {
        var e = event || window.event;
        var target = e.target || e.srcElement;
        var cropped;
        var result;
        var input;
        var data;

        if (!cropper) {
            return;
        }

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
            // 绑定对象
            target: target.getAttribute('data-target'),
            // 参数1
            option: target.getAttribute('data-option') || undefined,
            // 参数2
            secondOption: target.getAttribute('data-second-option') || undefined
        };

        cropped = cropper.cropped;

        if (data.method) {
            if (typeof data.target !== 'undefined') {
                input = document.querySelector(data.target);

                if (!target.hasAttribute('data-option') && data.target && input) {
                    try {
                        data.option = JSON.parse(input.value);
                    } catch (e) {
                        console.log(e.message);
                    }
                }
            }

            switch (data.method) {
                case 'getCroppedCanvas':
                    try {
                        data.option = JSON.parse(data.option);
                    } catch (e) {
                        console.log(e.message);
                    }

                    if (uploadedImageType === 'image/jpeg') {
                        if (!data.option) {
                            data.option = {};
                        }

                        data.option.fillColor = '#fff';
                    }

                    break;

                default:
            }

            result = cropper[data.method](data.option, data.secondOption);

            switch (data.method) {
                case 'scaleX':
                case 'scaleY':
                    // X,Y翻转，将data-option值取反
                    target.setAttribute('data-option', -data.option);
                    break;

                case 'getCroppedCanvas':
                    // 生成模态框
                    if (result) {
                        // Bootstrap's Modal
                        $('#getCroppedCanvasModal').modal().find('.modal-body').html(result);

                        if (!download.disabled) {
                            download.download = uploadedImageName;
                            download.href = result.toDataURL(uploadedImageType);
                        }
                    }

                    break;

                case 'destroy':
                    cropper.destroy();
                    cropper = null;

                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                        uploadedImageURL = '';
                        image.src = originalImageURL;
                    }

                    break;

                default:
            }

            // 得到的数据显示在显示区
            if (typeof result === 'object' && result !== cropper && input) {
                try {
                    input.value = JSON.stringify(result);
                } catch (e) {
                    console.log(e.message);
                }
            }
        }
    };

    // 键盘事件监听
    document.body.onkeydown = function (event) {
        var e = event || window.event;

        if (e.target !== this || !cropper || this.scrollTop > 300) {
            return;
        }

        switch (e.keyCode) {
            case 37:
                // 左
                e.preventDefault();
                cropper.move(-1, 0);
                break;

            case 38:
                // 上
                e.preventDefault();
                cropper.move(0, -1);
                break;

            case 39:
                // 右
                e.preventDefault();
                cropper.move(1, 0);
                break;

            case 40:
                // 下
                e.preventDefault();
                cropper.move(0, 1);
                break;
        }
    };

    // Import image
    var inputImage = document.getElementById('inputImage');

    if (URL) {
        inputImage.onchange = function () {
            var files = this.files;
            var file;

            if (cropper && files && files.length) {
                file = files[0];

                if (/^image\/\w+/.test(file.type)) {
                    uploadedImageType = file.type;
                    uploadedImageName = file.name;
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                    }
                    protrait.src = uploadedImageURL = URL.createObjectURL(file);
                    // cropper.destroy();
                    // cropper = new Cropper(protrait, options);
                    cropper.replace(uploadedImageURL, false);
                    inputImage.value = null;
                } else {
                    window.alert('Please choose an image file.');
                }
            }
        };
    } else {
        inputImage.disabled = true;
        inputImage.parentNode.className += ' disabled';
    }
};
