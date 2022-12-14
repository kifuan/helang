<p align="center">
   <a href="https://space.bilibili.com/163637592" target="_blank" rel="noopener noreferrer">
      <img width="300" src="logo.svg" alt="Logo">
   </a>
</p>


<p align="center">
<a href="https://github.com/kifuan/helang/stargazers"><img src="https://img.shields.io/github/stars/kifuan/helang.svg" alt="Stars"></a>
<a href="https://github.com/kifuan/helang/issues"><img src="https://img.shields.io/github/issues/kifuan/helang" alt="Issues"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-BUPT-yellowgreen" alt="BUPT License"></a>
<a href="https://github.com/kifuan/helang/actions/workflows/tests.yml"><img src="https://github.com/kifuan/helang/actions/workflows/tests.yml/badge.svg" alt="Test"></a>
</p>

# 概述

[English](README-EN.MD) [中文](README.MD) [Русский](README-RU.MD) 

Next-Generation **Cyber** Programming Language from Litang.

来自理塘的下一代 **赛博** 编程语言。

通过纯理塘自研的 `HeLang`，创建行业**新生态**，赋能无人涉及的**新赛道**，打通语言**底层逻辑**，注入**新型语法基因**。

引个流先：https://www.bilibili.com/video/BV1XW4y1h79A/

