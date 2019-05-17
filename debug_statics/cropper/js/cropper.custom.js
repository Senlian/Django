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
        autoCropArea: 0.6,
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
    var uploadedImageName = username;
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
            // 方法二
            secondMethod: target.getAttribute('data-second-method') || undefined,
            // 绑定对象
            target: target.getAttribute('data-target') || undefined,
            // 参数1
            option: target.getAttribute('data-option') || undefined,
            // 参数2
            secondOption: target.getAttribute('data-second-option') || undefined
        };

        cropped = cropper.cropped;

        if (data.method) {
            // 此处用于设置数据，没用到
            if (typeof data.target !== 'undefined') {
                // 显示框元素获取
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
                        data.option.fillColor = '#FFFFFF';
                    }
                    break;

                default:
            }

            // 执行cropper实例的方法
            result = cropper[data.method](data.option, data.secondOption);

            switch (data.method) {
                case 'scaleX':
                    target.setAttribute('data-option', -data.option);
                    var tipTarget = target.getElementsByClassName('docs-tooltip')[0];
                    if (tipTarget) {
                        tipTarget.setAttribute("data-original-title", "cropper.scaleX(" + -data.option + ")");
                    }
                    break;

                case 'scaleY':
                    // X,Y翻转，将data-option值取反
                    target.setAttribute('data-option', -data.option);
                    var tipTarget = target.getElementsByClassName('docs-tooltip')[0];
                    if (tipTarget) {
                        tipTarget.setAttribute("data-original-title", "cropper.scaleY(" + -data.option + ")");
                    }
                    break;

                case 'disable':
                    target.setAttribute("data-method", "enable");
                    target.setAttribute("title", "Enable");
                    var tipTarget = target.getElementsByClassName('docs-tooltip')[0];
                    if (tipTarget) {
                        tipTarget.setAttribute("data-original-title", "cropper.enable()");
                        var iconTarget = tipTarget.getElementsByClassName('fa')[0];
                        if (iconTarget) {
                            iconTarget.setAttribute("class", "fa fa-unlock");
                        }
                    }
                    break;

                case 'enable':
                    target.setAttribute("data-method", "disable")
                    target.setAttribute("title", "Disable")
                    var tipTarget = target.getElementsByClassName('docs-tooltip')[0];
                    if (tipTarget) {
                        tipTarget.setAttribute("data-original-title", "cropper.disable()");
                        var iconTarget = tipTarget.getElementsByClassName('fa')[0];
                        if (iconTarget) {
                            iconTarget.setAttribute("class", "fa fa-lock");
                        }
                    }
                    break;

                case 'getCroppedCanvas':
                    if (result) {
                        // 下载
                        if (!download.disabled) {
                            // 设置下载链接
                            download.download = uploadedImageName;
                            // JPEG不支持透明， JPEG转为PNG格式
                            download.href = getRoundedCanvas(result).toDataURL(uploadedImageType ? uploadedImageType === 'image/jpeg' : 'png');
                        }
                        if (typeof data.secondMethod !== 'undefined' && data.secondMethod == 'saveProtrait') {
                            var href = window.document.location.href
                            var host = href.substring(0, href.indexOf(window.document.location.pathname));
                            var protrait = result.toDataURL(uploadedImageType);
                            var index = parent.layer.getFrameIndex(window.name);
                            $.ajax({
                                url: host + postPath,
                                type: 'post',
                                dataType: 'json',
                                data: {'protrait': protrait},
                                success: function (e) {
                                    if (e.is_save === true) {
                                        layer.confirm('头像修改成功!', {yes:function () {
                                                parent.layer.close(index);
                                            }});

                                    } else {
                                        layer.alert('头像修改失败，请稍后再试!', {icon: 5, title: "错误"});
                                    }
                                    ;
                                },
                                error: function (e) {
                                    console.log('eee');
                                }
                            })
                        }
                    }
                    break;

                case 'destroy':
                    cropper.destroy();
                    cropper = null;

                    if (uploadedImageURL) {
                        // 释放URL
                        URL.revokeObjectURL(uploadedImageURL);
                        uploadedImageURL = '';
                        image.src = originalImageURL;
                    }
                    break;

                default:
            }

            // 此处用于将获得的数据显示到显示框，没用到
            if (typeof result === 'object' && result !== cropper && input) {
                try {
                    input.value = JSON.stringify(result);
                } catch (e) {
                    console.log(e.message);
                }
            }
        }
    };

    // 键盘方向键监听
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

    // 图片上传按钮
    var inputImage = document.getElementById('inputImage');
    // 图片上传
    if (URL) {
        // 监听图片上传框的值变化
        inputImage.onchange = function () {
            var files = this.files;
            var file;

            if (cropper && files && files.length) {
                file = files[0];
                // 图片格式判断
                if (/^image\/\w+/.test(file.type)) {
                    uploadedImageType = file.type;
                    uploadedImageName = file.name;
                    if (uploadedImageURL) {
                        URL.revokeObjectURL(uploadedImageURL);
                    }
                    // 创建一个仅存在于当前文件的URL
                    protrait.src = uploadedImageURL = URL.createObjectURL(file);
                    // cropper.destroy();
                    // cropper = new Cropper(protrait, options);
                    // 图像替换，onlyColorChanged设置是否按照原图比例显示， 默认false。
                    cropper.replace(uploadedImageURL, false);
                    inputImage.value = null;
                } else {
                    layer.tips('请上传一张图片。', this, {tips: 1});
                    // window.alert('Please choose an image file.');
                }
            }
        };
    } else {
        // 如果浏览器不支持URL，则不支持更改头像
        inputImage.disabled = true;
        inputImage.parentNode.className += ' disabled';
    }
};

// Canvas 绘制圆形图片
function getRoundedCanvas(sourceCanvas) {
    var canvas = document.createElement('canvas');
    var context = canvas.getContext('2d');
    var width = sourceCanvas.width;
    var height = sourceCanvas.height;

    canvas.width = width;
    canvas.height = height;

    // 设置图片是否平滑
    context.imageSmoothingEnabled = true;

    context.drawImage(sourceCanvas, 0, 0, width, height);
    // 组合方式
    context.globalCompositeOperation = 'destination-in';

    // 图层透明度
    // context.globalAlpha = 0.9;
    context.beginPath();
    // 绘制圆形
    context.arc(width / 2, height / 2, Math.min(width, height) / 2, 0, 2 * Math.PI, true);
    context.fill();
    return canvas;
};