/**
 * Created by senlian on 2018/4/26.
 */
/******************************************************************/
/**
 * 打印消息
 * @param msg
 */
function print(msg) {
    console.log(msg);
}

/**
 * 获得Cookie值
 * @param name
 * @returns {*}
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = (cookies[i]).replace(' ', '');
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * 自动填充表单
 * @param id
 * @param json_data
 * @returns {*|jQuery|HTMLElement}
 */
function fillFormData(id, json_data) {
    var formEl = $(id);
    $.each(json_data, function(key, value) {
        formEl.find('[name=' + key +']').val(value);
    });
    return formEl;
}

/******************************************************************/
/**
 * 字符串操作
 */
/**
 * 去除字符串特定字符
 */
String.prototype.stripStr = function () {
    var str = this.toString() || this;
    if (!str || arguments.length < 1) {
        return str;
    }
    if (arguments.length === 1) {
        var reStr = arguments[0];
        return str.replace(eval(reStr), "");
    }
    return str;
}

/**
 * 去除字符串两端的特定字符，默认字符为空格
 */
String.prototype.strip = function () {
    var reStr = "/(^\\s*)|(\\s*$)/g";
    if (arguments.length === 1) {
        var reStr = "/(^(" + arguments[0] + ")*)|((" + arguments[0] + ")*$)/g";
    }
    return this.stripStr(reStr);
}

/**
 * 去除字符串左边特定字符，默认字符为空格
 */
String.prototype.lstrip = function () {
    var reStr = "/(^\\s*)/g";
    if (arguments.length === 1) {
        var reStr = "/(^" + arguments[0] + "*)/g";
    }
    return this.stripStr(reStr);
}

/**
 *  去除字符串右边特定字符，默认字符为空格
 */
String.prototype.rstrip = function () {
    var reStr = "/(\\s*$)/g";
    if (arguments.length === 1) {
        var reStr = "/(" + arguments[0] + "*$)/g";
    }
    return this.stripStr(reStr);
}

/**
 * 删除字符串中所有特定字符，默认字符为空格
 */
String.prototype.stripAll = function () {
    var reStr = "/(\\s*)/g";
    if (arguments.length === 1) {
        var reStr = "/(" + arguments[0] + "*)/g";
    }
    return this.stripStr(reStr);
}

/******************************************************************/
/**
 * 数组操作
 */
/**
 * 将拥有length属性的对象转成数组
 * @param obj
 * @returns {Array.<T>}
 */
function toArray(iterator) {
    // 从第0个元素开始截取
    return Array.prototype.slice.call(iterator, 0);
}

/**
 * 判断数组是否包含特定元素
 * @param item
 * @returns {boolean}
 */
Array.prototype.hasItem = function (item) {
    for (var x in this) {
        if (item === this[x]) {
            return true;
        }
    }
    return false;
}

/**
 * 数组添加元素
 * @param item
 * @returns {Array}
 */
Array.prototype.addNewItem = function (item) {
    if (!this.hasItem(item)) {
        this.push(item);
    }
    return this;
}

/******************************************************************/
/**
 * HTML元素操作
 */
/**
 * 通过ID，获取元素
 * @param id
 * @returns {Element}
 */
function getElmtById(id) {
    return document.getElementById(id);
}

/**
 * 元素窗口全屏
 */
HTMLElement.prototype.fullScreen = function () {
    this.style.width = document.documentElement.clientWidth + 'px';
    this.style.height = document.documentElement.clientHeight + 'px';
    this.style.left = 0;
    this.style.top = 0;
    this.style.display = 'block';
}

/**
 * 元素父体全屏
 */
HTMLElement.prototype.coverParent = function (el) {
    var el = el || this.parentNode;
    this.style.width = el.clientWidth + 'px';
    this.style.height = el.clientHeight + 'px';
    this.style.left = 0;
    this.style.top = 0;
    this.style.display = 'block';
}

/**
 * 元素窗口居中
 */
HTMLElement.prototype.autoCenter = function () {
    this.style.display = 'block';
    var bodyW = document.documentElement.clientWidth;
    var bodyH = document.documentElement.clientHeight;

    var elW = this.offsetWidth;
    var elH = this.offsetHeight;

    this.style.left = ( bodyW - elW  ) / 2 + 'px';
    this.style.top = ( bodyH - elH  ) / 2 + 'px';
}

/**
 * 元素父体居中
 */
HTMLElement.prototype.parentCenter = function () {
    this.style.display = 'block';
    var bodyW = this.parentNode.clientWidth;
    var bodyH = this.parentNode.clientHeight;

    var elW = this.offsetWidth;
    var elH = this.offsetHeight;
    this.style.position = 'absolute';
    this.style.left = ( bodyW - elW  ) / 2 + 'px';
    this.style.top = ( bodyH - elH  ) / 2 + 'px';
    this.style.zIndex = 99999;
}

