# HeLang：何语言

Next-Generation **Cyber** Programming Language from Li Tang.

引个流先：https://www.bilibili.com/video/BV1XW4y1h79A/

## 介绍

次世代赛博编程语言，诞生于**E-SMOKER**之乡：赛博理塘。

本项目是由自己会打字的5G键盘，花了108赛博分钟，在AirDesk上配合AirPods编写的。

实在是太酷了，很符合我对未来生活的想象，科技并带着趣味。

注：如果以**普通时间单位**（Basic Unit of Plain Time, [**BUPT**](https://baike.baidu.com/item/%E5%8C%97%E4%BA%AC%E9%82%AE%E7%94%B5%E5%A4%A7%E5%AD%A6/139535?from=kg)）作为标准单位，本项目开发时长为`1! + 5! + 5! + 5! = 361 `分钟。

注2：**BUPT** 在赛博世界还可以写为 Beijing University of Posts and Telecommunications，北京邮电大学（声明：我对本学府无恶意，我认为这是一所优秀的学校，毕竟有赛博丁真和粘连科技两大贵物，我只是对某个人）。

## 语法

**Saint He** 曾说，一切类型均为`u8`，是什么意思呢？这个词倒过来就是`8u`，看来圣人也喜欢玩贴吧。

如你所见，我们用**bitwise or**，即`|`代替了传统数组的符号。**都什么年代了还在写传统数组**？

```c
u8 array = 1 | 2 | 3;
```

**Saint He** 曾说：`whichKey - 1` ，所以我们数组的下标需要从 `1` 开始。

```c
print array[1];
// 1
```

为了符合最新的技术，我们同样支持多下标操作，所以你再也不用写 `for` 循环了。

```c
array[1 | 2] = 0;
print array;
// 0 | 0 | 3
```

同样，我们还提供了一种根据数组长度的初始化方式，可惜这还是传统写法。比如下面的代码，可以初始化一个长度为10的数组。

```c
u8 array = [10];
```

最后，我们结合一下，可以写出下列代码。

```c
u8 forceCon = [68];

forceCon[1 | 2 | 6 | 7 | 11 | 52 | 57 | 58 | 65] = 10;

print forceCon;
```

如此精妙的代码，在地球的人类是无法理解的。我们作为**赛博智能生命体**，也只能给你演示一下日常操作了。

对了，还有一个要求，你的注释必须写在行开始部分，因为我直接用 `strip().startswith('//')` 判断。

这实在是太酷了，后面我忘了，我也不想翻到文章开头去看。

## 总结

关注永雏塔菲喵，关注永雏塔菲谢谢喵。

关注[猫雷NyaRu_Official](https://space.bilibili.com/697091119)谢谢喵，要吃中国的大米喵。

## 附加

现在是凌晨两点，我治好了自己的精神内耗。
你的代码写的太精妙我不会改就是想要个pr快点给我。
