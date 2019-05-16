# Cropper 插件教程 #
[cropper官网](<https://fengyuanchen.github.io/cropper/>)

[cropperjs下载地址](<https://github.com/fengyuanchen/cropperjs#getting-started>)

[cropper视频教程](<https://www.bilibili.com/video/av38512574/?p=15>)

## 插件导入 ##
```html
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    <link href="{% static 'cropper/css/cropper.min.css' %}" rel="stylesheet">
    <script src="{% static 'common/js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'cropper/js/cropper.min.js' %}"></script>
```

## 用法 ##
`new Cropper(image|canvas,options)`
- image 的宽必须设定为100%
- 界面分层
    - 容器
    - 画布
    - 图像
    - 裁剪框

## Options ##
- VIEWMODE
    > 定义裁剪器的视图模式
    - 0
        > 默认，无限制，裁剪框可以移出画布，画布可以移出容器
    - 1
        > 裁剪框不可以移出画布，画布可以移出容器
    - 2
        > 裁剪框不可以移出画布，画布不可以移出容器，
        画布尺寸如果大于容器，则按照长宽最小尺寸调整画布以适应容器，同时画布只能在未铺满容器方向移动
    - 3
        > 裁剪框不可以移出画布，画布尺寸如果超过容器，超出部分被容器遮盖，同时画布只能在超出端移动
  
        
- dragMode
    > 定义裁剪器的拖动模式
    - crop
        > 默认,单机拖动创建新的裁剪框,可拖动裁剪框     
    - move 
        > 移动画布,可拖动裁剪框       
    - none 
        >  仅拖动裁剪框
        
        
- initialAspectRatio
    > 定义裁剪框初始化比例，默认与画布比例相同，例：1/1，16/9
    
    
- aspectRatio
    > 裁剪框固定比例，默认自由比例，例：1/1，16/9
    
    
- data 
    > 默认`null`，当`autoCrop`设置为`true`时，调用`setData`初始化裁剪框
    
    
- preview
    > 裁剪预览容器，可以是容器的选择器`'.img-preview'`|`'#id_pre'`，
    容器对象`$('#id_pre')`，容器对象列表`$('.img-preview')`，
    容器的css样式必须包含`overflow: hidden;`，否则无法达到裁剪预览的效果 ,
    容器的长宽比最好与裁剪框一致。
    
    
- responsive
    > 默认`true`，当窗口大小改变时重新渲染裁剪器。
    
    
- restore 
    > 默认`true`，当窗口大小改变时是否保留裁剪区。
    
    
- checkCrossOrigin
    > 为非本地图片添加`crossOrigin`属性。
    
    
- checkOrientation
    > 检测图片的方向值，`rotatable`和`scalable`必须设置为`true`。
    
    
- modal
    > 默认`true`，是否显示遮罩。
    
  
- guides
    > 默认`true`，是否显示裁剪框虚线
        
        
- center
    > 默认`true`，裁剪框是否位于画布中间
    
    
- highlight
    > 默认`true`，裁剪区是否高亮显示
    
    
- background                                 
    > 默认`true`，容器马赛克是否显示 
    
    
- autoCrop                                 
    > 默认`true`，画布加载后是否自动显示裁剪框
    
    
- autoCropArea
    > 默认`0.8`，自定义裁剪框占画布的比例
    
    
- movable
    > 默认`true`，画布是否可移动
    
    
- rotatable 
    > 默认`true`，画布是否可旋转
    
    
- scalable 
    > 默认`true`，画布是否可缩放（测试无效） 
    
    
- zoomable 
    > 默认`true`，画布是否可缩放
    
      
- zoomOnTouch 
    > 默认`true`，画布是否可通过触摸缩放 
    
    
- zoomOnWheel 
    > 默认`true`，画布是否可通过鼠标滚动缩放
    
    
- wheelZoomRatio 
    > 默认`0.1`，画布缩放比例
    
    
- cropBoxMovable
    > 默认`true`，裁剪框是否可以拖动 
    
    
- cropBoxResizable
    > 默认`true`，裁剪框是否可以通过拖动改变大小
    
      
- toggleDragModeOnDblclick
    > 默认`true`，是否允许通过双击使得`dragMode`模式在`move`和`crop`直接切换
    
    
- minContainerWidth
    > 默认`200`，容器最小宽度
    
    
- minContainerHeight
    > 默认`100`，容器最小高度
    
    
- minCanvasWidth
    > 默认`0`，画布最小宽度
    
    
- minCanvasHeight
    > 默认`0`，画布最小高度
    
    
- minCropBoxWidth
    > 默认`0`，裁剪框最小宽度，大小相对的是页面，而非画布
    
    
- minCropBoxHeight
    > 默认`0`，裁剪框最小宽度，大小相对的是页面，而非画布
    
    
- cropBoxMovable
    > 默认`true`，裁剪框是否可以拖动 
    
     
- ready
    > 函数方法，裁剪器就绪事件
    
     
- cropstart
    > 函数方法，裁剪开始事件
    
      
- cropmove
    > 函数方法，裁剪移动事件
    
      
- cropend
    > 函数方法，裁剪结束事件
    
      
- crop
    > 函数方法，裁剪事件，裁剪框发生变化时候执行的函数
    
           
- zoom
    > 函数方法，裁剪器缩放事件
    
    
    
## Methods ##
> 方法，除了`setAspectRatio`, `replace` 和 `destroy`之外的其他方法都必须在`ready`事件以后调用         
- crop()
    > 函数方法，显示裁剪框
    ```demo1
        new Cropper(image, {
          autoCrop: false,
          ready() {
            // Do something here
            // ...
        
            // And then
            this.cropper.crop();
          },
        });
    ``` 


- reset()
    > 函数方法，重置裁剪框和画布
    
    
- clear()
    > 函数方法，删除裁剪框
    
    
- replace(url[, hasSameSize])
    > 函数方法，画布替换
    - url
        > 新图像的`url` 
    - hasSameSize
        > 默认`false`，是否保持旧图片的长宽比例


- enable()   
    > 启用cropper 
  
         
- disable()
    > 禁用cropper,锁定所有操作
  
            
- destroy() 
    > 销毁cropper，并删除预览
   
           
- move(offsetX[, offsetY]) 
    > 利用相对偏移量移动画布
    - offsetX
        > 数字，水平移动的尺寸，单位px，负数左移          
    - offsetY
        > 数字，缺省与offsetX相同，垂直移动的尺寸，单位px，负数上移 
        
                   
- moveTo(x[, y])  
    > 设置画布在容器的位置
    - x
        > 画布的左上角x坐标         
    - y
        > 画布的左上角y坐标        
     
     
             
- zoom(ratio)
    > 按比例缩放画布
    - ratio
        > 缩放比例，正数放大，负数缩小
        ```demo zoom
            cropper.zoom(0.1);
            cropper.zoom(-0.1);
        ```               


- zoomTo(ratio[, pivot])
    > 以`pivot`坐标为中心，将画布缩放至`ratio`倍   
    - ratio
        > 缩放比例，大于0的数字        
    - pivot
        > 相对于容器左上角的坐标，{ x: Number, y: Number }
    ```demo zoomTo
        cropper.zoomTo(1); // 1:1 (canvasData.width === canvasData.naturalWidth)
        
        const containerData = cropper.getContainerData();
        
        // Zoom to 50% from the center of the container.
        cropper.zoomTo(.5, {
          x: containerData.width / 2,
          y: containerData.height / 2,
        });
    ```   
    
             
- rotate(degree)
    > 画布旋转`degree`度 
    - degree
        > 旋转度数，正数右转，负数左转
    ```demo rotate
        cropper.rotate(90);
        cropper.rotate(-90);
    ```    
 
              
- rotateTo(degree)
    > 将画布旋转至`degree`度
 
             
- scale(scaleX[, scaleY])
    > 翻转图像，负数翻转，需要css2d支持，IE9+ 
    - scaleX
        > 默认`1`，为1则什么都不做，-1水平翻转
    - scaleY
        > 默认与`scaleX`相同，为1则什么都不做，-1垂直翻转
    ```demo scale
        cropper.scale(-1); // Flip both horizontal and vertical
        cropper.scale(-1, 1); // Flip horizontal
        cropper.scale(1, -1); // Flip vertical
    ```   
   
        
- scaleX(scaleX)
    > 水平缩放图像，负数翻转，绝对值小于1缩小，大于等于1放大  
    - scaleX
        >  默认`1`，为1则什么都不做，-1水平翻转

           
- scaleY(scaleY)
    > 垂直缩放图像，负数翻转，绝对值小于1缩小，大于等于1放大 
    - scaleY
        >  默认`1`，为1则什么都不做，-1水平翻转    
     
     
- getData([rounded])
    > 获取裁剪框基于原始画布的坐标，长宽，旋转角度以及水平和垂直缩放比例 
    - rounded
        > 默认`false`， 是否四舍五入
    - 返回值
        ```json objects
            {
            x: 左侧偏移量
            y: 顶部偏移量
            width: 宽
            height: 高
            rotate: 转角
            scaleX: 水平扭曲
            scaleY: 垂直扭曲
            }
        ```
        
               
- setData(data)
    > 设置裁剪框基于原始画布的坐标，长宽，旋转角度以及水平和垂直缩放比例
    - data
        > 同`getData([rounded])`返回值
        
                 
- getContainerData()
    > 获取容器大小数据
    - 返回值
        ```json objects
            {
            width: 容器当前宽度
            height: 容器当前高度
            }
        ```
           
                     
- getImageData()
    > 获取图片的位置、大小等数据
    - 返回值
        ```json objects
            {
                left: 左侧偏移量
                top: 顶部偏移量
                width: 图像宽
                height: 图像高
                naturalWidth: 图像自然宽度
                naturalHeight: 图像自然高度
                aspectRatio: 图片比例
                rotate: 图片转角
                scaleX: 水平缩放比例
                scaleY: 垂直缩放比例
            }
        ```
       
                 
- getCanvasData()
    > 获取画布的位置、大小等数据
    - 返回值 
    ```json objects
        {
            left: 画布左侧偏移量
            top: 画布顶部偏移量
            width: 画布宽
            height: 画布高
            naturalWidth: 画布自然宽度，只读
            naturalHeight: 画布自然高度，只读
        }
    ```      
    ```demo 
        const imageData = cropper.getImageData();
        const canvasData = cropper.getCanvasData();
        
        if (imageData.rotate % 180 === 0) {
          console.log(canvasData.naturalWidth === imageData.naturalWidth);
          // > true
        }
    ```    
    
   
      
- setCanvasData(data)     
    > 设置画布的位置、大小等数据
    - data
        ```json object
            {
                left: 画布左侧偏移量
                top: 画布顶部偏移量
                width: 画布宽
                height: 画布高(跟画布比例有关，基本只受width影响)
            }
        ```   
        
         
- getCropBoxData()
    > 获取裁剪框位置和大小数据
    - 返回值
    ```json objects
        {
            left: 左侧偏移量
            top: 顶部偏移量
            width: 宽
            height: 高
        }
    ```     
    
        
- setCropBoxData(data)  
    > 设置裁剪框位置和大小
    - data
        > 与`getCropBoxData()`的返回值相同
  
     
- getCroppedCanvas([options]) 
    > 根据新画布参数`options`,用新的画布绘制裁剪区的图像。
    - options
        ```options
            width: 输出画布的目标宽度
            height: 输出画布的目标高度
            minWidth: 输出画布的最小宽度，默认0
            minHeight: 输出画布的最小高度，默认0
            maxWidth: 输出画布的最大宽度，默认无限制
            maxHeight: 输出画布的最大高度，默认无限制
            fillColor: 透明区域填充色，默认透明，JPEG图像如果不设置则透明区域为黑色背景
            imageSmoothingEnabled: 图像是否平滑，默认`true`
            imageSmoothingQuality: 图像平滑质量，可选`low` ,`medium`,或`high`，默认`low` .
        ```
    - 返回值
        > HTMLCanvasElement
        - 方法
            - HTMLCanvasElement.toDataURL
            - HTMLCanvasElement.toBlob
    - 注意项
        -  画布长宽比例自动与裁剪框一致           
        -  JPEG图像如果不设置`fillColor`则透明区域为黑色背景           
        -  `maxWidth`和`maxHeight` 不设置可能导致得到空白图像        

    ```getCroppedCanvas
        cropper.getCroppedCanvas();
        
        cropper.getCroppedCanvas({
          width: 160,
          height: 90,
          minWidth: 256,
          minHeight: 256,
          maxWidth: 4096,
          maxHeight: 4096,
          fillColor: '#fff',
          imageSmoothingEnabled: false,
          imageSmoothingQuality: 'high',
        });
        
        // Upload cropped image to server if the browser supports `HTMLCanvasElement.toBlob`
        cropper.getCroppedCanvas().toBlob((blob) => {
          const formData = new FormData();
        
          formData.append('croppedImage', blob);
        
          // Use `jQuery.ajax` method
          $.ajax('/path/to/upload', {
            method: "POST",
            data: formData,
            processData: false,
            contentType: false,
            success() {
              console.log('Upload success');
            },
            error() {
              console.log('Upload error');
            },
          });
        });
    ```    
    
         
- setAspectRatio(aspectRatio)     
    > 设置裁剪框长宽比,见`Options`中关于`aspectRatio`的介绍
    - aspectRatio
        > 大于0的数字
        
        
- setDragMode([mode])  
    > 设置拖拽模式,见`Options`中关于`dragMode`的介绍
    - mode
        > `none`, `crop`, `move`,默认`none`    
        

## Events ##        
- ready
    > 图像加载完并准备好操作cropper时触发
    ```ready
        let cropper;
        
        image.addEventListener('ready', function () {
          console.log(this.cropper === cropper);
          // > true
        });

        cropper = new Cropper(image);
    ```    
    
                                                                                                                                                                                                                         
- cropstart
    > 画布或裁剪框开始变动时触发
    - 触发的事件
        - event.detail.originalEvent:
            - mousedown
                > 鼠标按下
            - touchstart
                > 触摸
            - pointerdown
                > 指针按下
        - event.detail.action:
            - crop
                > 创建新的裁剪框                
            - move
                > 画布移动                
            - zoom 
                > 触摸缩放画布              
            - e 
                > 调整裁剪框东侧               
            - w
                > 调整裁剪框西侧                
            - s
                > 调整裁剪框南侧                
            - n
                > 调整裁剪框北侧                
            - se
                > 调整裁剪框东南侧                
            - sw 
                > 调整裁剪框西南侧               
            - ne 
                > 调整裁剪框东北侧               
            - nw
                > 调整裁剪框西北侧                
            - all 
                > 移动裁剪框               
        
        ```event
            image.addEventListener('cropstart', (event) => {
              console.log(event.detail.originalEvent);
              console.log(event.detail.action);
            });
        ```   
        
                                                                                                                                                                                                                          
- cropmove 
    > 画布或裁剪框已经变动时触发
    - 触发的事件
        - event.detail.originalEvent:   
            - mousemove
                > 鼠标移动
            - touchmove 
                > 触摸移动
            - pointermove
                > 指针移动
        - event.detail.action:
            > 同`cropstart`                 
  
                                                                                                                                                                                                                                            
- cropend
    > 画布或裁剪框停止变动时触发  
    - 触发的事件
        - event.detail.originalEvent
            - mouseup
                > 鼠标抬起 
            - touchend
                > 停止触摸 
            - touchcancel
                > 触摸取消 
            - pointerup
                > 指针抬起
            - pointercancel
                > 指针取消 
                
        - event.detail.action 
            > 同`cropstart`     
      
      
                                                                                                                                                                                                                           
- crop 
    > 当画布或裁剪框变动时触发。
    - 事件
        - event.detail.x
        - event.detail.y
        - event.detail.width
        - event.detail.height
        - event.detail.rotate
        - event.detail.scaleX
        - event.detail.scaleY

    - 注意事项 
        - 当`autoCrop`参数设置为`true`的时候，将在`ready`事件前触发`crop事件`
        - 设置了`data `参数后，将在`ready`事件前触发`crop事件`
    
                                                                                                                                                                                                                           
- zoom 
    > 缩放画布时触发
    - event.detail.originalEvent
        > 事件
        - wheel 
            > 鼠标缩放                                                                                                                                                                                                                     
        - touchmove
            > 触摸移动                                                                                                                                                                                                                                
    - event.detail.oldRatio 
        > 旧画布长宽比                                                                                                                                                                                                                   
    - event.detail.ratio
        > 缩放后新画布长宽比
    ```zoom
        image.addEventListener('zoom', (event) => {
          // Zoom in
          if (event.detail.ratio > event.detail.oldRatio) {
            event.preventDefault(); // Prevent zoom in
          }
        
          // Zoom out
          // ...
        });
    ```
    

## No conflict ##
> 无抵触，如果必须使用相同命名空间的`cropper`，则可以调用`Cropper.noConflict`静态方法还原它
```No conflict
    <script src="other-cropper.js"></script>
    <script src="cropper.js"></script>
    <script>
      Cropper.noConflict();
      // Code that uses other `Cropper` can follow here.
    </script>
```


## Browser support##
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Opera (latest)
- Edge (latest)
- Internet Explorer 9+                                                                                                                                                                                                                                   