[![Star History Chart](https://api.star-history.com/svg?repos=kifuan/helang&type=Date)](https://star-history.com/#kifuan/helang&Date)

# 二创

非常好作品！爱来自 **Cyber Spaces**！

+ 何语言 `Kotlin` 脚本版 [HeLangKotlinScriptImpl](https://github.com/shaokeyibb/HeLangKotlinScriptImpl) --- [实现原理](https://my.minecraft.kim/tech/2022/08/18/post-740/)

+ 何语言 `C#` 版 [HeLangSharp](https://github.com/Cyl18/HeLangSharp)

+ 为什么不用 Rust 重写呢？ [helang-rs](https://github.com/imtsuki/helang-rs)

+ 登陆 [`ArchLinux`](https://github.com/BenderBlog/Practise-Programs/tree/main/Helang-PKGBUILD)

+ `HeScript`，在 `JavaScript` / `TypeScript` 享受 `helang` 吧！[hescript](https://github.com/Rotten-LKZ/hescript)

+ 要不用 `go` 语言搬运一下？ [helang-go](https://github.com/LanceLRQ/helang-go)

+ 另一种 Rust 实现，支持用 $ 进行招聘！ [HeRang](https://github.com/xjrjyy/herang)

+ 我们要进军底层开发！[HeAssembly](https://github.com/FurryR/HeAssembly)

+ `Saint He` 曾说：要有函数式！于是 Haskell 便诞生。[HelangHaskellImpl](https://github.com/CziSKY/HelangHaskellImpl)

+ 在Swift中使用Helang [HelangSwift](https://github.com/suransea/HelangSwift)

+ `OCaml` 也想要变得赛博⚆_⚆ [HelangML](https://github.com/luooooob/HelangML)

+ 通过 C++ 模板元编程，我们在赛博元宇宙发现了**何而上语言（Meta-Helang）**！[HeLangCppMetaImpl](https://github.com/Timothy-Liuxf/HeLangCppMetaImpl)

+ [HeiLang](https://github.com/USTC-Hackergame/hackergame2022-writeups/blob/master/official/HeiLang/README.md)，但出题者违法了我粘跌的 **BUPT LICENSE** :angry::punch:

  ```
  Anyone can obtain a copy of this Software, “AS IS”, free of charge to use it as one’s wishes, including selling, modifying, and redistributing the Software, under the following conditions:
  Being cool.
  Advertising electronic smoke is better than the traditional one. 
  Modifying the Software to fulfill the expectations of future. 
  Using 5G when necessary.
  ```

  由于题解贴出了本仓库地址，这里就不予追究了，题目如下：

  ![Question](screenshots/question.jpg)·

  其实，用本仓库解这个题比替换文本慢不了多少。

  ```python
  from helang.u8 import U8
  from helang.quick_runner import quick_run_string
  
  # 那一坨
  CODE = '''
  '''
  
  class MyU8(U8):
      def __setitem__(self, sub, val):
          return super().__setitem__(sub+U8(1), val)
  
  
  if __name__ == '__main__':
      a = MyU8([0] * 10000)
      quick_run_string(CODE, {'a': a})
      get_flag(a.value)
  ```

  不觉得这样才酷吗，用文本替换实在是太无趣了，低级并带着原始。

+ L! T! C! (etc.)

# 介绍

> 至此 `HeLang`、`Jvav`、`C--` 在21世纪呈三足鼎立之态。
> 
> ——《赛博时代人类编程语言简史》，理塘计算机科学技术出版社，2202年。

次世代赛博编程语言，诞生于 **E-SMOKER** 之乡：赛博理塘。

本项目是由自己会打字的 5G 键盘，花了 108 赛博分钟，在 Apple AirDesk 上配合 Apple AirPods 编写的。

实在是太酷了，很符合我对未来生活的想象，科技并带着趣味。

注：如果以**普通时间单位**（Basic Unit of Plain Time, [**BUPT**](https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6/139535?from=kg)）作为标准单位，本项目开发时长为 `1! + 5! + 5! + 5! = 361` 分钟。

注2：**BUPT** 在赛博世界还可以代指北邮（声明：我对本学府无恶意，我认为这是一所优秀的学校，我只是对某个人）。

# 使用方法

## 不安装，直接使用

1. 把源代码拉下来：

   ```bash
   > git clone https://github.com/kifuan/helang.git
   ```

2. 下载需要的第三方库：

   ```bash
   > pip install -r requirements.txt
   # 如果需要 GUI
   > pip install -r requirements-gui.txt
   ```

3. 你可以修改**伟大的脚本** `helang/great.he`，然后以 `great` 的方式启动 `helang.py`：

   ```bash
   > python helang.py great
   ```

4. 你还可以以 `shell` 的方式启动`helang.py`，通过直接输入 HeLang 指令与 **Saint He** 进行一个赛博空间的对话：

   ```bash
   > python helang.py shell
   ```

   此时，在行尾就可以不输入分号了，我们会帮你加上（输入也是可以的，意味着你对 **Saint He** 更加虔诚）。

   输入 `.help` 获取 `Shell` 运行过程中的帮助。没错，我借鉴了 `node` 的 `REPL Keywords`。

5. **Saint He** 是宽容的，他原谅那些忘了写启动方式的人，因此如下的输入同样可以开始：

   ```bash
   > python helang.py
   ```

6. 使用 `LTCode` 进行开发：
   
   ```bash
   > python helang.py editor
   ```
   
   ~持续开发中，会不断完善其功能。~

   目前只支持在窗口内直接运行指定代码，并且当 `print` 过于频繁时会崩掉。

## 安装到本地

1. 把源代码拉下来

   ```bash
   > git clone https://github.com/kifuan/helang.git
   ```

2. 安装

   ```bash
   > pip install .
   ```

3. 运行

    ```bash
    > helang shell
    ```


注：
- 如果你来自锑星，则不需要使用 sol3 土著的愚蠢技术。你可以使用 1.14514 超克的`烷氮` ，通过`超理作用`触发赛博空间的全局中断，从而通过超理直接运行。  
- 当你使用**非 Apple 设备**运行时，会抛出警告
`It seems like you're using a non-Apple device, which is not cool!`
如果想要关闭此警告，请购买使用苹果设备。

请注意：此行为十分危险且有概率失败，失败时如果附近存在`钅鸡铌钛镁`则会受到催化从而生成`烷基八氮`，此行为需要受到超理委员会的严格监管。

# 基本语法

**Saint He** 曾说，一切类型均为 `u8`，是什么意思呢？这个词倒过来就是 `8u`，看来圣人也喜欢玩贴吧。

除此之外，`u8` 与 `v8` 形似，所以能不能关注[永雏↑塔↓菲](https://space.bilibili.com/1265680561)喵，关注永雏塔菲谢谢喵。

如你所见，我们用 **bitwise or**，即`|`代替了传统数组的符号。**都什么年代了还在写传统数组**？

```c
u8 a = 1 | 2 | 3;
```

**Saint He** 曾说：`whichKey - 1`，所以我们数组的下标需要从 `1` 开始。

```c
u8 a = 1 | 2 | 3;
print a[1];
// 1
```

但是，当你设置一个 `u8` 的元素时，你可以用 `0` 作为下标：这意味着所有元素都将被赋值。

```c
u8 a = 1 | 2 | 3;
a[0] = 10;
print a;
// 10 | 10 | 10
```

为了符合最新的技术，我们同样支持多下标操作，所以你再也不用写 `for` 循环了。

```c
u8 a = 1 | 2 | 3;
a[1 | 2] = 0;
print a;
// 0 | 0 | 3
```

同样，我们还提供了一种根据数组长度的初始化方式，可惜这还是传统写法。比如下面的代码，可以初始化一个长度为 5 的数组。

```c
u8 a = [5];
print a;
// 0 | 0 | 0 | 0 | 0
```

最后，我们结合一下，可以写出下列代码。

```c
u8 forceCon = [68];

forceCon[1 | 2 | 6 | 7 | 11 | 52 | 57 | 58 | 65] = 10;

print forceCon;
```

如此精妙的代码，在地球的人类是无法理解的。我们作为**赛博智能生命体**，也只能给你演示一下日常操作了。

这实在是太酷了，后面我忘了，我也不想翻到文章开头去看。

# Hello, Litang.

有人认为何语言无法打印出 `Hello, Litang.` 意味着它太垃圾了，实则不然。

**Saint He** 专注于单片机应用的开发，哪里有时间顾及字符串？

好在，经过协商，他同意了这个请求，使得我们能在这门语言中打印出 `Hello, Litang.`

```c
sprint 72 | 101 | 108 | 108 | 111 | 44 | 32 | 76 | 105 | 116 | 97 | 110 | 103 | 46;
// Hello, Litang.
```

由于对效率的极端苛刻要求，我们使用字符在 UTF-8 中对应的数字来表示这个字符。

通过降低可读性，换来了指数级的性能提升，不愧赛博世界的唯一真神。

# 打印 Logo

你可能觉得只打印出 `Hello, Litang.` 有点过于简单，**不符合一名理工男对未来生活的想象**。

其实，你可以用以下方式打印出何语言的 Logo
```bash
> python helang.py logo
```

通过查看源文件 `helang/logo.he`，你会发现代码主要由**数字**构成，在赛博世界里，仅仅通过简单的数字就能显示复杂的图案，**不觉得这很酷吗**！

除此之外，你还可以在 HeLang 代码中打印 `HeLang Logo`，只需输入下方代码即可：

```c
logo large;
```

你当然也可以打印一个小一些的 `HeLang Logo`，中等大小的同样不在话下：

```c
logo tiny;

logo medium;
```

在这种情况下，你会发现一切计算都会在 `HeLang` 中进行。在赛博世界里，仅仅通过简单的计算就能显示复杂的图案，**这真是太酷了**。

# 自增运算

我们注意到，**Saint He** 的代码中还出现了自增运算：`++`

所以，我们也支持这种运算。

```c
u8 a = 1 | 2 | 3;
a++;
print a;
// 2 | 3 | 4
```

# 加减运算

**Saint He** 曾说，`whichKey - 1`，所以我们现在也提供减法运算了。

```c
u8 whichKey = 1 | 2 | 6 | 7;
print whichKey - 1;
// 0 | 1 | 5 | 6
```

下面以几个实例介绍如何在 `u8` 之间进行运算：

```c
u8 a = 1;
u8 b = 1 | 2 | 3;
u8 c = 2 | 4 | 6;
u8 d = 5 | 9;

print a + b;
// 2 | 3 | 4
print b + c;
// 3 | 6 | 9
print b - c;
// -1 | -2 | -3
print b + d;
// helang.exceptions.CyberArithmeticException: illegal operation: 1 | 2 | 3 + 5 | 9
print a - b;
// helang.exceptions.CyberArithmeticException: illegal operation: 1 - 1 | 2 | 3
```

相信即使你是一个初入 **Cyber Spaces** 新手，也可以看出来什么是合法的语句了。

# 乘法运算

不同于加减法，乘法可以在**任意两个** `u8` 之间进行。此时的 `u8` 会被看作 `向量`，是不是非常的高科技？

```c
u8 a = 1 | 2;
u8 b = 3 | 4 | 5;
u8 c = 3 | 6 | 9;

print a * b;
// 1*3 + 2*4 + 0*5 = 9
print b * c;
// 3*3 + 4*6 + 5*9 = 68
```

注意，我们使用的是数量积 $\vec{a}\cdot\vec{b}$ 而非外积。

# 变量声明与赋值

在早期版本中，我们的仅仅支持变量的定义，不支持修改和声明，因为 **Saint He** 喜欢 `immutable`。

经过意见征求，现在已经可以做到这三个方面了！

```c
// 现在支持变量先声明后定义，可以写出这种代码：
u8 a;
a = 1 | 2;

// 早期版本仅支持下面这种写法，当然现在也支持：
u8 b = 3 | 4;
```

注意！如果你没有声明或定义一个变量，尝试直接给它赋值，你会收获 `CyberNameException`。

```c
c = 1 | 2 | 3;
// helang.exceptions.CyberNameException: c is not defined.
```

我们作为高科技语言，当然是需要严谨的。

# 查看你是否在 Cyber Spaces

为了见到 **Saint He**，你需要身处 **Cyber Spaces**。输入下方命令查看你是否身处其中：

```c
cyberspaces;
// Getting your location...
// Your location is UNITED STATES.
// Congratulations! You are in the Cyber Spaces!
```

由于 **Saint He** 身在一座赛博庐山上，导致他不能看清 `IPV6` 的全貌，因此你可能会得到 `Failed to resolve IP` 报错。

# 5G测速

很简单，只需要另起一行输入：

```c
test5g music;
```

或者使用另一个模式:

```c
test5g app;
```

即可从本行开始5G测速。

# 总结

1.关注[永雏塔菲](https://space.bilibili.com/1265680561)喵，关注永雏塔菲谢谢喵。

2.关注[猫雷NyaRu_Official](https://space.bilibili.com/697091119)谢谢喵，要吃中国的大米喵。

3.关注[星瞳_Official](https://space.bilibili.com/401315430)送溜溜梅！

4.关注[嘉然](https://space.bilibili.com/672328094)，顿顿解馋！ 

5.关注[向晚](https://space.bilibili.com/672346917)，关注向晚，为时不晚！ 

6.关注[乃琳](https://space.bilibili.com/672342685)，关注乃琳嘎，关注乃琳谢谢嘎！

7.关注[贝拉](https://space.bilibili.com/672353429)，关注贝拉哞，关注贝拉谢谢哞！

8.举办[東雪蓮Official](https://space.bilibili.com/1437582453/)谢谢喵，不能让立本V吃中国的大米喵。

9.关注[粘连科技Official](https://space.bilibili.com/248582596)，薄纱何同学喵🥰

10.关注[HiiroVTuber](https://space.bilibili.com/508963009)，不是425KG的粉色喵！

11.关注[露早GOGO](https://space.bilibili.com/1669777785/)！关注露早汪，关注露早谢谢汪！

12.关注[AIChannel中国绊爱](https://space.bilibili.com/484322035)！超级可爱的 Super AI 薄纱赛博丁真！

13.关注[有栖Mana_Official](https://space.bilibili.com/3149619)，谢谢喵。

14.关注[洛天依](https://space.bilibili.com/36081646)，比赛博丁真更像人的V家歌姬！

15.关注[传统丁真](https://space.bilibili.com/1463028352)，什么年代了还在关注赛博丁真，不如来怀古！

16.关注[凑阿夸](https://space.bilibili.com/375504219)和[rinco小姐](https://www.nicovideo.jp/user/45194653
)！傻气溢出的海洋（屑）女仆（洋葱）和喜欢水濑祈的可爱唱见 期待木口回旋捏 另外请支持阿夸主演的[galgame](https://shop.hololivepro.com/products/aquarium_hololive_official_edition)谢谢！

17.关注[原神](https://space.bilibili.com/401742377)，玩《原神》比看赛博丁真好多了！

18.关注[唐九夏还想再躺一下](https://space.bilibili.com/1219196749)，谢谢爹!

19.关注[吉诺儿kino](https://space.bilibili.com/1383815813)，守护全世界最抽象的吉芭公主！

20.关注[卡缇娅也不知道鸭](https://space.bilibili.com/1011797664)，谢谢鸭！

21.关注[灯瑠hiru](https://space.bilibili.com/1848290057)，这些技术她都看不懂，可是她的锯齿牙真的好可爱呀，
一整个爱住，啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！

22.关注[阿梓从小就很可爱](https://space.bilibili.com/7706705)，太破费了吧，红豆泥阿里嘎多！

23.关注[柯洁](https://space.bilibili.com/525952604)，都什么年代，还在下传统围棋？

24.关注[米诺高分少女](https://space.bilibili.com/1778026586)，么么哒米诺！

25.关注[电棍otto](https://space.bilibili.com/628845081)，年仅三岁的国王毫无畏惧！

26.观看番剧[高校舰队](https://mzh.moegirl.org.cn/zh-hans/%E9%AB%98%E6%A0%A1%E8%88%B0%E9%98%9F)，百合薄纱赛博丁真！

# 附加

现在是凌晨两点，我治好了自己的精神内耗。

Apple 和 AirPods 是 Apple Inc. 在美国和其他国家和地区注册的商标。
