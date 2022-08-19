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

# Summary

[English](README-EN.MD) [中文](README.MD) [Русский](README-RU.MD) 

Next-Generation **Cyber** Programming Language from Li Tang.

WATCH THE GREAT VIDEO! https://www.bilibili.com/video/BV1XW4y1h79A/

[![Star History Chart](https://api.star-history.com/svg?repos=kifuan/helang&type=Date)](https://star-history.com/#kifuan/helang&Date)

# Re-creation

Very good works! Love from **Cyber Space**!

+ Helang `Kotlin` Script Implementation [HeLangKotlinScriptImpl](https://github.com/shaokeyibb/HeLangKotlinScriptImpl) --- [Implementation Rationale](https://my.minecraft.kim/tech/2022/08/18/post-740/)
+ Helang `C#` Implementation [HeLangSharp](https://github.com/Cyl18/HeLangSharp)
+ Why not rewrite with Rust? [helang-rs](https://github.com/imtsuki/helang-rs)
+ NOW ON `ArchLinux`! https://github.com/BenderBlog/Practise-Programs/tree/main/Helang-PKGBUILD
+ `HeScript`, enjoy `helang` in `JavaScript` / `TypeScript`! [hescript](https://github.com/Rotten-LKZ/hescript)
+ L! T! C! (etc.)

# Description

> Nowadays in the 21st century, `Helang`, `Jvav` and `C--` have become the three irreplaceable programming languages.
>
> Saint He. (2202). *A Brief **He**story of Cyber Programming Languages*. Lithang Computer Science and Technology Press.

Next generation cyber programming language, born in the **E-SMOKER** town, Cyber Lithang.

This program was written by a self-typing 5G keyboard on AirDesk with AirPods in 108 cyber minutes.

It's so cool! What a just fit with my imagination for a better future. Science with delight.

PS: It took about `1! + 5! + 5! + 5! = 361` [BUPTs](https://en.wikipedia.org/wiki/Beijing_University_of_Posts_and_Telecommunications) (Basic Unit of Plain Time) to develop this language.

PS 2: **BUPT** also refers to **Beijing University of Posts and Telecommunications** in the cyber world. (Disclaimer: This project is just a satire of a particular person. No malice to the outstanding university!)

# Usage

## Use without installation

1. Pull the source code:

   ```bash
   > git clone git@github.com:kifuan/helang.git
   ```

2. Install third-party libraries:

   ```bash
   > pip install -r requirements.txt
   ```

3. Modify **The Great Script** `great.he`, then run `helang.py` in a `great` way：

   ```bash
   > python helang.py great
   ```

4. You can also launch `helang.py` in `shell` mode, to communicate with **Saint He** in HeLang in the cyberspace.

   ```bash
   > python helang.py shell
   ```

   Now, there's no need to append semicolons to the line end: we will do that for you. (Of course, you can choose to use semicolons to show your loyalty to **Saint He**)

   Type `.help` to get the runtime help. Yeah, a copy-paste from `node`'s `REPL Keywords`.

5. Develop with `LTCode`：
   
   ```bash
   > python helang.py editor
   ```
   
   WIP. New features are planned.
   
## Install locally

1. Pull the source code：

   ```bash
   > git clone git@github.com:kifuan/helang.git
   ```

2. Install：

   ```bash
   > pip install .
   ```

3. Run

   ```bash
   > helang shell
   ```


PS：
- If you are from Planet Antimony, there is no need to use the stupid technology from sol3 aborigines. You can use 1.14514 sg (supergrams) `nitrane` to trigger the global termination of the cyberspace through the `exprinciple reaction` to run the program directly.
- When you're using **Non-Apple devices** to run, it will raise a warning.
`It seems like you're using a non-Apple device, which is not cool!`
If you want to disable this warning, please use Apple devices.

Attention: This is a very dangerous action with a chance of failing. If there is `chickenium-niobium-titanium-magnesium` nearby when you fail, it will be catalyzed and produce `CH2N8`. This action should be strictly regulated by exprinciple commitee.

# Basic Grammar

**Saint He** noted that every type is `u8`. What does that mean? Reverse it so we get `8u` (Ba You). Does Saint He use Tieba?

Besides, `u8` is similar to `v8` in shape. So follow [Ace Taffy](https://space.bilibili.com/1265680561) nya, follow Ace Taffy thank you nya.


As you can see, we use `|`, **the bitwise or**, to replace the traditional array. **Why are you still using traditional arrays nowadays?** 

```c
u8 a = 1 | 2 | 3;
```

**Saint He** also noted that `whichKey - 1`, so the index starts at `1`.

```c
u8 a = 1 | 2 | 3;
print a[1];
// 1
```

But when you operate against a `u8` variable, you can use index `0` to assign a value to all elements in the array.

```c
u8 a = 1 | 2 | 3;
a[0] = 10;
print a;
// 10 | 10 | 10
```

To catch on with the latest technology, multi-index operations are also supported. No more `for` loops!

```c
u8 a = 1 | 2 | 3;
a[1 | 2] = 0;
print a;
// 0 | 0 | 3
```

Also, we provide a way to initialize an array with a fixed length. Unfortunately, it's traditional. For example, the following code can initialize an array with 5 elements.

```c
u8 a = [5];
print a;
// 0 | 0 | 0 | 0 | 0
```

In the end, we can combine all the grammar above to write the following code.

```c
u8 forceCon = [68];

forceCon[1 | 2 | 6 | 7 | 11 | 52 | 57 | 58 | 65] = 10;

print forceCon;
```

Such fine code can't be understood by humans on earth. As a **cyber intelligent life form**, we could only show you the basics.

It's so cool. too long didn't write.

# Hello, World!

Some programmers consider Helang as a piece of shit because it can't print `Hello, world!` .

But **Saint He** focuses on the development of MCUs. How can he take strings into account?

Well, after consultation, he agreed our request and allowed us to print `Hello, world!` in the language.

```c
sprint 72 | 101 | 108 | 108 | 111 | 44 | 32 | 119 | 111 | 114 | 108 | 100 | 33;
// Hello, world!
```

To strictly optimize the performance, We use UTF-8 decimals instead of characters.

By decreasing readability, we gain exponential performance increase. Credits to the real god in the cyber world.

# Increment

We noticed that increment (`++`) also appeared in the code by **Saint He**.

So, we allow this operation too.

```c
u8 a = 1 | 2 | 3;
a++;
print a;
// 2 | 3 | 4
```

# Addition and Subtraction

**Saint He** said `whichKey - 1`, so now we provide subtraction too.

```c
u8 whichKey = 1 | 2 | 6 | 7;
print whichKey - 1;
// 0 | 1 | 5 | 6
```

Examples of operations between `u8` variables:

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

It's so easy for you to figure out which statements are legal, even if you're a **cyberspace newbie**!

# Multiplication

Unlike addition and subtraction, multiplication can be done between **any** two `u8`s. `u8`s will be treated as `vectors`. Isn't it high-tech?

```c
u8 a = 1 | 2;
u8 b = 3 | 4 | 5;
u8 c = 3 | 6 | 9;

print a * b;
// 1*3 + 2*4 + 0*5 = 9
print b * c;
// 3*3 + 4*6 + 5*9 = 68
```

Note: we use dot product ( $\vec{a}\cdot\vec{b}$ ), not out product.

# Declarations and Assignments of Variables

In early versions, we only support variable initializations and don't support mutation and declarations. Because **Saint He** loves `immutable`.

After consulting, we can now support them!

```c
// Now we support declarations before assignments. The code below is legal:
u8 a;
a = 1 | 2;

// In early versions only the following code worked, but it still works now.
u8 b = 3 | 4;
```

Warning! If a variable isn't declared or initialized, assigning it will raise `CyberNameException`.

```c
c = 1 | 2 | 3;
// helang.exceptions.CyberNameException: c is not defined.
```

As a high-tech language, we need to be strict and precise.


# Check If You Are in Cyberspace

To meet with **Saint He**, you need to be in **Cyberspace**. Use the command below to check if you're in position: 

```c
cyberspaces;
// Getting your location...
// Your location is UNITED STATES.
// Congratulations! You are in the Cyber Spaces!
```

# 5G Speedtest

Theoretically, this is also a part of the grammar, but I just want to single it out.

It's very simple, and all you need is to start a new line and type: 

```c
test5g;
```

Then you can start a 5G speedtest from this line. 

# Summary

Follow [Ace Taffy](https://space.bilibili.com/1265680561) nya, follow Ace Taffy thank you nya.

Follow [NyaRu](https://space.bilibili.com/697091119) thank you nya,  nya.

Follow [Xingtong](https://space.bilibili.com/401315430), liuliu plums give out!

Follow [Diana](https://space.bilibili.com/672328094), satisfy your craving for good food every dinner.

Follow [Ava](https://space.bilibili.com/672346917), it's never too late to follow her!

Follow [Eileen](https://space.bilibili.com/672342685), follow Eileen ga, follow Eileen thank you ga!

Follow [Bella](https://space.bilibili.com/672353429), follow Bella mur, Follow Bella thank you mur! 

Report [Rarity](https://space.bilibili.com/1437582453/) thank you nya, we can't let a Japanese eat Chinese rice nya. 

Follow [AdhesionTek](https://space.bilibili.com/248582596), violently kill Saint He nya🥰

Follow [HiiroVTuber](https://space.bilibili.com/508963009), it's not a pink cat with 425KG nya! 

Follow [GOGO](https://space.bilibili.com/1669777785/)! Follow GOGO woof, follow GOGO thank you woof! 

Follow [KizunaAI_CN](https://space.bilibili.com/484322035)! Super cute Super AI violently kills cyber Tenzin!

Follow [Mana](https://space.bilibili.com/3149619), thank you nya.

Follow [Luo Tianyi](https://space.bilibili.com/36081646), a more human-alike VSinger than Cyber Tenzin!

Follow [Tenzin Tsundue](https://space.bilibili.com/1463028352), why are you still following cyber Tenzin nowadays? You'd better pay attention to the traditional Tenzin!

Follow [Minato Aqua](https://space.bilibili.com/375504219) and [Rinco](https://www.nicovideo.jp/user/45194653
)! Stupid-overflowing ocean maid (shit onion) and a cute singer who likes Minase Inori. Looking forward to wood mouth spinning nie. Also, please support the [galgame](https://shop.hololivepro.com/products/aquarium_hololive_official_edition) that Minato Aqua stars in!

Follow [Genshin Impact](https://space.bilibili.com/401742377), playing Genshin Impact is much better than watching cyber Tenzin!

Follow [Tang Jiuxia](https://space.bilibili.com/1219196749), thank you my father!

Follow [Kino](https://space.bilibili.com/1383815813), guard the most abstract princess in the world!

Follow [Katya](https://space.bilibili.com/1011797664), thank you yee!

Follow [Hiru](https://space.bilibili.com/1848290057), she can't understand all of these but her serration-shaped tooth are so cuuuuuuuuuteeeeeeeee I LOOOOVVEEEEEE HEEEERRRRRR AAAAAAAAAAAAAAA!

# Addition

It's 2:00 a.m. now, I cured my mental internal friction.