### 创建一个Git仓库

![image-20220901140211284](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901140211284.png)

### 安装Picgo，安装githubPlus插件

![image-20220901140448030](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901140448030.png)

### 获取一个token

以此打开 `Settings -> Developer settings -> Personal access tokens`，最后点击 `generate new token`；

![image-20220901140650141](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901140650141.png)

![image-20220901140825005](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901140825005.png)

点击生成最终会得到一个`token`。

`token` 生成，注意它只会显示一次，所以你最好把它复制下来到你的备忘录存好，方便下次使用，否则下次有需要重新新建；

### 配置Picgo

![image-20220901141132429](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901141132429.png)

按照图片参考配置即可，

`repo:`仓库名

`branch:`分支名

`token:`刚刚获取到的token

`path：`默认留空即可

`customUrl:`自定义域名，这个需要获取cdn，留空容易被墙。

### 获取cdn域名

当前使用的`cdn`是：

`https://cdn.staticaly.com/gh/用户名/仓库名/分支名`



可以通过`油猴`中的`Github加速插件或增强插件`来获取可靠的`cdn`。

随便进入一个我们上传到`Github`中的文件

![image-20220901141955215](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901141955215.png)

![image-20220901142149775](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901142149775.png)

选择一个可以正常显示文件的线路。根据其链接格式解析即可。

`https://raw.iqiq.io/1eexk/Image/master/image-20220901140211284.png)`

这个链接就可以解析为：

`https://raw.iqiq.io/用户名/仓库名/分支/图片名)`

这样我们`Picogo`中的自定义链接就可以填:

``https://raw.iqiq.io/用户名/仓库名/分支``

### 配合Typroa使用

`文件->偏好设置`

![image-20220901142456593](https://cdn.staticaly.com/gh/1eexk/Image/master/image-20220901142456593.png)