/**
 * 元素添加属性
 * @param attrtype
 * @param attrname
 * @returns {HTMLElement}
 */
HTMLElement.prototype.ctAttribute = function (attrtype, attrname) {
    var attr = document.createAttribute(attrtype);
    // 属性名和值相同则跳过属性赋值
    if (attrtype != attrname) {
        attr.value = attrname;
    }
    this.setAttributeNode(attr);
    return this;
}

/**
 * 元素添加样式
 * @param styleJson
 * @returns {HTMLElement}
 */
HTMLElement.prototype.addStyle = function (styleJson) {
    var styleCss = "";
    for (var style in styleJson) {
        styleCss += style + ":" + styleJson[style] + ";";
    }
    this.ctAttribute("style", styleCss.rstrip(";"));
    return this;
}

/**
 * 添加子元素
 * @returns {*}
 */
HTMLElement.prototype.ctElement = function () {
    // 参数长度
    var argLength = arguments.length;
    if (argLength < 0) {
        return false;
    }
    // 元素类型
    var tagName = arguments[0];
    var newElement = document.createElement(tagName);
    if (argLength > 1) {
        for (var x = 1; x < argLength; x++) {
            var args = arguments[x];
            if (args.search("=") > 0) {
                var attrtype = args.split("=")[0];
                var attrName = args.split("=")[1];
                // 添加带id元素，判断id是否已经存在
                if ((attrtype.toLowerCase() === "id") && (getElmtById(attrName))) {
                    return getElmtById(attrName)
                }
                newElement.ctAttribute(attrtype, attrName);
            } else {
                newElement.ctAttribute(args, args);
            }
        }
    }
    this.appendChild(newElement);
    return newElement;
}

/**
 * 元素删除制定类名
 * @param cls
 * @returns {HTMLElement}
 */
HTMLElement.prototype.removeClassName = function (cls) {
    if (this.className == undefined) {
        this.removeAttribute("class");
        return;
    }
    var classNames = " " + this.className;
    var classArray = classNames.split(" ");
    var newClass = new Array();
    for (var x in classArray) {
        if (cls != classArray[x]) {
            newClass.addNewItem(classArray[x]);
        }
    }
    var newClassName = newClass.join(" ").strip();
    if (newClassName === "") {
        this.removeAttribute("class");
    }
    this.className = newClassName;
    return this;
}

/**
 * 获取元素类型名的大写
 * @returns {string}
 */
HTMLElement.prototype.tagNameUpperCase = function () {
    return this.tagName.toUpperCase();
}

/**
 * 元素添加文本内容
 * @param textContent
 * @returns {*}
 */
HTMLElement.prototype.setValue = function (textContent) {
    return this.innerHTML = textContent;
}

/******************************************************************/
/**
 * Node节点操作
 */
/**
 * 判断元素是否包含特定子元素
 * @param sonNode
 * @returns {boolean}
 */
Node.prototype.hasSonNode = function (sonNode) {
    var fathertNode = sonNode.parentNode;
    while (fathertNode) {
        if (fathertNode === this) {
            return true;
        }
        else {
            fathertNode = fathertNode.parentNode;
        }
    }
    ;
    return false;
}

/**
 * 判断元素是否拥有该类名
 * @param clsName
 * @returns {boolean}
 */
Node.prototype.hasClassName = function (clsName) {
    if (!this.hasAttribute("class")) {
        return false;
    }
    var classList = this.className.split(" ");
    for (var x in classList) {
        if (classList[x] === clsName) {
            return true;
        }
    }
    return false;
}

/**
 * 元素添加类名
 * @param clsName
 */
Node.prototype.addClassName = function (clsName) {
    var clsNames = this.className;
    if (this.hasClassName(clsName)) {
        return;
    }
    var clsAttLength = clsNames.length;
    if (clsAttLength > 0) {
        this.className = clsNames + " " + clsName;
    }
    else {
        this.className = clsName;
    }
}

/**
 * 元素添加类名，并将类名从其他元素中移除
 * @param clsName
 */
Node.prototype.addOnlyClassName = function (clsName) {
    var elist = document.getElementsByClassName(clsName);
    this.addClassName(clsName);
    for (var e in elist) {
        var em = elist[e];
        if (typeof(em) != "object") {
            continue;
        }
        if (!this.isEqualNode(em)) {
            em.removeClassName(clsName);
        }
    }
}

/**
 * 获取元素的所有子孙元素
 * @returns {Array}
 */
Node.prototype.getSonNodes = function () {
    var sonArray = new Array();
    if (!this.hasChildNodes()) {
        sonArray.addNewItem(this);
    }
    var sonNodes = this.children;
    if (sonNodes) {
        for (var x in sonNodes) {
            var sonNode = sonNodes[x];
            if (sonNode.nodeType != 1) {
                continue;
            }
            sonArray.addNewItem(sonNode);
            if (sonNode.hasChildNodes()) {
                sonNode.getSonNodes();
            }
        }
    }
    return sonArray;
}

