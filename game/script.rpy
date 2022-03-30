## 定义图片
## image语句:[url=https://www.renpy.cn/doc/quickstart.html?highlight=image#image]https://www.renpy.cn/doc/quickstart.html?highlight=image#image[/url]
## 注意文件格式 png 与 jpg
image af-1 :
    "images/cg/af.png"
    size (1920 ,1080) ## 原图尺寸：1920*1080，改为：1280*720

image bf-1 :
    "images/cg/bf.png"
    size (1920 ,1080)

image cf-1:
    "images/cg/cf.png"
    size (1920 ,1080)

image df-1 :
    "images/cg/df.png"
    size (1920 ,1080)
image ef-1 :
    "images/cg/ef2.png"
    size (1920 ,1080) ## 原图尺寸：1920*1080，改为：1280*720
image rem-1 :
    "images/cg/rem3.png"
    size (1920 ,1080)

image end1-1 :
    "images/cg/end1.png"
    size (1920 ,1080)

image end2-1:
    "images/cg/end2.png"
    size (1920 ,1080)
image fin-1:
    "images/cg/final.png"
    size (1920 ,1080)
image af-1-p = "images/cg/afl.png"
image bf-1-p = "images/cg/bfl.png"
image cf-1-p = "images/cg/cfl.png"
image df-1-p = "images/cg/dfl.png"
image ef-1-p = "images/cg/efl.png"
image rem-1-p = "images/cg/reml.png"
image end1-1-p = "images/cg/end1l.png"
image end2-1-p = "images/cg/end2l.png"
image fin-1-p = "images/cg/finall.png"
## 定义 未解锁缩略图
image locked :
    "images/cg/locked.png"
    size (270 ,150) # 调整原图尺寸。

init python:
## 创建Gallery对象。
## 名为“g_cg”，名称可更改，但不能数字开头，更不能使用汉字。
    g_cg = Gallery()

## 未解锁的图片，尺寸与CG缩略图相同。
    g_cg.locked_button = "locked" # 绝对路径图片。

## 在画廊中按钮和CG图像 unlock_image对应自动解锁CG图。
    g_cg.button("af-1") # 按钮的标识。
    g_cg.unlock_image("af") # 该按钮对应的CG图片。

    g_cg.button("bf-1")
    g_cg.unlock_image("bf")


    g_cg.button("cf-1")
    g_cg.unlock_image("cf")


    g_cg.button("df-1")
    g_cg.unlock_image("df")


    g_cg.button("ef-1")
    g_cg.unlock_image("ef2")


    g_cg.button("rem-1")
    g_cg.unlock_image("rem3")

    g_cg.button("end1-1")
    g_cg.unlock_image("end1")


    g_cg.button("end2-1")
    g_cg.unlock_image("end2")


    g_cg.button("fin-1")
    g_cg.unlock_image("final")

## 创建 画廊界面（screen）
screen gallery:

## # 确保任何其他菜单界面都会被替换。
    tag menu

## 背景图。
    add "images/cg/hualang.png"

## 创建 vbox布局参考。具体参考文档：[url=https://www.renpy.cn/doc/displayables.html?highlight=vbox#VBox]https://www.renpy.cn/doc/displayables.html?highlight=vbox#VBox[/url]
    vbox: # 框体内成员布局顺序从上到下。
        xalign 0.5
        yalign 0.335
        spacing 77 # 方框(box)样式特性，方块内成员之间的空间距离，单位为像素。

## 调用make_button
## 关于make_button，参考中文文档：[url=https://www.renpy.cn/doc/rooms.html?highlight=make_button#Gallery.make_button]https://www.renpy.cn/doc/rooms.h ... Gallery.make_button[/url]
        hbox: # 框体内成员布局顺序从左到右，与vbox相反，都是用来结构布局。
            spacing 165
            add g_cg.make_button("af-1", "af-1-p", xalign=0.5, yalign=0.5) # "1-1_p.png"是"1-1_cg"缩略图。
            add g_cg.make_button("bf-1", "bf-1-p", xalign=0.5, yalign=0.5)
            add g_cg.make_button("cf-1", "cf-1-p", xalign=0.5, yalign=0.5)
        hbox:
            spacing 165
            add g_cg.make_button("df-1", "df-1-p", xalign=0.5, yalign=0.5)
            add g_cg.make_button("ef-1", "ef-1-p", xalign=0.5, yalign=0.5)
            add g_cg.make_button("rem-1", "rem-1-p", xalign=0.5, yalign=0.5)
        hbox:
            spacing 165
            add g_cg.make_button("end1-1", "end1-1-p", xalign=0.5, yalign=0.5)
            add g_cg.make_button("end2-1", "end2-1-p", xalign=0.5, yalign=0.5)
            add g_cg.make_button("fin-1", "fin-1-p", xalign=0.5, yalign=0.5)


## 可以继续增加，不过需要调整布局以及 spacing间距了。

## 返回键
    imagebutton:
        idle "gui/button/back_3.png"
        hover "gui/button/back_4.png"
        xalign 0.86
        yalign 0.91
        action Return()


# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define f = Character("四")
define a = Character("向晚")
define b = Character("贝拉")
define c = Character("珈乐")
define d = Character("嘉然")
define e = Character("乃琳")
define f1 = Character("四 ")
define a1 = Character("向晚 ")
define b1 = Character("贝拉 ")
define c1 = Character("珈乐 ")
define d1 = Character("嘉然 ")
define e1 = Character("乃琳 ")
define f2 = Character("四  ")
define a2 = Character("向晚  ")
define b2 = Character("贝拉  ")
define c2 = Character("珈乐  ")
define d2 = Character("嘉然  ")
define e2 = Character("乃琳  ")
define ad = Character("二人")
define k = Character("空寰")
define x = Character("心雩")
define x1 = Character("心雩 ")
define n = Character("？？")
define n1 = Character("？？ ")
define n2 = Character("？？  ")
define k1 = Character("■■")
define u = Character(" ")
define u1 = Character("  ")
define u2 = Character("   ")
define z = Character("众人")
define fadehold = Fade(0.5, 1.0, 0.5)
define fadeholdd = Fade(0.5, 2.0, 0.5)
# 游戏在此开始。

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为"bg room.png"或"bg room.jpg"）来显示。
    play music "audio/深竹.ogg" fadeout 1.0 fadein 1.0
    scene world with fade
    # FIXME: 为什么会闪一下？
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # "eileen happy.png"的文件来将其替换掉。

    u """
    遥远的世界、遥远的时间之外，我试图找到第三种色彩。

    哪怕伤痕累累也没有办法，这是唯一的选择。

    ……

    我会吃这个吗？染血的骨肉。

    当然不吃！绝不会予以考虑。

    那么，这个呢？

    纯净的糖水。

    我怀着好奇去尝试，不祥的预感却如锁链般将我束缚，又如空气般无处不在。

    我还是尝了一口。

    太甜了，甜到不真实。

    不断提纯的过程筑起了空中花园般的幻境。

    ……

    为什么、选择的是她们？
    """
    show xinyu with dissolve
    u "我曾严厉地质问■■。"
    u "■■却不予回答。"
    u "她是个恶劣的灵体，我不想提起她的名字。"
    u "不过，对于如今的我，这也不再重要。"
    u "我已成为，被放逐的■。"
    u "……"
    u "对了，我仍与人类有一个约定，但是不确信，她是否也记得。"
    u "只是，她现在如此闪耀，我或许已不该打扰她。"
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    scene bg3 with fadehold
    u2 """
    六月的枝江，正值炎夏。

    训练室中，即使一直开着空调，也很难维持舒适的温度。

    木质的地板已经被汗水打湿了一大块。

    我叫贝拉，现在正带着我的队友做舞蹈训练。

    我现在是偶像团体A-SOUL的队长。
    """
    show a11 with dissolve
    u2 "这个大的双马尾是向晚，是个哭包大小姐，不过现在的她已经坚强了许多。"
    hide a11
    show d11 with dissolve
    u2 "粉色的小的是嘉然，平时乖巧听话，大家都很喜欢她。"
    hide d11
    u2 "但在所有人里，向晚反倒是年龄最小的那个。"
    u2 "当然，我还有两位队友，不过她们暂时不在。"

    show b1 with dissolve
    b2 "我先来做一遍，你们注意我动作上的细节。"
    hide b1
    show a21 at right
    show d21 at left
    ad "好！"
    hide a21
    hide d21
    play music "audio/mto.ogg" fadeout 2.0 fadein 2.0
    u2 """
    音乐响起，我仿佛身处舞台中央。

    我随着音乐起舞，忽然想到，从前我有个芭蕾舞演员的梦想。

    虽然现在是在做偶像，有一些小小的区别……

    但梦想也算是实现了吧？那种执念早已不再强烈。

    ……

    我尽量将自己放空在音乐中。
    """
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    u2"音乐结束，动作停止，就像是肌肉记忆。"
    scene bg3 with fade
    show a21 at right
    show d21 at left
    ad "拉姐厉害！"
    hide a21
    hide d21 with dissolve
    u2 "动作随着音乐停止下来，但听到她们的赞美和掌声，我的思绪才回到训练中。"
    show b10 with dissolve
    b2 "行了行了，少拍我马屁。有什么问题嘛？没有的话，我们就开始了，你们跟着我，做好每一个动作。"
    hide b10
    show a21 at right
    show d11 at left
    ad "好！"
    hide a21
    hide d11
    u2 "我将舞蹈的动作分解，短暂熟悉之后，她们已经能够跟上节拍了。"
    show b3
    b2 "一，二，三，四，晚晚，注意，节奏，八。二，二，三，四，五，六，然然，跟上……好，我们再来一遍！"
    hide b3
    u2"""
    嗯……学得比我预想还要快嘛！

    这样的话，之后的演出就完全没问题了，只要不出意外，时间足够，一定能筹备充分的！
    """
    show b1 with dissolve
    b2"好，现在你们自己跳一遍！"
    hide b1 with fade
    u2"""
    ……

    不愧是偶像，她们很快便掌握了动作。

    我从然然身旁走过，揉了揉她的头。
    """
    show b2 with dissolve
    b2"然然真棒，这么快就学会了。"
    hide b2
    show d21 with dissolve
    d2"然然可厉害了！"
    hide d21 with dissolve
    u2"我仔细看着她们的动作，以便及时纠正出错的地方。"
    show a41 with dissolve
    show b1 behind a41 with moveinright
    b2"晚晚，你这里手要抬高一点。"
    u2"我来到晚晚身后，抓住她的手腕。"
    b2"还有，身体的角度需要调整一下……"
    u2"这种细微的调整很难用语言表述清晰，还是直接用手比较方便。"
    hide a41
    hide b1
    show a131 with vpunch
    a2"拉姐你摸哪里啊，你摸太上面啦……你又摸我！"
    hide a131
    u2"碰的位置好像……"
    u2"碰到的一瞬间，晚晚就像是触电一样，尖叫着弹开了。"
    show b2 with dissolve
    b2"什么嘛……就是规范一下动作。不过……软软的，哈哈哈哈哈！"
    hide b2
    show d41 with dissolve
    d2"什么软软的？我也要摸！"
    hide d41
    show a181 with dissolve
    a2"不许摸！要摸的话摸拉姐去！"
    hide a181
    u2"""
    我微微愣神，晚晚已经在训练室里跑了起来。

    不假思索，我便追了上去。

    ……
    """
    scene bg3 with fadehold
    show d21 with dissolve
    d2"好热！"
    hide d21 with dissolve
    u2"一番笑闹之后，我们都是又出了一身汗。"
    show a121 with dissolve
    a2"哼，谁让你非要追上来嘛！"
    hide a121 with dissolve
    u2"这可以说是我们A-SOUL的默契，刚刚看到我去追晚晚，然然也随即加入了追逐游戏。"
    show b1 with dissolve
    b2"好了好了，大家先别闹了，继续训练！"
    hide b1 with dissolve
    stop music fadeout 2.0
    scene bg3 with fadehold
    u2"……"
    u2"不知道是第几次音乐结束后，晚晚一屁股坐在地上。"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show a91 with dissolve
    a2"……我不行了！我们歇一会吧，拉姐……"
    hide a91
    u2"晚晚喘着气哀求着。"
    show b9
    b2"不行，这才练了几次，还不是你刚刚非要闹！"
    hide b9
    show a121
    a2"明明是拉姐追我我才跑的！"
    hide a121
    show b10
    b2"明明是你先跑我才追的！"
    hide b10
    show a121
    a2"那拉姐要是不追我我就不跑了……"
    hide a121
    show b2
    b2"我是担心你自己跑尴尬才追你。"
    hide b2
    show a141
    a2"嘿嘿……那是我错了，拉姐……我们能不能歇一歇呀？"
    hide a141
    show b2
    b2"加油，你看然然还在坚持呢！"
    hide b2
    u2"不过晚晚还是不想放弃，反而转过身拉住然然的手晃了晃。"
    show a21
    a2"然然，你肯定也累了吧！我们休息一下好不好？"
    hide a21
    show d31 with dissolve
    d2"拉姐，然然饿了，想吃零食！"
    hide d31
    u2"说完她也坐倒在了地上，一脸可怜地看着我。"
    u2"说起来，她们今天已经很努力了，就到此为止吧？"
    u2"一会让乃琳和珈乐出去买点好吃的作为奖励吧。"
    u2"但是也不能就这样懒散地结束了！"
    u2"我装作生气，轻轻在她们头上一边打了一下。"
    show a31
    a2"哎哟，疼疼疼疼疼疼！"
    hide a31
    show b1
    b2"哼，别以为我不知道你们俩串通好了，然然你也学坏了是吧？快起来好好练！"
    hide b1
    u2"耳边传来了晚晚的哀嚎。"
    show d41
    d2"没关系的晚晚，练嘛！"
    d2"你又不是第一天认识拉姐……"
    hide d41
    u2"她看了看我，小声对晚晚这样说。"
    u2"……虽然我还是一字不漏地听到了。"
    show b2
    b2"好了好了，你俩快起来。练完最后一遍我带你们去吃好吃的。"
    hide b2
    show a141 at right
    show d21 at left
    ad"谢谢拉姐！"
    hide a141
    hide d21
    u2"没想到，已经当了她们两年的队长，居然还要像哄孩子一样哄着她们训练。"
    u2"不过这句话果然有效，她们好像顿时有了力气，站了起来。"

    scene bg3 with fadehold
    u2"……"
    u2"训练很快结束了，不知道是不是因为食物的诱惑，最后一遍排练比之前还要整齐。"

    show b2 with dissolve
    b2"今天辛苦了！中午想吃什么？"
    hide b2
    show d11
    d2"然然想吃泡面。"
    hide d11
    show b1
    b2"可以再贪心一点哦。"
    hide b1
    show a141
    a2"那我们可以吃大碗的泡面吗？"
    hide a141
    u2"如果说然然想吃泡面，那是因为真的累了，才想要吃这种最朴素的美味。"
    u2"但是，晚晚是真的喜欢吃这种毫无营养的食品！"
    u2"所以必须制止！"
    show b10
    b2"不行！还有晚晚你以后也要少吃点泡面。"
    hide b10
    show b2
    b2"我已经让乃琳和珈乐去准备午饭了，你们还想吃什么就打电话告诉她们吧。"
    hide b2
    show a141 at right
    show d21 at left
    ad"哇，拉姐万岁！"
    hide a141
    hide d21
    u2"我拉起她们的手，一起离开了训练室。"
    scene res with fadehold
    u2"现在已经是中午了。"
    u2"我们在休息室中等着乃琳和珈乐带午饭回来。"
    u2"几个小时训练下来，感觉筋骨已经完全舒展开了，"
    u2"整个人就像要飞起来一样……拦都拦不住的那种感觉！"
    u2"我挺直了腰，看着窗外飞过的鸽子——"
    show b2 with dissolve
    b2"练舞真的是超快乐的！是不是各位？"
    hide b2
    u2"一片静默。"
    u2"我转头看向室内。"
    u2"嘉然慵懒地靠在沙发上，拿着湿毛巾擦拭着头上的汗珠。"
    u2"而另一位紫色的丸子头，整个人呈U型躺在沙发上。"
    show b3
    b2"乃琳和乐已经去买我们的大餐了，只需要再等……"
    hide b3
    u2"我说到一半，不由得停住了——忽然意识到，一个小时前我好像就是这么说的。"
    u2"她们两个怎么还没回来？"
    u2"我看了看晚晚，她没有看向我。"
    show a82
    u2"她空洞的双眼朝着天花板的方向，却没有看着什么，仿佛被抽干了灵魂，嘴巴机械式地跟着呼吸一张一合，像一条刚捞出来的带鱼。"
    hide a82
    u2"这幅邋遢样子简直不堪入目"
    show b5
    b2"……啧。"
    hide b5
    u2"不好！没控制住，啧出声了！"
    u2"在我出声的一瞬间，我就后悔起来，果然，两个小朋友立刻在沙发上打了个冷颤。"
    u2"嘉然立刻坐直了身体，小手乖巧的放在膝盖上。毛巾盖在腿上，小脑袋低了下去。"
    u2"果然不管怎么看都觉得，"
    u2"然然真是可爱呀！"
    u2"而另一边的紫色丸子头则只是颤了一下。"
    u2"稍稍尝试着坐起身体，但长时间保持着U型，整个人的身子似乎用不上力，却又完全懒得调整，"
    u2"又一次挣扎之后，晚晚便不再动弹了。"
    show a82 with dissolve
    a2"适可而止的努力、知难而退的放弃，并不是错误……练了这么久的舞还没有饭吃……拉姐也来这里，一起躺着吧。"
    hide a82
    show a92
    a2"你看，你透过天花板去看，看最遥远的地方，是不是有一只像人一样的大水母？"
    hide a92
    show b2 with dissolve
    b2"哼！你这样躺着就算了，还躺出幻觉了是吧？给我起来！"
    hide b2 with dissolve
    u2"她却彻底瘫了下来，脸上浮现出怪异的笑容，眼角……居然有了泪珠？"
    u2"但……不是吧？明明我的表情没有很严肃……"
    u2"可我是不是真的过分了？现在如果要推卸责任的话……等乃琳和珈乐回来骂她们一顿？怪她们为什么回来得那么晚……算了算了……"
    show b3 with dissolve
    b2"然然，晚晚。"
    hide b3 with dissolve
    u2"然然小脸绷得紧紧的，生怕惹得我不高兴了。"
    u2"一旁的晚晚，居然真的哭了。"
    u2"我朝她们走去，一步、两步……忽然感觉，我的腰好像也有些酸痛。"
    u2"到底是我真的精力充沛，还是只是在骗自己呢？"
    stop music fadeout 3.0
    u2"我已经能听见她们隐约的心跳声，频率很高。"
    u2"有这样怕我吗？"
    show b10 with dissolve
    b2"哼……"
    hide b10 with dissolve
    u2"我站到了她们的面前，伸出了双手。"
    u2"然后——"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 1.0
    show a32 at right
    show d31 at left with hpunch
    $ renpy.pause(1, hard=True)
    scene res with dissolve
    u2"我把她们都抱在了怀里。"
    show b2
    b2"都快两年了，还这样怕我吗？这样我也很难办啊……今天都辛苦啦，你们已经很努力了，现在就好好休息吧！"
    hide b2
    u2"被抱住的嘉然像只粘人的小猫一样，朝我的怀里蹭了蹭。橙黄色的头发，有股焦糖一样的甜香气，和太阳一般的温暖。"
    show d31
    d2"拉姐，你好温柔啊！"
    hide d31
    u2"你又不是今天才知道……为什么要怕我呢？"
    show a32
    a2"呜呜……拉姐……"
    hide a32
    u2"感受到一点温柔，晚晚直接放肆地哭了起来，这一点我无比习惯！"
    show b2 with dissolve
    b2"诶嘿……别哭，别哭。"
    hide b2
    u2"我抚摸着晚晚紫色的头发，她的头发很长，这样扎起来也是件麻烦的事情。"
    u2"相较而言，然然的头发短了许多，打理起来也方便得多。"
    u2"左腰怎么湿湿的？"
    show a32
    a2"呜……呜呜……"
    hide a32
    u2"几乎不用看的——晚晚正靠在我的怀里大哭特哭呢。"
    u2"如果她不是坐在沙发上，湿的应该就是肩膀了吧。"
    show d11
    d2"晚晚！"
    hide d11
    show d11 at left
    show a32 at right
    a2"干嘛……？"
    hide d11
    show d41 at left
    d2"晚晚，我来给你讲个故事吧！"
    a2"呜……唔……"
    hide d41
    show d31 at left
    d2"以前呢，有一个很好的很好的裁缝。"
    a2"嗯……"
    hide d31
    show d11 at left
    d2"他做的东西非常非常完美，而这在于他自己的窍门。谁也不知道他的秘密……其实，他的布是有生命的！"
    hide a32
    show a162 at right
    a2"……呜？"
    d2"那天他缝出来了一条世界上最完美的裤子，全国为之轰动，国王花了六百万金币只是想知道他能缝出这条裤子的原因。裁缝嘿嘿一笑，说就是在于他的布早上跟他说的话。"
    hide d11
    hide a162
    u2"说到这里，嘉然停顿了下来。"
    show a162
    a2"说……说了什么？"
    hide a162
    show d21
    d2"嘿嘿嘿～"
    hide d21
    show a122 with hpunch
    a2"说了什么嘛？！"
    hide a122
    u2"听不到后续的向晚，着急地摇着然然的手臂。"
    show d21
    d2"布要裤嘛，布要裤嘛，不要哭嘛～"
    hide d21
    u2"……好冷，但是我要做出表率！"
    show b2
    b2"哈哈哈哈哈哈哈哈哈——"
    hide b2
    u2"看到我发笑的瞬间，嘉然都惊呆了！"
    show a142
    a2"拉姐、你……好好笑啊……哈哈哈……"
    hide a142
    u2"成功！"
    u2"关于冷笑话，总需要一个带头狂笑的人！"
    u2"不过，等晚晚破涕为笑，我也就不需要再演下去了、等等……"
    show b2
    b2"哈哈哈哈哈……"
    hide b2 with dissolve
    u2"为什么我笑得停不下来了啊？！"
    scene res with fade
    u2"过了一会儿，晚晚好像又想起了什么，擦了擦湿红的眼睛。"
    show a122
    a2"我才没哭！刚刚……只不过是因为松了一口气的同时，被……被拉姐稍稍感动到了而已！"
    hide a122
    show b2 with dissolve
    b2"是……晚晚你说得没错。"
    hide b2 with dissolve
    u2"听起来好像真的是这样诶！毕竟刚刚湿掉的衣服，现在已经被空调吹干一半了。"
    u2"那……就是没哭的吧？"
    show d11 with dissolve
    d2"没关系的，想哭就哭出来！小哭包如果有一天不哭了，大家是会担心的！"
    hide d11
    show a122 with dissolve
    a2"……哼。"
    hide a122 with dissolve
    u2"每到这个时候，都会觉得莫名放松。"
    u2"有她们在的话，不管是什么困难，都能够承受吧？"
    u2"有我的队友们，在哪里都是乐园，都是我的家！"
    n"拉姐，我们回来了！"
    u2"本想要说些什么，门外的声音打断了我。"
    u2"那这样就好。"
    stop music fadeout 3.0
    scene res with fadehold
    u2"下午，午饭过后。"
    show e2
    n"拉姐！十分抱歉！"
    hide e2
    u2"我背对着她，双臂抱怀，一言不发。"
    show e4
    n"哎呀～你也知道我有点选择恐惧症的嘛，然后就跟乐多逛了一会儿……"
    hide e4
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    u2"高挑的身段，成熟的气质。奶白色的长发，天使般的容颜。"
    u2"第一眼更像是从希腊神话里跑出来的女神。"
    u2"虽然我们早已熟识，但偶尔还是会这样想。"
    show e1
    n"拉姐你别不说话呀！这样很吓人的呀！"
    hide e1
    u2"她是我们团里的乃琳，看似温柔知性，但某种程度上，是团里最不靠谱的一个，或许。"
    show e4
    e2"呜呜呜！拉姐不理人家了！"
    hide e4
    u2"呃，又或者说是小孩子气……"
    u2"说起来，她可是除了我在团里面最大的一个，"
    u2"有时候的言行举……啊！"
    show e4 with hpunch
    e2"拉姐拉姐拉姐拉姐拉姐拉姐拉姐拉姐拉姐拉姐拉姐拉姐——"
    hide e4
    u2"她突然搂着我的腰晃来晃去。"
    show e2
    e2"不要生气了嘛～啊～"
    hide e2
    show b9
    b2"做作。你—再—晃—我—就——"
    hide b9
    u2"她一瞬间就停止了晃悠，但还是没有松开搂着我的手。"
    show e2
    e2"拉姐……对不起……"
    hide e2
    show b1
    b2"嗯？对不起什么啦？"
    hide b1
    show e2
    e2"因为我才让两个小妹妹饿了这么久，明明快速决定一下就好……"
    hide e2
    show b10
    b2"乃琳，我可没因为这事儿生气！"
    hide b10
    show b1
    b2"刚刚吃饭的时候她们也非常开心啊。"
    hide b1
    show e7
    e2"诶……那你为什么……"
    hide e7
    show b2
    b2"我是装的！本来想看看你有什么反应，但你实在是……太吓人了！我认输！"
    hide b2
    show e7 with vpunch
    e2"诶？"
    hide e7
    show b3
    b2"诶什么，我们可是队友诶！我哪有那么容易生气……"
    hide b3
    show b10
    b2"倒不是说你做得对，但如果所有事情都像预想一样，生活不是也少了许多乐趣嘛！"
    hide b10
    show b2
    b2"更何况，你是我们的一员，我们是你的同伴。"
    hide b2
    show b1
    b2"身为队长，我当然要照顾好你们每一个人了，不管是身体还是心灵。"
    b2"所以说，安啦——"
    hide b1 with dissolve
    u2"刚刚说的话仔细想想好像有点羞耻，但只要安慰到这丫头就可以了。"
    u2"这个人怎么不说话？难道是感动得不成样子了？"
    u2"刚转过头去，想让她不要太在意，却看到她一副奸计得逞的笑容。"
    show b9
    b2"你！你……"
    hide b9
    show e1
    e2"贝拉姐姐，你能重复重复刚刚自己说的话吗？"
    hide e1
    u2"她的俏脸凑了过来，高档香水味传入我的鼻腔。"
    u2"这种喜欢捉弄人的性格，真像个小孩子。"
    u2"论小把戏，我确实玩不过她。"
    u2"但如果我不想输——"
    show b1
    b2"身为队长，我当然要照顾好你们每一个人了，不管是身体还是心灵。"
    hide b1
    u2"我看到乃琳的眼中闪过几丝温暖的什么，注意到我的目光，她避开了头。"
    show e2
    e2"拉姐……"
    hide e2
    show b3
    b2"所以说为了照顾你的身体，午饭后的训练还是很关键的！"
    hide b3
    show e7
    e2"？"
    hide e7
    show e7 with vpunch
    e2"？？？"
    hide e7
    show b2
    b2"你刚刚也表示自己很感动吧，觉悟很值得褒奖哦！"
    hide b2
    u2"我拽住她的肩膀，不给她逃跑的机会。"
    show b1
    b2"那！我们出发吧！"
    hide b1
    u2"具体应该是什么训练项目呢？我还要好好想想。"
    show e4
    e2"不！我拒绝——"
    hide e4
    show b3
    b2"这样挺好的嘛！比起毫无意义的拒绝，你还不如想想怎么逃跑呢！"
    hide b3
    show e2
    e2"在拉姐面前想要逃跑才是毫无意义的吧？"
    hide e2
    u2"一定会让她度过一段充实的训练时光！"

    play music "audio/Zki.ogg" fadeout 3.0 fadein 3.0
    scene black with fadehold
    u2"一天的训练结束"
    scene bg4 with dissolve
    u2"夜深了。"
    u2"对于我来说，又是充实的一天，充实得，有些不真实。"
    u2"一个人的晚上，难免会有些思绪。"
    u2"刚刚玩手机的时候，无意间看到了自己的跳舞视频。"
    u2"……"
    u2"如果我没有受伤。"
    u2"如果一开始没有加入这个集体，我现在是在哪里呢？"
    u2"或许会有不一样的人生，遇到不一样的人吧？"
    u2"窗外没有看到月亮，但墙壁上的月亮挂画还是挺漂亮的。"
    show b10 with dissolve
    b2"我记得去年好像有一个我打穿了月球的视频……"
    hide b10
    u2"说起来，我最近的新团服，也被说过像是魔法少女呢。"
    u2"虽然我从没想过要打穿月球，但飞到星空中去，也未尝……"
    u2"嗯？什么声音……"
    u2"屋外隐约传来一丝奇异的旋律。"
    u2"若有若无，却又让我心系于此。"
    show b1 with dissolve
    b2"去看看吧！"
    scene zl with fade
    u2"不是队友们的房间，声音要更加遥远。"
    u2"我试着偏了偏头，锁定了声音的来源。"
    show b1 with dissolve
    b2"是在天台。"
    hide b1
    u2"我朝着声音的方向走去。"
    scene bg5 with fade
    n"……"
    u2"高处传来阵阵歌声，犹如百灵鸟的婉转轻吟。"
    u2"简单却又直击人心，像是在心头上挠痒痒一样。"
    show b3
    b2"乐！"
    hide b3 with dissolve
    show c1 with dissolve
    c2"拉姐！"
    hide c1
    u2"歌声戛然而止，我有点后悔出声叫住她了。"
    show c3 with dissolve
    c2"拉姐……还没睡吗？"
    hide c3
    u2"看见了我，本来靠着栅栏弓着腰唱歌的少女，好像有些慌张。"
    u2"帅气的穿着，潮流的造型，在外人面前，偶尔会以大哥来自称。"
    u2"但面对我的时候，却总是要装得很柔弱，更甚于本性！"
    show b1
    b2"嗯，有些睡不着，最近的星象，看上去就像有大事发生。"
    hide b1
    u2"睡不着倒是真的，星相当然是我看见那满天繁星，随口乱编的。"
    show c5
    c2"拉姐，你每天不是沾床就睡的吗？而且你什么时候还会看星相了？莫非又勾搭上了哪个妹妹？"
    hide c5
    u2"她手捂着唇，然后眼睛眯成了一条缝，看着我笑。"
    u2"珈乐是个爱笑的小姑娘，平时也喜欢逗我开心。"
    show b10
    b2"哼，拿着应付乃琳的话术直接用到我身上？真敷衍！"
    hide b10
    u2"我一只手搭在她的头上，作为惩罚，胡乱揉了几下。"
    u2"她两只手抓着我以示反抗，虽然半点力气也没用。"
    show c6 with hpunch
    c2"啊……拉姐你干什么嘛！"
    hide c6
    show b2
    b2"我开心！再说，乐你为什么不睡觉？"
    hide b2
    u2"她突然就笑了，双手也从头上撤下来，任我揉捏了。"
    show c4
    c2"有些睡不着觉……而且，为了月末的演唱会，想要练一练歌。"
    hide c4
    show b1
    b2"练习不要太辛苦了，要注意休息！"
    hide b1
    show b3
    b2"另外……睡不着是因为想到要去那么大的舞台而紧张吗？"
    hide b3
    show c7
    c2"不，我们出道也快两年了，经历了那么多困难，我不会提前半个月就感到紧张的。"
    hide c7
    show b10
    b2"那是什么？"
    hide b10
    show c2
    c2"今天我和乃琳出门的时候，遇见了令人注意的……人。"
    hide c2
    show b1
    b2"令人注意？"
    hide b1
    show c1
    c2"嗯，我从来没见过那样的人类。"
    hide c1
    show c5
    c2"那时候我去取炸鸡，乃琳在外面等我。"
    hide c5
    show c2
    c2"我出来的时候，发现她在和一个非常不像人的人说话！"
    hide c2
    show b1
    b2"那到底是不是人？"
    hide b1
    show c5
    c2"应该是的吧？那是一个非常非常非常漂亮的红衣女人。"
    hide c5
    show b3
    b2"哇，你居然用了三个非常来形容人漂亮？我也有些好奇她的样子了！"
    hide b3
    show c2
    c2"但是关键不在于她漂亮，她美得简直不像是人类。"
    hide c2
    show b2
    b2"像是希腊神话里的女神吗？"
    hide b2
    u2"我忍不住笑了。"
    show c3
    c2"不是啦！乃琳可能是像，但是那个人……"
    hide c3
    show c5
    c2"更像是古神话中的不死鸟。"
    hide c5
    show b2
    b2"所以，乐你就因为人家长得漂亮，直到现在都睡不着？"
    hide b2
    show c7
    c2"什么呀？我是认真谈这件事的！我说过关键在于她不像人类……可惜拉姐没有见过她，我也不好形容那种感觉……还有，更让我在意的是乃琳。"
    hide c7
    show b10
    b2"乃琳怎么了？该不会她又干了什么坏事？"
    hide b10
    show c2
    c2"拉姐不要乱想，这次是个严肃的事情！我不知道她们谈了什么，但是乃琳那时候居然也一脸严肃。"
    hide c2
    show b10
    b2"乃琳会严肃的事情……发生了什么？"
    hide b10
    show c7
    c2"不知道。等我出来以后，那个人就走了，乃琳对刚刚的谈话也是遮遮掩掩的……"
    hide c7
    show b1
    b2"乃琳……我想，她一定有自己的理由吧？我们认识她这么久，如果是我们该知道的事情，她不会故意瞒着我们的。"
    hide b1
    show c3
    c2"但乃琳不是在瞒着我们，而是单纯无法解释清楚。"
    hide c3
    show c7
    c2"她说，那个人和自己说话就像是在猜谜语一样难懂，自己努力想通一部分，又忘了那个人原本的话。"
    hide c7
    show b2
    b2"是那个人的问题吗？可能是乃琳比较笨的缘故！"
    hide b2
    show c7
    c2"……"
    hide c7
    show b10
    b2"抱歉，我不该开玩笑的，乐你继续。"
    hide b10
    show c4
    c2"不是……我忘记说到哪里了。"
    hide c4
    show b2
    b2"……"
    hide b2
    show c1
    c2"让我想想……乃琳太笨了，是因为忘了那个人原本说的什么……"
    hide c1
    show c2
    c2"我想起来了！乃琳说，如果她再转述给我们，可能就连自己仅存的理解都无法正确传达。她说，这似乎是个重要的暗示，她只能尽量总结出一种印象来。"
    hide c2
    show b1
    b2"但是今天，乃琳还是和平时没什么差别呀，至少我这样觉得。"
    hide b1
    show c5
    c2"因为我们玩得很开心，回来以后，也就没怎么在意这件事情了。"
    hide c5
    show c4
    c2"我也只是到了深夜才想起来这件事，拉姐不要担心！"
    hide c4
    show b1
    b2"我当然不担心！小的时候，我也遇到过占卜的巫女呢。可能她就是觉得乃琳的气质十分投缘，就多说了几句吧？但是她又想让自己表现得高深一些，就开始猜谜了！"
    hide b1
    show c4
    c2"拉姐说得对，除了非常漂亮这一点，她也没什么特殊的嘛！"
    hide c4
    show b10
    b2"不管怎样，六月末的舞台，算是眼前最重要的事情了。"
    hide b10
    show c4
    c2"那，拉姐，我们一起练练歌怎么样？"
    hide c4
    show b1
    b2"不，今天的训练时间已经结束了。"
    hide b1
    show c4
    c2"好吧……那我们回去？"
    hide c4
    show b2
    b2"不！现在要唱歌，就不要想着练习了，想着星光吧！"
    hide b2 with dissolve
    u2"星光闪闪，并不璀璨，我们的歌声不知飘向何处。"
    u2"又是平凡却充实的一天。"
    u2"这样就好。"
    u2"但今年的六月，注定不会平凡吧……"
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    scene bg2 with fadehold
    u2"六月有两件大事。"
    u2"一是六月十二日，要给晚晚过生日。"
    u2"那一天，除了我们私下的庆祝，还有一场她的个人演唱会。"
    u2"第二件大事是在月末，我们终于有机会前往北方都会的鸟巢，在那里举办我们的专场演唱会。"
    u2"两个都是演唱会，对于有着接近两年偶像生涯的我们来说，筹备工作真的太熟悉了！"
    u2"可是最近，好像总有些奇怪的错觉？"
    u2"不知道为什么，有种说不出的安心,又有种莫名其妙的期待。"
    show c3 with dissolve
    c2"拉姐……你醒得好早啊，早安。"
    hide c3
    show b2
    b2"早安！"
    hide b2 with dissolve
    u2"昨天晚上唱过歌以后，珈乐也来我的房间睡觉了。"
    show c5
    c2"为什么感觉拉姐好像很兴奋的样子？已经在期待舞台了吗？"
    hide c5
    show b1
    b2"不知道！但是，我有一种直觉，好像有什么绝妙的灵感在接近我！"
    hide b1
    show c1
    c2"灵感？是新舞蹈吗？"
    hide c1
    show b3
    b2"乐，你有没有想过，自己能跳出一支惊世骇俗的舞来？"
    hide b3
    show c3 with dissolve
    c2"哇！拉姐……已经强到这个地步了吗？"
    hide c3
    show b10 with dissolve
    b2"没有啦……只是好像抓住了一丝感觉，可是……我甚至连它是什么都形容不出来，好烦！"
    hide b10
    show c1 with dissolve
    c2"为什么会突然想到这个？"
    hide c1
    show b2
    b2"我也不知道……不然怎么叫灵感嘛！"
    hide b2
    show c1
    c2"那我先去练歌了，真是难得看到拉姐醒这么早，还这么有精神！"
    hide c1
    show b1 with dissolve
    b2"好，加油！"
    hide b1 with dissolve
    u2"珈乐每天都醒得很早，然后去天台上练歌。"
    u2"她唱歌真的很厉害，她也真的很爱唱歌。"
    u2"大概我对练舞也是这样的情感。"
    scene bg3 with fade
    u2"胡思乱想的时候，我不知不觉已经来到了训练室。"
    u2"跳出优美的舞蹈，靠的并不是天赋，而是勤奋刻苦的练习。"
    u2"很少有人能够走到那个需要天赋的境地。"
    u2"如果需要用到天赋，那么优美已经不足以形容跳出的舞蹈了吧？"
    u2"或许该叫做、绝妙？"
    u2"我也开始做起早餐前的训练，如果自己没有努力，又怎么能奢望灵感眷顾自己呢？"
    u2"贝拉，今天也要加油！"
    u2"我刚要开始练习，训练室外就传来了脚步声。"
    show a11 with dissolve
    a2"拉姐你来得好早！"
    hide a11
    show b2 with dissolve
    b2"晚晚也是，这么早就来训练啦！"
    hide b2
    show a21 with dissolve
    a2"嗯！之后有很重要的演出，这个月可不能松懈了！"
    hide a21 with dissolve
    u1"拉姐也是这样想吧？不然，她又为什么会来的这么早？"
    u1"或者说……她一直都是这样吗？"
    u1"不过，眼下的重要事项，可不需要考虑太多——"
    u1"第一件重要的事情，准备生日演唱会。"
    u1"第二件重要的事情，准备月末的演唱会。"
    u1"总结一下，过生日只是给我的庆祝活动，生日那天，有一场关键的演唱会必须要做好准备！"
    u1"再加上月末的演唱会，这一个月的重要事情只有训练，"
    u1"练舞、练歌，这是作为偶像的基础，一天都不能荒废！"
    u1"其实，我也很好奇她们会给我准备什么生日的惊喜，但！理性告诉我，要克制住胡思乱想，把精力投入到训练之中！"
    u1"不管怎样，等到那一天，所有的一切都会仿佛扑面而来吧！"
    scene bg3 with fadehold
    stop music fadeout 3.0
    u1"直到六月十二日，每一天都是平静无波的训练生活……"

    scene sta with fadeholdd
    u1"终于到了这一天！"
    u1"2022年6月12日，我，向晚，十九岁了！"
    u1"嗯……其实早在十几个小时前我就已经十九岁了。"
    u1"现在的我，已经登上演唱会的舞台！"
    play music "audio/Medusa.ogg" fadeout 1.0 fadein 2.0
    u1"……"
    u1"一切都十分顺利，要开始唱歌了！"
    show a21 with dissolve
    a1"有时也会厌烦逆来顺受的自己……"
    scene sta2 with fadehold
    u "是这首歌……"
    hide a21 with fade
    show a51
    a"请来一束追光，照亮这海底……"
    hide a51 with fade
    u "你……为的是那个约定吗？向晚……"
    show a11 with fadehold
    play music "audio/第四约定.ogg" fadeout 1.0 fadein 1.0
    a"谢谢大家的陪伴，今天的生日过得很开心！"
    hide a11
    show a21
    a"希望我们也可以一起度过更多个生日，大家也要快乐地过好每一天！"
    hide a21
    show a141
    a"晚安啦！"
    hide a141
    scene oce2 with fadehold
    u "必须这样……结果如何，我不知道，我只能尽我所能……晚晚……你会允许我这样称呼你吗？"

    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    scene res with fadehold
    show b2 with dissolve
    b2"演唱会结束了，我们去接她回来吧！"
    hide b2
    show c1
    c2"好，演唱会很完美，看到我们准备的生日礼物，晚晚一定会很高兴的。"
    hide c1
    show b1
    b2"那是我们一起过去，还是我先去接她？"
    hide b1
    show d21
    d2"拉姐先去吧，我们在这里给她一个惊喜！"
    hide d21
    show b2
    b2"那你们藏好了，我带她来休息室！"
    hide b2
    show e1
    e2"拉姐放心吧！"
    hide e1
    show b3
    b2"好，那我先走了。"
    scene zl with fade
    u2"很快，我来到了那条走廊。"
    u2"从演唱会舞台离开，来到后台，回到休息室，一定会经过这里。"
    u2"……"
    play music "audio/Qm.ogg" fadeout 2.0 fadein 3.0
    scene zl with fade
    u2"嗯？"
    u2"怎么回事？好像是灯突然灭了一下。"
    u2"又像是我自己晕了一下……"
    u2"可能是最近有些太累了，还是要注意休息的。"
    u2"晚晚还没有出来吗？我以为会在这里就遇到呢。"
    u2"好慢啊，晚晚。"
    u2"我加快了脚步，穿过走廊、"
    u2"后台，"
    scene sta3 with fade
    u2"来到了空无一人的舞台。"
    u2"咦……晚晚呢？"
    u2"我四处观望，却完全看不到她的身影。"
    u2"这么晚了，她会去哪里？"
    u2"有些担心，先给她打个电话吧。"
    u2"您拨打的用户暂时无法接……"
    u2"和平时忘带手机不一样。"
    u2"如果是忘了带手机或者没电，不会是“无法接通”的。"
    show b10 with dissolve
    b2"晚晚！"
    hide b10
    u2"空旷的会场里，只有我的声音隐隐回荡着。"
    u2"没有回应。"
    u2"她会不会躲在观众席里和我开玩笑？"
    u2"我冲进观众席中，除了一排排空荡荡的座椅，什么也没有。"
    u2"她会不会没有回后台，而是从正门走掉……"
    u2"想不出任何理由，但抓着这一丝可能性，我还是冲出了会场。"
    scene rof with fade
    u2"正门上的天台，能看到夜晚的枝江……"
    u2"真的从这里离开，又怎么能找到一丝踪迹呢？"
    u2"尽管有一头冲进这夜色找人的冲动，但是理性告诉我，我还是应该回去和队友们商讨一下。"
    scene res with fade
    show b10 with dissolve
    b2"晚晚回来了吗？"
    hide b10
    u2"回到休息室，我四处搜寻着她的身影。"
    show e1 with dissolve
    e2"什么？拉姐你……没找到晚晚？"
    hide e1
    show b9
    b2"乃琳你别骗我！我现在真的很着急！她一定是回来了吧？告诉我实话！"
    hide b9
    show e5
    e2"拉姐你先别着急……我真的没骗你，晚晚她确实没有回来。"
    hide e5
    u2"我知道这个表情，虽然乃琳喜欢和我开玩笑，但是，她现在这认真的样子，就一定没有骗我。"
    u2"我倒希望她是在骗我……"
    u2"我转头看了看嘉然和珈乐。"
    show c2
    c2"她说的是真的，晚晚确实没有回来。"
    hide c2 with dissolve
    stop music fadeout 2.0
    u2"……"
    u2"我不知道我现在是什么样的表情。"
    u2"有一瞬间，甚至连头脑也好像宕机了。"
    show d31 with dissolve
    d2"拉姐……我们分头去找找吧？"
    hide d31
    show b4
    b2"不……一起去找！"
    b2"晚晚突然找不到了，你们不能也……"
    hide b4
    show c7
    c2"好，那我们一起去。"
    hide c7 with dissolve
    play music "audio/Qm.ogg" fadeout 2.0 fadein 2.0
    scene bg32 with fade
    u2"训练室。"
    scene bg5 with dissolve
    u2"天台。"
    scene bg4 with dissolve
    u2"我的房间。"
    scene bg1 with dissolve
    u2"晚晚的房间……"
    u2"没有线索，完全找不到……"
    scene res with fade
    u2"又一次回到休息室，我很想要就这样坐倒在椅子上。"
    u2"……但是还不行，我是队长。"
    u2"我自己没什么的……即使是那一次受伤，我也仍然没有放弃舞蹈！"
    u2"现在怎么可能会放弃寻找？"
    u2"我……是绝对不会输的！"
    show e2 with dissolve
    e2"拉姐，要不要先休息一下？我们这样盲目地找不是办法……"
    hide e2
    show b13
    b2"不能停下来，这才刚刚到哪里？"
    hide b13 with dissolve
    u2"在这种时候，我必须要站出来，亲自冲在最前面。"
    u2"因为我是队长，保护她们是我的职责。"
    show b10 with dissolve
    b2"我知道……你们可能因为寻找没有头绪就想要放弃了。"
    hide b10
    show b9
    b2"但是，没有什么是可以一帆风顺而成功的。"
    b2"比如我，从一个受伤的芭蕾舞演员，在最灰暗的时光里坚持下来，直到今天，成为了A-SOUL的队长。"
    hide b9
    show b1
    b2"而且，我们能有今天，大家也不会忘记了在出道前的训练，还有刚刚出道时经历的那些挫折吧？"
    b2"大家想想这一切……"
    hide b1
    show b3
    b2"是什么让我们成长起来，变得强大？"
    b2"最近一年的时光里，我们一直在进步，一直在走向更大的舞台。"
    hide b3
    show b10
    b2"但是，大家不能因为过上了好日子，就丢失了我们最初的坚强和韧性。"
    hide b10
    show b9
    b2"更何况，现在消失的是晚晚，是我们不能缺少的成员。"
    hide b9
    show b2
    b2"所以，别放弃，我们再找一遍！"
    hide b2
    show c1 at left
    show e1 at right
    show d11
    z"好！"
    scene res with dissolve
    u2"这一番鼓励果然有效果。"
    u2"不止是大家，我也仿佛热血沸腾。"
    u2"但是……"
    scene bg32 with fade
    u2"训练室。"
    scene bg5 with dissolve
    u2"天台。"
    scene bg4 with dissolve
    u2"我的房间。"
    scene bg1 with dissolve
    u2"晚晚的房间……"
    u2"一次几乎毫无悬念的重复。"
    u2"我刚刚说的每一个字仿佛都在嘲笑着我。"
    scene res with fade
    u2"又一次回到休息室。"
    show c7 with dissolve
    c2"拉姐……"
    hide c7
    u2"她拽住我的衣袖。"
    show b5 with dissolve
    b2"大家……再找一遍。"
    hide b5 with dissolve
    scene res with fadehold
    u2"……"
    u2"又是一遍，全无新意的重复。"
    u2"怎么会这样？"
    u2"完全没有头绪的挫败……"
    u2"不，还没有。"
    u2"我不能停下来。"
    u2"只要我还没停下来，就没有输。"
    u2"我不会输……"
    show b5 with dissolve
    b2"还没有结束……我不停下来……"
    hide b5
    show b6
    b2"我就不会输……"
    hide b6
    show d31
    d2"拉姐？"
    hide d31
    show b5
    b2"然然……你想说什么？"
    hide b5
    show d51
    d2"……没，没什么的。"
    hide d51 with dissolve
    u2"她好像欲言又止，但是，我不能停下。"
    u2"最大的敌人往往是自己，在与自己的战斗里我不能退缩……"
    u2"我向着门口走去。"
    show e5 with dissolve
    e2"贝拉！"
    hide e5 with dissolve
    u2"我被用力地拉住了。"
    u2"我转过身，乃琳盯着我，胸口不断起伏着。"
    show e3 with dissolve
    e2"你清醒一点！别再做毫无意义、自我感动的努力了！"
    hide e3
    show b5
    b2"你……你说什么？有没有意义可不是你能够断言的！"
    hide b5
    show e3
    e2"你照镜子看看自己的样子！"
    e2"如果你做的事情有意义，你就不会在乎我“无所谓”的评价。"
    e2"如果你不是已经自我感动，就更不会对我的话感到生气！"
    hide e3
    show b5
    b2"我知道……哈哈，就是我的问题……"
    hide b5
    show b6
    b2"是我在自我感动，做没意义的努力。"
    hide b6
    show b7
    b2"来，你告诉我，告诉我你合理的、有意义的、计划、"
    hide b7 with dissolve
    u2"说出这几句话，声音甚至不受控制地打颤。"
    show e6 with dissolve
    e2"我……"
    hide e6 with dissolve
    u2"她突然扩张的瞳孔显得有些失神。"
    u2"是在害怕我吗？"
    u2"我好像……确实说得有些过分……"
    show c8 with dissolve
    c2"队长、乃琳……大家不要吵架……"
    c2"我知道现在，大家都不好受，"
    c2"但越是这种时候，我们才越该冷静下来，去想想办法的……"
    hide c8 with dissolve
    u2"珈乐哭了。"
    u2"我顿时清醒了许多，“队长”，她们已经好久没有这样称呼我了。"
    u2"刚刚的一切，的确不是队长该有的做法。"
    show e2 with dissolve
    e2"没错，你是我们的队长啊！你都这样失去了理智，我们该怎么办？"
    hide e2
    show b10
    b2"对不起，是我太冲动了……"
    b2"大家先在这里坐下吧，演唱会结束以后，大家还没有吃过东西。"
    hide b10
    show b13
    b2"……我们一边吃饭，一边想一想接下来该怎样做吧。"
    hide b13 with fade
    u2"休息室里摆满了丰盛的菜肴，现在已经凉了。"
    u2"本是给晚晚准备的庆功宴……"
    show b10 with dissolve
    b2"能找的地方，我们都已经找过了，大家还有什么别的办法吗？"
    hide b10
    show d31 with dissolve
    d2"我们要不要给晚晚的家里打一个电话？"
    hide d31
    show e2
    e2"我觉得不妥，如果晚晚要回家，她一定会告诉我们，而且，她的父母也支持她和我们一起，不可能偷偷把她接走的。"
    hide e2
    show b10
    b2"没错，所以晚晚不可能偷偷回家，如果打了电话，反倒会让她的家人担心……"
    hide b10
    show c2
    c2"那怎么办？我们现在也没有什么别的办法，不然……我们报警？"
    hide c2
    show e5
    e2"不……"
    hide e5
    show c7
    c2"怎么了？"
    hide c7
    show e5
    e2"直觉……这件事情太过奇怪，直觉告诉我，报警解决不了问题，只会带来更多的麻烦。"
    hide e5
    show b10
    b2"但是这直觉有依据吗？至少要有一个、微小的缘由？"
    hide b10
    show e5
    e2"最近几天……我总是遇到奇怪的事情。"
    hide e5
    show b10
    b2"嗯，乐和我说过，那天你们去准备午餐的时候，有一个红衣女人。"
    hide b10
    show e5
    e2"是的……她问了我一些奇怪的问题，就像是猜谜语一样。"
    hide e5
    show b10
    b2"她说了什么？"
    hide b10
    show e2
    e2"我记不清……她离开以后，那些话就像在我脑中被消除了一样。"
    e2"如果说，我真的感受到了什么，大概是……"
    hide e2
    show b9
    b2"大概是？"
    hide b9
    show e5
    e2"这个世界的一切常识与法则，好像并不是那么牢不可破。"
    hide e5
    show b10
    b2"……"
    hide b10 with dissolve
    u2"一时间，我不知道该说什么。"
    u2"心中泛起莫名的寒意。"
    show b10 with dissolve
    b2"你是说……或许有这样一种可能，我们是虚假的，只是活在梦里？"
    hide b10
    u2"我说出这句话以后，嘉然和珈乐都变了脸色。"
    show e2 with dissolve
    e2"拉姐别乱猜啊！世界当然是真实的，我要说的是……"
    stop music fadeout 1.0
    e2"神灵，或者某种高级的生命……可能真的存在。"
    hide e2 with dissolve
    u2"我不知道这个可能，与我刚刚的猜测哪个更加可怕。"
    play music "audio/Qm.ogg" fadeout 2.0 fadein 2.0
    show e5 with dissolve
    e2"在刚刚寻找晚晚的时候……我还收到了一封奇怪的短信。"
    hide e5
    show b10
    b2"我们一起来看一看。"
    hide b10 with dissolve
    show mb with dissolve
    u2"8873788985"
    u2"水是媒介。"
    u2"249142521"
    hide mb
    show b10 with dissolve
    b2"水是媒介？就只是这样？"
    hide b10
    show d31
    d2"好奇怪，号码不像是正常的号码，结尾的数字也意义不明……"
    hide d31
    show e5
    e2"恰好在今天收到奇怪的短信，我觉得并不是巧合。"
    hide e5
    show c3
    c2"……不管怎样，我们还在一起，我相信一定能找到办法的。"
    hide c3
    show b1
    b2"大家说的没错，不过，现状是然然说的那样——"
    hide b1
    show b10
    b2"这封短信意义不明。"
    b2"所以……我有一个想法。"
    hide b10
    show b9
    b2"月末演唱会里，我们的新团舞，也应该做好四人编舞的准备……"
    b2"大家怎么想？"
    hide b9
    show c7
    c2"如果……拉姐这样决定，我……"
    c2"没有异议。"
    hide c7 with dissolve
    u2"我又看向乃琳，她和我对视一眼，就把头低了下来。"
    show d61 with dissolve
    d2"拉姐。"
    hide d61
    show b1
    b2"然然怎么想？"
    hide b1
    show d61
    d2"四人编舞……尤其是那一支舞……我不能同意。"
    d2"A-SOUL的团舞，不可能不是五个人的。"
    hide d61
    show b10
    b2"我知道。这对我来说也是最坏的考虑……但是，我们必须有后备的计划。"
    hide b10
    show d61
    d2"我明白，但是，拉姐能不能给我一个机会？"
    d2"我要去找线索，我会努力不被感情影响判断的……拉姐，再给我两天时间可以吗？"
    hide d61 with dissolve
    u2"她虽然是在发问，但是语气却无比坚决，我没有办法拒绝。"
    u2"然然一直都很听话……好久没见她如此坚定自己的意见了。"
    show b1 with dissolve
    b2"好，我相信然然。"
    b2"今天到此为止吧……大家也一定很累，吃完后大家就去休息吧。"
    play music "audio/Zki.ogg" fadeout 3.0 fadein 3.0
    scene bg41 with fadeholdd
    u2"……"
    u2"回到自己的房间，今天的经历开始在我脑中闪回。"
    u2"……主要是演唱会之后的部分。"
    u2"水是媒介，还有那两串奇怪的数字……"
    show mb with dissolve
    u2"是什么意思呢？"
    hide mb with dissolve
    u2"看着乃琳刚刚共享给我们的短信内容，我开始思考，"
    u2"却什么都想不出来。"
    u2"不过，忽然留意到，房间中的星星灯好像有些黯淡。"
    u2"星星会寂寞吗？"
    u2"……今天明明很累了，却还是全无睡意。"
    u2"晚晚一个人联系不上我们，她会害怕的吧？"
    u2"忽然，想要去找她们一起睡觉了。"
    u2"虽然是毫不现实的担心，但我还是害怕、自己突然在不认识的地方醒来……"
    u2"如果和她们一起，就不会害怕了。"
    u2"想去找然然，可她那么认真地说要去找线索，我居然有些不敢去找她……"
    u2"她和晚晚平时有些害怕我，难道也是这种心理吗？"
    u2"……去找乃琳吗？她会不会还在生我的气呢？"
    u2"我那个时候……真的太急了……"
    u2"最后，还是决定去找乐一起。"
    stop music fadeout 1.0
    play sound "audio/qiaomen.ogg"
    u2"嗵嗵嗵——"
    u2"谁在敲门？"
    n"拉姐睡了吗？"
    u2"乐居然来了！"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene bg4 with dissolve
    show b2 with dissolve
    b2"我还没睡！正想要去找你呢！"
    hide b2 with dissolve
    u2"珈乐推门而入，随手打开了大灯。"
    show c4 with dissolve
    c2"你现在还好吗？"
    hide c4
    show b10
    b2"我……"
    hide b10 with dissolve
    u2"怎么可能会好？但是……"
    show c4 with dissolve
    c2"拉姐不要再逞强了，我知道拉姐很厉害，但不要总是这样勉强自己。"
    hide c4
    show b10
    b2"但是我是队长……这一次，本该处理得更好，可我却没有做到……"
    b2"只是带着大家训练是不够的，我本该保护好大家的。"
    hide b10
    show c5
    c2"十全十美永远不该成为必须完成的任务。你又不是真的机器人。"
    hide c5
    show b13
    b2"如果可以，我真的希望自己是机器人。"
    hide b13
    show c6
    c2"但是我不希望！"
    hide c6 with dissolve
    u2"珈乐忽然变得十分坚决。"
    show c4 with dissolve
    c2"我心中的队长不是不会错的机器，而是贝拉。"
    hide c4
    show b10
    b2"可我今天还是让乃琳生气了……而那的确是我的错。"
    hide b10
    show c5
    c2"她没有怪你哦。"
    hide c5
    show c4
    c2"拉姐，你看这个。"
    hide c4 with dissolve
    u2"说着，她拿出一个精致的小盒子，看起来像是糖果盒。"
    show b1 with dissolve
    b2"这是什么？"
    hide b1
    show c4
    c2"乃琳一直在自责，为了刚刚她冲动下说出的话。但是她不敢来找拉姐道歉，就让我把这一盒糖果带来。"
    hide c4
    show b10
    b2"这……这样吗……我并没有怪她，刚刚的确是我的错……"
    hide b10 with dissolve
    u2"我接过糖果盒，心里暖暖的，想说话却有些哽咽。"
    show c5 with dissolve
    c2"别这样，拉姐，乃琳和我都不想看见你这样责怪自己。"
    hide c5
    show c3
    c2"我来到这里就是要说一件事——"
    hide c3
    show c4
    c2"我们已经认识这么久了，拉姐还是不愿意更多地依靠我们吗？"
    hide c4
    show b2
    b2"没有的事情……"
    hide b2
    show c1
    c2"拉姐，我们一直都会支持你的，这些事情不要自己扛着，我们是一个整体。"
    hide c1
    show b1
    b2"嗯……我明白。"
    hide b1
    show c1
    c2"“我们是A-SOUL”，这不只是一句口号的。拉姐……今天我可以留在这里陪你吗？"
    hide c1
    show b2
    b2"当然了！谢谢你这样说……我真的很开心！"
    hide b2 with dissolve
    play music "audio/第四约定.ogg" fadeout 3.0 fadein 3.0
    scene oce5 with fadeholdd
    u1"……"
    u1"？？？"
    show a41 with dissolve
    a1"这……是哪里？"
    hide a41 with dissolve
    u1"演唱会太过投入，出现幻觉了吧……"
    u1"我忙用手揉了揉眼睛，又用力眨了眨，"
    scene oce6 with dissolve
    u1"但是视线之中，反而逐渐清晰。"
    u1"尽管很奇怪，心中却有种莫名的宁静感。"
    u1"就好像是……久别重逢？"
    u1"我被水流包裹着，四处是闪光的小鱼、珊瑚。"
    u1"还有在我身边围成一团的水母。"
    u1"应该是海底吧？"
    u1"但是，我为什么会在这里？"
    u1"我明明才结束了自己的生日演唱会，正在回去的路上……"
    u1"而且，我居然能够呼吸？"
    u1"这一定是做梦吧……"
    show a141 with dissolve
    u1"什么嘛！原来是做梦呀。"
    hide a141
    u1"不对！"
    u1"以我以往做梦的经验，即使我能够意识到自己是在做梦，也不会这么快记起之前发生的事情！"
    u1"而且，更关键的一点是，如果是在梦里，水中呼吸就会被当作理所当然的常识！"
    u1"这一次显然不是做梦……"
    u1"……但是，不管怎么说，这里还是很美的嘛。"
    u1"从惊异之中渐渐恢复，我开始去认识这个……"
    scene oce3 with dissolve
    u1"新世界。"
    u1"居然有人！"
    show f0 with dissolve
    u1"高高的石头上，她独自坐在阴影里。"
    u1"一动不动。"
    u1"阴影中，我看不清她的脸。"
    hide f0 with dissolve
    show a41
    a1"你是谁？"
    hide a41
    show f0 with dissolve
    n1"……我是■……"
    hide f0 with dissolve
    u1"她的声音就好像被水流冲散了一样，我并没有听清她的名字。"
    show a21 with dissolve
    a1"抱歉，我没有听清楚！可以大声些吗？我叫向晚！"
    hide a21
    show f0 with dissolve
    n1"……"
    hide f0
    show f4 with dissolve
    n1"我的名字是……四。"
    hide f4 with dissolve
    u1"我最初的勇气与冲动渐渐消散，在她开口以后，那种宁静的气场也变得飘忽起来。"
    u1"她来到我的身边，我终于看清她的样子，我能确认，这是我此生仅见的奇异生命。"
    u1"从见到她的那一瞬间，我便有了种不知源起的熟悉感。"
    u1"可这种熟悉是不真实的，当我尝试将她与记忆中寻到的模糊印象对比，我更加相信这是初次见面。"
    u1"仿佛是源于梦境的既视感。"
    u1"我望着那极致美丽的生物。"
    u1"极致美丽，却莫名阴暗。"
    u1"她有人类最完美的身材，却散发着迥异于人类的气质。"
    u1"若是神灵，她的阴暗让我无法忽视，"
    u1"若是鬼魂，却有着令我惊艳的圣洁……"
    show a151 with dissolve
    a1"初次见面，你好……这是哪里？"
    hide a151
    show f4 with dissolve
    f1"这里是……"
    hide f4 with dissolve
    u1"她说了一半，却忽然陷入了沉默。"
    u1"沉默了许久，身影也愈加飘忽。"
    u1"难道她在紧张吗？"
    u1"甚至和我一样，她不但没有预想过这次相遇，更不属于这里？"
    u1"但是，她与这世界的气质如此相似，"
    u1"直觉告诉我她属于这里。"
    show f1 with dissolve
    f1"这里是、始源的海，是正反狭缝之中的世界。"
    hide f1
    show a141 with dissolve
    a1"不好意思，我听不太懂你讲的话……"
    hide a141
    show a21
    a1"不过，我本来以为你和我一样，也是不了解这里呢。"
    hide a21
    show f4 with dissolve
    f1"那些概念……无所谓的，"
    hide f4
    show f1
    f1"欢迎你来到这里。"
    hide f1
    show a11 with dissolve
    a1"哦……好、谢谢你。"
    hide a11 with dissolve
    u1"“欢迎”这个词听起来还是怪怪的。并不是我自己选择来到这里游玩，更像是我不小心掉入了这里。"
    u1"只是这个世界真的好奇怪啊！"
    u1"除了四，我只看到了不计其数的水母和鱼。"
    u1"更奇怪的是，这像是深海的世界里，居然有着闪烁辉光的天空与星星。"
    u1"也许我真的是在做一个完全清醒的梦也说不定……"
    u1"月末的演出，不论如何准备充分，都不能够完全放心。"
    u1"在北方都会的专场演唱会，是我们一直以来的梦想。"
    u1"……没有压力是绝不可能的！"
    u1"也许、是天意让我做一个奇异又美丽的梦来放松心灵吧？"
    show a21 with dissolve
    a1"这里有好多水母。"
    hide a21
    show f1 with dissolve
    f1"嗯，它们在发光。"
    hide f1
    show a141 with dissolve
    a1"说起来，我还为水母写过一首歌呢。"
    hide a141
    show f9 with dissolve
    f1"真的吗？为什么会为水母写歌？"
    hide f9 with dissolve
    u1"为什么会为水母写歌？如果是那个理由……谁都不会相信的吧？"
    u1"而且、那大概只是个儿时的梦，"
    u1"连我自己都记不清晰。"
    show a51 with dissolve
    a1"为了水母写歌，说起来也没什么啦……"
    hide a51
    show a21
    a1"我之前表演过一个水母的模仿，本来只是随便玩的……但是出乎意料，大家都很喜欢，我也就写了一首歌，没什么的……"
    hide a21
    show f1 with dissolve
    f1"是这样啊。"
    hide f1 with dissolve
    u1"她这样说着，平静的话音听不出来是什么心情。"
    u1"是失望吗？但阴影之下，她的嘴角好像轻轻扬了扬。"
    show f1 with dissolve
    f1"突然来到这里，不会惊慌吗？"
    hide f1
    show a21 with dissolve
    a1"嗯……这里似乎能够让人平静下来。"
    hide a21
    show a11
    a1"倒不如说，我比平时还要冷静。"
    a1"没有任何的关系与身份，我只是我自己。"
    hide a11
    show a51
    a1"就好像是做梦一样。"
    hide a51
    show f9 with dissolve
    f1"但这里不是你的梦哦。"
    hide f9 with dissolve
    u1"她意味深长地笑了。"
    show f1 with dissolve
    f1"会察觉这里是所谓梦境，是因为这深海的世界不合常理吧？"
    hide f1
    show a151 with dissolve
    a1"没错，我本不可能像这样在水中呼吸的……"
    a1"所以，这也许是个清醒的梦。"
    hide a151
    show f1 with dissolve
    f1"据说在清醒的梦境里，人可以做到任何自己相信的事情。"
    hide f1
    show f2
    f1"你相信自己会飞吗？"
    hide f2
    show a41 with dissolve
    a1"不……我现在没办法相信这个。"
    hide a41 with dissolve
    u1"我几乎从没有像现在这样清醒冷静过，我甚至想象不出飞行该如何发力，当然不可能相信自己会飞啊！"
    show f2 with dissolve
    f1"那现在呢？"
    hide f2 with dissolve
    u1"有一个瞬间，亮光在她的身上一闪而逝。"
    u1"同时，我的脑中好像被清晰刻印了有关飞行的知识。"
    show a21 with dissolve
    a1"我……我真的会飞了……"
    hide a21
    show f1 with dissolve
    f1"试试看。"
    hide f1
    show a141 with dissolve
    a1"好！"
    hide a141 with dissolve
    u1"兴奋、期待，我按照那种方式尝试飞起。"
    u1"……"
    show a121 with dissolve
    a1"什么嘛，还是飞不起来呀。"
    hide a121 with dissolve
    u1"虽说是理所当然，但还是有一点点失落的。"
    show f3 with dissolve
    f1"刚刚只是向你证明，这里不是梦境。"
    hide f3
    show a151 with dissolve
    a1"嗯……我相信了……"
    hide a151
    show f1 with dissolve
    f1"不过我没有骗你，现在你真的可以飞了。"
    hide f1 with dissolve
    u1"但是，"
    u1"确认了不是梦境，我已经不敢在这虚假的宁静中继续沉醉下去了！"
    u1"虽然确实有些在意“能飞”这件事，但也只是有些在意的程度……"
    show a41 with dissolve
    a1"这里不是梦……那么我的队友找不到我，她们一定会很着急的！"
    hide a41
    show f1
    f1"是为了月末的演出吗？"
    hide f1
    show a151
    a1"嗯，我们还要排练舞蹈，如果我不在，会给大家添麻烦的！"
    hide a151
    show f9
    f1"我明白你的担心，但是，有很多人关心你，你现在相信她们就好。"
    hide f9
    show a161
    a1"正因为大家关心我，我才更不该成为大家的麻烦……"
    hide a161
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene oce with pixellate
    a1"诶？这是……"
    u1"眼前突然亮起了柔和的光，世界也随之扭曲、重组，"
    u1"仍然是这海的世界，却比刚刚更加奇异。"
    u1"倒悬在上的建筑群、看不到尽头的由水母铺成的粉色的路……"
    show f1 with dissolve
    f1"再次介绍一下我自己，我的名字是四，数字四，正是我带你来到的这个世界。"
    hide f1 with dissolve
    u1"这一次更正式的相识后，我才真的意识到她是多么美丽的生灵。"
    u1"不只是因为她，更是因为这个世界。"
    u1"尽管早就有过准备，心中仍是不免惊叹不已。"
    u1"但是，现在有更重要的问题。"
    show a151 with dissolve
    a1"四……为什么会带我来到这里？"
    hide a151 with dissolve
    u1"虽然名字很奇怪，但四并不像是坏人。"
    u1"我想，她一定有着合适的原因吧？"
    show f3 with dissolve
    f1"带你来到这里，有着若干个原因……"
    hide f3
    show f6
    f1"其中一个是，你引起了危险分子的关注。"
    hide f6
    show a151
    a1"危险分子？如果有证据，是可以报警的吧？"
    hide a151
    show f17
    f1"那么如果贝拉现在报警，能带你回到原先的世界吗？"
    hide f17
    show a161
    a1"……不能。"
    hide a161 with dissolve
    u1"答案还是很显然的。"
    show f1 with dissolve
    f1"带你来到这里，对我来说是轻而易举的事情。"
    hide f1
    show f3
    f1"但即使是我，也不能忽视那个关注你的危险分子，所以你明白她的危险性了吗？"
    hide f3
    show a141
    a1"那个危险分子是谁呀？"
    hide a141
    show f1
    f1"谈这个以前，你先回答我。你害怕鬼吗？"
    hide f1
    u1"我很想说不怕的，但是，在她的面前，我完全没有逞强的意义。"
    show a121
    a1"嗯，我很害怕鬼……每次和队友讲怪谈，我都很害怕……"
    hide a121
    show f6
    f1"而她是一个比任何构思的鬼魂都更强大、更直观、也更冷血的灵体，即使是我也无法猜测她的目的。"
    hide f6
    show a141
    a1"可是我只是普通的人，为什么会……"
    hide a141
    show f3
    f1"所以我才会担心。"
    f1"她对你当然不会怀有恶意，但是与她产生联系，可能就会被当作赌注、当作筹码，毫无意义地被牺牲掉，这才是我担心的事情。"
    hide f3
    show a141
    a1"原来是这样，虽然我还不是很明白……不过谢谢你！"
    hide a141
    u1"还是有些抱歉的……她那么认真想要警告我，我还是很难警觉起来。"
    show f9
    f1"你不要谢我……"
    hide f9
    show a151
    a1"为什么？"
    hide a151
    show f3
    f1"你知道我为什么那样了解她吗？"
    hide f3
    show a151
    a1"……我不知道。"
    hide a151
    u1"但是，我内心的最深处却仿佛已经知道了。"
    show f6
    f1"因为我和她是同类的灵体。"
    hide f6
    u1"她说出这句话，我并没有觉得惊讶。"
    show a161 with dissolve
    a1"我明白了……四其实也很矛盾吧？"
    hide a161
    show f4
    f1"嗯？"
    hide f4
    show a161
    a1"让我来到这里，是四想要保护我。但是四和那个灵体又是同类的存在，而我和四产生了联系，也算是被卷入了这件事情。"
    hide a161
    show f10
    f1"你说得对，抱歉……"
    hide f10
    show a141
    a1"不要说抱歉的话啦。我并没有责怪的意思。"
    hide a141
    show a21
    a1"相反，我很感激哦。"
    hide a21
    show a11
    a1"说起来，从我第一眼见到你的时候，就总有一种奇异的感觉。"
    hide a11
    show a51
    a1"虽然我们是第一次见面，却有种熟悉与安宁的情绪。"
    hide a51
    show a21
    a1"所以我相信四是好人！"
    hide a21
    show f1
    f1"谢谢你这样说。我在今天给你许下一个承诺："
    hide f1
    show f17
    f1"希望你可以相信我，在此之后，不论是那个灵体的事情，还是月末的演出——"
    hide f17
    show f2
    f1"不论我最后怎样，我都会承诺给你最完美的结果的！"
    hide f2
    show f20
    f1"……还有，生日快乐！"
    hide f20
    show a141
    a1"……谢谢你。"
    hide a141 with dissolve
    u1"然后，她向我伸出手——"
    u1"仿佛透明的手掌是奇异的颜色。"
    u1"有些发凉，但是很柔软，很光滑。"
    u1"嗯……是一种让我不想放开的感觉。"
    u1"只是……这种温柔，会不会突然消失在星辰中呢？"
    u1"突然、起了奇怪的联想……"
    show f1 with dissolve
    f1"人类那边的时间已经不早了，我先送你去休息。"
    f1"不论是困惑，还是什么想法，都留待明天吧。"
    hide f1
    show a11
    a1"好。"
    hide a11 with dissolve
    scene bg7 with fadehold
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    u1"咦……这是？"
    u1"我的房间？"
    u1"有一个瞬间，我以为回到了自己的世界。"
    u1"但是，窗外的一片深蓝告诉我，这里只是我的房间的复制品。"
    u1"仍然有很多在乎的事情。"
    u1"离我的消失已经有几个小时了吧？"
    u1"我的队友们……"
    u1"如果可以的话，至少希望能让她们不要担心我。"
    u1"拿出手机，果然没有任何信号。"
    u1"……不然的话，她们一定早就联系我了。"
    u1"我有些麻木地坐在床上。"
    u1"静静地听着，听见窗外隐隐传来鲸的歌声。"
    u1"这里的生物真的是活着的吗？还是仅仅以人的认知构筑的呢？"
    u1"我不知道为什么会想到这些，至少这不是我平时会思考的问题。"
    u1"一个人的时候，就会这样吧？"
    u1"如果以后我也永远活在这里，会不会有一天就大彻大悟了呢？"
    u1"不不不！我怎么可能永远活在这里啊！我还要回到枝江呢！"
    u1"……还是想要有个人说话……"
    u1"好寂寞……"
    u1"我怔怔地倒在了床上，望着天花板。"
    u1"平时我绝对不会在洗澡之前去碰自己的床的。"
    u1"我现在也意识到了这一点，但是我不想去洗澡。"
    u1"……咦？"
    scene bg8 with dissolve
    u1"那边的水母箱……"
    u1"我的房间里也有一个一模一样的，但是我养的是很常见的海月。"
    u1"而这里……"
    u1"海月下方的阴暗之中，是一只幽灵般的大水母。"
    u1"标志一样的四条鬼魅般的触手，我知道，它的名字是冥河。"
    u1"尽管我从未真正见过这种生物，"
    u1"尽管我知道现实中的冥河水母是一种更加巨大的存在，"
    u1"但我确定、它一定就是。"
    u1"并不是幼体之类的，就像被指定成了这样的大小，恰好适合生活在这水母箱中。"
    u1"……但如果是四的所作所为，我也不会感到惊讶。"
    scene bg9 with dissolve
    u1"还是有一些困了啊……"
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 3.0
    scene black with fadehold
    u1"仿佛置身于海底。"
    u1"模糊……诡异，却朦胧又熟悉。"
    u1"大概在多年以前，我便曾来到此处。"
    scene dream with dissolve
    u1"……我知道，这是我在做梦。"
    u1"我不止一次在梦中回到这里。"
    u1"但是我为什么要回来？"
    u1"……"
    u1"我好像漂浮在水中。"
    u1"好冷啊，只有我一个人……"
    u1"也没有别的生物了……"
    u1"……有鱼，却不像是活着的。"
    stop music fadeout 3.0
    scene dream1 with dissolve
    u1"好安静，这孤独的梦境中漂着诡异的水草，像是已经湮灭的深海。"
    u1"在遥远之处好像有光，"
    scene dream4 with dissolve
    u1"我努力想去接近那光点，却控制不住自己，向着更深的黑暗中坠落。"
    u1"然然、拉姐……？"
    u1"想要呼喊她们的名字，却发不出声音。"
    scene black with dissolve
    u1"除了那个名字，没有人听得见我的呼喊……"
    u1"但那是什么？"
    u1"我一定能喊出的，却忘记了内容。"
    u1"……"
    scene bg10 with fadehold
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    show a151 with dissolve
    a1"四……"
    hide a151 with dissolve
    scene bg9 with dissolve
    u1"梦醒了。"
    u1"房间里只有我在。"
    scene bg7 with dissolve
    u1"现在是几点了？"
    u1"我下意识地去摸手机，幸好还可以用。"
    u1"明明之前就知道手机没有坏掉，现在看到它发光的屏幕，仍会感到庆幸。"
    u1"五点四十八分。"
    u1"是一个起床太早，又不愿继续入睡的时间。"
    u1"……我现在格外清醒。"
    u1"刚刚……我到底做了什么梦？"
    u1"是那个熟悉的、模糊的海底般的梦。"
    u1"已经有好久没有见过了。"
    u1"当我熟悉了A-SOUL的大家，成为了现在的我以后，就再也没有做过那个梦。"
    u1"……最早是什么时候呢？"
    u1"……也许是十年前？"
    u1"……"
    u1"……但是在夜晚醒来，发现自己孤身一人，整颗心就像被沉入了海底。"
    u1"如果可以的话，真的好想要找人聊天。"
    u1"四是神明一样的人，她不会睡觉的吧？"
    u1"但是，去哪里找她呢？"
    u1"我试探着推开房门……"
    scene medusa with fadehold
    stop music fadeout 2.0
    u1"一片水的世界。"
    u1"整个屋子的框架也变得透明起来，脚下，是摆动的透明触须。"
    u1"这所谓的我的房间，竟然是一只巨大的水母吗？"
    u1"尽管在这世界中，这应该不算什么特别稀奇的事情。"
    u1"但……看到这种场面，又怎么可能不惊讶？"
    u1"我呆呆地望着眼前这奇异的景象。"
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    show a21 with dissolve
    a1"好美……"
    hide a21 with dissolve
    f1"很高兴你喜欢这里，不过你醒得好早，还没有睡过六个小时，对人类来说很辛苦吧？"
    show a151 with dissolve
    a1"四？我还好……但你在哪？"
    hide a151 with dissolve
    u1"我清楚听见她的声音，却分辨不出方位，也看不见她在哪里。"
    show f1 with dissolve
    f1"我就在你身边。"
    hide f1
    show a161
    a1"哇……是什么时候……这么早，没有睡觉吗？"
    hide a161
    show f1
    f1"知道你醒了，我就来了。我是不需要睡觉的。"
    hide f1
    show a11
    a1"那你平时都做些什么？"
    hide a11
    show f2
    f1"创造，创造一切我想要看见的存在。"
    hide f2
    show a21
    a1"真是自由的生活啊！"
    hide a21 with dissolve
    u1"我由衷赞叹。创造，这就是神明消磨时光的方式吗？"
    show f1 with dissolve
    f1"你看这世界没有寒暑，没有昼夜，如果对应人类的时间，这里的生活是过分缓慢的。"
    hide f1
    show f9
    f1"还有，你看见那些鱼了吗？"
    hide f9
    show a141
    a1"嗯，我看得到！也是你创造的吗？很漂亮！"
    hide a141
    show f10
    f1"果然你也觉得漂亮吧！看那远处的鱼，那样游过来，又渐渐远去，淡出视线，这个过程可能需要十分钟。然后呢，我可能就会看它十分钟。"
    hide f10
    show a151
    a1"不会觉得枯燥吗？"
    hide a151
    show f9
    f1"不会。或许，你有见过嘉然画画？"
    hide f9
    show a21
    a1"嗯，当然见过了！"
    hide a21
    show f1
    f1"她有的时候，也会不知不觉地画上一天吧？"
    hide f1
    show a141
    a1"……好像真的是这样，然然她好厉害的！"
    hide a141
    show f1
    f1"没错，创造或者欣赏，就是这样忘我的事情了。"
    hide f1
    show f2
    f1"更何况我的身体不会疲倦，创造的范围大到这一颗星球，至于创造的内容——"
    hide f2
    show f17
    f1"就像是你熟悉的游戏一样，我可以用类似于贴图的复制粘贴，也可以去刻画出完全不同的细节，甚至可以设下一个规则，按照这个规则，让世界完成自动的演算。"
    hide f17
    show a141
    a1"好厉害！"
    hide a141
    show f9
    f1"……无论如何，这都是个可以永远继续下去的工作，甚至曾经有过，我想要建一幢楼，等到完成的时候，已经过去了一年。"
    hide f9
    u1"将一年的时光沉浸在建一座楼吗？是啊，她可能会用几十年建一座城，用几百年建这一颗星……相比之下……"
    show a151
    a1"你说，人类的存在，应该是无比短暂的吧？"
    hide a151
    show f4
    f1"不，我从来没有这样想过。"
    hide f4 with dissolve
    u1"她真诚地作答，听起来完全不像在撒谎！"
    u1"虽然……我也不太能分辨出别人是不是在说谎。"
    show a151 with dissolve
    a1"你这样永恒的生命，居然不会觉得人类短暂？这是为什么？"
    hide a151
    show f1
    f1"我曾经不关心任何一个人类，对我而言，人类是一种从我存在的日子开始时就已经存在着、也会一直存在下去的概念，是接近于永恒的。"
    hide f1
    show a151
    a1"那你为什么会注意到我的事情呢？还那么了解我的队友们……"
    hide a151
    show f1
    f1"偶然认识你们以后，我为了看每一场直播，开始记住了人类的时间。"
    hide f1
    show f4
    f1"我开始有了关心的个体，于是人类在我眼中，也再不会是短暂的生物。"
    hide f4
    show a141
    a1"原来四也有一直在看我们吗？谢谢你！"
    hide a141
    u1"虽然几乎猜到是这样的，但听她亲口承认，还是超开心！"
    show f4
    f1"当然了！对我来说，你们是重要的存在。"
    hide f4
    show f1
    f1"但还是先不谈这个，说一说你关心的事情吧。"
    hide f1
    show a11
    a1"……好。"
    hide a11 with dissolve
    u1"虽然刚刚谈的事情我也不是不关心……但是面对近在咫尺的神灵，我仍没有反驳的勇气。"
    show f1 with dissolve
    f1"现在的时间对于人类还是太早了，她们应该都在睡觉。"
    hide f1 with dissolve
    u1"我当然知道，她说的“她们”指的就是我的四位队友。"
    show f9 with dissolve
    f1"你要继续休息吗？或者跟着我去四处走一走？"
    hide f9
    show a11
    a1"我现在没有困意……还是先走一走吧。"
    hide a11
    show f2
    f1"好，那至少在这边的世界，我给你与我一样充沛的精力，你现在不需要靠睡眠来保持精神。"
    hide f2 with dissolve
    u1"她话音还没落下，我已经觉察到身体变得格外轻盈。"
    show a21 with dissolve
    a1"哇……真的感受到了，这就是神的力量吗？"
    hide a21
    show f9
    f1"你没有察觉到吗？其实从你离开卧室以后，就已经是在飞的了。"
    hide f9 with dissolve
    u1"！"
    u1"这时我才惊觉，明明没有觉察到水的浮力，我竟然像是呼吸一样自由地浮在空中。"
    u1"我曾经不敢想象的一切，如今，竟然像是本能一样潜藏在我身体的最深处。"
    u1"最初的兴奋过后，我被一股强烈的虚幻感包裹了起来。"
    show a161 with dissolve
    a1"对不起……我不该这样说，但是，为什么在意识到自己像是本能一样地飞起之后，我会感觉到畏惧……"
    hide a161
    show a171
    a1"我不敢想象，如果我回到枝江，可以随意飞起来的我会成为什么……"
    hide a171
    show f9
    f1"原来如此……我明白的。"
    f1"我们在你的房间谈吧，我给你讲一个故事。"
    hide f9 with dissolve
    u1"她宽慰般地笑着，我也点了点头。"
    scene bg7 with fadehold
    u1"回到了卧室，我们坐在了床边。"
    u1"就像是和亲近的朋友随意的夜谈一样……只是我无法忽视她是一个神。"
    show f3 with dissolve
    f1"刚刚意识到自己在飞，你感到畏惧。那么，如果让你拥有从概念上认知、改变一切的能力呢？你会怎样看？"
    hide f3 with dissolve
    u1"从概念上认知、改变一切？"
    u1"我在心中重复了一遍，仍然只是领会到了模糊的印象。"
    show a121 with dissolve
    a1"对不起，我没太听懂。"
    hide a121
    show f9 with dissolve
    f1"天上的月亮是什么颜色的？"
    hide f9
    show a151 with dissolve
    a1"是……白色的？"
    hide a151 with dissolve
    u1"在回答她的问题的时候，我不自禁地犹豫了。"
    show f2 with dissolve
    f1"嗯，没错。如果我让你相信月亮是黑色的呢？"
    hide f2
    show a151 with dissolve
    a1"这……"
    hide a151 with dissolve
    stop music fadeout 2.0
    u1"完全不可能……咦？不对……"
    u1"月亮就是黑色的呀。"
    u1"什么？！"
    u1"刚刚有一瞬间，我竟然真的觉得月亮是黑色的了？"
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 3.0
    show f1 with dissolve
    f1"感受到了吗？刚刚有一个瞬间，你的认知被我修改了。"
    hide f1 with dissolve
    u1"我的身体忍不住打颤，冷汗已经浸湿了我的衣领。"
    show f9 with dissolve
    f1"别害怕，这只是个简单的解释，我不会去真的制造认知障碍的。"
    hide f9
    show a161
    a1"我知道的……我只是……完全想象不到这种力量……"
    hide a161
    show f1
    f1"仍然是月亮是黑色的这个假设，想要实现有两种方式。"
    hide f1
    show f2
    f1"一种如你刚刚所见，只要让知道月亮的人认为它是黑色的，就算是成功了。"
    hide f2
    show a41
    a1"那另一种呢？"
    hide a41
    show f3
    f1"另一种是，你真的把月亮定义为黑色，它真的就成为了黑色的。"
    hide f3 with dissolve
    u1"……"
    show f2 with dissolve
    f1"而这种定义，是凌驾于一切你所知的物理定律之上的——"
    hide f2
    show a151
    a1"就是改变了“月亮”的概念……"
    hide a151
    show f2
    f1"是的，这种能力就是如此，直接以结果论，不需要任何原理，便实现任何一种感性的想法。"
    hide f2
    show a41
    a1"这种力量真的好可怕。"
    hide a41
    show f2
    f1"如果让你拥有这种力量呢？"
    hide f2
    show a151
    a1"我不知道会怎样……老实说，这种“心想事成”，应该是每个人都梦寐以求的能力，但是，如果它真的就降临在自己面前……至少我会感到畏惧。"
    hide a151
    show a171
    a1"我一直都想要站在那最高的舞台之上，也凭借着一步步的努力，离那里越来越近……"
    hide a171
    show a161
    a1"但是，如果让我在出道那天，就直接站在最高的舞台，唱着自己梦里也不敢想象的美妙歌曲，收获了一切……"
    hide a161
    show a171
    a1"我好害怕那种空虚的感觉。"
    hide a171
    show a21
    a1"比起那种荣光，和A-SOUL的大家一起努力变强的经历、我们的友谊、还有一直支持我们前进的大家……这些才是更加珍贵的。"
    hide a21
    show f4
    f1"你说的没错，我也会害怕这些。"
    hide f4
    show f1
    f1"不过……你知道吗，一直以来，我羡慕的有两个人。"
    hide f1 with dissolve
    u1"我没有说话，认真地听她说下去。"
    show f12 with dissolve
    f1"第一个人，她是人间的天选。"
    hide f12
    show f17
    f1"她有着最美的容颜，最高的天赋，最深的智慧，作为一个完美的人存在着。"
    hide f17 with dissolve
    u1"这个好像拉姐呀……虽然她没有强得那么过分，而且在智慧这一点上……不做评价，但是她的舞蹈真的好像是天选一样，在我的心中就是最完美的了。"
    show f3 with dissolve
    f1"直到有一天，十几岁的她为了去救自己的朋友，面对生死的考验。"
    hide f3
    show a41
    a1"十几岁就要面对生死……很严峻啊。"
    hide a41
    show f1
    f1"是啊，你知道赫拉克勒斯的十二试炼吗？"
    hide f1
    show a121
    a1"乃琳和我讲过一些……但我记不太清楚了。"
    hide a121
    show f1
    f1"嗯，人类还有一句诗是这样说的，“亦余心之所善兮，虽九死其尤未悔”。"
    hide f1
    show a21
    a1"这句话我知道！《离骚》，我以前还背过呢！"
    hide a21
    show f20
    f1"嗯，不错不错！回到刚刚的故事，你猜猜，她怎么了？"
    hide f20
    show a121
    a1"她也经历了赫……什么那样的试炼吗？"
    hide a121 with dissolve
    u1"没办法……就是记不住那么长的名字嘛！"
    show f9 with dissolve
    f1"不一样的。赫拉克勒斯的试炼，是让他成为英雄。"
    hide f9
    u1"赫拉克勒斯……这次应该记住了。"
    show f17
    f1"而她经历的，是字面意义上的“九死”。"
    hide f17
    show a41 with dissolve
    a1"她……真的被杀死了九次？"
    hide a41
    show f1 with dissolve
    f1"可以这样说……而第一次死是最痛苦的。"
    hide f1
    show f2
    f1"她虽然是魔法世界的天选之人，但是讽刺的是，她在魔法上并没有什么天赋。"
    hide f2
    show f3
    f1"而那一次她面对的是神造的机械，规则很简单，打倒神造机械，就可以拿到解救自己朋友的钥匙。"
    hide f3
    show a41 with dissolve
    a1"神造机械……听起来完全不是对等的战斗啊！"
    hide a41
    show f1 with dissolve
    f1"没错。但如果是完全没有胜算的战斗，她当然不会去送死……尽管那微弱的胜算，她和送死也没有什么区别。"
    hide f1
    show f3
    f1"她看到了自己的剑可以划伤那机械，就义无反顾地冲了上去。"
    hide f3
    show a151 with dissolve
    a1"她……真的能赢吗？"
    hide a151
    show f3 with dissolve
    f1"从物理意义上毁掉这精巧的神造机械并不是难事，但是对于人类来说，不存在赢的可能。"
    f1"机械并非坚不可摧，只是有着最顶尖的剑术，能毁掉它的唯一办法，就是用自己的肉身去接住剑，然后再用自己的剑反击。"
    hide f3
    show a41 with dissolve
    a1"这是同归于尽的方法！"
    hide a41
    show f1 with dissolve
    f1"也是唯一的方法，而她也是这样做的。"
    f1"她的肺被从前到后刺透了，但她也成功刺穿了机械的核心，找到了钥匙。"
    hide f1
    show f2
    f1"她将死之时，头脑却格外清醒……清醒地感知到每一次呼吸带来的剧痛……然后，走上几十级台阶，走向第一道门，到了门的前面，打开了它……"
    hide f2
    show a41 with dissolve
    a1"人类的身体……真的能坚持下来吗？"
    hide a41
    show f3 with dissolve
    f1"客观上来说，是完全不能的。"
    hide f3
    show f1
    f1"也正是这个原因，她意识到了问题所在。"
    hide f1
    show f9
    f1"你猜是什么问题？"
    hide f9
    show a11 with dissolve
    a1"为什么、自己还没有死？"
    hide a11
    show f1 with dissolve
    f1"没错，就是这个问题。"
    f1"忍耐疼痛，并不能让一个重伤之人活得更久。"
    hide f1
    show f2
    f1"她知道，自己要面对九轮的考验，所以万万不能死，即使是中了必死的一剑，她也必须认为自己不会死，相信自己赢了那机械。"
    hide f2
    show f3
    f1"但是理性告诉她，能走到这里，对于身体来说已经是不可能的神迹了。"
    hide f3
    show f17
    f1"她发现，也许自己的信念可以影响现实。于是她开始强化自己不会死的认知。"
    hide f17
    show f1
    f1"实际上，从这时开始，她已经给自己创造了不死的身体。"
    hide f1
    show a11
    a1"所以……她本就是那种可以随意定义的神灵？"
    hide a11
    show f1
    f1"没错。之后她所经历的死亡，其实是八种锻造神性的试炼，她逐渐掌握了自己终极的力量。"
    f1"其中最让我难以忘记的，是她在了解了自己不会死去以后，面对着前方一扇定义为不可被破坏的门。"
    f1"……而走进那扇门，她的肉身就会被完全毁灭。"
    hide f1
    show a11
    a1"那是最后一扇门吗？"
    hide a11
    show f3
    f1"不是的。"
    hide f3
    show a41
    a1"那如果她被完全破坏，也根本不可能救自己的朋友了呀！"
    hide a41
    show f3
    f1"没错，但是她已经明白，自己与人类不同。因此这不只是救朋友的事情，这更意味着放弃为人，追求进化。"
    hide f3
    show f2
    f1"她的身体被毁灭以后，她便和宇宙连通，所见所知是无尽的星海。她用星辰重塑自我，创造了不朽的躯体。"
    hide f2
    show a21
    a1"那就像是重生的凤凰……"
    hide a21
    show f3
    f1"凤凰……"
    hide f3
    show f2
    f1"是啊……而在一切试炼的最终，她拾起了神灵的骄傲，接受了那一切让你我畏惧的力量，成为了最强大的神灵。"
    hide f2
    show a141
    a1"她真的好厉害，但是……我还是很难羡慕她，就像是我不会羡慕希腊神话中的英雄一样。"
    hide a141
    show f4
    f1"没错，她的故事听起来像是宿命，像是天选，也因为一些复杂原因……就好像是刻意编造的。"
    hide f4
    show a21
    a1"不……我没有怀疑你在编故事的！这个故事我很喜欢！"
    hide a21
    show f9
    f1"没关系，这些不重要。重要的是，我羡慕的第二个人却完全不一样。"
    hide f9
    show a21
    a1"哦？这个又是谁？"
    hide a21
    show f10
    f1"这个人……之后再和你说吧！说好要带你到处走一走的，却讲起故事来了。"
    hide f10
    show a141
    a1"没关系，刚刚的故事我也很喜欢听！"
    hide a141
    show f1
    f1"不过这一个还是要留待之后再和你讲！我带你去了解这边的世界，枝江那里，也快该开始新的一天了。"
    hide f1
    show a11
    a1"她们怎么样了？"
    hide a11
    show f3
    f1"她们在尝试寻找你，而这一次，对所有人都是一个考验。"
    hide f3
    show a41
    a1"……我想见一见她们。"
    hide a41
    show f1
    f1"好，我带你去。"
    hide f1 with dissolve
    scene oce with dissolve
    u1"忽然，我们又回到了那一条由水母组成、通向遥远之处的路。"
    u1"最初，我好奇过这样的路要如何行走，但是现在我明白了，这条路本就不是用脚踩在上面走的，它只是给出一个方向。"
    u1"走进建筑群中，发现好多建筑都是残破的。"
    u1"或者说，不是因时间而损伤，这些仿佛现代都市的高楼，从建造的时候就没有建造完全。"
    u1"而且，还有一部分甚至只是拼接起的方块，连建筑都算不上。"
    show a21 with dissolve
    a1"这些建筑看起来不像是能住人的样子，天上居然还有倒着的楼？"
    hide a21
    show a141
    a1"而且……那里明明该是水面啊！好奇怪！"
    hide a141
    show f1
    f1"它们的确是奇怪的事物。比起“房屋”的功能，这些建筑更类似于艺术品。"
    hide f1
    show f2
    f1"这里可以说是我的试验场。"
    hide f2
    show f9
    f1"说起来……你有没有梦想过，成为一个公主，拥有一座童话里的城堡？"
    hide f9
    show a131
    a1"没有过的！我可不会去想这些……这些好羞耻啊！"
    hide a131
    u1"我连忙否认。虽然……在很小的时候可能真的想过，但那太久了，根本不算数！"
    show a141
    a1"但是，如果是拉姐的话，一定想过的！"
    hide a141 with dissolve
    show f4 with dissolve
    f1"反应好大……该不会……算了！不过我以为人类的女孩子都会这样想呢，我觉得这样想是很能够理解的——"
    hide f4
    show f1
    f1"除非你真的有能力轻而易举地复制童话中的世界。"
    hide f1
    show a41 with dissolve
    a1"除非？"
    hide a41
    show f1
    f1"没错，你知道的，在千百年前，那时的人类画家会很努力地把现实惟妙惟肖地复刻到画布之中。"
    f1"但是现在有了照相机，仅仅是极致拟真的画技，已经不足以被称为艺术。"
    hide f1 with dissolve
    u1"我隐约理解了她想要说的。"
    show f3 with dissolve
    f1"人类对美的追求是被抑制的——被能力的有限抑制，而为了使用那有限的能力，又被更加有限的财力抑制着。创造出美的事物是如此艰难。"
    hide f3
    show a11
    a1"所以那些艺术品才尤为可贵。"
    hide a11
    show f1
    f1"没错。而如果那些抑制解除，创造变得易如反掌，那些美还是美吗？"
    hide f1
    show f3
    f1"曾经确立的最高标准被轻易达到，完美变得廉价，那么在此之后又该怎么办呢？"
    hide f3 with dissolve
    u1"我不知道。"
    show f9 with dissolve
    f1"……当然，可以选择提升完美的标准，创造愈加浮夸的事物，穷竭一切的想象力，试图实现突破。"
    f1"但是，如果你需要的是将无尽的一生完全致力于这件事，它很快就会因为达到瓶颈而变得无聊。"
    hide f9 with dissolve
    u1"我想，我应该明白了她要表达的意思，但是，将这些想法组织成语言，仍然十分困难。"
    show a41 with dissolve
    a1"所以……你害怕极致完美的事物。"
    hide a41
    show a11
    a1"极致的完美和那种修改概念、创造事物的力量相辅相成，而它们会扼杀掉你心中的……某种事物。"
    hide a11
    show a141
    a1"对不起，我不能够说得太清楚，这种话题我之前从没想过。"
    hide a141
    show f1
    f1"没关系的。你说的没错，那种被扼杀的东西，就是可能性。"
    f1"如你所见，世界是模糊的，这些水、倒悬的建筑……"
    hide f1
    show f2
    f1"水面之上是什么？不重要。这一切都是先有的结果。因为这些奇异结果的产生，自然的法则也被打破、重塑。"
    hide f2
    show f3
    f1"也如你所见，这个世界是不完美的，我创造了许多半成品，它们可以被摧毁、被放逐，但是，它们创造了可能性。"
    hide f3
    show a141
    a1"放逐？建筑是怎样被放逐的呢？"
    hide a141
    show f9
    f1"……没什么，不小心用错了词，我们来聊聊别的吧！"
    hide f9
    show a11
    a1"好。"
    hide a11 with dissolve
    stop music fadeout 2.0
    scene sch with fadehold
    show f1 with dissolve
    f1"我们就要到了，看这里，感觉熟悉吗？"
    hide f1 with dissolve
    u1"当我看见这一切的时候，我甚至有些恍惚。"
    u1"熟悉的学校，熟悉的天空！"
    play music "audio/01.二千嬢.ogg" fadeout 1.0 fadein 1.0
    show a21 with dissolve
    a1"没错！这里是枝江学园！我当然知道！"
    hide a21 with dissolve
    u1"久违地见到这些，我抑制不住心中的兴奋！"
    show a21 with dissolve
    a1"我们曾经也在这里直播过的，好多次都是在教室里。"
    hide a21
    show a141
    a1"还有一次，大家投过来好多份报名表，虽然有好多奇奇怪怪的……但那一次我们也很开心。"
    hide a141
    show f9
    f1"我记得。我还记得你的报名表上写着“理性与感性的完美结合”。"
    hide f9
    show a121
    a1"不要说这个啦！都……都是多久之前的事情了……"
    hide a121
    show f1
    f1"那么久以前的事情也会害羞吗？"
    hide f1
    show a121
    a1"没有，没有害羞……"
    hide a121
    show f9
    f1"好，那就不提这个了。"
    scene sc with fadehold
    u1"空无一人的走廊中，只有我的脚步声。"
    u1"四还是在用飞的方式，我也好奇，她那双裸露的锥形的脚，看起来那么柔弱，真的能用来走路吗？"
    u1"在看到天空与阳光的瞬间，我有了种自己回到枝江的错觉……"
    u1"不过，这只有我们两个的学校，证明了这里仍然是四的领域。"
    scene bg3 with dissolve
    show f1 with dissolve
    f1"我们到了。"
    hide f1 with dissolve
    u1"训练室啊……"
    u1"诶？怎么会！……"
    u1"走进训练室的一瞬间，我愣住了。"
    show b1 with dissolve
    u1"我看见了贝拉、"
    hide b1
    show c1 with dissolve
    u1"珈乐、"
    hide c1
    show d11 with dissolve
    u1"嘉然、"
    hide d11
    show e1 with dissolve
    u1"乃琳。"
    hide e1
    show a12 with dissolve
    u1"还有向晚。"
    hide a12
    show a12 at left
    show a181 at right with hpunch
    a1"为什么你们会在？还有，你又是谁？"
    hide a12
    hide a181
    u1"虽然见到了熟悉的面孔，但是！总是感觉怪怪的！"
    u1"对！尤其是还有一个和我一模一样的人！"
    u1"她们并没有回答我，仍然一动不动，微笑着站在那里。"
    show a151 with dissolve
    a1"这些……都是你创造的……人偶？"
    hide a151
    show f9
    f1"嗯，说好要带你见你的队友们嘛。"
    hide f9
    show a161
    a1"你骗人！"
    hide a161
    show f10
    f1"对不起，那个……你太可爱了。"
    hide f10 with dissolve
    u1"她笑着这样说，看起来没有一点要道歉的意思。"
    show f1 with dissolve
    f1"不过带你来这里，当然也不是为了骗你玩的，我和你讲一讲这些人偶的故事。"
    hide f1
    show a11
    a1"……好。"
    hide a11 with dissolve
    u1"我仔细地去看这些熟悉的面孔，与蜡像不同，除了不会动，这些人偶与我们没有任何区别。"
    show f2 with dissolve
    f1"其实我可以让她们说话的，你知道吗？只要复制了你们五人的情感与记忆，这并不是多么困难的事情。"
    hide f2
    show f1
    f1"我也曾犹豫过许多次，要不要这样做。"
    hide f1
    show a11
    a1"为什么犹豫？是因为仿制品只能够复制过往的记忆，而之后的一切都不在控制之中吗？"
    hide a11
    show f1
    f1"并不只是如此……你要知道，我做的复制，是完全不会有误差的，也就是说，如果这一个“向晚”有了生命，她在这里不会做出与你不同的抉择。"
    hide f1
    show a41
    a1"那……为什么没有决定下来呢？"
    hide a41
    show f3
    f1"……创造哪怕只是一个灵魂，都是一种对道德的巨大挑战。"
    f1"创造灵魂，让它背负起生命的一切重量，那么从这个生命诞生之时起，创造者就理当对其负有责任。"
    hide f3
    show f6
    f1"……我不喜欢那种自以为是，任意创造灵魂的神明，所以我最终没有那样做。"
    hide f6
    show f3
    f1"更何况，这些本就是仿制品，如果她们真的有了生命，那该是以什么身份呢？从被赋予意义的一刻起，就是赝品，就是影子，我不能够做这样的决定。"
    hide f3 with dissolve
    u1"训练室中，她们一个个消失了，只剩下我们。"
    show a21 with dissolve
    a1"那么……我什么时候可以再次见到我的队友们呢？"
    hide a21
    show f3
    f1"这个问题要取决于她们的。时间快到了，我必须做出一些决定……希望我没有错。"
    hide f3
    show a11
    a1"什么决定？"
    hide a11
    show f1
    f1"……没什么的，相信你的队友们就好。我也和你一样相信她们。"
    hide f1
    show a11
    a1"好……那我就先不担心……"
    hide a11
    stop music fadeout 1.0
    play sound "audio/niaoming.ogg"
    u1"忽然，窗外传来了一声清脆的鸟鸣。"
    u1"是小鸟吗？好可爱！"
    u1"来到这里以后，见到的都是鱼类和水母，还是第一次看见有鸟呢！"
    play music "audio/深竹.ogg" fadeout 3.0 fadein 1.0
    u1"……不对，这是什么……好冷！"
    u1"不知从何处而来的冷风，就像是要夺走一切的生命，从我的身边掠过。"
    u1"四不知何时抬起了手臂，好像是朝着那只鸟的方向。"
    u1"她的头发飘起，眼神也充盈着杀气。"
    u1"强大的压迫感甚至让我不敢看向她。"
    show a151 with dissolve
    a1"四……你还好吗？"
    hide a151
    show f5 with dissolve
    f1"我……"
    hide f5 with dissolve
    u1"沉默片刻，她的手臂缓缓放下，寒冷的气息倏然散去。"
    show f6 with dissolve
    f1"抱歉，那只鸟……不，没什么的。也许我曾无意间创作出一些毫无意义的东西。不论如何，它也就是一只愚蠢无知的鸟而已……又能够窥见什么呢？"
    hide f6 with dissolve
    u1"她开始四处张望，好像是在检查些什么，眼中像是困惑，又逐渐变得失落。"
    u1"可是，我该如何问她呢？我甚至不知道她为什么会对一只鸟如此介意，更不知道她是在如何想这只鸟。"
    u1"我只能沉默。"
    play music "audio/Zki.ogg" fadeout 2.0 fadein 3.0
    scene black with fadeholdd
    n"相信自己，飞起来，飞到天上去。"
    u2"伤口已经愈合了，我的双翅有力，羽毛柔顺而美丽。"
    n"你已不是过去的自己。"
    u2"是的，我曾战胜了她。"
    u2"我骤然飞起，越飞越高。"
    u2"虽然害怕，还是向着更高飞去，飞到完全陌生的地方。"
    u2"不，我还是想要停一停……"
    u2"却忽然发现，我怎么无法控制自己？"
    u2"地面的一切急剧地缩小，而我在风中摇摇欲坠……"
    u2"不要再一次摔下来！"
    scene oce4 with dissolve
    u2"不对……这是哪里？"
    u2"光与我越来越远，深蓝色，黑暗……"
    u2"被吸入深海之中……"
    stop music fadeout 2.0
    scene black with dissolve
    n"你怎么了？醒一醒！"
    scene bg2 with dissolve
    u2"……"
    u2"眼前的一切终于恢复了实感，珈乐正担心地望着我。"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    show b8 with dissolve
    b2"乐……我做噩梦了……"
    hide b8
    show c4 with dissolve
    c2"没关系的，我在这里。"
    hide c4 with dissolve
    u2"她轻轻抱住我，用极温柔的声音对我说着。"
    show b8 with dissolve
    b2"我……"
    hide b8 with dissolve
    u2"……困境…职责…方向…未来…高空…深海。"
    u2"不知道从哪里而来的概念充斥了我的脑海。"
    u2"……之后，就成了空白。"
    show b8 with dissolve
    b2"乐……只有你是真的……"
    hide b8 with dissolve
    u2"我也不知道为什么，就是完全控制不住……"
    u2"……我双手用力抱住了她，伏在她肩头哭了起来。"
    show c4 with dissolve
    c2"想哭就哭出来吧，拉姐。"
    hide c4
    show b8 with dissolve
    b2"我真的好累……你说，为什么晚晚会不见了？为什么啊？"
    b2"明明所有事情都计划得很好……"
    hide b8 with dissolve
    stop music fadeout 1.0
    play sound "audio/qiaomen.ogg"
    u2"咚咚咚~"
    u2"试探的敲门声。"
    d2"拉姐？"
    u2"是然然来了。我连忙擦干眼泪，打开门，她和乃琳就在门外。"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show b2 with dissolve
    b2"你们来啦……"
    hide b2 with dissolve
    u2"我努力收住还没涌出来的眼泪，做出笑脸来，不想被她们看见我刚刚哭过。"
    show d31 with dissolve
    d2"拉姐……是刚刚哭过吗？"
    hide d31
    show b14
    b2"没……我才没有哭！"
    hide b14
    u2"我转过身去，在调整好面部表情前，不想让她们看见……"
    b2"……好了，先不说我的事情。你们这么早来，应该是有找到一些线索吧？"
    show e5
    e2"没错，虽然这个线索似乎不太重要……但是我想，还是要让你们也知道。"
    hide e5
    show e1
    e2"然然找出了那两串数字的规律。"
    hide e1
    show b3
    b2"什么规律！快说！"
    hide b3
    u2"听到了好消息，刚刚起床的小伤感顿时烟消云散。"
    u2"乃琳却好像并没有十分兴奋，她拿出一张早就准备好的纸条递给我。"
    show e1
    e2"拉姐你看！"
    hide e1 with dissolve
    u2"纸条上写着两行数字，第一行是“88 73 78 89 85”，第二行是“24 9 14 25 21”"
    u2"那两串数字，这一次被拆分开了。"
    show d11 with dissolve
    d2"把这些数字拆成两个一组，就发现相邻的数字之间，它们的差值是相等的，就像88比73多了15，24也比9多了15。"
    hide d11
    show b2
    b2"那这个说明了什么呀？"
    hide b2 with dissolve
    u2"就算有着这样的规律，我还是想不通这是要表达什么。"
    show e2 with dissolve
    e2"这意味着，这两串数字可能表示的是同一种信息。"
    hide e2
    show e1
    e2"用数字密码来表达一种消息，最容易的就是数字和字母的对应，第二组数看起来像是二十六字母的标准顺序，我找到了对应的关系，猜测是x，i，n，y，u这五个字母。"
    hide e1
    show d21
    d2"没错！虽然当时我们不确定这种推测正确，但是，我们在网上去找数字替代字母的对照表，很容易就找到了那个叫……叫什么？我记不住了……乃琳！"
    hide d21
    show e1
    e2"是ASCII。"
    hide e1
    show d11
    d2"对，就是这个名字！给我们发信息的人没有为难我们，第一串数字就是用那个规则，把x、i、n、y、u转换成了一串数字！"
    hide d11
    show e1
    e2"这验证了我们对第二串数字的猜测没错。"
    hide e1
    show c2
    c2"但是，仅仅是这五个字母，又能说明什么呢？"
    hide c2
    show c3
    c2"“心”、“雨”，这难道是那个人的署名吗？听起来像个女孩子的名字。"
    hide c3
    show e2
    e2"嗯，我和然然也觉得是她的署名，提醒我们的线索已经直接说了出来，这种编了密码的内容，也许本来就是无关紧要的，只是想和我们猜个谜语吧？"
    hide e2
    show b1
    b2"我也觉得是这样。她让我们注意水，大家有发现什么水的变化吗？"
    hide b1
    show e2
    e2"我想，这种暗示只是先记住就好，我们还是要先按照正常的方式排查原因。昨天我们自己乱了阵脚，甚至忘了去查看监控录像，我想，我们应该先去看一看监控的内容。"
    hide e2
    show d11
    d2"我同意乃琳说的。"
    hide d11
    show c1
    c2"那拉姐，我们去监控室看一看？"
    hide c1
    show b1
    b2"好，去监控室！"
    hide b1 with dissolve
    scene black with dissolve
    u2"我们好像抓住了唯一的钥匙，飞快地朝监控室跑去。"
    stop music fadeout 2.0
    scene moni with dissolve
    u2"我们很快调出了昨天的监控录像。"
    scene sta4 with dissolve
    show a17
    u2"晚晚在演唱会结束后，离开了舞台，回到后台……这个部分没有问题。"
    scene zl2 with dissolve
    show a17 at left
    u2"走廊里只有她一个人，也没有问题。"
    hide a17
    show b11 at right with dissolve
    u2"与此同时，另一边的监控录像中，去接她的只有我，也是没有问题。"
    hide b11 with dissolve
    u2"我们中间的走廊也是空无一人。"
    u2"按照这种发展，我们当然会见面。"
    u2"我紧紧盯着摄像头——马上，我们就要到达同一个摄像头的画面中。"
    scene black
    u2"咦……不对！"
    scene moni with dissolve
    u2"为什么她那边的监控画面……黑屏了？"
    play music "audio/Qm.ogg" fadeout 2.0 fadein 2.0
    scene zl2 with dissolve
    u2"仅仅三秒钟后，画面恢复正常，她的身影完全在录像中消失了！"
    show b11
    u2"画面中，只有我一个人。"
    scene moni with fade
    show b10
    b2"这……这是什么？"
    hide b10
    show c2
    c2"没有看到别人，那个地方也不可能藏人！她怎么会……怎么可能就这样消失了！"
    hide c2
    show d51
    d2"是……是鬼吗……拉姐？"
    hide d51
    u2"手心忽然传来软软的触感，她因为害怕，已经拉住了我，躲在了我身后。"
    show b1
    b2"没关系的，然然，就算是有鬼，我也不怕！"
    hide b1 with dissolve
    u2"……我另一只手却忍不住紧紧握拳，掌心渗出了汗。"
    show e5 with dissolve
    e2"我们应该去现场看一看，也许有我们没有注意到的细节。"
    hide e5
    show b10
    b2"好，我们现在就去。"
    hide b10 with dissolve
    u2"还好，即使是在这种诡异的事件之中，乃琳仍然保持着冷静。"
    scene zl with fadehold
    u2"我们离开了监控室，到了事发地点，但走廊里看起来并没有什么特异。"
    u2"当然也没有短信中说的水。"
    show c2 with dissolve
    c2"这里看上去没什么特殊的。"
    hide c2
    show d31
    d2"是啊，但是晚晚就是在这里消失的，这里会不会有什么暗门？"
    hide d31
    show e2
    e2"但是这里是我们自己的舞台，如果有暗门我们怎么会不知道呢？"
    hide e2
    show b10
    b2"大家说得有道理，但这里还是不能就这样不管，我们仔细看看，找一找是否有我们没注意到的细节。"
    hide b10 with dissolve
    u2"我试探着敲着墙壁，声音很实。"
    u2"……"
    u2"我们敲敲打打，很快，这个走廊被我们几乎敲了一遍，但仍然没有发现。"
    show b10 with dissolve
    b2"不管是墙还是地板都很硬啊！完全没什么特殊的。"
    hide b10
    u2"我不由得叹气，本来以为这是一个希望，没想到却仍然看不到什么结果。"
    u2"但是！"
    u2"我忽然想到了！"
    show b1 with dissolve
    b2"对了，天花板我们还没有试过！我这就去拿长棍子！"
    hide b1
    show d11
    d2"天花板吗？确实是容易被忽略的地方呀。"
    hide d11
    show e2
    e2"等一等！"
    hide e2
    show b1
    b2"怎么了？"
    hide b1 with dissolve
    u2"我朝她看去，她正有些疑惑地看着自己的水杯，摇了摇头。"
    show e2 with dissolve
    e2"没什么……是我的错觉。"
    hide e2 with dissolve
menu:
    "不能放过天花板的可能性，去找长棍子":
        jump one
    "问乃琳关于水杯的事情":
        jump two
label one:
    u2"是我昨天的举动让她过分紧张了，应该让她先休息一下的，我去找长棍子。"
    scene zl with fade
    u2"很快，我把长棍子取了回来，对着天花板，尝试了无数个角落……"
    u2"仍然没有发生什么奇迹。"
    u2"这一切的所作所为，忽然变得好像是在安慰自己而已。"
    u2"不知道过了多久，我还站在那里发怔。"
    show b10 with dissolve
    b2"大家……去休息吧。"
    jump five
label five:
    stop music fadeout 2.0
    scene res with fadehold
    u2"两天后，然然同意了四人编舞的排练。而我们别无他法，只能选择公布向晚因个人事务无法归队的消息。"
    u2"一时间，听到了好多不满、遗憾的声音，但是，大家毕竟还是温柔的，他们终究还是表达了理解，以及对晚晚的关心。"
    u2"只是，我们没有办法把那些关心传达给她。"
    scene bg3 with fadehold
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    u2"半个月后，演唱会举办前一天。"
    show a12 with dissolve
    u2"晚晚居然回来了！"
    hide a12 with dissolve
    u2"尽管做了半个月的四人排练，但是，我们一致决定，明天的演唱会，必须五个人上场！"
    u2"幸运的是，晚晚就像是做了半个月的特训，不但没有跟不上训练，反而带领着我们，对编舞做出完美的修改。"
    u2"谁也不知道，她究竟经历了什么，好像变得更加强大了！"
    u2"她说，要在明天的演出结束以后，好好和我们讲一讲发生的事情，让我们认识一位新的朋友！"
    u2"相当期待！"
    scene bg6 with fadehold
    u2"终于结束了！"
    u2"一切都得到了应有的回报。这些天来，毫不马虎的训练成效卓著，北方都会的演唱会，取得了前所未有的大成功！"
    u2"晚晚的突然回归，更是让每一个支持者都开心、感动。"
    u2"终于实现了一直以来的梦想，我们决定吃一顿大餐来庆祝！"
    u2"……"
    show b2 with dissolve
    b2"晚晚，这些天你去了哪里？你昨天说，要在演出结束以后，和我们好好讲讲的！"
    hide b2 with dissolve
    stop music fadeout 2.0
    show a151 with dissolve
    a2"对不起……我记不清了。"
    hide a151
    show e2 with dissolve
    e2"怎么会？"
    hide e2
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    show a41 with dissolve
    a2"快给我一支笔！不知道是为什么，现在，就连剩下的印象也在飞快地消失……"
    hide a41 with dissolve
    u2"……明明是庆功宴，居然开始找起了纸笔？"
    u2"但是没关系！我们立刻去找！"
    u2"……找到了！"
    u2"晚晚拿着笔，却疑惑地盯着那张纸……"
    u2"……晚晚，你会写下什么？"
    u2"…………"
    u2"静止许久……最后……"
    u2"仅仅点下四个墨点。"
    show a151 with dissolve
    a2"对不起、我……什么都记不住了……"
    hide a151
    show b2 with dissolve
    b2"没关系没关系！今天该是快乐的庆祝，忘了这些吧！"
    hide b2 with dissolve
    u2"我们收起纸笔，开始欢笑着庆祝。但是，我却莫名觉得脑中空空的。"
    u2"好像有什么重要的事情忘记了。"
    u2"有谁……曾经离开过吗？"
    u2"……"
    show a141 with dissolve
    a2"对不起，我肚子有些不舒服，我要先回一下房间！"
    hide a141
    show d31 with dissolve
    d2"你还好吗？没关系吧？"
    hide d31
    show a11 with dissolve
    a2"没关系，很快就能调整好的，不要担心我！大家好好吃饭！"
    hide a11 with dissolve
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    scene bg1 with fadehold
    u1"我躺在床上，呆呆望着天花板。"
    u1"并没有真的肚子疼，也不是不想和大家一起庆祝，只是有一件很重要的事情，无论如何都想不起来了。"
    u1"……1…9…2…6…5…7…3…8……"
    u1"我毫无目的，只是数着眼前的数字灯。"
    u1"总觉得少了些什么。"
    u1"嗯……这数字灯为什么没有4呢？"
    u1"想到那个数字的瞬间，我心中好像涌起一股温暖，像熟悉的风从远方吹来。"
    u1"但那只是幻觉……虚幻到，甚至马上就能觉察到它过分的遥远，那大概是永不可能跨越的阻隔。"
    u1"为什么明明已经成功了，那淡淡的失落却像是吹不散的薄雾？"
    stop music fadeout 2.0
    u1"好困……"
    scene black with fadehold
    u1"……"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene dream with fadehold
    u1"这里是梦，我知道的。我曾无数次见这梦境。"
    u1"这个梦……曾是阴暗的、模糊的蓝色。"
    scene dream2 with dissolve
    u1"只是这一次……"
    u1"沉默的蓝好像很久很久的朋友。"
    u1"但直觉告诉我，这是最后一次的见面。"
    u1"也许是诀别时刻？"
    u1"只是……为什么要诀别呢？"
    u1"早已记不清初见的理由……哪怕这一次的自我无比清晰。"
    scene dream3 with dissolve
    a1"永别了……我深蓝色的梦。"
    $ quick_menu = False
    scene dream8 with Dissolve(3.0)
    stop music fadeout 8.0
    scene dream9 with Dissolve(3.0)
    $ renpy.pause(5, hard=True)
    return
label two:
    show b10 with dissolve
    b2"什么错觉？你的水杯怎么了吗？我看到你刚刚在注意它。"
    hide b10
    show e2
    e2"刚才，突然有了一种莫名的直感，就好像……我的水杯里有一只水母……但是我去看的时候，却一切正常。"
    hide e2
    show b3
    b2"我认为乃琳说的很重要！虽然只是一种感觉，并没有真的出现什么……但它一定是有意义的！"
    hide b3 with dissolve
    u2"乃琳一直都很可靠，她不会做毫无意义的举动，这一定是有价值的信息！"
    show d11 with dissolve
    d2"我也认为那不是幻觉，现在奇怪的事情已经够多了，看到的已经不能相信，也许直觉才是最准确的！"
    hide d11
    show c1
    c2"没错，乃琳，从那天和你猜谜的奇怪女人，到你收到的谜语短信，再到你现在的奇异直觉，我想，你就是解开这困局的关键！"
    hide c1
    show e2
    e2"但是我也不知道该怎么办……"
    hide e2
    show b1
    b2"总之，现在我们一定要相信彼此！这一次面对的，很可能是真正超出我们认知的事物，我们可能见到一些常理之外的东西，必须要互相信任！"
    hide b1
    show c3
    c2"嗯……对！"
    hide c3 with dissolve
    u2"她虽然答应着，但状态似乎有些恍惚。"
    show d31 with dissolve
    d2"乐，你怎么了？"
    hide d31 with dissolve
    u2"原来不只是我这样觉得！"
    show c4 with dissolve
    c2"我……我有些冷。"
    hide c4 with dissolve
    u2"不行，必须要让大家振作起来。"
    show b1 with dissolve
    b2"我们要解决问题，自己不能先累倒了，大家昨晚没有好好吃饭吧？我们准备一下，去休息室吃早饭吧！"
    hide b1 with dissolve
    u2"她们答应着，我心不在焉地带着她们去往休息室。"
    scene res with fade
    u2"早餐已经准备好了。"
    u2"坐下的一瞬间，我竟有些晕眩。"
    u2"我一边吃着饭，一边想办法说一些轻松的话题，不去提晚晚的事情，想让大家尽量打起精神。"
    u2"……只是说过之后，我都忘了自己说的什么。"
    u2"我观察着大家的一举一动，乃琳看起来还是平时的样子，这让我放心好多。"
    u2"但然然很不正常，她居然会不认真吃饭！"
    u2"比起饭菜，她显然对乃琳的水杯更有兴趣。我偶尔抬头，就发现然然在盯着水杯看。"
    u2"看来有些事情，大家还是心照不宣的。"
    u2"……快吃完了。"
    show d11 with dissolve
    d2"我果然还是觉得，乃琳刚刚的发现并不简单。"
    hide d11
    show d61
    d2"她说感觉杯子中有水母，但是看了一眼却又没有……可是可是！如果真的有水母在杯子里，又能怎么样呢？"
    hide d61
    show b10
    b2"对，它又不会说话！"
    hide b10
    show d11
    d2"我们相信乃琳，所以就当作是有！因为出现了一只水母，我想，是在暗示我们去有水母的地方。"
    hide d11
    show e1
    e2"晚晚的房间？那里有养着水母！"
    hide e1
    show d11
    d2"对，我想我们要不要去喂一喂水母？"
    hide d11
    show b2
    b2"那我们现在就去！"
    hide b2
    show c3 with dissolve
    c2"那个……"
    hide c3
    show b1
    b2"怎么了？乐。"
    hide b1
    show c7
    c2"我一直在犹豫这个。刚刚在走廊，我说自己感觉冷，但是当我离开晚晚消失的那一小段后……就不觉得冷了。"
    hide c7
    show c2
    c2"而且，我之前好像看到墙壁上有浮动的水草……但我怀疑自己看错了，那里又只是墙壁，所以就没有说。"
    hide c2
    show c7
    c2"我觉得还是应该回走廊，也许真的有什么在那里。"
    hide c7 with dissolve
menu:
    "去走廊":
        jump three
    "去向晚的房间":
        jump four
label three:
    show b1 with dissolve
    b2"浮动的水草吗？也许是重要的情报！我们再去调查一下吧！"
    scene zl with fade
    u2"又一次回到走廊，沿着水草这条线索，尝试了无数种方式……"
    u2"只是这一切的所作所为，都好像是在安慰自己而已。"
    u2"不知道过了多久，我还站在那里发怔。"
    show b10 with dissolve
    b2"大家……去休息吧。"
    hide b10 with dissolve
    jump five
label four:
    show b10 with dissolve
    b2"乐，我相信你说的。但就像刚刚然然说的那样，杯子里面是不是有水母并不重要，晚晚不在杯子里。"
    hide b10
    show b1
    b2"走廊我们也已经搜索得很仔细了，比起回去检查，还是去考虑这些是在暗示什么比较好。"
    hide b1
    show c1 with dissolve
    c2"我明白了，那我们去晚晚的房间吧。"
    scene bg1s with fade
    u2"我们昨天也曾来过晚晚的房间，但是没有留意水母缸的情况。"
    u2"水母是一种脆弱的生物，如果不了解如何喂养，很容易出现问题。所以晚晚一直不让我们喂她的水母。"
    scene bg1s1 with dissolve
    u2"水母缸中，上层的海月水母是我们见过的。"
    u2"但是……下面这阴暗的巨大生物是什么？"
    show b10 with dissolve
    b2"这……她有养过这样的水母吗？"
    hide b10
    show d31
    d2"没有……之前来的时候还没有这个。"
    hide d31
    show e5
    e2"昨天我没有注意水母缸，不知道是什么时候出现的。"
    hide e5
    show c2
    c2"……这是……我认识这个！"
    hide c2
    show b2
    b2"哇！乐乐你好厉害！这是什么？"
    hide b2
    show c1
    c2"如果我没有猜错……这应该就是冥河水母！但是它好小，难道是幼崽吗？"
    hide c1
    show d31
    d2"小？这居然还小吗……冥河水母是什么？"
    hide d31
    show c2
    c2"嗯，冥河水母可是巨型生物呢！真的很像很像，但是太难以置信……我们再查一查资料吧！"
    hide c2 with dissolve
    u2"我们都拿出了手机，在网上对照起冥河水母的参考图。"
    u2"……除了体型差异太大，外观上也并不算完全一致，但是，那种幽灵般的气质却更加浓郁。"
    u2"真的好像是，来自于冥河的生物。"
    show e5 with dissolve
    e2"这是哪里来的？即使是晚晚的家境，也很难相信她能够弄到一只冥河水母幼崽。"
    hide e5
    show d31
    d2"这种深海中的生物，不可能在水母缸里活下来的……吧？"
    hide d31
    show b10
    b2"这应该不是晚晚养的，它就像是幽灵一样，晚晚应该不会养这种可怕的生物吧？"
    hide b10
    show d11
    d2"不过它和海月之间似乎挺和谐的？"
    hide d11
    show e2
    e2"海月在怕它……你看，下层的阴影就像是个单独的空间一样，仿佛是它不可入侵的领域。"
    hide e2 with dissolve
    u2"我看着这只诡异的水母，但对之后的事仍然没有头绪。"
    scene bg1s with dissolve
    show b1 with dissolve
    b2"虽然不知道之后怎么办，但好消息是，我们来到这里，果然找到了一些线索！之后的计划，大家来说说想法吧！"
    hide b1
    show c1
    c2"这就证明乃琳的直觉是有道理的。"
    hide c1
    show d11
    d2"事到如今，我们应该放弃最初的思路，用一些……魔法的手段来解决问题？"
    hide d11
    show b2
    b2"没错！乃琳你会什么法术，就都用出来吧！我相信你！"
    hide b2
    show e7
    e2"不是，我……"
    hide e7
    show e4
    e2"你们真的觉得我会法术？"
    hide e4
    show b2
    b2"至少说明你很有天赋！加油！"
    hide b2 with dissolve
    u2"忽然想到，我是不是在借此推卸责任呢？"
    u2"终于有一件事情是我有心无力的，就可以光明正大地推给队友了……"
    u2"我好坏啊……"
    show e1 with dissolve
    e2"办法的话，倒是有一个听起来不那么靠谱的尝试。"
    hide e1
    show b1
    b2"什么尝试？"
    hide b1
    show e1
    e2"之前晚晚买过一套塔罗牌，说是很喜欢那个设计风格，就收藏了下来。而我恰好记得它被放在了哪里。"
    hide e1
    show e2
    e2"我可以试着用这个来做一次占卜……不一定准！你们别抱太大希望。"
    hide e2
    show d11
    d2"没关系的，有一个尝试也是好的。"
    hide d11
    show c1
    c2"加油，乃琳！"
    hide c1 with dissolve
    u2"乃琳郑重地点了点头，在一旁的柜子中找到了那盒塔罗牌。"
    stop music fadeout 2.0
    show e5 with dissolve
    e2"说真的，我只是略懂一点点，而且也记不清具体的步骤细节，没办法深入分析牌面的含义……但是、我拿到这副牌的瞬间，就好像看到了遥远的真相。"
    hide e5
    show b10
    b2"是直觉吗？"
    hide b10
    show e4
    e2"没错。"
    hide e4
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    u2"她打开盒子，将牌摆在了床上。"
    show e1 with dissolve
    e2"我们只用这二十二张大阿卡纳吧，我没有自信解读全部的牌面。"
    hide e1
    show e2
    e2"因为我们是为了晚晚做占卜，所以，大家分别抽一张牌吧。"
    hide e2
    show d11
    d2"拉姐先抽吧？"
    hide d11
    show b10
    b2"好。"
    hide b10 with dissolve
    u2"望着那一张张精致的牌背，我有些不敢做出选择。"
    show e1 with dissolve
    e2"没关系的，拉姐，相信直觉！"
    hide e1
    show talot1 with dissolve
    u2"我深吸了一口气。"
    hide talot1
    show talotb
    u2"我抽出一张牌，甚至能感受到自己的心跳。"
    hide talotb
    show tower
    u2"THE TOWER，女王低垂着头，好像被放逐般，禁锢在枷锁中。"
    hide tower
    show e5 with dissolve
    e2"高塔……正位，但不知道为什么，这一套牌面，和我记忆中差得很多。"
    hide e5 with dissolve
    u2"乃琳的神情有些严肃，紧皱着眉头。"
    show b10 with dissolve
    b2"怎么了？乃琳，这张牌预示着什么？"
    hide b10
    show e5
    e2"没什么……拉姐。然然，抽下一张吧。"
    hide e5
    show d61
    d2"……好。"
    hide d61 with dissolve
    u2"她的手微微颤抖着，伸向牌堆。"
    u2"我紧紧盯着她抽牌的手。"
    u2"可她好像太过紧张，这张牌居然没有拿住，掉在了地上。"
    show d31 with dissolve
    d2"对不起，我……"
    hide d31 with dissolve
    u2"可能她已经把这次抽牌，和晚晚的安危联系在了一起吧。"
    show wheel with dissolve
    u2"乃琳看着地上的那张牌，好像有些困惑。"
    hide wheel
    show e5 with dissolve
    e2"命运之轮，但因为掉在了地上，又恰好是横着的，所以没有正逆位。"
    hide e5
    show b10
    b2"要重新抽吗？"
    hide b10
    show e5
    e2"不，没有正逆位，也许正是因为未来尚有着无限的可能。乐，你来抽下一张吧。"
    hide e5
    show c2
    c2"好，我会努力的！"
    hide c2 with dissolve
    u2"现在，这好像不止是一个占卜，更成了为晚晚争取好运的战斗。"
    show talot2 with dissolve
    u2"她面对着眼前的牌阵。"
    hide talot2
    show talotb
    u2"抽出一张……"
    hide talotb
    show world1
    u2"这是……翻转的图像，看不出来是什么。"
    hide world1
    show e5 with dissolve
    e2"世界，逆位。"
    hide e5
    show b10
    b2"乃琳，所以晚晚现在究竟还好吗？"
    hide b10
    show e2
    e2"当拉姐抽出那张正位的高塔之时，我真的吓到了。"
    hide e2
    show b10
    b2"所以那真的是一张很坏的牌？"
    hide b10
    show e5
    e2"那张牌的含义……与毁灭相关，在这种时候抽到它，很难不严肃对待呀。"
    hide e5
    show d11
    d2"但是你现在看起来很平静，是不是之后的牌比较好，将它化解了？"
    hide d11
    show e1
    e2"不是这样，我们回到最初的前提——"
    hide e1
    show e5
    e2"我并不是很会解牌，甚至只是了解了最基础的含义。"
    hide e5
    show e2
    e2"可能在一些占卜师那里，他们要根据现实的问题来解释那些结果，但是我不会。"
    hide e2
    show c1
    c2"乃琳也不需要会解牌，你的灵感就已经很厉害了！"
    hide c1
    show e2
    e2"谢谢你这样讲，至少对我来说，比起如何按照流程解牌，更重要的应该是我感受到了什么。"
    hide e2
    show e1
    e2"改变我想法的，正是一个突如其来的直觉——大家想想，是因为这只水母，我们才用塔罗占卜的吧？"
    hide e1
    show b10
    b2"没错，但是水母怎么了？"
    hide b10
    show e5
    e2"水母有传递一种信息，它让我们相信了这些奇异的方式。那么，如果水母传递的不止这些呢？"
    hide e5
    show d31
    d2"是啊，它就像是被放逐的生物，自己在阴暗的缸底，好孤独的样子……"
    hide d31
    show e2
    e2"乐，你怎么看？"
    hide e2
    show c3
    c2"我觉得然然说得有道理。"
    hide c3
    show e2
    e2"没错，放逐，孤独，这就是它传达出来的感受，我也和然然有着同样的体会。"
    hide e2
    show b10
    b2"那这个和塔罗有什么关系呢？"
    hide b10
    show e5
    e2"关系就在于，它让我意识到这次占卜很可能不是关于晚晚的结果！"
    hide e5
    show b9
    b2"那是谁？"
    hide b9
    show e1
    e2"大概是这一整个事件的前因后果吧。"
    hide e1
    show e2
    e2"我们先从这正位的高塔说起。彻底的毁灭，然后改变。大概就像是“放逐”的概念，因为被放逐，过去的一切也因此摧毁，所以不得不做出改变。"
    hide e2 with dissolve
    u2"我们都静静地听着，开始认真地去想这些平时根本不会接触的概念。"
    show e5 with dissolve
    e2"然后是命运之轮，它的含义是“轮回”，但轮回与我们想知道的关联不大。更重要的在于，它应该是预示着未来走向的。"
    hide e5
    show e1
    e2"不过它因为意外，并没有显示正位或是逆位，也就无法判断未来的走向，也许不止是晚晚，我们每一个人都要面临着自己的选择吧。"
    hide e1
    show e2
    e2"最后的世界牌——含义本该是“完成”，一切都会宣告完结。但命运之轮的不确定，让世界无法达到正位，一切也都变得扑朔迷离。"
    hide e2
    show e5
    e2"……但是、应该不只有这些信息的……让我想想……"
    e2"毁灭、轮回、完成、毁灭、轮回……"
    hide e5 with dissolve
    u2"听她重复着那些词语，我也不由得屏住了呼吸。"
    show d31 with dissolve
    d2"乃琳……我们现在怎么办？"
    hide d31 with dissolve
    u2"能看出然然有些害怕。当然会害怕的，我也在害怕……尤其是“毁灭”这个词，当它真的悬在自己无比熟悉的人的头顶，那是一种恐怖的感觉。"
    show e1 with dissolve
    e2"说起来你们可能很难相信，但是，就像是在梦里一样，我已经找到了一个框架。"
    hide e1
    show e2
    e2"这是一种连接起我们和晚晚的框架，可现在缺少一种东西。"
    hide e2
    show b1
    b2"缺少什么？如果可以，我一定会找到的！"
    hide b1
    show e5
    e2"这个框架缺少连接现实的逻辑。在梦中，我们可以变得无所不能，我们知道如何实现现实中不可能实现的事情，但是一旦苏醒，那些逻辑就会显得荒诞又简单。"
    e2"我们欠缺的，就是将现实与框架连接起来的媒介。我们需要的也正是这个媒介，不管是寻找遗留下的奇怪物品，还是我们自己去建立，我们必须要有！"
    hide e5
    show c2
    c2"水……水是媒介！短信中有提到过！"
    hide c2
    show e5
    e2"没错，但并不仅仅是水。水很关键，却不足以连接框架。"
    hide e5
    show d11
    d2"我想，也许我们需要准备一些水，才好去寻找媒介。"
    hide d11
    show b1
    b2"那我去打水！"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene bg1s with fadehold
    show b2 with dissolve
    b2"水……水打回来了！"
    hide b2
    show e1
    e2"拉姐好快！"
    hide e1
    show b1
    b2"还好啦……不过这盆水能告诉我们什么吗？"
    hide b1
    show sp with fade
    u2"我低头看着水盆，水盆中映出了我们的倒影。"
    hide sp with dissolve
    u2"嗵——"
    u2"水花溅起，是有什么东西掉进了水盆之中。"
    show e5 with dissolve
    e2"等一等，大家先不要碰它！"
    hide e5 with dissolve
    u2"当然了，我甚至连眨眼都不敢，生怕错过了什么重要的信息。"
    show sp1 with dissolve
    u2"水花落下，又化作了两圈波纹。"
    u2"掉下来的是房间中的字母灯，恰好是“A”这个字母。"
    u2"恰好落在了那个空处——"
    u2"我才发现，这个水盆恰好装得下五个人的倒影。"
    window hide
    $ renpy.pause(2.0)
    hide sp1 with dissolve
    show b2 with dissolve
    b2"是晚晚！"
    hide b2
    show d11
    d2"没错，你们看那两圈波纹，那是她的丸子头！"
    hide d11
    show c1
    c2"你们看，这波纹正扩散开，又成了一个大的波纹，好像把我们圈了起来。"
    hide c1
    show e1
    e2"我们把手拉起来，就是现在！"
    hide e1
    show sp1 with dissolve
    u2"我拉起珈乐的手，但右边本来是晚晚的位置，所以是空的。"
    u2"只是现在也不知道该不该调整位置，只是按着乃琳说的去做。"
    show sp2 with dissolve
    $ renpy.pause(.5)
    b2"亮起来了！那圈波纹在发亮！"
    e2"我们去喊她的名字，她应该能够听见的！"
    e2"三！"
    e2"二！"
    e2"一！"
    b2"晚晚！"
    stop music fadeout 2.0
    scene white with dissolve
    u2"我闭上眼睛高喊着，听到她们也和我喊出一样的名字。"
    u2"那一刻，我真的感受到，A-SOUL是不可分离的整体。"
    u2"然后……我的右手被拉住了。"
    scene xinyu with fadeholdd
    play music "audio/Qm.ogg" fadeout 3.0 fadein 2.0
    n2"你何必执著于这座都会？世界如此之大，这个位置不一定是最美好的。"
    k1"那你又何必创造如此完美的我？"
    n2"我可以选择你，但是■■，你愿意走上哪一条路？"
    k1"你预设的道路就没有正确的！你想想那几千万的死难者，你曾感到过愧疚吗？"
    n2"那次的确是我的过失……"
    k1"算了，你不需要承认，你就算再害死十倍的人，也没有什么存在能审判你。"
    n2"对此我很抱歉……"
    k1"你也不必如此做作。你想要我走，直接开口就好，我也不敢违抗你，是吧？"
    n2"■■，我并非希望你走……"
    k1"不要再用这个名字称呼我！你给了我两个绝不可能的选项，不就是为了让我离开你的世界吗？也好……总有一天！我会让你看到……你的傲慢是多么可笑！"
    n2"我可以等那一天……但是，你不让我叫你的名字，我该如何称呼你？"
    k1"我从被创造的那天起，就不属于你的世界，被放逐者、不配用你给的名字！以后，我就叫四。"
    f"被放逐的第四原灵，用这种名字再合适不过！"
    n2"我不奢求你能理解我，只是希望时间可以给你安宁的幸福。"
    f"哼！假惺惺！"
    n2"……我是认真的，你以后会明白的。"
    u "她的声音无论多么温柔，也无法掩饰她利刃般冰冷锋利的本性。"
    show world with dissolve
    u "我早已被那利刃刺穿了全身，我用最后的勇气在她面前逞强，然后转过头，害怕着，用最高傲的姿态离开，在确定脱离她的感知范围后，拼命地逃离。"
    u "我不知道要逃到哪里，但我一定要逃离她的正反世界。"
    scene oce4 with fadehold
    u "最终，仿佛找到了终点，我逃入了名为深海的昏暗狭缝，将自己永远地封闭起来。"
    scene black with dissolve
    u "……黑暗的深海忽然扭曲，像是漩涡，将我困在中心。"
    stop music fadeout 2.0
    u "不，不要……"
    u "我无助地想要呼救，却发不出任何声音。"
    u "喉咙好像被堵住了，也早已看不见任何东西。"
    u "……"
    scene oce5 with dissolve
    u "又是这样……"
    u "已经数不清经历这个梦境的次数了，尽管熟悉了每一个细节，最后的恐惧与惊慌都不能避免。"
    u "距离那时已经过去了几百年？我忘记了许多事。"
    show oce6 with dissolve
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    u "甚至忘记了我曾经的名字，但只有这放逐，仿佛刻印在了灵魂之中。"
    u "我的一切意义，作为天选之神的意义，都是她赋予我的。"
    u "但是，就像是在戏耍我一样，本该伴着一切权能而生的意义、责任，根本就是我的自我想象？"
    u "仿佛我唯一的意义就是作为完美的劣质品，被她观察相对失败的一生。"
    u "于是我也开始自己的观察。"
    u "很快得出结论——即使是劣质的神明，也是人类不可企及的存在。"
    u "之后，我开始注意人类。"
    u "去探索人类的世界，去到不见光明的真正深海，去到海拔八千多米的孤高雪峰，甚至去到那高高闪烁的充满酸蚀的星球。"
    u "但是，这一切对我来说，早已在数百年的时光之中变得平平无奇。"
    u "最终……还是决定真正去接触人类。"
    u "……人类个体的信息早已被收录，作为人类的技巧也在脑海中格外清楚。"
    scene tunnel1 with fadehold
    u "但……那一天与她偶然在那里相遇的时候，却忽然不能熟练地掌握那一切。"
    u "尽管经历了数百年，在那一天的我却变得像个孩子。"
    scene black with dissolve
    u "从那天的分别以后，创造自己的艺术之余，我会偶尔关心她的成长。"
    show a17 with dissolve
    u "她是普通的人类，看不出什么令人惊叹的天赋。"
    scene oce6 with dissolve
    u "她弹吉他的时候，磨破了手指会哭。"
    u "人类的身体与意志果然都很脆弱……但是我不讨厌。"
    u "她还在学习钢琴，听着自己弹出的不成调子的曲子，又哭了。"
    u "……不管怎样……即使是在人类之中，她也过于爱哭了吧？"
    u "我要不要去帮一帮她呢？"
    u "那时，我犹豫着。但是……到了第二天，她又是格外努力地练起那些让她哭泣的乐器。"
    u "这就是人类吗？总是充满了干劲与活力啊。"
    u "这样的话，我还是不要出现了。"
    u "……后来，她加入了一支偶像团体。"
    u "A-SOUL？这个名字听起来怪怪的。"
    u "另外她做得到吗？实力要再提升很多吧，而且她那么爱哭……"
    u "我要不要去稍稍帮助她呢？"
    u "……但人类应该是害怕我的。与我产生交集，并不是什么好事。"
    show f6 with dissolve
    u "如果让我找到自己的生命幻象，那么与我对应的应该是深海之中，阴暗的剧毒水母。"
    hide f6 with dissolve
    u "……是个相对负面的概念。"
    u "还是不要去了。"
    scene oce6 with fadehold
    u "……不久，她们出道了。"
    u "不成熟的她们面对的恶语相向远远多于鼓励支持。"
    u "演出结束的后台，她当然又哭了，而且，不止是她在哭。"
    u "……也许、这就是该我出现的时候了吧？"
    u "但是……忽然发现，情况好像没有那么坏。"
    u "在我下定决心前，她们的队长贝拉站了出来。"
    u "就像是无法击倒的女武神。"
    u "……如果是贝拉，她的意志闯得过那九道死门吗？"
    u "忽然想起了那个人的事情。"
    u "我不知道……但至少这一次，她们当然坚持得下来。"
    u "我发现她们如此相似。尽管她——向晚——是最爱哭的，但是那种努力的热情，却与其余四人没有分别。"
    u "努力着充满斗志，她们当然不会被击垮。"
    u "会失败，但是不会倒下……真是顽强的人。"
    u "……终于，一切都开花、结果。"
    u "“请来一束追光，照亮这海底……”"
    u "……"
    u "她的努力为自己点亮了那束光。"
    u "看着舞台上光彩夺目的她们，我也明白，不会再需要我了。"
    u "曾经我有过无数个机会，但是我选择沉默。"
    u "如今的我羡慕她，却也只能远离。"
    u "一定要去见她也是可以的，因为我是神，无论何时，都能够让人类惊叹。"
    u "但是除了这天赋的诅咒，我完全不剩下什么可谓高尚的价值。"
    scene oce6 with fadehold
    u "直到2022年6月12日，她，向晚的十九岁生日。"
    u "那个创造我的冷漠灵体居然也关注着这边的世界。"
    u "我要在这有限的时间里、为她们留下一些只有我能创造的……"
    u "在她的生日演唱会上，我听见她的歌声再一次呼唤海底。"
    u "她是否还记得我？"
    u "我不知道……无论如何，那个灵体会带来灾厄，我必须给她们留下永恒的礼物……"
    u "……但是，我必须承认，想出这一切的理由，都只是为了让我不要放弃这最后的机会。"
    u "我，想要再见她一次。"
    u "至少要在一个宁静的空间，为这一直以来的感动道谢。"
    u "……于是，她出现在了我的面前。"
    scene oce3 with dissolve
    show a11 with dissolve
    u "像是光明降临于我的世界。"
    hide a11 with dissolve
    u "有些耀眼……于是我躲在了高处的阴影之中。"
    u "这就是，我与向晚重逢的故事。"
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    scene bg7 with fadeholdd
    u1"今天是六月十三日，四带着我来到了这边的学院，见到了我们五人的仿制人偶。"
    u1"本来，一切都还好……但是，四自从见到了一只普通的鸟以后，就好像有些奇怪……"
    u1"她的另一面……多少让我有些畏惧。"
    u1"我能察觉到她的恨意与杀意……我担心，她遇上了什么麻烦。但是……我完全没办法插手。"
    u1"她将我送回房间，又将房间与校舍连接以后，就匆匆离开了。"
    u1"我的房间中被设下了传送阵，可以去到这个世界的一些区域。"
    u1"她说，我可以随意走动，不用担心走丢，因为在这世界中任何一个角落去呼唤她，她都能够立刻赶来。"
    u1"……记得这边的世界里有一座藏书室。我有些好奇，她平时会看些什么书。"
    u1"而且……这里没有网络，没有信号，如果想要找到回去的路，也许只有藏书室查得到方法吧？。"
    u1"我走入传送阵中。"
    scene lib with pixellate
    u1"咦……这藏书室的风格居然出乎意料的简洁。"
    u1"除了空中漂浮的书，和常见的图书馆没有什么分别。"
    u1"很多都是常见的小说，还有一些记录怪谈的书，名字大多很熟悉。"
    u1"看起来，都是原来世界的书呢。"
    show f1 with dissolve
    f1"你来了。"
    hide f1 with dissolve
    u1"她的声音忽然出现在身边，不过我也习惯了她的神出鬼没。"
    show a11
    a1"嗯，我想知道四平时会看些什么书。"
    hide a11
    show f9
    f1"都是人类会喜欢的作品，我偶尔有读一些。不过，对你来说现在有更重要的事情。"
    hide f9
    u1"她这样说，是猜出我想要寻找回到原有世界的办法了吧？"
    show a151
    a1"没错，我一直都想见到我的队友们……但是我不知道该怎么办。"
    hide a151
    show f2
    f1"现在，契机正在成立。"
    hide f2
    show a41
    a1"什么契机？"
    hide a41
    show f1
    f1"我看到她们在为见到你而努力。"
    hide f1
    show a161
    a1"她们？你是说我的队友们？"
    hide a161
    show f2
    f1"没错。但是，单向的心愿需要回应，才能够变得有意义。"
    hide f2
    show f3
    f1"即使她们做好了一切，但是没有你的回应，一样见不到你。"
    hide f3
    show f2
    f1"这座藏书馆有一个特殊之处，凡是进入其中的书，就意味着得到了我的认可。"
    hide f2
    show f17
    f1"这个世界因我而运转，一本书如果得到我的认可，那么它记载的一切幻想，就都能够实现。"
    hide f17
    show a21
    a1"也就是说……我可以学习书中的知识，来联系到我的队友们？"
    hide a21
    show f2
    f1"没错，甚至可以打开时空的门，穿越星海，回到那个世界。"
    hide f2 with dissolve
    u1"她没有阻止我离开，又告诉我离开的方式，但为什么不直接将我送回原有的世界呢？"
    u1"她希望我在这个过程中学到什么吗？"
    u1"也许我确实应该学习一些奇怪的知识。"
    u1"她在一旁坐下，我也开始翻阅起这些书籍。"
    u1"现在的目标很明确，要学会制作“门”的方式，打开通往枝江的门。"
    u1"所以，首先排除掉那些小说。"
    u1"我快速浏览着书脊，一时间找不到想要的书名。"
    u1"嗯……怎么就没有什么魔法大全之类的？"
    u1"不过仔细想想，以四的能力，也完全不需要看什么魔法教材呀。"
    u1"对了！刚刚好像看到有记载怪谈的书。"
    u1"如果能找到一些招鬼仪式，招一个能解答问题的灵，不就找得到合适的书了嘛！"
    u1"至于危险方面……有四在，她一定能保护我的！"
    u1"我循着记忆找到那本书，前面的页数的确记载了一些我眼熟的游戏。"
    u1"像是笔仙、碟仙，还有许多奇奇怪怪的仪式……但这些要么需要准备道具，要么不是一个人能够进行的。"
    u1"我继续向后翻页，书的内容逐渐变得陌生。"
    show a41 with dissolve
    a1"至高召唤仪式……"
    hide a41
    show f1
    f1"哦？你打算玩招灵游戏，来找到合适的书吗？"
    hide f1
    show a141
    a1"是呀，四一定会保护我的吧？"
    hide a141
    show f17
    f1"当然了，你随意玩，有我在，没有恶灵伤得到你！"
    hide f17
    show f4
    f1"……虽然我也可以直接告诉你书的位置的！"
    hide f4
    show a141
    a1"是吗？不过这个召唤似乎还挺有趣的！"
    hide a141
    show a11
    a1"召唤不朽的凤凰原灵，全能的凤凰会实现你的心愿……"
    stop music fadeout 1.0
    hide a11
    show f5
    f1"等等……你说什么？"
    hide f5 with dissolve
    u1"她的声音无比严厉，瞬间闪到了我的身前，好像我说出了极度冒犯她的话。"
    show a151
    a1"……怎么了，四，发生什么了吗？"
    hide a151
    show f6
    f1"对不起，和你没有关系……但是、现在的问题很大……这本书让我看一看。"
    hide f6
    u1"我连忙点头，把那本书交给她。"
    play music "audio/Qm.ogg" fadeout 1.0 fadein 1.0
    show f6 with dissolve
    f1"凤凰图腾？我的世界怎么可能会收录这种图腾！"
    f1"果然是你……从那个时候莫名出现了一只鸟，我就察觉到异常！我就说这种绝对禁止的生物怎么可能被我创造出来，果然是你一直在监视我吧！"
    hide f6
    show f8
    f1"你想让我做什么，又何必畏畏缩缩？而且，你这算是什么？你是在帮她回家？我从来就没打算一直留她在这里，关于向晚的事情还不需要你来插手！"
    hide f8
    show f6
    f1"你出来，我知道你听得见！告诉我，为什么要暗示和影响我的朋友？明明她和你的伟大计划完全没有联系！"
    hide f6 with dissolve
    u1"我怔在原地，看着四歇斯底里地朝着空气大吼。"
    u1"我甚至不敢大口呼吸。"
    show lib1 with pixellate
    u1"忽然，红色的影子降临在藏书室中。"
    n1"我不会对人类做什么的，我只是希望能帮你。"
    show f7 with dissolve
    f1"帮助我？你在开什么玩笑……如果不是你，我何必让她来到我的世界？你以为我不知道你在枝江做的事情吗？我可是你亲手创造的，全知全能的第四原灵！"
    hide f7
    u1"她愤怒地将书毁作碎屑，疯狂般地在藏书室中搜寻着一切剩余的凤凰图腾。"
    show f8
    f1"我毁了这书，向晚，你听好了，我不是要强留你。让你自由离开，根本不需要这只凤凰来插手！带你来到这里，我有着绝对的把握，绝不可能影响六月末的舞台！"
    hide f8
    n1"你心中明白的。她本不必来此，你也并非无错……"
    n1"放过自己吧，■……"
    show f7
    f1"我说过、你 不许 再 叫 我 那个 名字！"
    hide f7
    u1"四深深喘息着，脸上露出扭曲的笑。"
    u1"我没听清那个发音，就像是被什么刻意消除了一样。"
    show f7
    f1"五百年……我一个人在这孤独的深海，你知道我为了什么离开光都，对吧？"
    hide f7
    show f8
    f1"如今我终于遇到了关心的人，对，只是人类，明明只是最普通的人类，为什么你还要来破坏我微小的满足？"
    hide f8
    n1"我没想过破坏什么，我反倒希望帮你抓住这最后的机会。"
    n1"仅此而已。"
    show f8
    f1"最后的机会……真是好笑。"
    hide f8
    u1"她忽然沉默了许久。"
    show f6
    f1"你走，我不想看见你。"
    hide f6
    u1"红色的影子没有继续说话，只是仿佛深深地看了我一眼。"
    u1"似乎是一种期许？"
    u1"虽然看不清晰，但直觉告诉我，那是一个很美丽的生物。"
    hide lib1 with pixellate
    stop music fadeout 2.0
    u1"然后，就忽然消失掉了。"
    show a161 with dissolve
    play music "audio/破碎冬日.ogg" fadeout 2.0 fadein 2.0
    a1"你还好吗？"
    hide a161
    show f8 with dissolve
    f1"轻而易举就歇斯底里的神灵的确是不完美的。果然……阴暗的被放逐者不配在光的身边。"
    hide f8
    show lib3 with pixellate
    u1"她并没有回答我。而她的话音落下，纯白闪光的门就在我眼前打开。"
    u1"我想要反驳她，但是，在她强大的压迫力下，我慌乱、胆怯，甚至说不出话。"
    u1"况且……现在的她也听不下去我说什么吧？"
    show f8 with dissolve
    f1"你也走，向晚，回到枝江去吧，不要再回来。"
    hide f8 with dissolve
    u1"我点头答应，但是脚下仍然犹豫着，无法走向那闪光的门。"
    u1"我曾无比期待与队友重逢，但是现在，我不应该留四自己在这里。"
    show f3 with dissolve
    f1"你去看一看这门。"
    hide f3 with dissolve
    u1"……焦急哭泣的贝拉与珈乐、"
    u1"一夜不眠梳理线索的嘉然和乃琳……"
    u1"她们的身影在门中闪过。"
    show a161 with dissolve
    a1"对不起……"
    hide a161 with dissolve
    u1"是我让大家担心了。"
    u1"我再次望着四，她的眼中是本就属于她的孤高。"
    u1"并不是我留她在这里……她本就属于这里。"
    n1"晚晚！"
    u1"是她们……我听见了她们在门中的呼喊！"
    show lib4 with dissolve
    u1"门变得像是水波纹一样，她们的影子晃动着，却那么真切。"
    u1"触手可及的重逢，我看见了那个属于我的位置。"
    u1"我也再一次确定，我属于哪个世界……"
    show a161 with dissolve
    a1"再见……四，照顾好自己。"
    hide a161
    show f19 with dissolve
    f1"嗯……不要担心我！月末的演出会成功的，一切都会好的。"
    hide f19 with dissolve
    u1"她没有说再见，难道说这就是最后一面了吗？"
    scene white with dissolve
    u1"但是，没有不会醒来的梦，我该醒了。"
    stop music fadeout 2.0
    u1"走过门去，我拉住了两只温暖的手。"
    scene black with fadeholdd
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    u1"我还没有看清门外的世界，就被一个软软的东西撞了上来。"
    a1"什……"
    u1"砰——哗——"
    scene rem1 with dissolve
    d1"晚晚你终于回来了！我……我……"
    u1"我被扑过来的然然……呜哇，脚好凉！什么……"
    show rem2 with dissolve
    u1"我被撞倒在了地上，只能看到抱着我的然然……"
    d1"晚晚……"
    u1"……但脚下是什么？我是踩进了水母缸里？"
    u1"我想要去看，但完全看不到发生了什么。"
    d1"晚晚……哈哈哈，终于回来啦！！……"
    c1"……盆！"
    u1"珈乐好像在着急地喊些什么，我却完全没有头绪。"
    a1"怎么了怎么了？为什么好像……出了什么事故的样子？"
    e1"嗯？事故，什么事故？哈哈……我怎么不知道？"
    d1"嘿嘿……嘿嘿嘿……哈哈哈哈哈哈……"
    u1"发生什么了……然然怎么一直在傻笑啊？"
    b1"没关系没关系！还好你回来了，真的太好啦！"
    c1"那个……关心的话等收拾一下再谈吧……大家真的不管那个水盆吗？"
    a1"……水盆？什么水盆？"
    scene rem3 with dissolve
    u1"然然抱着我的手终于稍稍松开了些。我朝周围看去，才看到地板上已经洒得到处是水，水盆就倒扣在然然的腿上。"
    b1"然然你先站起来一下，我们收拾一下房间！"
    d1"好……对不起。"
    scene bg1s with fade
    u1"我看着凌乱的房间，仿佛看到了她们为了接我回来，所做的一切努力，"
    u1"我看到她们的时候，也是无比的感动，"
    u1"但是，我还是好奇，她们究竟做了什么啊！水盆又是干什么的？"
    show a11 with dissolve
    a1"虽然不是很合适！但是我真的想要问一下——"
    hide a11
    show a141
    a1"我刚刚是从水盆里回来的吗？"
    hide a141
    show b2 with dissolve
    b1"不是啦！虽然这个水盆是用来召唤你的，但你是从门出来的，很优雅的，就像是天使降临一样。"
    hide b2
    show a11 with dissolve
    a1"那水盆为什么翻了？"
    hide a11
    show e4 with dissolve
    e1"然然看到你回来太兴奋了，就直接扑过去抱住了你……然后把水盆撞翻了。"
    hide e4
    show d21 with dissolve
    d1"抱歉！抱歉！"
    hide d21
    show c1 with dissolve
    c1"没关系的，这个应该叫接风洗尘吧？真的有在洗呢！"
    hide c1 with dissolve
    u1"虽然有了一个小插曲，但能看到她们的脸，简直比什么都开心！"
    u1"而且，与四分别的沉重，反倒因此消散了许多。"
    u1"……很快，我们就把房间里的水都擦干净了。"
    u1"我和然然也都换好了衣服，之后，我们彼此一定都有好多事情要讲！"
    u1"……为了接我回来，她们究竟做了多少努力？而且，她们也一定好奇我在那边的故事吧！"
    show a21 with dissolve
    a1"我们换一个地方吧？我有好多事情要和大家讲！"
    hide a21 with dissolve
    scene bg6 with fade
    u2"为了庆祝晚晚回来，大家一致决定，准备一顿大餐，来弥补昨天没能一起过生日的遗憾！"
    u2"而且，虽然早餐吃过了，但是那个时候，大家都没什么心情吃饭。"
    u2"更何况，这一番奇异的折腾以后，很难不饿的吧？"
    u2"我们互相讲述起这短短半天的奇异经历。"
    show a11 with dissolve
    a2"……最后，四感受到了大家的呼唤，就为我打开了门，送我回来啦！"
    hide a11
    show d11
    d2"哇，所以她也没有让你一定要学会那些法术，居然就这样放你回来了，这个结局我没有想到！"
    hide d11
    show a141
    a2"哈哈……毕竟是神嘛！她的心思，也不是我能随意揣测的。"
    hide a141
    show b3
    b2"说起来，你在那边有没有听到过这个名字？xin，yu，不知道是什么发音，但一定是这个拼法的。"
    hide b3
    show a11
    a2"我没有听过，这是谁？"
    hide a11
    show e1
    e2"可能是一个神……她给了我们关于水的提示。可是，你说神的名字是“四”。"
    hide e1
    show a141
    a2"哦……这样嘛？那我不清楚呀……"
    hide a141
    show c1
    c2"而且，虽然不能确定，但是乃琳或许见过她！"
    hide c1
    show a21
    a2"哦？是什么时候？"
    hide a21
    show c1
    c2"就是你和然然跟着拉姐练舞，我和乃琳出去买吃的那天！"
    hide c1
    show a141
    a2"那又不是什么很少见的情况……不过，我好像记起来了……"
    hide a141
    show a21
    a2"那么早的事情吗？那么有意思的事情，你们居然没和我讲过！"
    hide a21
    show e1
    e2"当时也没把她和神联系起来嘛！以为她就是一个长得很漂亮的红衣女人呢。"
    hide e1
    show a41
    a2"红衣女人？"
    hide a41
    show e2
    e2"对，你们没有见过可能想象不到，她那种气质就像是凤凰一样！"
    hide e2
    stop music fadeout 2.0
    show a41 with dissolve
    a2"凤凰……"
    a2"心、雨……原来是这个名字啊……"
    hide a41
    show d31
    d2"晚晚，怎么了？"
    hide d31
    show a141
    play music "audio/Zki.ogg" fadeout 2.0 fadein 1.0
    a2"不，没什么的！就是听到了神的名字，有些激动而已，不用在意的！"
    hide a141
    show b10
    b2"……哦。"
    hide b10
    u2"听到我“哦”了一声，晚晚的身体居然微微颤了一下。"
    u2"不会吧？到了这种时候……还要害怕我吗？明明又不是在练舞！"
    u2"……不过我也不该这样说的，本来就知道她们比较敏感，我还是应该温柔一些。"
    u2"但是，她今天的态度真的有些奇怪啊！"
    u2"……总感觉她讲的故事收尾好仓促，还没有听得过瘾，就戛然而止了。"
    u2"如此难以预测，也许这就是神的作风？"
    u2"我还是不要想太多了！"
    u2"……之后，我们喝着果汁庆祝，但晚晚好像有些累了，除了和我们一起干杯，就只是低着头慢吞吞地吃饭。"
    show c1 with dissolve
    c2"为了我们A-SOUL的重逢，干杯！"
    hide c1
    show b3
    b2"干杯！今天我们暂停训练一天，但是大家之后要更加努力！月末的演唱会，一定要好好表现！"
    hide b3 with dissolve
    u2"……"
    u2"吃过饭后，晚晚好像真的累了，向我们告别后就回到了自己的房间。"
    u2"我收拾得比较慢，最后，休息室中只剩下我和然然。"
    show d41 with dissolve
    d2"拉姐，那个……其实我有话想和你说。"
    hide d41
    show b1
    b2"怎么还犹犹豫豫的？该不会要说喜欢我吧？"
    hide b1
    show d31
    d2"不是啦！我是真的有事情……拉姐，你不觉得晚晚有些不对劲吗？"
    hide d31
    show b2
    b2"嗯，应该是她累了吧？这种离奇的事情刚刚发生在她身上，怎么可能还像之前一样充满活力呢。"
    hide b2
    show d11
    d2"不，晚晚如果累了，她一定会抱怨的，而且还会找我们撒娇！"
    hide d11
    show b1
    b2"说得对诶！但是会不会，她已经累得没力气撒娇了？"
    hide b1
    show d31
    d2"她回来的时候还很精神呢！我是感觉，她好像有什么事情瞒着我们。"
    hide d31
    show b10
    b2"什么事情？"
    hide b10
    show d61
    d2"拉姐，你现在能讲清楚，为什么四将晚晚带去了自己的世界，又将她送了回来吗？"
    hide d61
    show b2
    b2"我……我好像明白，却又讲不明白……"
    hide b2
    show d31
    d2"直觉告诉我，晚晚隐瞒了一些关于四的事情。而且，这种事不是无关紧要的，晚晚不是那种会计较鸡毛蒜皮的小事的人！"
    hide d31
    show b10
    b2"嗯……我也觉得晚晚在那个时候以后，突然变得怪怪的——"
    hide b10
    show b3
    b2"就是……就是我们提到那个叫xinyu的神以后！"
    hide b3 with dissolve
    u2"忽然，餐厅的门被推开了。"
    u2"乃琳和珈乐居然又回来了！"
    show e5 with dissolve
    e2"没错，拉姐，我刚刚也有和乐讨论这件事情，我们也觉得晚晚的样子不太正常。"
    hide e5
    show c2
    c2"她一定知道些什么关于神的事情，但是因为某种原因，没有告诉我们。"
    hide c2
    show b1
    b2"也许是她和四的小秘密吧？我们也没必要什么都知道呀。"
    hide b1
    show e2
    e2"拉姐，还记得塔罗牌的结果吗？"
    hide e2
    show b1
    b2"可我们已经带晚晚回来了！"
    hide b1
    show e5
    e2"但是占卜之后，我们并没有真的做出什么选择，而除了晚晚的归来，这件事情也并没有一个清晰的结局。"
    hide e5
    show c2
    c2"这有什么说法吗？"
    hide c2
    show e1
    e2"那只冥河水母传递出“放逐”的概念，这指的应该是四。而关于四，命运之轮还没有转动，世界也没有完成。"
    hide e1
    show b10
    b2"但是，这需要我们去……“转动”吗？"
    hide b10
    show e1
    e2"当然！这一件事的核心并不只是四，而且，正是因为晚晚，我们才会做那次占卜。所以，在这个事件中，四和晚晚是彼此关联的。"
    hide e1
    show d61
    d2"也就是说，晚晚之后还会去转动那“命运之轮”？"
    hide d61
    show e5
    e2"是的，恐怕必然如此。"
    hide e5
    show c2
    c2"所以拉姐，我们才希望你可以去和晚晚单独谈一谈，如果那边留有隐患，恐怕四还是会找上晚晚的。"
    hide c2
    show b10
    b2"好……老实说，我也不能够完全信任四，毕竟直到现在，我也不明白她的动机。果然还是要去和晚晚聊聊的。"
    scene black with fade
    stop music fadeout 2.0
    play sound "audio/qiaomen.ogg"
    b2"晚晚？"
    a2"拉姐吗……"
    b2"是我，我可以进来吗？"
    a2"当然可以！"
    scene bg1s with fade
    play music "audio/Zki.ogg" fadeout 2.0 fadein 3.0
    u2"我走进她的房间，尽量保持着轻松的表情，在床边坐下。"
    show b10 with dissolve
    b2"刚刚……你是不是在隐瞒一些事情？"
    hide b10
    show a122
    a2"我……我……"
    hide a122 with dissolve
    u2"她支吾着，不敢与我对视。"
    show a142 with dissolve
    a2"我没有……"
    hide a142
    show b1
    b2"你看，你果然一点都不会说谎！没关系的，我没有怪你的意思。只是，大家很担心你。"
    hide b1
    u2"她低下头，沉默着不说话。"
    show b1
    b2"关于四，你还有很关键的部分没有说，对吧？"
    hide b1
    show a162
    a2"嗯……"
    hide a162
    show b10
    b2"我没有想要逼你交代一切，但是，按照乃琳的占卜，你并没有完全与那边的世界脱离联系。如果……终将再次面对那些神灵，我们是不可能坐视不管的！"
    hide b10
    show b1
    b2"晚晚，你知道你可以相信我们的。把真正的前因后果告诉我吧，我们一起想办法解决问题！"
    hide b1
    show a152
    a2"好……我不知道究竟什么才是一切的根源。四的名字应该是随意起的，因为她是全知全能的第四原灵……"
    hide a152
    show a172
    a2"而联系起现有的一切信息，我想……"
    hide a172
    show a42
    a2"创造她的，大概就是这个、可能叫心雨的神。"
    a2"不知道具体的读音，我暂时叫她心雨了……就像四的化身是水母，心雨的化身则是凤凰。"
    hide a42
    show b2
    b2"原来她们果然认识呀！"
    hide b2
    show a152
    a2"但是在四的眼中，心雨是一个冷漠无情的神……她对心雨的恨一直持续了几百年。"
    hide a152
    show a162
    a2"据四所说，她将我带去她的世界，是因为发现心雨已经注意到我，希望可以将我保护起来。"
    hide a162
    show b1
    b2"但是……心雨真的是坏人吗？"
    hide b1
    show a152
    a2"我不清楚她们过去发生了什么，但是现在，也许心雨是想要帮助四的……可因为一些我不知道的原因，四对她有着很深的怨念。"
    hide a152
    show a162
    a2"至于这件事的结尾，因为害怕大家担心，就没有说……"
    hide a162 with dissolve
    u2"然后，她细细讲了从在学校看到鸟，一直到四发现凤凰图腾而变得疯狂的事情。"
    show a162 with dissolve
    a2"最后，她坚持让我走，我在门中看到了大家担心我的样子，而且，她又摆出了一副神灵的高傲姿态……"
    a2"……可是现在想起来，她应该是为了让我决心离开，才做出那个样子的。"
    hide a162
    show b1
    b2"所以你是担心她，想要主动一些，尝试帮她解开心结？"
    hide b1
    show a12
    a2"是……我想，我们应该已经算是朋友了，而且，她也有一直在看我们的。"
    hide a12
    show b10
    b2"但是现在，你还能够轻易回去吗？"
    hide b10
    show a172
    a2"我不知道。但她告诉过我，不要再回去。"
    hide a172
    show b10
    b2"“不要再回去”，让我想想……"
    hide b10
    show b3
    b2"这是劝告！那、是不是意味着，选择权在你的手上？"
    hide b3
    show a162
    a2"好像是诶！但是拉姐，我现在也不知道该怎么办了……"
    hide a162
    show b1
    b2"为什么？"
    hide b1
    show a152
    a2"即使我真的能去往那里，但是大家为了带我回来，那么辛苦，我们还有着月末的演出，一定要好好准备的……"
    hide a152 with dissolve
    u2"晚晚说得对，我们之后还有着重要的演出，四的情绪又反复无常，或许应该让她冷静一段时间，我们也全力准备月末的演出。"
    u2"既然她对我们抱有善意，那么等到演出结束以后，我们当然也可以回馈这心意的吧？"
    show a22 with dissolve
    a2"但是，她在那边的世界，不但能够让我轻易学会飞，甚至还说过、类似于确保月末演出一定会成功的话……或许现在就去找她，也不会影响演出的！"
    hide a22 with dissolve
    u2"这也有道理，她是那么强大的神灵……更何况，我们的演唱会本就是为了给人带去快乐。"
    u2"既然命运将我们连接起来，或许回应才是好的选择。"
    show b1 with dissolve
    b2"晚晚，你怎样想？"
    hide b1
    show a152
    a2"我不知道，所以才希望拉姐能告诉我。"
    hide a152 with dissolve
    u2"忽然，乃琳的话在我心中闪过。"
    u2"在那个占卜之中，四和晚晚是关联在一起的，而晚晚和我们更是在一起的。"
    u2"……如今，要让我来推动这命运之轮了吗？"
    show b10 with dissolve
    b2"我需要想一想，晚晚，你先休息一下吧。"
    hide b10
    show a142
    a2"好，拉姐，我相信你！"
    hide a142
    scene zl with fade
    u2"我走出晚晚的房间，我不知道要走向哪里，但是，也许我想有一个人聊聊。"
    u2"我拿出手机，犹豫了片刻，打通了一个电话。"
    stop music fadeout 2.0
    show b3 with dissolve
    b2"乐，你在哪里？"
    hide b3 with dissolve
    c2"怎么了，拉姐？你需要我在哪里，我可以现在就过去。"
    show b2 with dissolve
    b2"那可以来一下我的房间吗？我想和你说一说话。"
    hide b2 with dissolve
    c2"好，我这就来！"
    scene bg2 with fade
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show b1 with dissolve
    b2"乐，我刚刚有和晚晚谈过了。"
    hide b1
    show c5
    c2"晚晚怎么样？"
    hide c5
    show b10
    b2"她没什么事的，只是我……有一些害怕……"
    hide b10
    show c1
    c2"这是进步哦！以前的拉姐可从来不会和我们承认自己害怕的。"
    hide c1
    show b2
    b2"哈哈，这次的事情也让我知道了，我又不是无所不能……我也要多依靠大家一些。"
    hide b2
    show c4
    c2"拉姐这样很可爱！那么，是在害怕什么？"
    hide c4
    show b10
    b2"现在，命运之轮的枢纽好像交到了我的手里。"
    hide b10
    show c2
    c2"……是选择？"
    hide c2
    show b10
    b2"嗯，虽然我以前也做过选择……"
    hide b10
    show b1
    b2"我并不会介意去聊我的腰伤，因为那虽然是痛苦的过去，但是我做出了自己的选择，坚持到了最后，伤痛反倒成了一种证明。"
    hide b1
    show b10
    b2"但是这一次，我却不是在为自己做选择……所以我真的害怕。"
    hide b10
    show c1
    c2"是为了谁选择呢？"
    hide c1
    show b10
    b2"……是四。她的世界会如何完成，也许就是由我们推动的。"
    hide b10
    show c7
    c2"晚晚和四更加熟悉吧？为什么她没有做出选择？"
    hide c7
    show b1
    b2"她说她不知道……所以希望我能够告诉她。"
    hide b1
    show c3
    c2"四是支持着我们的，这一点，大家都知道。"
    hide c3
    show c4
    c2"所以我猜，晚晚不是不知道，而是她认为，命运之轮的推动者不该是向晚，而应该是A-SOUL。"
    hide c4
    show b2
    b2"然后……因为我是队长，所以我来做这个决定吗？"
    hide b2
    show c1
    c2"是的，哈哈……其实某种意义上，不论是晚晚还是我……我们都是在逃避去做决定的。"
    hide c1
    show b2
    b2"哇……你们好坏！"
    hide b2
    show c1
    c2"但是我们永远会是你的支持者，拉姐做出了选择，那么我们就会在你的背后。"
    hide c1
    show c4
    c2"我想，这也是晚晚的想法。"
    hide c4 with dissolve
    u2"我明白，队长不止是作为那个承担一切责任的人。"
    u2"队长也同样会收获到大家的支持，那种支持是如此温暖，值得依靠。"
    show b1 with dissolve
    b2"谢谢你，我明白了。"
    scene zl with fade
    u2"我走出门，向着晚晚的房间走去。"
    u2"是时候做出决定了。"
    stop music fadeout 2.0
menu:
    "暂时先准备训练，等待演出的结束":
        jump six
    "重返四的世界，制定新的训练安排":
        jump seven
label six:
    play music "audio/破碎冬日.ogg" fadeout 2.0 fadein 2.0
    u2"我想，这个世界上，也许有些事只有一次机会。"
    u2"也许，四与心雨之间维持这个状态，已经有了数百年，再过半个月，也并不会有什么改变。"
    u2"但是，去往北方都会的鸟巢，是我们最大的梦想。"
    u2"我们不清楚未来的样子，也正是因为不清楚，没有办法假设接下来发生的事……"
    u2"我们必须全力以赴。哪怕十拿九稳，也要尽量降低那一成失败的可能性。"
    u2"绝对不能失败！"
    u2"晚晚再次前往那里，也许不会有危险。"
    u2"但是，仅仅是这两天，我们就已经冒了太多的风险，我真的不想再赌一次未来。"
    u2"我从来没有幻想过，人生会有存档。"
    u2"我也从没有为我的任何一个决定后悔过。"
    u2"……但是，经历过无数的坎坷，一步步走到今天，偶尔梦回昔日，也会心惊胆战。"
    u2"如果可以回到过去，回到那一天前，避免那一次腰伤……"
    u2"我不知道我会如何选择……哪怕知道今天的结局，我又是否有勇气选择接受命运呢？"
    u2"也许没有那些磨难，就不会有今天的贝拉……"
    u2"……但一次的决定不只是为了我自己，所以我绝对不能留下遗憾。"
    u2"我朝着晚晚的房间走去，仿佛我悬着的心也终于放下。"
    u2"晚晚，我已经决定好了。"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 3.0
    scene bg6 with fadehold
    u2"半个月后。"
    u2"一切都得到了应有的回报。这些天来，毫不马虎的训练成效卓著，北方都会的演唱会，取得了前所未有的大成功！"
    u2"终于实现了一直以来的梦想，我们决定吃一顿大餐来庆祝！"
    u2"……"
    show a151 with dissolve
    a2"拉姐，我们是不是、还有某个地方要去？"
    hide a151
    show b10 with dissolve
    b2"嗯……好像是的。但是你能想起来那是哪里吗？"
    hide b10
    show a161 with dissolve
    a2"应该是要去找一个人……可那是谁呢？"
    hide a161
    u2"嗯……是有这么一回事……可那是谁呢？"
    show b1 with dissolve
    b2"抱歉……我也想不起来……但今天是开心的一天，就不要想那些了！"
    hide b1 with dissolve
    u2"餐桌边，我们欢笑着庆祝。但是，我却莫名觉得脑中空空的。"
    u2"好像有什么重要的事情忘记了……却甚至连记忆的碎片都无法抓住。"
    u2"有谁……曾经离开过吗？"
    u2"……"
    show a141 with dissolve
    a2"对不起，我肚子有些不舒服，我要先回一下房间！"
    hide a141
    show d31 with dissolve
    d2"你还好吗？没关系吧？"
    hide d31
    show a11 with dissolve
    a2"没关系，很快就能调整好的，不要担心我！大家好好吃饭！"
    hide a11 with dissolve
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    scene bg1 with fadehold
    u1"我躺在床上，呆呆望着天花板。"
    u1"并没有真的肚子疼，也不是不想和大家一起庆祝，只是有一件很重要的事情，无论如何都想不起来了。"
    u1"……1…9…2…6…5…7…3…8……"
    u1"我毫无目的，只是数着眼前的数字灯。"
    u1"总觉得少了些什么。"
    u1"嗯……这数字灯为什么没有4呢？"
    u1"想到那个数字的瞬间，我心中好像涌起一股温暖，像熟悉的风从远方吹来。"
    u1"但那只是幻觉……虚幻到，甚至马上就能觉察到它过分的遥远，那大概是永不可能跨越的阻隔。"
    u1"为什么明明已经成功了，那淡淡的失落却像是吹不散的薄雾？"
    stop music fadeout 2.0
    u1"好困……"
    scene black with fadehold
    u1"……"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene dream with fadehold
    u1"这里是梦，我知道的。我曾无数次见这梦境。"
    u1"这个梦……曾是阴暗的、模糊的蓝色。"
    scene dream2 with dissolve
    u1"只是这一次……"
    u1"沉默的蓝好像很久很久的朋友。"
    u1"但直觉告诉我，这是最后一次的见面。"
    u1"也许是诀别时刻？"
    u1"只是……为什么要诀别呢？"
    u1"早已记不清初见的理由……哪怕这一次的自我无比清晰。"
    scene dream3 with dissolve
    a1"永别了……我深蓝色的梦。"
    $ quick_menu = False
    scene dream8 with Dissolve(3.0)
    stop music fadeout 8.0
    scene dream9 with Dissolve(3.0)
    $ renpy.pause(5, hard=True)
    return
label seven:
    play music "audio/破碎冬日.ogg" fadeout 2.0 fadein 2.0
    u2"我想，这个世界上，也许有些事只有一次机会。"
    u2"也许，四与心雨之间维持这个状态，已经有了数百年。但是，当女王成为流放者、戴上枷锁的时候，命运之轮就不再是停滞的了。"
    u2"我不清楚她们之间的恩怨，也正是因为不清楚，没有办法假设接下来发生的事。"
    u2"……如果我们放手不管，命运之轮会继续转下去。"
    u2"也许就在某个平凡的日子，我们欢笑着训练，另一侧的一切已经无法挽回……"
    u2"我不允许这样！"
    u2"晚晚再次前往那里，会有危险吗？一定不会的。"
    u2"即使是最艰难的时候，我们都能够连接彼此，最终重逢，更何况是现在呢？"
    u2"会影响训练吗？当然会的。"
    u2"但是这种困难完全可以克服！如果只是这种程度，都能够让我们退缩不前，我们也不会是今天的A-SOUL。"
    u2"我从来没有幻想过，人生会有存档。"
    u2"因为我从没有为我的任何一个决定后悔过。"
    u2"哪怕是可以回到过去，回到那一天前，避免那一次腰伤，也完全没有必要！"
    u2"如果没有那些磨难，也不会有今天的贝拉。"
    u2"这一次的决定也是一样，我相信自己不会后悔。"
    u2"我朝着晚晚的房间走去，忽然间，感觉像是奔赴战场的士兵一样。"
    scene bg1s with fade
    show b3 with dissolve
    b2"晚晚，我已经决定好了！"
    hide b3 with dissolve
    stop music fadeout 2.0
    $ quick_menu = False
    scene dt with fadehold
    $ renpy.pause(8, hard=True)
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene black with fadehold
    $ quick_menu = True
    b1"晚晚，我已经决定好了！"
    u1"迷迷糊糊的我正游离在梦境边缘，忽然被拉姐一把拽了出来。"
    scene bg1s with dissolve
    u1"我连忙下床，看到她就像是要出征一样，腰挺得笔直，一副坚定的表情。"
    show b10 with dissolve
    b1"我决定了，四的事情，不能够耽搁，那边的世界情况复杂，她和另一个神的关系我们也不能把握。我不知道，继续拖下去会不会有什么意料之外的事情。"
    hide b10
    show a21
    a1"所以拉姐同意我回去找她了？"
    hide a21
    show b1
    b1"没错，但是不完全准确！首先，这一次你去那边的世界，我们之间一定要能够保持联系，这是为了保证训练不出问题！"
    hide b1
    show a11
    a1"好，如果能够回去，四不会不同意我们联系的！"
    hide a11
    show b2
    b1"然后，这一次让你单独回去是出于礼貌——晚晚你到了以后，去问一问她……我们是不是也可以一起去。"
    hide b2
    show a141
    a1"我一定会问的！如果她不同意，那我就想办法让她同意！"
    hide a141
    show b3
    b1"好！气势上很到位，那么晚晚，祝你好运，我去和大家讨论接下来的事情了！"
    hide b3 with dissolve
    u1"拉姐似乎很开心，挺着胸离开了我的房间。"
    u1"但是，之后我该怎么让四听见我呢？"
    u1"我应该是有办法回去的吧？我还记得我临走之时，那红色神灵的期许。"
    u1"现在想来，也许她正是希望我去帮助四……如果是这样，我一定是有办法回去的！"
    u1"……不知道用她的方法，在这边的世界能不能飞起来呢？"
    u1"我忽然想到了这个毫不相关的事情，而且，非常想要试一试。"
    stop music fadeout 1.0
    scene bg1s with vpunch
    play sound "audio/fly.ogg"
    u1"……几乎在我有了这个想法的同时，我就已经悬空而起！"
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    u1"这……这就是神的能力吗？居然在这边的世界也毫不受限？"
    u1"这就是宇宙……"
    u1"始源。一种概念在我的心里逐渐清晰——四所拥有的力量的根本法则，那种无所不能的力量，在宇宙之中无处不在。"
    u1"我正是被她赋予了一缕这奇异的能力，我能够感知到始源的存在。"
    u1"我伸出手，在空中想象出门的形状。"
    u1"当然，我的力量远远不够穿透空间，但我确信，我的心意一定已经穿越了遥远的星河。"
    show a21 with dissolve
    a1"四——你能听见我吗？我想要见你！"
    hide a21 with dissolve
    u1"门没有出现，但是，我分明觉察到，始源已经在动荡。"
    u1"四听见了，她在犹豫！"
    show a41 with dissolve
    a1"我知道你听得见我，不要再逃避了，可以打开门吗？"
    hide a41 with dissolve
    u1"这一次，始源却彻底安静了。"
    show a151 with dissolve
    a1"四？"
    hide a151 with dissolve
    u1"安静得异常，我甚至开始怀疑最初只是我的错觉。"
    u1"但是，这种感知是不可能出错的！"
    show a161 with dissolve
    a1"如果你听见我的心愿，可以给我一些回应吗？你给了我始源的能力的，我现在能够感受到你！"
    hide a161 with dissolve
    u1"没有回应。"
    u1"为什么？她真的不想要再见我了吗？"
    u1"如果是这样……那该怎么办呢？"
    u1"一时间，种种灰暗的假设纷纷涌进脑海，我一切的幻想都被打破了，刚刚在心中为她设计的一切，此时都好像成为了对我的嘲……"
    stop music fadeout 1.0
    play sound "audio/qiaomen.ogg"
    u1"咚咚咚！"
    b1"晚晚！"
    u1"拉姐一边敲着门，一边喊着我的名字，直接把我从失落中打断。"
    u1"我立刻打开门，拉姐的喘息有些急促，好像是跑着来的。"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show b2 with dissolve
    b1"我忽然发现了一本书，你或许用得上！"
    hide b2 with dissolve
    u1"《传送门的制作方法》！"
    u1"这简直是不能更直接的书名了吧？"
    show a141 with dissolve
    a1"这是哪里来的？"
    hide a141
    show b1
    b1"刚刚在走廊里捡到的，觉得你可能会需要！"
    hide b1 with dissolve
    u1"我忍不住笑了出来。"
    show a141 with dissolve
    a1"哇……这么直球的傲娇吗？"
    hide a141
    show b2
    b1"什么？"
    hide b2
    show a121
    a1"是四啦，我还以为她真的不想再见我了呢！刚刚她不给我开门，还藏了起来！但是她一定又怕我真的不去了，所以才临时丢了这本书让拉姐带给我。"
    a1"不然，哪里有人类会写这么奇怪的书！"
    hide a121
    show b2
    b1"那她好像还挺可爱的！"
    hide b2 with dissolve
    u1"我接过了书，还是要先确定内容。毕竟，即使这本书百分之九十九是出自四的设计，仍然有那百分之一的可能，让这一切化为我的自作聪明。"
    u1"很快确认完毕！还好这本书是真的想要教会我！"
    u1"临时传送门、永久传送门、单向传送门、双向传送门、通讯门……十几种传送门的构建方法都用最简单的语言解释得清清楚楚，实践起来甚至像是吃饭一样简单！"
    show a21 with dissolve
    a1"拉姐，我们先尝试一下，开几个临时的门，把我们所有人传送到休息室去！"
    hide a21
    show b10
    b1"好……不过晚晚，你真的能用这些方法？"
    hide b10
    show a41
    a1"应该能的吧？准备好了！"
    hide a41
    show a21
    a1"三、"
    a1"二、"
    a1"一！"
    scene res with pixellate
    u1"下一刻，我们所有人都真的到了休息室！"
    u1"哇，这种感觉太奇妙了！"
    show e7
    e1"咦……这是？"
    show c3 at right
    c1"为什么大家突然都到了这里？"
    show d31 at left
    d1"刚刚有一瞬间，我好像看到有门打开了！"
    hide d31
    hide e7
    hide c3
    show a21 with dissolve
    a1"没错！就是我打开了传送门，这次是一个小小的尝试。"
    hide a21
    show e2
    e1"哇！晚晚，你好厉害！"
    hide e2
    show a141
    a1"没有啦……这些东西都是四教给我的，我也没想到，在这边居然也能用这些能力！"
    hide a141
    show b1
    b1"你说，有没有一种可能？那本书其实是心雨给你的？"
    hide b1
    show a21
    a1"怎么可能？她不是一直在和你们猜谜嘛！那么喜欢猜谜的凤凰，怎么可能会用这么直接的方式！"
    hide a21
    show c1
    c1"之后，你是要打开去往那边的门吗？"
    hide c1
    show a11
    a1"没错！我会去问她的。这一次如果可以，大家也要和我一起去！"
    hide a11 with dissolve
    u1"休息室中，我打开了一扇永久的、双向的门。"
    show a21
    a1"我很快就会回来的！"
    play music "audio/第四约定.ogg" fadeout 3.0 fadein 3.0
    scene oce7 with fadeholdd
    u "一天前。"
    u "那个我一直关注着的少女，来到了我的世界。"
    u "……但是，我该怎样面对她呢？"
    u "我躲在高处的阴暗之中，一边窥视着她，一边想着无趣的措辞。"
    u "即使曾有过无数的想法，但真的见到了她……还是好紧张！"
    u "我该怎么办？"
    u "是要用神的姿态，让她能够重视我，还是亲切一些呢？"
    show a18 with dissolve
    a"你是谁？"
    hide a18
    u "没有时间继续考虑了。"
    show f14 with dissolve
    f"……我是四。"
    hide f14
    u "也没有什么选择空间，我只能这样回答。"
    show a19
    a"抱歉，我没有听清楚！可以大声些吗？我叫向晚！"
    hide a19
    u "嗯，向晚……我一直都知道的。"
    u "不过，我的名字是什么？"
    u "……"
    u "曾经的名字充满了诅咒，我不愿再提起。如今，我的名字也只是个被放逐者的编号。"
    u "果然，还是这个吧。"
    show f14 with dissolve
    f"我的名字是……四。"
    hide f14
    u "最初的相遇，我真的好紧张。"
    u "虽然对我来说，这更应该算是一次重逢。"
    u "……不过，如果以后真的会再见面，对我来说，会不会再次成为初次相遇呢？"
    scene oce2 with fade
    u "我有好多话想对她说，如果可以，我愿意给她无比充足的精力，和她聊上一天一夜。"
    u "但是，最后向她祝福过生日快乐，我已经没办法控制自己的困倦了。"
    scene medusa1 with fade
    u "送她来到了这边的房间后，我就像是彻底垮掉一样，躺在了她的屋子上。"
    u "屋子是一只大水母，从外面碰起来，感觉还是软软的。"
    u "远处，传来了鲸的歌声。"
    u "向晚……"
    u "……我轻轻咳嗽着。我也不知道，这一切还能够持续多久。"
    u "不管怎样，我还是要看着她的。"
    u "等她睡着以后，我再休息吧。"
    u "我只要半个小时就够了。"
    stop music fadeout 2.0
    scene black with fade
    u "……"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 3.0
    u "熟悉的颜色。"
    u "我看不清太远的事物，而眼前的一切也有些似是而非。"
    scene dream5 with fadehold
    u "你会不会在意水母的想法？哪怕……？"
    scene dream6 with dissolve
    scene dream7 with dissolve
    u "什么？"
    stop music fadeout 2.0
    scene oce8 with pixellate
    u "……不，是有些熟悉的。"
    play sound "audio/shuipao.ogg"
    u "是啊……一直。都很熟悉、……只是，世界好像不是很熟……悉。"
    u "……好像溺死在水中，听不清愚蠢又丑陋的密谋。"
    scene black with fade
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 3.0
    u "迷幻的疼痛之中，好像有着低语的幽灵。"
    u "幽灵在悲伤的高音钢琴中尖声嗤笑。"
    u "似曾相识，又仿佛不同……是又一次重复的音阶吗？"
    u "……好想就这样睡去，沉入一场大梦。"
    stop music fadeout 2.0
    u "但这是哪里？"
    u "不论如何……这不是该停留的地方。"
    u "……"
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    scene bg11 with fade
    u "我醒了吗？"
    u "刚刚是做梦啊……我现在居然这么容易做梦了。"
    u "我看着前方的时钟，嘀嗒，嘀嗒，它缓慢又有节奏地走着。"
    u "我轻轻舒了口气，闭上眼睛，去做一次深呼吸。"
    scene bg11 with fade
    u "再睁开眼睛。"
    stop music fadeout 1.0
    u "？！"
    u "什么？三个小时？"
    scene black with fade
    u "崩溃般的失落将我完全占据，我也不知道，自己为什么会对时间如此介意。"
    u "但是，这怎么可能？怎么可能呼吸之间，就过去了三个小时！"
    u "恐惧之中，我坐了起来。"
    play music "audio/第四约定.ogg" fadeout 2.0 fadein 2.0
    scene medusa1 with fadehold
    u "我正坐在那只大水母上面。"
    u "这一次……我真的、终于醒了。"
    u "时光……"
    u "如果真的能够慢一些该多好！"
    u "不知道为什么，我也开始变得为时间的流过而伤心，曾经的几百年里，大概没有过这样的时候。"
    u "她还在熟睡着，而我也真的只是睡了半个小时。"
    u "不过最近每一次睡觉，需要的时间都会变长。"
    u "……好冷。"
    u "如果我到房间中去，是不是可以不那么冷呢？"
    scene bg11 with fade
    u "我在她的床边坐下，默默地看着她睡觉的样子。"
    u "听着轻微的呼吸声，我也没有那么冷了。"
    u "但是，为什么我自己创造的世界都会让我觉得寒冷？"
    u "我不知道是世界的发展真的如此不可思议，还是，仅仅是我不想面对一些事情。"
    u "……"
    u "她暂时留在了这里，尽管只是不到一天的时间，我仍然觉得，她已成了我很重要的朋友。"
    u "只是现在的美好时刻，应该也会转瞬即逝吧。"
    u "像我这样的劣质品，再微小的渴求，也可能是过分的奢望。"
    u "我当然不想要背负着“劣质品”的标签，所以我逃离了那个伤心之地。"
    u "但在这漫长的生命之中，也总会有一些事情……不间断地提醒着我，我究竟是多么不堪。"
    u "有些头晕……没有办法，我在被创造的时候，就被附加了这些不完美的要素。"
    u "好冷……又开始冷了。"
    u "这海的世界，本该让我能够麻醉自己的。"
    u "……本该让我把这些诅咒，不加思索地甩给它……"
    u "只是我看着她，思考的每一件事情都变得格外清醒。"
    u "即使头晕，仍然清醒。"
    u "她在熟睡着，熟睡的呼吸声很有趣。"
    u "我在看着她，我没有呼吸，我甚至遮蔽了自己一切的存在感。"
    u "没错，我就在这里看着她，但是，我不会将她惊醒。"
    u "我曾就这样看着遥远的枝江，也有好久不曾惊动过她们。"
    u "我有没有在做些什么？"
    u "我只是存在着吗？"
    u "……我或许有在做着什么的。"
    u "早已将自己放空进了世界的节奏，在世界的旋律之中无限地弹奏着，因为一切都如此相似，我也成了世界的一部分。"
    u "但是，这个世界是什么世界呢？当我开始怀疑这一切，"
    u "……我好像成了梦里的歌者。"
    u "绞缠的蛛网早就将我困住了。我曾有过划破它的勇气吗？"
    u "也许一切的反抗终不过是自暴自弃，但是，如果一切已经不会更差，那么就由着心来爱恨，又能够如何呢？"
    u "……"
    u "我在想什么？"
    u "狂乱的声音逐渐安宁，我就这样看着她……至少，我该带给她一些好的方面。"
    u "无论多么不堪，在人类的眼中，我还算是个神明。"
    u "我飘散在空气中，至少现在，我的存在已经完全成为了守护此处的概念。"
    u "遥远的世界里，还有着一群熟悉又陌生的生物摆动着自己的肢体，发出难懂的声音。"
    u "或许我本听得懂，但这世界已成了专属于我的障壁。"
    u "……嗯，你叫向晚。我叫什么？"
    u "我叫什么其实并不重要，如果你一定要能够称呼我，那我的名字是四。"
    u "忽然与队友分离，会感到无助吧？"
    u "那么从梦中醒来，也会孤单的吧？"
    u "我会一直在这里的。"
    u "……"
    play music"audio/Zki.ogg" fadeout 3.0 fadein 3.0
    scene lib5 with fadehold
    u "之后的事情，就像是梦一样。"
    u "我也希望它真的只是一场梦。"
    scene lib6 with pixellate
    u "她来了。"
    u "心雩，无论何时，这两个字对我来说都格外沉重。"
    u "像一场梦，一场噩梦，因为那个我不愿提起名字的梦魇，我几乎失去了理智。"
    scene black with fade
    u "甚至赶走了晚晚，我自己终结了这一场须臾的美梦。"
    u "可是晚晚明明什么都没有做错，被我带到这世界，又被我莫名其妙地赶走。"
    u "我好后悔……不愧是劣质品，不愧是我……心雩欺负我，我就去欺负晚晚……哈哈，我真厉害……"
    u "我想要哭，但是我不能哭……我哭也不会有人来安慰我。"
    u "或许本来会有的，但是她被我赶走了。"
    u "没关系的……没关系的，一切都会结束的，错误会湮灭，痛苦也会很快消失的。"
    scene white with dissolve
    u "事情本该如此，可是我听见了。"
    scene bg1s with pixellate
    show a21 with dissolve
    u "我听见了想象中的呼唤，来自她遥远的世界。"
    hide a21 with dissolve
    play music"audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    u "并不是幻觉。我的心脏剧烈地跳动，我几乎压抑不住狂喜，那一个瞬间，好像有一个陌生的我苏醒了。"
    u "也许那是我在过于久远的时候的样子，那一切早已模糊在了时间里。"
    scene oce6 with pixellate
    u "这一刻，我甚至有些感激心雩，这个名字在我的心中，第一次有了些柔和的色彩。"
    u "毕竟，如果不是因为她的出现，也许从最开始我就不会做出那个决定。"
    u "将防备心雩作为了理所当然的借口，也就说服自己，名正言顺地将向晚带到我的世界。"
    u "只是，我既不知道心雩安了什么坏心，也不敢相信她会安什么好心。"
    u "尽管……如果从结果来看，倘若将心雩的名字换成向晚，说这一切是为了帮助我设计的，我应该会很容易接受的。"
    u "……神多是自我中心的生物，心雩更是如此。如果说她会如何帮助别人，那一定是出于无聊或者某种极度深远的目的，我真的很难想象，她会抱着单纯的好心。"
    u "但现在无论如何，也不是继续记恨心雩的时候了！"
    scene bg1s with pixellate
    show a11 with dissolve
    u "向晚想要回来，她会为了我，想要再次打开来到这里的门！"
    hide a11
    u "我几乎就要毫不犹豫地过去接她了……但是，不行！"
    u "刚刚还说要她永远不要回来，现在就这个样子……太丢脸了！"
    scene zl with pixellate
    show b10 with dissolve
    u "咦？贝拉就在走廊……有办法了！"
    hide b10
    u "送去一本书吧！教她怎样打开门，她一定会回来的。"
    play music "audio/破碎冬日.ogg" fadeout 3.0 fadein 3.0
    scene oce6 with fadeholdd
    show a11 with dissolve
    u1"走进传送门，再一次去到那世界，心中的感受却完全变了。"
    hide a11 with dissolve
    u1"第一眼并没有找到四，但是我知道，我不需要在这世界中到处找她。"
    u1"她一定知道我在这里，她也不会不想见我，不然，她为什么要给我开门的方法呢？"
    u1"所以……她一定就在……"
    show a21 with dissolve
    a1"哈哈！看到你了！"
    hide a21 with dissolve
    u1"在一片珊瑚丛中，我发现了一抹白色。"
    u1"我立刻追了上去，她象征性地逃跑，但完全没有表现出一点要逃走的意愿。"
    u1"就像是在那里等着被我抓住一样。"
    show a141 with dissolve
    a1"为什么这一次这么害羞呢？之前你可不是这样子的！"
    hide a141
    show f4 with dissolve
    f1"我不是说过……让你不要再回来了，你为什么还要回来呢？"
    hide f4
    u1"她并没有回答我，但我明白，她不是在赶我走。"
    show a141
    a1"我不知道，但是我更不明白另一件事，为什么我不能再回来呢？"
    hide a141
    show f18
    f1"是你自己要回来找我的……这一次我可没有强迫你。"
    hide f18
    show a11
    a1"嗯，但不止是我，而是我们。"
    hide a11
    show a21
    a1"我的队友们可以一起来到这里吗？"
    hide a21
    show f18
    f1"什么……她们也要来吗？也、也不是不可以！但是，我需要先做些准备！"
    hide f18
    u1"话音落下，她的身影就一闪而逝，消失得无影无踪。"
    u1"她要准备什么呢？不管怎样，总觉得现在的她好像换了一个人！"
    u1"之前的她好像永远掌控着主动权，我的想法几乎都被她轻易看破，但是现在，就好像一切都反过来一样。"
    u1"不过这样也好，至少变得可爱了许多！"
    u1"我拿出手机，在群里发出消息。"
    u1"向晚：“大家直接从传送门过来吧！四已经同意了。”"
    u1"面对这样的四，我变得大胆起来，也不想要再等她做好准备了。"
    u1"让她紧张一些，也不是坏事吧！"
    f1"什么？这么快就通知她们过来了！"
    u1"我听见她的声音在我身后，看来，她已经发现我的队友们来到了这边。"
    u1"不愧是A-SOUL的行动力！"
    u1"我转过头，是……"
    show a62 with hpunch
    u1"什么？"
    u1"一瞬间的震惊之后，我还是反应了过来。毕竟她曾造出过我们的人偶，现在变成我的样子，也不算是稀奇的事情。"
    hide a62
    show a141 at left
    a1"但是，这就是你说的准备？"
    hide a141
    show a72 at right
    f1"嗯，去见这么多人，我还是会有些紧张……用自己真正的样子去，就更紧张了……"
    hide a72
    show a121 at left
    a1"喂！但是两个向晚只会更加让人注意吧！而且，我要和自己说话也好奇怪啊！"
    hide a121
    show a62 at right
    f1"那你要不要变成我的样子？"
    hide a62
    show a21 at left
    a1"好，这个有意思！"
    hide a21
    show a102 at right
    f1"但是，你不是也一样要和自己说话吗？"
    hide a102
    show a141 at left
    a1"说得对诶……那我们就这样去见她们吧，看看她们是不是分得出来哪个是我！"
    hide a141
    show a62 at right
    f1"好，她们已经在休息室了。"
    hide a62
    show a11 at left
    a1"你讲实话！你是不是有偷偷操控传送门？为什么我开的门在这里，她们却到了休息室？"
    hide a11
    show a112 at right
    f1"我没有刻意做什么的，只是我的世界会为我做出一些调整！"
    hide a112 with dissolve
    u1"她开心地走在前面，而在有一个瞬间，我忽然在她的身上找到了一种奇异的熟悉感。"
    u1"我为什么会对水母有种奇异的情感呢？"
    u1"模糊的梦境，模糊的概念，遥远的时间，那一切都已经不可捉摸。"
    u1"但是，一定有什么事情，作为那种印象的契机，曾真实发生在我的过去。"
    u1"我忘记了，但记忆的残片却深深留在我的心里。"
    u1"当她终于开始展现出胆怯、害羞这些对于神灵或许显得软弱的方面，我记忆中的残片却好像被唤醒。"
    show a41 at left with dissolve
    a1"四，我们曾经见过面的，是不是！"
    hide a41
    u1"她顿时僵住了。"
    show a72 at right
    f1"你说的曾经、是什么时候？"
    hide a72
    show a161 at left
    a1"我不知道，也许是很久很久以前，久到我没办法记住你的样子，甚至连在哪里都记不清楚，所有的一切都成了模糊的印象。"
    hide a161
    show a171 at left
    a1"但是，那个是你，对吧？"
    hide a171
    show a142 at right
    f1"我现在告诉你那个是或不是我没有意义，但是，我很开心！"
    hide a142
    show a41 at left
    a1"没有意义？为什么没有意义？"
    hide a41
    show a72 at right
    f1"现在还不是最好的时候。"
    hide a72
    u1"最好的时候？那又是什么时候呢？我不知道，但是，也许她说得对。"
    show a141 at left
    a1"好吧，那我听你的。"
    hide a141
    show a72 at right
    f1"其实我还有一个小小的心愿。"
    hide a72
    show a21 at left
    a1"什么？快说快说！"
    hide a21
    show a112 at right
    f1"就是……我，我可以叫你晚晚吗？"
    hide a112
    show a141 at left
    a1"什么……就是这个嘛？"
    hide a141
    u1"这本来不算什么，她直接这样叫我，我也不会觉得有什么不对。"
    u1"但是，如果一定需要我来同意一下，那真的有些羞耻！"
    show a121 at left
    a1"你、你想叫就叫嘛！不用……不用问我的……"
    hide a121
    show a62 at right
    f1"诶嘿……晚晚！"
    hide a62
    show a141 at left
    a1"嗯！"
    hide a141
    u1"不过说到称呼嘛，我是有想过叫她小四的。"
    u1"但是把我们A-SOUL五个人加起来，估计还没有她五分之一的年龄大！"
    u1"可她不止是看上去的年龄，就连性格也和我们差不多……"
    u1"因为常年远离人世，所以反倒意外单纯？"
    show a11 at left
    a1"那我可以叫你小四吗？"
    hide a11
    show a72 at right
    f1"晚晚你想怎样叫都可以的。"
    hide a72
    u1"嗯……不过对着自己说话果然还是好奇怪！"
    u1"不知道我的队友们会对怎么想呢？看到两个向晚，会不会吓到？"
    scene oce9 with pixellate
    u1"我跟着小四，但是她很快停了下来，又随手开了一道门。"
    show a11 at left
    a1"那边就是休息室了吧？其实我一直有一个疑问的。"
    hide a11
    show a62 at right
    f1"怎么了？"
    hide a62
    show a41 at left
    a1"这边世界的各个场所，真的是在地理上连接的吗？还是说，这一切都是由传送阵连接的不同空间呢？"
    hide a41
    show a102 at right
    f1"这个世界……应该是连接着的吧？"
    hide a102
    show a11 at left
    a1"应该？这不是你创造的世界吗？"
    hide a11
    show a62 at right
    f1"是我创造的没错，但是，我创造世界中的各个场所，就像是用不同的画布作画一样。每次都是一张新的画布，并没有考虑怎么连接它们。"
    hide a62
    show a72 at right
    f1"其实我自己也不知道哪里在哪儿。"
    hide a72
    show a21 at left
    a1"那传送阵不就是唯一的路嘛！为什么小四还总是要为我带路呢？"
    hide a21
    show a102 at right
    f1"因为聊天也是重要的！有一些话题，就是在路上才最合适去聊的！"
    hide a102
    show a141 at left
    a1"……嗯，有道理！"
    hide a141
    u1"至于是不是真的如此，我也不清楚，但是，听起来有道理就是没有问题！"
    show a72 at right
    f1"像这一次的路，就设计得短了，我们已经在这门前停留了好久。"
    hide a72
    show a141 at left
    a1"不，这是门的价值！如果不是有这扇门，我们也触发不了这一段对话！就像在游戏里，有些台词只有在你等电梯的时候才会说一样。"
    hide a141
    show a102 at right
    f1"原来是这样吗？以后有机会的话，我也想和你一起玩游戏。"
    hide a102
    show a21 at left
    a1"当然可以了！"
    hide a21
    show a62 at right
    f1"我们现在就进去吧！"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene res2 with fadehold
    show b10 with dissolve
    b2"说起来真的有一点奇怪！为什么我们从休息室的传送门过来，还是到了休息室啊！这两边完全没有什么区别吧！"
    hide b10
    show d11
    d2"会不会我们根本就没有离开，只是单纯过了一扇门？"
    hide d11
    show e2
    e2"那晚晚去哪里了呢？她先走过了传送门，然后就不见了。"
    hide e2
    show c1
    c2"晚晚说过的，四可以随意复制任何存在的事物，完全看不出区别，这个房间就是复制品吧。"
    hide c1
    show b3
    b2"不对！我发现了，这里多了一个小沙发，还多了一盏水母形状的灯！"
    scene res1 with fade
    u2"我回想起了这间休息室在枝江的样子。"
    scene res2 with fade
    show a72 with pixellate
    a2"我……我回来啦！"
    hide a72
    u2"蓝色的身影忽然在休息室中闪烁而出。"
    show b2
    b2"晚晚，只有你一个人吗？"
    hide b2
    show a62
    a2"小四她在后面……不过，还是要先欢迎大家来到这里！"
    hide a62
    show f121 with moveinright
    n"没错没错，我来啦！"
    hide f121
    u2"休息室的中央，一道惊艳的白色，做了一个偶像式的华丽出场！"
    u2"这就是传说中的四吗？好漂亮！"
    show f16
    f2"大家好！我是宇宙的原灵，全知全能的神王，美丽与智慧、可爱与性感的完美集合体，很开心见到大家！"
    hide f16
    u2"哇！原来四是这样的吗？和想象中的不一样！该不会是被晚晚同化了吧？"
    show a72
    a2"喂！你在说什么啊！再说……你，你也不是神王啊！"
    hide a72
    u2"晚晚不愧是最熟悉她的人，在我们几个都处于震惊状态的时候，她第一个做出了反驳！"
    show f16
    f2"没关系啦没关系啦！"
    hide f16 with moveoutleft
    u2"她一边说着，一边飘了过去，笑着摸了摸晚晚的头。"
    show a72 with hpunch
    a2"你……你为什么要摸我啊？"
    hide a72
    show f121
    f2"因为……你的身体很有魅力！"
    hide f121
    u2"哇，该说不愧是神吗？这么久远的经典都还知道！"
    u2"那个故事可是我们都清楚的，堪称是传世经典的《害羞小向晚》！"
    show e1
    e2"没错，晚晚，你这个新的美瞳也很漂亮，之前还没有注意到呢。"
    hide e1
    show a102
    a2"是吗？谢谢你这样说……"
    hide a102
    u2"看着眼前的景象，我忽然不知如何是好。"
    u2"我们之所以回到这里，是因为听晚晚说，四可能有着数百年的心结。"
    u2"我们曾经做好了准备，将要面对一场艰难的攻心战！"
    u2"……但是！这是什么？"
    u2"来到这里以后，四就好像和我们早已十分熟悉一样，而我们对她也完全没有陌生感，甚至懒得和她客套！"
    u2"可晚晚却不知道怎么回事，反倒勾起了我们当年的记忆。"
    show d21
    d2"晚晚，你之前不是说过，自己不会再害羞了嘛？"
    hide d21
    show a72
    a2"哪有……我哪有害羞……"
    hide a72
    show c1
    c2"晚晚又在嘴硬了！"
    hide c1
    u2"没错！又在嘴硬！……只是现在无论如何，还是要优先来到这里的任务吧？"
    u2"我要试探着和四说话！"
    show b2
    b2"刚刚听晚晚叫你小四，我们也可以这样叫你吗？"
    hide b2
    show f11
    f2"当然可以！"
    hide f11
    u2"不知道为什么，被这双眼睛看着，总有种熟悉的感觉。"
    u2"之后该说些什么？夸她漂亮吗？她自己已经夸过了啊！"
    u2"忽然，我发现了一个有趣的点！"
    show b2
    b2"小四，为什么你的手……好像是透明的呢？"
    hide b2
    show f13
    f2"什……什么？？我还没想过这个问题！晚晚！"
    hide f13
    show b10
    b2"嗯？"
    hide b10
    u2"我有些奇怪地看着她，为什么这种事情也要找晚晚呢？"
    u2"而且，总觉得有些怪怪的！刚刚她就好像不敢与我继续对视一样！"
    show b3
    b2"捏一捏……哇！好软！"
    hide b3
    u2"虽然不知道她为什么好像在躲避我，但我还是主动捏了捏她的手……"
    show f15
    f2"不行……"
    hide f15
    u2"小四整张脸都红红的，是不是我太自来熟……还是把她的手放开吧……"
    show f15
    f2"拉姐的威慑力果然还是太强了……小四！你快把我们变回来！"
    hide f15
    u2"……？？？"
    u2"变回来？这是什么意思？"
    u2"刚刚看到她们就觉得好奇怪，该不会是……"
    show a72
    a2"那个……对不起，大家先等一等！其实我是四……那边的才是晚晚！"
    hide a72
    u2"什么？果然……"
    u2"虽然有些难以置信，但好像格外合理。"
    u2"然后，她们就好像瞬间交换了位置一样，但又不完全是。"
    u2"现在想起来，刚刚她们眼睛的颜色都没有变化！"
    show f4 with dissolve
    f2"……晚晚，以后我不信你了……你骗我！"
    hide f4
    show a141
    a2"我哪有骗你，明明是你骗我的！说好是两个向晚让她们去猜真假，怎么我进了门以后就变成了你的样子！"
    hide a141
    show f18
    f2"……我不管！用自己的样子见大家会很害羞……没想到变成晚晚也还是好害羞……想让你转移一下大家的注意力……但是为什么我变成你的样子，结果却更……你都不告诉我！"
    hide f18
    show a141
    a2"没关系啦！这不就省去了客套的过程，大家直接熟悉了，多好啊！"
    hide a141
    show f4
    f2"那个……重新自我介绍一下，我是第四原灵，名字叫四，刚刚那些奇怪的介绍……都是晚晚乱说的，大家当作是她借着别人的样子，说出自己平时不敢说的话就好……"
    hide f4
    show a21
    a2"哈哈，我是无所谓啦！她们和我开了两年这样的玩笑，我早就无懈可击了！"
    hide a21
    show e2
    e2"两个小朋友不要拌嘴……"
    e2"还有，小四认真害羞的样子也好可爱！"
    hide e2
    u2"说着，乃琳去拉住了她们的手……"
    show e4
    e2"咦？小四你的手……真的是皮肤的触感呀！"
    hide e4
    show f18
    f2"嗯……因为它就是手啊……"
    hide f18
    show c1
    c2"然然，你和小四谁比较高？"
    hide c1
    show d11
    d2"她是飞着的，所以应该是我高一点点吧？"
    hide d11
    show a141
    a2"没错，所以然然也不用那么希望长高啦！"
    hide a141
    show d31
    d2"为什么！"
    hide d31
    show a21
    a2"小四选择了这个身高一定有她的理由！如果她觉得不满意，一定早就修改自己的身高了！"
    hide a21
    show b2
    b2"没错，神选择可爱，一定是有她的理由的！"
    hide b2
    show f4
    f2"但我不知道的……我被创造的时候就是这个样子，也没有人会看到我，所以之前没有思考过这些……"
    hide f4
    show d11
    d2"没关系的，现在我们都看到了你！"
    hide d11
    show f1
    f2"嗯！大家能来到这里，我很开心。我复制了枝江的部分构造，已经准备好了所有的设备器材，大家如果要准备月末的演出，也可以在这里训练的。"
    hide f1
    show f9
    f2"我想要先去准备一些我家乡的食物……大家想要训练或者是玩游戏，在这里都可以，这里的房间布局是完全复制的，大家应该很熟悉！"
    hide f9
    show b1
    b2"今天说要给大家放假一天的，就没有训练了。要不然，我们去帮忙准备食物吧！"
    hide b1
    show e4
    e2"但是……有些人的厨艺，怕是只会添麻烦吧？"
    hide e4
    show a41
    a2"乃琳你是不是在暗示我？"
    hide a41
    show d11
    d2"晚晚，我觉得她不是在暗示你。"
    hide d11
    show c4
    c2"没错，大家的厨艺应该一样烂吧？"
    hide c4
    show e1
    e2"乐你要对号入座别带上我！"
    hide e1
    show f1
    f2"没关系，大家都是厉害的人！既然知道自己厨艺不好，至少说明有做过菜！"
    hide f1
    show f4
    f2"如果没做过，谁知道是好是坏呢！……就像我这次一样，还请多多指教！"
    hide f4
    show b2
    b2"啊……哈哈。"
    hide b2
    u2"我已经预感到即将到来的暴风雨了。"
    show a11
    a2"拉姐你这是什么表情？相信小四，神灵做菜的方式和我们又不一样！"
    hide a11
    show f20
    f2"谢谢晚晚的信任，你去藏书室帮我找一找菜谱吧！然后有什么感兴趣的书都可以一并带过来。"
    hide f20
    show a11
    a2"交给我吧！"
    hide a11 with moveoutright
    show f1 with dissolve
    f2"嗯，晚晚去拿东西，我们先聊一聊……我有听说，枝江有些奇怪的传闻。"
    hide f1
    show d11
    d2"什么传闻？"
    hide d11
    show f2
    f2"一位红色的女武神击穿了月亮。"
    hide f2
    show c3
    c2"没错，是拉姐！"
    hide c3
    show b2
    b2"那个……那个不是真的啦。"
    hide b2
    stop music fadeout 2.0
    show f17
    f2"那么小贝拉想要真的去试一试吗？真的有这个机会的。"
    hide f17
    u2"……"
    u2"十秒过去，还是一片安静，没有一个人发出声音。"
    show b10
    b2"……你……你是认真的？"
    hide b10
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show f17
    f2"也没有那么认真啦。要是打真正的月亮，可能会破坏环境，生产出好多宇宙垃圾，还要我来善后，这种程度即使是我来处理，也并不容易啊。"
    hide f17
    u2"……看来是相当认真啊。"
    show f1
    f2"不过，不开玩笑——你有渴望月亮吧？不是破坏，而是在它的身边。"
    hide f1
    show b1
    b2"嗯……是的。"
    hide b1
    u2"我从来都不是喜欢破坏的人。"
    u2"但是，飞到月亮的身边，真的能够实现吗？如果可以，我真的希望能有一次这样的机会。"
    show f1
    f2"月亮是一种只能远观的事物，真的接近了这巨大的反光镜，就只能见它灰色的外表，荒芜死寂。"
    hide f1
    u2"这样吗……虽然知道事实，但她这样说，我还是有些失落的……"
    u2"不过也是情理之中嘛！我当然理解，毕竟早就不是小孩子了！"
    show b2
    b2"我也只是普通人嘛，只能用人的眼光来看，也是没办法的事情……"
    hide b2
    show e5
    e2"不对！小四好像不是这个意思……那个，你该不会真的要去创造一个新的月亮吧？"
    hide e5
    show f2
    f2"哇！乃琳怎么知道？"
    hide f2
    show e1
    e2"拉姐说，希望飞到月亮的身边，你说月亮上是荒芜的环形山……如果是人类，说出这种话就显得读不懂气氛了。"
    hide e1
    show b1
    b2"嗯……人有的时候是会这样的。我也是……"
    hide b1
    show e2
    e2"是，我偶尔也喜欢这样说，说那种看似清醒，却改变不了现状的话。"
    hide e2
    show e5
    e2"但是、我忽然意识到，小四完全没有必要说这种话！她如果说了，那也许就是真的可以改变！"
    hide e5
    show a21 with moveinright
    a2"哦？改变什么？"
    hide a21
    u2"这个时候，晚晚刚好抱着书回来了。"
    show f17
    f2"改变月亮！我是想要去创造一个新的……曾经我无论如何也不能够理解姐姐，但是刚刚那一刻……我好像有些懂了。"
    hide f17
    show a11
    a2"你的姐姐？"
    hide a11
    show f9
    f2"没错，我一共有三个姐姐，那些事情也不必瞒着大家。不过，既然晚晚带着菜谱回来了，我们还是先来准备食物，之后再聊那些事情吧！"
    hide f9
    show c5
    c2"好啊！晚晚拿回来的是什么？……《光都食谱》？说起来，光都是在哪里？"
    hide c5
    show f17
    f2"是我曾经的家，一座魔法大都市，一个很美的地方。"
    hide f17
    show b2
    b2"大都市吗？大都市我还只来过枝江呢。"
    hide b2
    show d11
    d2"没关系的拉姐，我们这个月末就会去北方的都会了！"
    hide d11
    show b3
    b2"没错！小四会和我们一起去吗？"
    hide b3
    show f20
    f2"当然了，我一定会去的！先来看一看这里有什么看起来不错的菜吧。"
    hide f20
    show f21
    f2"看这个！这是国宴级别的菜式，可谓是彰显了光都格调的终极菜品，名为寒寂！"
    hide f21
    show a21
    a2"我来看一看！"
    hide a21
    show a141
    a2"咦，这不就是冰淇淋吗？"
    hide a141
    show f20
    f2"重点在于形啦！之所以叫寒寂，就是因为它是按照圣地寒寂雪峰的样子制作的。"
    hide f20
    show f1
    f2"而制作它的原料，是提纯的风戟花露。再用几种水果粉末混合成调料，与蓝色素一起融在花露中，构成了雪峰上冻结的溪流与瀑布，看上去就像是真的水一样！"
    hide f1
    show d11
    d2"这可真是高级的甜点！刚好来这里之前，我们才吃过饭，现在去做一些甜品也是最合适的。"
    hide d11
    scene res4 with dissolve
    show f1
    f2"我们就把这里当作厨房吧，过来过来！原料已经准备好了！"
    hide f1
    show e1
    e2"我来看一看原料——提纯风戟花露、草莓粉、樱桃粉、牛奶、白糖……哇，是要从最基础的部分开始吗？"
    hide e1
    show a11
    a2"当然了，这才是做菜真正有趣的地方！"
    hide a11
    show b2
    b2"可是晚晚你不是只会泡面吗？"
    hide b2
    show d21
    d2"不，她至少还会一样奶盖拌饭！"
    hide d21
    show c3
    c2"不过，就算不会做，按照菜谱的步骤也不会差得太多吧？"
    hide c3
    show f21
    f2"没错，今天我们来一次厨艺比赛！我们每个人都来做一次。另外，虽然原料很多，但我已经消除了它们过敏的可能性，所以即使是贝拉也可以放心品尝！"
    hide f21
    show b2
    b2"哇，谢谢你，这个好贴心！不过你说要比赛，这个怎么比呀？"
    hide b2
    show e1
    e2"听到比赛，拉姐的胜负欲就起来了吗？"
    hide e1
    show b2
    b2"没有！我也不是什么时候都只想着赢的……我只是在想，我们是应该比谁做得好，还是应该比谁做得烂……"
    hide b2
    show a141
    a2"每个人都认真做到最好，然后比谁做得最烂是吧！喂，多多少少对自己有点信心啊！"
    hide a141
    show f2
    f2"嗯……说比赛也许不太准确，重要的是，每个人都用心做出自己的一份，然后给大家品尝自己的心意！"
    hide f2
    show d11
    d2"我明白了，那么大家现在就开始做吧！"
    hide d11
    show c1
    c2"好，大家加油！"
    hide c1
    u2"然后，我们开始各自研究起制作的步骤。"
    u2"晚晚最初看到这道“寒寂”的时候，就说过它好像冰淇淋，最初的步骤也确实很相似。当然了，最难的地方是那些让这道菜漂亮起来的奇特技法。"
    u2"真的是一种全新的尝试！"
    scene black with dissolve
    u2"……"
    scene res4 with fade
    u2"经过一番互相学习，我们终于都做好了自己的一份！"
    show f1
    f2"大家都做好了，那么我们按照名字的顺序来分别品鉴吧！第一个是晚晚的。"
    hide f1
    show a21
    a2"好！大家看好啦！"
    hide a21
    show icea with dissolve
    u2"她打开盖子的一刻，我看着那一摊蓝白混合的糊状物，惊讶得说不出话。"
    hide icea
    show e4
    e2"这……我们做的真的是同一种食物吗？"
    hide e4
    u2"晚晚得意地摇了摇头。"
    show a141
    a2"这你就不懂了！这是根据我的经验，想出的让味道均匀的最好方法，虽然看着可能不好看，但吃着一定好吃！"
    hide a141
    show d11
    d2"你的经验……是指奶盖拌饭和泡面吗？那些的确都是要拌开吃的。"
    hide d11
    show c1
    c2"既然晚晚对它的味道这么自信，那我们就尝一尝吧！"
    hide c1
    u2"刚刚入口，就是冰淇淋的甜香，但稍稍仔细感受后，又有一种格外奇异的清香味道。"
    show b3
    b2"是风戟花露！我在制作的时候，就有察觉到花露和水在味道上的区别，吃起来的时候，这股清香真是太棒了！"
    hide b3
    show e1
    e2"没错！如果这一份在外观上给五分的话，那么口感就是一百分！"
    hide e1
    show a21
    a2"喂！五分过分了吧？"
    hide a21
    show f20
    f2"没关系的晚晚，食物嘛，最重要的还是好吃！看起来大家都很喜欢你做的呢！"
    hide f20
    show d21
    d2"嗯，虽然看起来怪异，但吃着真的很棒！"
    hide d21
    show a141
    a2"就像是泡面一样，看着廉价但是很好吃吗？没什么啦……实际上就是按照比例把原料混合了起来……总之还是谢谢你们喜欢啦！"
    hide a141
    u2"吃过了晚晚做的，下一个就轮到我了！"
    u2"这一次，是给重要的人们做的甜点，所以我尽了最大的努力去做好！"
    u2"我打开了盖子。"
    show iceb with dissolve
    u2"看上去虽然比晚晚的那个好得多，但也远远称不上精致，看上去就像是冰冻的金字塔，从尖顶流下蜿蜒的水流。"
    hide iceb
    show c3
    c2"拉姐做得很好啊，从外表上就能看出来拉姐非常努力！"
    hide c3
    show b1
    b2"我在尽量还原它的做法……但是我不够专业，也只能做到这些了。"
    hide b1
    u2"将它切开品尝，虽然味道与刚刚晚晚做的有些微妙的不同，但应该也只是用料多少导致的差别。"
    show d11
    d2"没关系，我能感受到，这是拉姐用心在做的！"
    hide d11
    show b13
    b2"但是吃起来还是有些奇怪啊……那些水果粉混合成的蓝色糖浆是很重要的料，但是我做的这个却没有撒好，有的地方太多了，而下面又完全没有……"
    hide b13
    show c1
    c2"没关系的拉姐！这都不是问题……等你见到我做的，就明白我为什么这样说了！"
    hide c1
    show e2
    e2"吃起来，满满的都是队长的关怀！"
    hide e2
    show b2
    b2"全是关心，没有技巧是吧！"
    hide b2
    show a11
    a2"哪有！先不谈甜品，拉姐是越来越可爱了！"
    hide a11
    show f9
    f2"嗯，这些是大家对于队长的认可。"
    hide f9
    show b1
    b2"好……我们快开始下一个吧，去看看珈乐做了什么！"
    hide b1
    show icec with dissolve
    u2"这是？"
    hide icec
    u2"我终于明白，为什么刚刚珈乐说我的糖浆没有撒好没有关系了。"
    u2"这半蓝半白，一边是全部都有，一边是完全没有！"
    show b2
    b2"哈哈……乐的料用得足呀。"
    hide b2
    show e1
    e2"不过这个该怎么切呢？之前的都能切成六等份。"
    hide e1
    show f21
    f2"我来切吧！"
    hide f21
    u2"这甜品在一瞬间被切成了十二份，六蓝六白，每人只要一边取一份就好了。"
    show a21
    a2"哇……一道甜品居然做出了饭菜的感觉！"
    hide a21
    show c3
    c2"……我自己已经有不好的预感了。"
    hide c3
    show d11
    d2"好，我先尝一尝蓝色的……"
    hide d11
    show d31
    d2"呜哇，这也……"
    hide d31
    u2"她没有继续点评下去，赶紧又吃了一口白色的。"
    show c4
    c2"抱歉……不过，是什么味道？"
    hide c4
    show d11
    d2"蓝色的用料太足了，有一种……很意外的冲击力！但是如果两边配合起来吃，会有种很奇特的体验……莫名很好吃！"
    hide d11
    u2"大家品尝过后，对然然的评价，也是纷纷赞同。"
    u2"能把甜点做到黑暗料理的程度，但是最后的结果是“莫名很好吃”，乐也算是很厉害了！"
    show c4
    c2"哈哈……我本来以为是做坏了的，没想到这种吃法，意外的还不错！"
    hide c4
    show f20
    f2"没错，因为不论结果怎样离奇，大家都是想做出好吃的食物，顶级的食材辅以一颗认真的心，做出来的不会不好吃的！"
    hide f20
    show e1
    e2"我道歉！"
    hide e1
    show b10
    b2"你为什么道歉？我也有不好的预感。"
    hide b10
    show e4
    e2"因为我没有一心想要做出好吃的食物，我做了一点……可能会有很大影响的创新。"
    hide e4
    show d11
    d2"那就先来品尝乃琳做的吧，我想看看她究竟做了什么！"
    hide d11
    show b10
    b2"毕竟除了真正的关键时刻，乃琳是绝对不会放弃坑我们的机会的，所以这次乃琳先吃！"
    hide b10
    show c2
    c2"乃老师是这样的，你不能奢望她有什么好心思，小四以后要注意防范！"
    hide c2
    show e2
    e2"我……你们太过分了！"
    hide e2
    show a141
    a2"没关系的乃琳，不要在意！毕竟大家这么熟悉，都是基于平时对你的了解嘛！"
    hide a141
    show e1
    e2"晚晚你这是在安慰人吗？"
    hide e1
    show a141
    a2"哈哈，不算是啦！"
    hide a141
    show icee with dissolve
    u2"乃琳做的从外表上看起来格外有少女感，点缀的蓝色有种清新的气息。"
    u2"看起来居然意外的不错！而且好香，刚刚打开盖子，花的香气便扑鼻而来。"
    hide icee
    show b1
    b2"哇，目前来看，可以说是最好看的了！"
    hide b1
    show a11
    a2"好香啊，简直就像艺术品。"
    hide a11
    show f4
    f2"但是这样用香料……有些危险啊。"
    hide f4
    show d31
    d2"危险？"
    hide d31
    show f20
    f2"一种猜测，可能它吃起来……不像是看上去那样好。"
    hide f20
    u2"乃琳切下一块，小小地尝了一口。"
    u2"然后，她的眉头就皱了起来。"
    show e3
    e2"不行……太奇怪了，大家还是不要尝试了，直接去尝然然做的吧！"
    hide e3
    u2"但是，她这样说，我反倒好奇那究竟是什么味道了。"
    show a141
    a2"没关系的，还是尝一尝嘛！你越是这样说，我们就越好奇。"
    hide a141
    show e4
    e2"好吧……你们不要后悔！"
    hide e4 with dissolve
    stop music fadeout 1.0
    u2"……"
    u2"尽管无法准确描述出那种味道，但最后我们每个人的表情都相当一致。"
    show e4
    e2"后悔了吗？"
    hide e4
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    show b2
    b2"它真的好难吃！为什么闻起来那么好，吃起来却是这种感觉？但也正因为这样，我才不后悔，因为你一生中都很难有机会吃到这么离奇的食物！"
    hide b2
    show a41
    a2"拉姐说得对，它的味道很荒诞，但是它并不是冲击你的味蕾、让你想要吐出来的那种……它反而会引起你思索，思考为什么会有这种味道的哲思之甜品！"
    hide a41
    show e2
    e2"我不是故意做成这样的，我只是觉得，这样或许会不错……不过风险有点大。算了算了，还是快进到然然做的吧！"
    hide e2
    show c1
    c2"然然做了什么？"
    hide c1
    show d11
    d2"我做了一个超大号的！"
    hide d11
    show iced with dissolve
    u2"打开盖子，我的确震惊到了！"
    hide iced
    show b3
    b2"哇，真的好大！"
    hide b3
    show a11
    a2"然然的厨艺我还是相信的，至少味道上不会很奇怪，不过……有点可惜了呀。"
    hide a11
    show c3
    c2"为什么可惜？"
    hide c3
    show a11
    a2"如果是在乃琳之前品尝然然做的，会因为太大而吃不完，吃过乃琳的那份之后，就可以继续吃这份大的来平复心情，但是，现在没有吃两次的机会了，所以才很可惜啊！"
    hide a11
    show f20
    f2"那个……其实之后还有我的一份的。"
    hide f20
    show b1
    b2"但是小四做的……不可能不好的吧？我其实有偷偷看到一点的，好像非常完美！"
    hide b1
    show f1
    f2"……谢谢你这样说，希望如此！"
    hide f1
    u2"吃然然做的甜品，有一种朴素的幸福感。"
    u2"十分好吃，也没有什么过分高贵的形状，以至于不敢破坏。"
    u2"更重要的是，量真的很足！完全不担心不够吃！"
    u2"吃了大致三分之一，感受到了暂时的满足，是时候去品尝小四的作品了！"
    u2"神灵的甜品，神灵故乡“光都”的国宴级别菜品，真正的最高规格的美食——寒寂！"
    u2"它的特色应该在于风戟花露这种原料，而风戟大概不是存在于我们世界中的植物，至少我没有听过。"
    u2"不知道小四会做得怎么样？"
    u2"她打开了最后的盖子。"
    show icef with dissolve
    u2"看到的瞬间，没有人可以不发出惊叹！"
    hide icef
    show b3 with dissolve
    b2"这也太美了吧？真的就像是雪山一样……"
    hide b3
    show a21
    a2"看上去就完全像是艺术品。"
    hide a21
    show f4
    f2"我希望可以带给大家最好的体验……甚至超越原本的味道！"
    hide f4
    show d21
    d2"我很期待！"
    hide d21
    u2"只是，我看着这艺术品一样的甜点，还是会莫名感到奇怪。"
    stop music fadeout 2.0
    u2"并不是因为和菜谱上的图样有什么分别，反而可以说是几乎完全一致。"
    u2"完全没有什么原因，好像是一种忽然升起的情感。"
    u2"如果一定要形容，应该类似于，在某一刻，我的心中被种下了一颗种子？"
    play music "audio/Zki.ogg" fadeout 2.0 fadein 2.0
    u2"怀着期待的心情，我们终于开始品尝这最后一份甜点！"
    show b13 with dissolve
    b2"嗯，很好吃……但是？……"
    hide b13
    u2"吃下第一口的时候，是那股熟悉的清甜，可那完美的味道却像是缺少真实感一样，又微微有些发涩，仿佛我在面对一个哭泣的人。"
    show e2
    e2"这究竟是？"
    hide e2
    u2"应该不只是我觉察到了异样。"
    show c6
    c2"我刚才明明有吃过，却又好像未曾经历这些……镜花水月般的感觉。"
    hide c6
    u2"我几乎不能形容出这一切，如果单纯用“好吃”或者“难吃”来区分并不恰当，不同于传统的美食，这一次绝对不能够称为享受，而更接近一种迷醉。"
    u2"像是在梦境之中，让人痴迷。"
    u2"但是梦终究会醒来的，一切留下的痕迹也终究会随着时光消逝。"
    u2"这……大概就是我能想到的最恰当的评价。"
    u2"而且，并不开心。当它在口中化掉，最后一丝余味消散，淡淡的惆怅就蔓延开来。"
    show a151
    a2"我曾经属于那里……"
    hide a151
    show b13
    b2"晚晚……你说什么？"
    hide b13
    show a161
    a2"……什么？"
    hide a161
    show b10
    b2"你刚刚说，自己属于哪里？"
    hide b10
    show a151
    a2"我不知道。"
    hide a151
    show f9
    f2"对不起……曾属于那里的是我，那里就是光都……"
    hide f9
    show f4
    f2"但我并不是有意的，我没有具体操纵它带给你们的情感……"
    hide f4
    show d31
    d2"我也感觉到了，但那是什么？"
    hide d31
    show f17
    f2"或许是我对这五百年的印象吧。其实，我也大概猜得出你们为什么会回来。"
    hide f17
    show f2
    f2"乃琳给你们做了占卜，在晚晚回去后，你们又将所知的一切联系起来了。"
    hide f2
    show a161
    a2"没错……所以我们都很担心你。"
    hide a161
    show f3
    f2"也好，那我来告诉你们，这一切究竟是什么吧。"
    hide f3
    show f6
    f2"那个我一直不想提到的名字，叫做心雩。"
    hide f6
    show b10
    b2"心雩？"
    hide b10
    u2"第一次听到心雩的读音，那两个字的写法居然就仿佛呈现出来。"
    show f3
    f2"“一个杯子两条鱼，翻手为云覆手雨。”这两句打油诗说的就是她。"
    scene xinyu with fade
    f2"她的右手托着圣杯朝天，那里面是爱与希望，这是作为最高神灵所固有的权能。"
    show e2 with dissolve
    e2"这个杯子听起来很好嘛！那两条鱼呢？"
    hide e2 with dissolve
    f2"她的左手有两条鱼朝下，是风鱼和水鱼，你们都听过“风水轮流转”这句话。"
    show d11 with dissolve
    d2"说的是命运吗？"
    hide d11 with dissolve
    f2"至高的神灵哪里有命运可言……八卦的学说你们有听过吗？天地山泽，风雷水火，这其中可称得上流转的，只有风与水。"
    f2"而流转，指的是物质的流向，是人所说的命数，也是她掌控的规则。阴阳的圆轮转化为风水流转的无穷形状，这就是她的风水 轮 流转。"
    show e1 with dissolve
    e2"有意思……那翻云覆雨如何解释？"
    hide e1 with dissolve
    f2"翻云覆雨不是一个好词……她右手朝天举着爱与希望的圣杯，但是圣杯高高在上。她左手指地，两条鱼掀起云雨，这才是留给人的，是灾厄与混乱。"
    f2"我不明白她做的很多事——包括她为什么是我的三姐。明明她是最古老的创造者，我和大姐二姐一样，都是这一千年以内被她创造出来的存在。"
    f2"我也不知道她为什么要创造我们这些与她一样强大的神，虽然她是创造者，但是我们在能力上与她没有本质的差异。"
    show a21 with dissolve
    a2"是啊！而且为什么明明是最古老的创造者，却把自己排在了第三位？"
    hide a21 with dissolve
    f2"如果不思索她的目的，大姐与二姐是正与反的天道，而心雩不在这之中。"
    show c2 with dissolve
    c2"她是观察者？"
    hide c2 with dissolve
    f2"也许是的，这是可能的解释之一，我自己并不清楚她想要什么。"
    show b10 with dissolve
    b2"你现在还生她的气吗？"
    hide b10 with dissolve
    f2"其实有那么一个瞬间，我好像领会到了她想要什么……至少是关于我的那部分。"
    f2"看到她留下的书的时候，我的确很生气，甚至把那本书撕成了碎片……现在想起来，我还是太软弱，也太任性了。"
    show b13 with dissolve
    b2"为什么这样说？"
    hide b13 with dissolve
    f2"就像是生气的人类，可能会喜欢破坏一些东西，尤其是不能反抗的死物——破坏了它们，内心的痛苦也就得到了释放。"
    f2"当然了……也可以做充足的准备，拿起锋利的刀刃，用自己最凌厉的斗志，去面对自然的一切。只是你锋利的刀在一块普通的石头面前，就像是一块废铁。"
    show d31 with dissolve
    d2"这说明了什么呢？"
    hide d31 with dissolve
    f2"人的斗志，人的锐气，当然不能够战胜宇宙。"
    show b3 with dissolve
    b2"但是有人说，人定胜天，小四怎么想？"
    hide b3 with dissolve
    f2"如何算是胜天呢？通过自己的努力改变命运的轨迹吗？"
    f2"那只不过是战胜了自己。"
    f2"什么是天……近在我们身边的气息，远在无尽的星辰，都属于天。能够改变这些的，只有我们这些自称为原灵的存在。"
    f2"作为原灵，我可以在一瞬间湮灭星辰，但是这不值得骄傲，这是心雩送我的，与我无关。至于我……仅仅是用了五百年与自己和解。"
    f2"所以，贝拉，你能够战胜自己，回到舞台，已经比我强太多了。"
    show b2 with dissolve
    b2"谢谢你这样说……"
    hide b2
    show a21 with dissolve
    a2"没关系！既然小四已经与自己和解了，那就还不晚。"
    hide a21 with dissolve
    f2"曾经我一直无法理解……也许我早已理解，只是不愿承认。"
    f2"我的确是作为神被创造的，但是，也的确因为一些原因，我没有办法像大姐那样，成为宇宙之中至高的神灵。"
    f2"那时候，我不理解为什么我们之间会有那些差异，以至于我不得不被排除在外，无法参与到秩序的制定。"
    f2"当时在我的眼中，也只有我们四个是有意义的生命……只是我不能接受，偏偏我是那最差的一个。"
    show a151 with dissolve
    a2"所以……你选择了逃离光都？"
    hide a151 with dissolve
    f2"是，我逃走了。直到今天，我用了五百年才想通心雩为何要创造我。"
    f2"有的神灵，从出现的那一天起，就是为了高天之上而存在。"
    f2"心雩她不会在意自己是第一还是第三，你们明白吗？"
    show e2 with dissolve
    e2"因为小四的姐姐们不在意那些，所以她们才处在了那种位置上？"
    hide e2 with dissolve
    f2"是啊，而我在意那些，所以我只能是人。"
    f2"其实大姐和二姐……算了，她们的事情太过遥远，而且，她们的未来也在变化之中，我无法看见。"
    show e1 with dissolve
    e2"时至今日，小四也还关注着光都的事情？"
    hide e1 with dissolve
    f2"我离开光都数百年，的确早该释怀。但是，我的心却不够那个高度。"
    f2"我偶尔会关注着斗争漩涡中的姐姐们，心中就会有一种冷眼旁观的优越感。这种事不关己的清高，很难说不是因为嫉妒。"
    show d11 with dissolve
    d2"但是你现在把这些都说出来了，毫无掩饰地告诉我们了。"
    scene res2 with fade
    show f9 with dissolve
    f2"嗯，因为我现在明白，那些事情对我来说并不重要。"
    f2"我曾经在乎那个位置，因为我的心仍是人的心。"
    hide f9
    show f10
    f2"我其实也知道，那不是会让我开心的位置，只是我直到今天才明白，我想要的究竟是什么。既然如此，那我更应该走入人世。"
    hide f10
    show a11
    a2"所以从我们决定回来的时候，小四就已经不再介意了吗？"
    hide a11
    show f1
    f2"是啊，也正是因为你们，我才能够从对心雩的恨意中脱身，当我的心改变了，她在我的眼中也就变了。"
    hide f1
    show c1
    c2"心雩是个什么样的神？"
    hide c1
    show f4
    f2"我不知道，现在也是一样不知道。但是在过去的那些年，我的心一直在阴暗的世界，也一直用着阴暗的想法去揣测她。"
    hide f4
    show f1
    f2"或许心雩并没有那么坏，虽然她的涉足总是搅动人间的风雨，还有一次害死了几千万人……但是这许多年来，风水鱼倒是一直稳定地流转着。"
    hide f1
    show c1
    c2"那……也许这一次她有在帮你？"
    hide c1
    show f3
    f2"也许……但人大概永远都不需要感激神的帮助。"
    hide f3
    show c2
    c2"为什么？"
    hide c2
    show f9
    f2"如果神会帮助人类，最可能的原因就是无聊……对于心雩来说，与我之间也是如此吧。"
    hide f9
    show a11
    a2"那小四和我们呢？"
    hide a11
    show f21
    f2"当然是真心的！我从来不曾算是一个神明。"
    hide f21
    show b2
    b2"那么在一些方面，也许心雩也是一样。"
    hide b2
    show f4
    f2"什么方面？"
    hide f4
    show b1
    b2"其实在A-SOUL之中，有的时候，我感觉自己不只是队长，更像是姐姐一样。"
    hide b1
    show b2
    b2"我没有见过心雩，但同样的，说不定比起神明，她更希望你把她当作姐姐。"
    hide b2
    show b1
    b2"当然……只是也许。"
    hide b1
    u2"我补充了一句。"
    u2"小四没有认同，但也没有反对。"
    show f1
    f2"不管怎样，直到现在才认识你们，真的是太晚了……之后我们回到枝江吧，我也会和大家一起！"
    hide f1
    show b3
    b2"为了月末演出的训练，小四也会帮忙吗？"
    hide b3
    show f2
    f2"当然了，一切都会变好的。"
    hide f2
    u2"她笑的样子，看上去和我们也没什么分别……"
    u2"除了某些时候……似乎她一旦激动，眼睛就会变成红色？"
    u2"无所谓啦……"
    play music "audio/破碎冬日.ogg" fadeout 2.0 fadein 2.0
    scene street with fadehold
    u "我的生命之中，还从未有过像现在这样兴奋、激动的时刻。"
    u "我作为被关心的客人，去了向往着的世界。"
    u "不再是一个人缩在海里，也不是在那曾让我无限伤心的光都。"
    u "这里是枝江。"
    show a141 with dissolve
    a"我们回来啦！"
    hide a141
    show f1
    f"这里的建筑明明与我的复制品没有什么差异，但是看上去却是那么不同……"
    hide f1
    show e2
    e"因为你的心改变了。"
    hide e2
    show f21
    f"就像开启了新的生命！"
    hide f21
    u "我深深呼吸着这里的空气，是新鲜的满足感。"
    u "我看见她们笑着，笑得很开心，我也很开心。"
    u "但是……不，现在没有但是了，我应该去享受这美好的时光。"
    u "尽量留下更多的美好吧！"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene bg3 with fadehold
    u1"终于，一切都恢复了正常。"
    u1"就好像什么都没有变过。"
    u1"起床，吃饭，训练。"
    u1"没什么特殊的，虽然小四也来到了这里，但的确没什么特殊的。"
    u1"她和我们一起吃饭，也偶尔和我们一起训练。"
    u1"当然，她更多的时候还是在帮我们，毕竟她最后不需要到舞台上表演。"
    u1"一切都好像自然而然，小四轻而易举地融入了我们之中。"
    u1"新的一天，训练室中，为了准备月末的演出，我们开始了日常的训练。"
    show b3
    b1"一、二、三、四、一、二、三、四……好，大家做得不错！先休息一下吧。"
    hide b3
    u1"不知道和小四有没有关系，现在的训练，好像比从前要轻松了。"
    u1"是因为小四给我的“能力”，还是因为拉姐的内心也有了些变化呢？"
    u1"小四正在一旁模仿我们刚刚的舞步，完全是完美的表现。"
    u1"如果我也能做到那样就好了。"
    u1"但这对她来说，只是不足为奇的事情，神灵的学习能力，我本不必感到惊讶。"
    u1"不管是现在学跳舞，还是之前学做菜，她与我们的学习方式都是不同的。"
    u1"如果说我们学习是模仿与理解，她的学习则是复制、计算、优化。"
    u1"而且，她不会犯……什么？"
    show b2
    b1"小四，跳错了哦！这对你来说可是挺难得的！"
    hide b2
    show f4
    f1"对不起，拉姐，因为有点冷，所以刚刚有一点没找好平衡……咳……"
    hide f4
    u1"她轻轻咳嗽着，很快调整好了身体的平衡。"
    u1"看到她也会偶尔犯错，还是有一种亲切感的……但是，她在半空飘着也会因为不平衡摔倒吗……"
    u1"不知道……不过有趣的是，她现在也开始跟着我们叫拉姐了。"
    show d11
    d1"能看到你犯错真不容易……但这里很冷吗？枝江夏天的训练室，就算是开了空调也会觉得热呢。"
    hide d11
    show f20
    f1"嗯……大家都流汗了，看来这空调的制冷的确不太好，我来修一下吧。"
    hide f20
    show d61
    d1"等等！你不是冷嘛？"
    hide d61
    show f2
    f1"没关系的，这和修空调不冲突。"
    hide f2
    u1"我能够感受到，训练室中顿时凉爽了许多。"
    show f9
    f1"有哪里不舒服要告诉我，有些方面我没办法感知得到。还好，现在没有问题了！"
    hide f9
    show a42
    a1"有问题！刚刚你还说自己冷，现在不是更冷了？"
    hide a42
    show f9
    f1"真的没关系，相信我,这里的冷暖我觉察不到，而我的冷暖与这里的温度无关。"
    hide f9
    show a12
    a1"好吧，我当然相信你了……那先不提这个……说起来，你学舞学得那么快，为什么不考虑走上舞台呢？"
    hide a12
    show f9
    f1"学舞很快，这的确是一个让我走上舞台的理由，但是，我有数不清的理由让我不要走上去。"
    hide f9
    show a42
    a1"但是，如果想走上去，只要一个理由就够了。"
    hide a42
    show b1
    b1"是啊，重点还是在于自己的心愿。"
    hide b1
    show f19
    f1"我的心愿吗？如果能看到你们走上那个舞台，我就很开心了。"
    hide f19
    show a12
    a1"嗯……我们会努力的！"
    hide a12
    u1"我这样回答她。但是，她自己想要的是什么呢？"
    u1"等到小四不在的时候，大家一起讨论一下吧。"
    u1"谁让她自己那么不坦率呢？"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene res2 with fadehold
    u1"小四来到枝江，就揽下了做饭的工作，只要是被记载下来的美食，就没有她做不出来的。"
    u1"现在又是我们等着她准备午餐的时候。"
    u1"训练室中，已经仿造着她的世界，加上了第六个小沙发和一只水母形状的灯。"
    show d31 with dissolve
    d1"拉姐，我忽然不想努力训练了。"
    hide d31
    show b10
    b1"为什么？"
    hide b10
    show d11
    d1"你说我们是为了什么在训练呢？"
    hide d11
    u1"贝拉愣了一下，没有回答。"
    show d41
    d1"我们努力成为最闪耀的偶像，想要吃到各种各样好吃的东西，但是现在，没有什么菜是小四做不出来的。"
    hide d41
    show b2
    b1"不要说我们，明明只是你！话说！然然你成为偶像该不会就是为了能有钱随便吃大餐吧？"
    hide b2
    show d31
    d1"当然还有很多别的理由，但是现在小四只是在准备饭菜。"
    hide d31
    u1"只是，这和小四又有什么关系呢？"
    show e1
    e1"……我明白然然的意思了。我们的事情，没有什么能难得住小四，她现在只是在做菜，那么以后呢？"
    hide e1
    u1"我忽然说不出话来，拿起杯子，用手指在空中画了一个圆。"
    play sound "audio/jieshui.ogg"
    u1"我把杯子接在下面，之后，水装满了杯子，那个圆也消失了。"
    show b10
    b1"这是什么？"
    hide b10
    show c1
    c1"没猜错的话，是那边世界的水？"
    hide c1
    show a41
    a1"是啊，空间门，即使是在动画里，也是最高级的魔法类型吧？但是她说教我就教我了……"
    hide a41
    show c4
    c1"乃琳要不然你直接和小四学魔法吧，你随便学一学，应该就比很多书里的法师都厉害了吧？"
    hide c4
    show e2
    e1"你说得对。"
    hide e2
    u1"然后，她陷入了沉默，好像既没有反对，也没有十分期待。"
    show b10
    b1"所以大家对这件事是怎么看的？"
    hide b10
    show d41
    d1"小四她有一些……太难捉摸了。"
    hide d41
    show a41
    a1"对！完全不知道她会在意什么！以我现在对她的了解，如果我们要让她教我什么，哪怕是那种做梦都不敢想的超级魔法，她估计也不会有什么犹豫！但是！"
    hide a41
    show e5
    e1"但是那些东西，对她来说都是最廉价的，如果不是用得上，根本都不会主动想起来。"
    hide e5
    show d31
    d1"是啊，有的时候，我会忍不住在想，她和我们一起回来，终于放下了那座“光都”，但如今的她，在意的又是什么呢？"
    hide d31
    u1"我也有些不知该怎么做了。来到枝江的她，相处起来，就像是同龄的女孩子一样容易亲近。"
    u1"但是，她又绝对不是一位“普通的人类朋友”，努力、梦想……这些词和她都是那么遥远。"
    show f19 with moveinright
    f1"大家来吃饭啦！"
    hide f19
    u1"她忽然从门外飘了进来，打断了我们的讨论。"
    show e1
    e1"刚刚的讨论就到此为止吧，之后，我会找机会的。"
    hide e1
    show b1
    b1"好，我相信你，乃琳！那我们先去吃饭吧！"
    hide b1
    stop music fadeout 2.0
    scene black with fade
    u "吃过饭后……"
    scene res2 with fade
    play music "audio/深竹.ogg" fadeout 2.0 fadein 2.0
    u "从餐厅回来，我一个人又到了休息室，胡乱地看着书。"
    u "我不清楚我想要找到什么书，但或许这里找得到我想要的。"
    u "我有想要做的事情，但是不能够去说。至少在目前，这还是秘密。"
    u "“为天地立心，为生民立命，为往圣继绝学，为万世开太平。”"
    u "一本书的封面上写着这样一句话。只是……这句话的作者应该已经不在人世了吧？"
    u "他的一生中，这些事又做到了几件呢？"
    show e1 with dissolve
    e"小四在看书吗？"
    hide e1
    show f1 with dissolve
    f"是啊，乃琳，你来啦。"
    hide f1
    u "她会回来，我不感到诧异。来到这里以后，拉姐说这休息室算是我们的储物间……当然，我也没什么要存放的东西。"
    scene ef2 with dissolve
    e"在看什么书？"
    f"……我不知道。"
    u "我看了看身边那一堆摆得很乱的书，我的确不知道自己在看什么。"
    u "身体感受到的微微寒冷，比书的内容更让我在意。"
    e"是在找某一本书吗？我有的时候也会向着一个模糊的方向去寻找。"
    f"是吗？有趣……也许是的吧？"
    u "我笑了笑。她说得很对，我也只是沿着一种印象，去寻找一种可能性。"
    f"不过，乃琳有着什么样的心愿呢？"
    u "我又瞥了一眼刚刚的那本书。也许是少数，但总有些人的心里有着伟大的愿望。"
    e"你知道的，我大学的专业，是学的法律。"
    f"嗯，我知道，乃琳是想要做律师吗？"
    e"曾经想过，不过，我现在已经做着偶像了，这也是我喜欢的职业。而不论是当初选择学习法律，还是现在的我成为了偶像，我希望的，大概是为更多人带来一些美好吧。"
    f"你真好。"
    e"谢谢你这样说。那么小四的心愿呢？"
    u "我的心愿……"
    f"……我吗？我是为了自己活着。"
    e"很多人都是为了自己活着，但往往不愿意坦率承认，而更愿意去寻找一个漂亮的修饰。"
    f"乃琳希望我是什么样的呢？"
    e"小四是什么样的都好，我只是希望，我们也能够帮助小四实现心愿，至少，能够可以带给你什么。"
    f"乃琳……你好认真啊。"
    e"当然了。也许你所做的一切，对你来说都是轻而易举的，可能一个无心的举动，就化解了一个大危机，你或许不会在意这些，但是我们会。"
    f"……是这样吗？"
    e"就像是刚刚，然然发现自己的嗓子有些疼，本来可能需要修养，需要紧急更改训练计划，但是你很轻松地把她治好了。"
    f"嗯……那个确实很容易。"
    e"所以，我们该如何回报这样的你呢？人间的一切繁华对你来说都是那么寻常，无论是什么高深的技巧也都可以轻易复制。"
    f"回报我吗？这一次是你错了。"
    e"为什么？"
    f"如果一定要谈回报，也是我要回报，你们化解了我五百年的执念，我无比感激。在很多人的眼里，我的确是无所不能的……"
    f"但是啊，无所不能的我也有五百年放不下的心结，而你们帮我放下了——这还不足以让我用一切来回报吗？"
    f"我说过，我是为自己活着的，我也不希望见到，有人的一生是在为了别人活着。灵魂最重要的应该是自由自在，更胜于遗世独立。"
    f"所以，我最大的心愿，并不是光都那最高的位置，我想要的是每一天都能开开心心。"
    f"现在的我，能和你们每天都在一起，就是最开心的事情，这对我已经足够了。"
    e"小四……"
    f"在你们踏入深海前，我是你们的粉丝。在我来到枝江后，我想……我们是朋友。"
    e"嗯，我们是朋友。"
    f"所以作为朋友，我需要送你一个东西。"
    e"是什么？"
    f"也许……我只是说也许，在以后的某一天，我不在了，大家如果遇到了难以想象的困难，不得不用到超越人类的力量，应该要有所准备的吧！"
    e"你不在了？这是什么意思？"
    f"没什么的……只是一种假设！"
    e"好吧……不过是什么准备？"
    f"如果放在修仙小说里，大概是那种最厉害也最简单的秘籍？应该挺万能的魔法教科书。"
    e"我不要。"
    f"为什么？"
    e"A-SOUL只是一个平凡的名字。我们被支持，被喜欢，并不是因为我们多么强大，或者天赋异禀。从最初的时候，我们追逐、超越的目标，一直都是昨天的自己。"
    f"是啊，阳光、善良、努力，是这些让大家走到了今天。那么……我送你一个许诺吧。"
    e"什么许诺？"
    f"是关于一切你不可见的世界的。"
    f"这一次，你们遇到那么多困难，最后还是彼此鼓励，找到唯一正确的办法，将晚晚接了回来，这样的壮举，本该有奖励的。"
    stop music fadeout 1.0
    e"如果小四一定要给我一些特殊的奖励，其实我也有想要的能力啦……"
    f"哦？你说！能做到的我一定给你！"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 1.0
    e"好！你说的！"
    u "她忽然坏坏一笑。"
    e"就是……有没有那种光环魔法？只要打开以后，就会让我身边的女孩子们更喜欢我的那种？"
    u "……"
    e"怎么不说话？是你说能做到就一定给我的，该不会做不到吧？"
    f"……她们知道吗？"
    e"这个不重要吧？"
    f"怎么不重要！我的良知告诉我不行……对了！"
    e"你想到了什么坏主意？怎么笑得不怀好意啊！"
    f"法师，一般都是有蓝条的吧？开光环类技能，应该都是有每秒蓝耗的。"
    e"你……怎么知道这么多？"
    f"晚晚教过我一些游戏的知识！但是，反正你没有蓝条，这个魔法给你也无所谓啦！"
    u "我相信，那些知识，现在一定已经像是水流一样流入了她的脑中，她只要有魔力值，一定能用出这种魔法！我也不算是言而无信！"
    e"算了算了……反正我也不是一定要和她们更近一步啦，真小气……"
    stop music fadeout 1.0
    f"但是，之前说的关于不可见世界的许诺，我是认真的。"
    play music "audio/青寂.ogg" fadeout 2.0 fadein 1.0
    e"不可见的世界？"
    f"枝江是你们的世界，你们在这里努力着，收获着，如果这会是永远，我就可以不用插手，让大家创造自己的幸福。"
    f"可惜永恒只存在于想象之中。我教你的，是关联到宇宙的预测法。倘若真的有一天，大家面临了世界之外的困难，这种办法可以算出最合适的选择。"
    f"我也希望，乃琳以后永远不会用上我教你的东西。"
    e"我明白。但是，有小四在，哪里会有那种困难呢？为什么我一直有一种感觉，就好像小四会离开一样？"
    f"当然不会，我可是会见证大家走上北方都会的大舞台的！"
    e"好，我明白了，谢谢你！"
    stop music fadeout 2.0
    scene zl with fade
    u1"……听到了不得了的事情啊！"
    u1"虽然说，偷听她们讲话不太好，但我们也只是想知道，小四想要的是什么。"
    scene res2 with dissolve
    play music "audio/01.二千嬢.ogg" fadeout 1.0 fadein 1.0
    u1"确定小四离开后，躲在门后的我们偷偷回到了休息室，乃琳也很有默契地回来了。"
    show e1
    e1"晚晚，小四之前有教过你做魔力药水一类的东西吗？"
    hide e1
    u1"……"
    u1"回来第一件事居然是说这个？"
    show a181
    a1"别惦记你的魔法光环了，你连个蓝条都没有！"
    hide a181
    show e7
    e1"你们居然偷听我们说话！"
    hide e7
    show c1
    c1"不愧是乃老师，在恶人先告状这方面做得很好！"
    hide c1
    show e1
    e1"既然你们都听到了，就先不提这个。更重要的是，你们说，小四为什么一定要给我们留下那种方法呢？"
    hide e1
    show d61
    d1"至少……在我们去到那个舞台以前，她说自己不会走。"
    hide d61
    show a151
    a1"所以她还是会走的吗？"
    hide a151
    show b13
    b1"别乱猜了！我还是理解小四的。而且，我们本来也不会依赖别人来解决问题的，对吧？比起把别的世界的困难留给小四解决，不如我们自己学会面对，不是吗？"
    hide b13
    show d31
    d1"拉姐说得对，但是，万一小四真的会走呢？"
    hide d31
    show b1
    b1"她走去哪里呢？光都还是深海？她说过，最大的心愿就是得到平凡的快乐，不论之后如何，我们就和她创造共同的快乐回忆吧，就像我们一直在做的这样！"
    hide b1
    show d11
    d1"我明白，关于小四的事情，我会认真思考的……我也想要送她一份特别的礼物。"
    hide d11
    show b2
    b1"嗯，我相信然然。不过说起小四，她来了以后，我们的训练效率高了好多！"
    hide b2
    show a11
    a1"没错！训练中所有的意外事件都被她解决掉了。"
    hide a11
    show c1
    c1"还有饭菜，她做饭就好像有什么奇异的配方，吃过以后就能够感觉到精力充沛！"
    hide c1
    show b3
    b1"之所以和大家提这个，就是因为我有一个想法。"
    hide b3
    show e1
    e1"拉姐又突发奇想了？"
    hide e1
    show b10
    b1"我感觉，凭我们现在的状态，月末表现完美简直是水到渠成！所以明天我打算暂停训练，大家来为了月末的舞台做些筹备，比如准备些舞台装饰物。"
    hide b10
    show e5
    e1"这些不是有专人负责的吗？还是说……"
    hide e5
    show d11
    d1"我明白了！拉姐的意思是，要和小四一起准备吧？"
    hide d11
    show b1
    b1"没错！然然聪明，这就是我的想法。"
    hide b1
    show c3
    c1"我同意，我们也当作是放松一下吧！第一次去做舞台的准备，还真是有些新奇呢。"
    stop music fadeout 2.0
    scene black with fadehold
    u "和乃琳聊过天后，一天很快过去了。"
    play music "audio/Zki.ogg" fadeout 2.0 fadein 2.0
    scene res2 with fade
    u "大家都去休息后，我又去了休息室，却一不小心睡着了。"
    u "这一次足足睡了一个小时，也并没有像上一次那样做梦，睡得很安稳。"
    u "昨天，然然兴奋地来找我，让我做好准备，今天要来筹备舞台了。"
    u "听她的想法，好像是要自己动手去做？有意思。"
    u "……好冷！"
    show f4 with vpunch
    f"咳……咳……"
    hide f4
    u "忽然，不受控制地咳嗽起来。"
    u "最近身体发冷是越来越严重了，几乎是不能忍耐的程度。"
    u "没办法……只能强行调节一下了。"
    u "……我在心中燃起一团火，将寒冷压了下去。"
    u "毕竟这也只是个提醒，又不是我真的患了什么不治之症。"
    u "而且，如果她们知道这些，一定会担心的吧？"
    u "好了好了，我该去准备早饭了！"
    u "等到吃过早饭，就要各自收拾一下去训练室集合了。"
    stop music fadeout 2.0
    scene black with fadehold
    u "……"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene bg3 with fade
    u "新的一天，今天的枝江阳光明媚。"
    show f1
    f"训练室真宽敞！然然，你昨天说要准备舞台装饰，是类似于做手工吗？"
    hide f1
    show d11
    d"对，就是要我们亲自动手去做！这是一种能够给大家传递心意的方式。"
    hide d11
    show f19
    f"很简单的，我们去网上查一下，找一个漂亮的样式，我直接把它造出来，然后将大家的心意填充进去，我们的观众只要看到，就能够感受到大家满满的心意！"
    hide f19
    show a42
    a"不行！"
    hide a42
    show c1
    c"小四，我们不能什么事情都只看结果的。"
    hide c1
    show e1
    e"没错，我知道小四很厉害，如果想的话，就连月末的演出，也都可以省去我们的训练。但是，一次演出不只是为了我们最后的完美表现，为了实现它所做出的努力也是很重要的！"
    hide e1
    show f4
    f"对不起，是我草率……"
    hide f4
    show b10
    b"没关系的，小四，大家不会怪你的。但是！这一次你要用最朴素的方式去做！不能直接创造成品，也不能直接复制别人的做法，人的心意，小四也要亲自感受才明白价值！"
    hide b10
    show f9
    f"那拉姐，我们现在要做什么？"
    hide f9
    show b2
    b"不知道诶，我们上网查一查吧。"
    hide b2
    show f20
    f"然然知道吗？"
    hide f20
    show d11
    d"拉姐说得对，我们还是要上网查查的！"
    hide d11
    u "……"
    u "连做什么都不知道，果然这些装饰品原本是该交给专人采购的吧！"
    u "最后……还是上网去查了。"
    u "与我最初说法的区别就是，虽然都是查到了需求与做法，但我被禁止直接把成品做出来了。"
    u "但是作为必然的一步，我还是造出了足够的彩纸、胶水、剪刀一类的原料和工具。"
    u "忽然想起了上一次我们一起做的甜品。"
    u "……我们这样做出来的东西，真的能够用在那么重要的舞台上吗？"
    show a142
    a"拉姐！"
    hide a142
    show b1
    b"干嘛？"
    hide b1
    show a142
    a"你过来陪我折小青蛙！"
    hide a142
    show b10
    b"为什么要折小青蛙啊？"
    hide b10
    show a12
    a"我们比一比谁跳得远！"
    hide a12
    u "这……拉姐不会同意的吧？"
    show b2
    b"好！"
    hide b2
    u "居然爽快地答应了！？"
    show c1
    c"我也要玩！"
    hide c1
    show a142
    a"好，那乐乐也来一起。"
    hide a142
    show e1
    e"小孩子贪玩，没办法……"
    hide e1
    u "她笑着摇摇头，在旁边专心画着什么。"
    play music "audio/破碎冬日.ogg" fadeout 1.0 fadein 1.0
    scene df with fade
    d"小四，我们不管她们！晚晚是小妹妹不懂事，嘉然姐姐和她不一样！"
    f"哦……好。然然，你在做什么呢？"
    u "她正把几条彩线编成一股，虽然不太熟练，但看起来格外认真。"
    d"嘘……不要说话！我要集中注意力，不然就编错了！"
    u "然后，训练室中虽然有六个人，却无比安静，只剩下乃琳那里笔尖划过纸的声音。"
    u "然然逐渐将手中的彩线，编到了接近一条手链的长度。"
    a"我折好了！"
    u "旁边的晚晚兴奋地喊着，我差点被她吓到。"
    b"等等，我马上就折好！"
    c"哇，你们这么快吗？"
    u "……这时候，然然已经编好了最后的部分，把线头紧紧系在一起。"
    u "青、红、紫、蓝、黄，五色的彩线编在一起，十分好看。"
    f"然然，现在可以告诉我这是什么了吗？"
    d"就是一条手链，送给你的。"
    u "说着，她又解下了自己的手链，拆下一颗橙色的珠子，串在了这条手链上。"
    d"做好啦，小四，把手伸出来。"
    f"我真的可以收下吗？谢谢你……"
    d"这算什么！把手给我……"
    f"好……"
    u "我伸出手，看着然然将它系在我的手腕。"
    play music "audio/01.二千嬢.ogg" fadeout 1.0 fadein 1.0
    scene bg3 with fade
    show a142
    a"看！我跳了好远！"
    hide a142
    show b2
    b"不如我远哦，哈哈！晚晚，乐乐，你们是赢不了我的！"
    hide b2
    show e4
    e"真是的……乐，你还陪着她们一起幼稚啊？"
    hide e4
    show c1
    c"乃琳！为什么我这个青蛙跳得这么近？你快过来！"
    hide c1
    show f22 with dissolve
    f"然然，谢谢你的心意，我感受到了。之后，我也会送给大家带着我的心意的礼物的！"
    hide f22
    show d12
    d"好，我会等着那一天的！"
    hide d12 with dissolve
    u "今天，然然的原计划算是以失败告终了。"
    u "她做好了那条手链以后，就和乃琳一起加入了玩青蛙的游戏中。"
    u "我尝试了好久的手工，想要做出一个看得过去的礼物送给她们，但是我太笨了，还是私下里多多练习吧！"
    u "……最后，我也加入了她们的游戏中，玩了一上午。"
    u "当然……不止玩了青蛙！"
    u "只是，最初的想法——舞台，完全没有准备！"
    u "结果是，我们度过了一个很开心的上午。"
    u "可能……这显得我有些自恋，但我有一个大胆的猜想。"
    u "会不会有这样一种可能？她们本就没想要做什么舞台的准备，只是想要为我留下开心的回忆呢？"
    u "我看着手链上那颗闪闪发光的橙色珠子。"
    u "答案是什么并不重要了，谢谢你们，来到枝江后的每一天，我真的都很开心。"
    play music "audio/02.レイSureaLY_1.ogg" fadeout 3.0 fadein 3.0
    scene bg2 with fadeholdd
    u2"按照晚晚生日演唱会以前的计划，这半个月，我们应该是全力筹备月末的演唱会。"
    u2"与小四的相遇是未曾设想的，这的确打乱了我们最初的规划。"
    u2"然后，我们也真的抽出了好多时间来玩，但训练没有受到影响，团舞和新团歌的排练也都十分顺利。"
    u2"毕竟，我们去那北方都会的鸟巢，靠的又不是临阵磨枪！"
    u2"除了团舞，我们每个人也都有着自己的个人节目。"
    u2"我刚刚做好个人部分的训练，感觉很不错！"
    u2"不知道她们自己部分的训练还顺利吗？"
    u2"团舞靠的是我们一支团队的默契与信任，这些已经在这两年的时光中磨合了无数次。"
    u2"但是个人部分，也许会面临一些特殊的困难。"
    u2"并不是不相信她们的实力，而是我自己也曾遇到过类似的困境。"
    u2"现在是下午三点，或许会有人在休息室吧……"
    scene res2 with fade
    u2"果然！"
    show c5
    c2"拉姐！"
    hide c5
    u2"看到我进来，珈乐便朝我挥起了手，小四在旁边冲我笑笑，没有说话。"
    show b1
    b2"怎么样？个人部分的准备还顺利吗？"
    hide b1
    show c7
    c2"现在只能有九十分的水平。"
    hide c7
    show b2
    b2"那不是很好嘛！再练一练，就轻松掌握了吧？"
    hide b2
    show c2
    c2"不，拉姐……虽然不想承认，但这剩下的差距，不是靠练习就能弥补的。"
    hide c2
    show b9
    b2"是什么差距呀？"
    hide b9
    u2"能让乐都没有办法弥补的差距，是绝对要严肃对待的！"
    hide b9
    show c2
    c2"这个……我不是很好形容，小四能帮我解释一下吗？"
    hide c2
    show f92
    f2"珈乐平易近人，温柔和善，曾经让她装高冷，是什么后果，拉姐你也知道。偏偏这一次她的个人部分，需要她从内心中表现出高傲的态度来，这可不简单。"
    hide f92
    show b1
    b2"原来是这样。最初排节目的时候，只想到整体的方面，却没有考虑好大家和各自的部分是不是合适……对不起，要不然我们把节目换一下？"
    hide b1
    show f22
    f2"没关系的，拉姐。让我先想想办法吧。"
    hide f22
    show c1
    c2"虽然我不知道小四在计划什么，但是，我愿意相信她。"
    hide c1
    show b10
    b2"小四，有什么办法吗？"
    hide b10
    show f12
    f2"那种骄傲可不是固守着自尊、掩饰着自卑的冷漠，更多的是自信和从容。我的大姐或许有这种心境，但我很难体会得到。"
    hide f12
    show c3
    c2"小四，难道你要找你的姐姐帮忙吗？"
    hide c3
    show f92
    f2"不，我虽然感受不到，但乐能感受到就够了，我在想一个完整的计划……嗯，明天吧！明天中午，去训练室！"
    hide f92
    u2"神神秘秘的，那就明天中午去看看，小四究竟要做什么。"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene bg3 with fadehold
    u "第二天，中午。"
    u "今天上午没有集体训练的安排，所以训练室只有我和珈乐会用。"
    u "现在的训练室中，只有我和她两个人，不知道拉姐会不会来。"
    u "我刚刚把装备带过来的时候，就发现珈乐已经到了，看来她是很在意这件事情呀。"
    u "明明昨天我还和她说过，不要多想，心情放松就好。"
    show c2 with dissolve
    c"小四……这是？"
    hide c2
    u "看来她已经大概明白我要做什么了。不然，她一定会好奇地问我，而不是感到困惑。"
    show f172
    f"冷兵器中，剑往往被认为是最高贵的，据说，即使是一个普通的剑客或决斗家，他们也都有着异乎常人的骄傲。"
    hide f172
    u "没错，我带着两把剑。"
    show c7
    c"可是……我不会用剑啊！这个就连拉姐也不一定会吧！"
    hide c7
    show f172
    f"不会用剑，才更能用外行的眼光来看这件事，毕竟，剑客的高傲可都是写在小说里的，哪个作家是真正练过的？接着！"
    hide f172
    show c7 with hpunch
    u "我把剑朝她丢了过去，她吓得躲开半步，但还是抓住了剑柄。"
    hide c7
    show f212
    f"而且，你的粉丝可是叫皇珈骑士，骑士们追捧的人，可不能不会用剑啊！"
    hide f212
    u "我试图开玩笑来缓和她的情绪，但她还是不住摇头。"
    show f32
    f"乐，之后的事情，也许你会很害怕，但是，你不能放弃。这不是鼓励，而是命令！"
    hide f32
    show f62
    f"这个世界上没有任何一个剑术家可以做到我接下来做的一切，我会让这一战成为刻印在你脑中的骄傲符号！"
    hide f62
    show c8
    c"不……我又不会用它，而且还没有防具！我真的害怕……小四，我知道你很厉害，但我完全做不了你的对手啊！"
    hide c8
    show f172
    f"乐，你问问自己的心。"
    play music "audio/Medusa.ogg" fadeout 2.0 fadein 1.0
    scene cf with fadehold
    u "我悬在半空，手中握着剑，剑气已经铺满了训练室。"
    u "从一开始，我就没打算用人间的剑法。"
    u "有什么能比用人的剑击落神明更加值得骄傲的呢？"
    c"我明白了，我准备好了。"
    u "她慌乱的目光平静下来，逐渐变得像是澄澈的湖水。"
    f"第一剑来了！"
    play sound "audio/jinshu.ogg"
    scene cf with vpunch
    u "巨响之后，我又回到了半空。"
    c"哇……好重的一剑！"
    u "我看见，她的手在轻轻发颤，凭她的身体硬接这高处劈下的一剑，显然并不轻松。"
    u "还要继续用这种剑法吗？这个威势，她恐怕撑不住啊……"
    f"第二剑要来了，如果不好接，就用别的办法！"
    play sound "audio/pengzhuang.ogg"
    u "这一剑被她灵巧地闪过了，剑芒划破了地板，但训练室中早已经成为了自动复原的领域，撕裂的地板很快恢复了原样。"
    c"我居然躲开了！"
    f"加油，你不仅仅能躲开的。"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    u "也许，很早以前就有人思考过这个问题。"
    u "人要如何才能打败神呢？"
    u "终究要适应神的力量，不能永远躲避。"
    u "当她明白，自己不可能永远躲开我无穷无尽的剑影，躲避只会让她远离我的时候，"
    u "——打败神的第二步，是接近她。"
    u "用最奇妙的方式拨开我的剑，她终于朝我踏出了第一步。"
    u "进攻的方法，你刚刚学会了吗？"
    u "……我仍在祈祷着，也在期待着。"
    u "幻象、剑影，我用的是最美丽的剑。"
    u "我没有教她任何驾驭幻影的技巧，但是，她学的也是最美的剑。"
    u "我不知道珈乐是否有闲暇来思考，但我希望她不要想这么多。"
    u "构建这一切的思路由我把控，她只需要去理解剑。"
    u "或者说，是理解我赋予剑的内涵。"
    u "那么，如何打败神呢？"
    u "不再逃避，正面接近，这不够。"
    u "神为什么喜欢高高的地方？"
    u "高高在上。"
    u "高高才能在上。"
    u "如果被发现，神只是一个站得高的人形，"
    u "如果人与神的距离被消除……"
    u "想要击落神明，先要到达同等的高度。"
    u "只是，这一步不能够有任何差错。"
    u "即使达到了同等的高度，也要有“想要击落神明”的心！"
    f"我不会受伤的，尽管用一切能想到的办法，尝试击落我吧！"
    u "终于——"
    scene cf with fade
    u "一闪。"
    u "我的眼中是她。"
    scene white with dissolve
    u "我看见了最美的一剑。"
    u "这一剑很快，在我眼中却无比漫长。"
    u "如果，我会死在这一剑下，我会后悔吗？"
    u "我当然会后悔的，现在的我，还有好多心愿没有完成，我绝对不可能死。"
    u "但是啊，如果我不得不死去，在这一剑下，我不会有遗憾。"
    stop music fadeout 2.0
    play sound "audio/posui.ogg"
    scene cf1 with dissolve
    u "好像是镜子碎裂的声音。"
    u "她击破了我的幻影，这不是普通的幻影，而是我为了挡住这一剑，用我的剑制造的影子。"
    play sound "audio/duanjian.ogg"
    scene cf2 with pixellate
    u "解除幻象，我用的剑已经从中间断成了两截。"
    play music "audio/01.二千嬢.ogg" fadeout 1.0 fadein 1.0
    scene bg3 with fade
    show f192 with dissolve
    f"乐乐，你赢啦！"
    hide f192
    show c3
    c"谢谢你，小四！你究竟做了什么？为什么我的剑术能这么厉害？我看过你的剑以后，你的每一次进攻，就好像都刻印在了我的脑海里一样！"
    hide c3
    show f12
    f"这个不重要的，现在的你，应该可以掌握那首歌了吧？"
    hide f12
    show c1
    c"一定可以！我现在真的太兴奋了，今天发生的事情，也许我一生都不会忘记吧！刺出最后那一剑的时候，我就知道，我已经找到那首歌需要的骄傲了！"
    hide c1
    show f92
    f"这把剑可以留着的。"
    hide f92
    u "我笑着把断剑也递给珈乐。"
    show c4
    c"这把剑对我来说，应该很有纪念意义吧！"
    hide c4
    show f192
    f"当然了！哈哈，然后你可以去和拉姐她们炫耀，“2022年6月小四比剑输给珈乐，望周知”，就像这样！"
    hide f192
    show b2 with moveinright
    b"我已经知道了！如果是之前有人说你们要比剑，我怎么也想不到小四居然会输！但不管怎么说，乐你也太厉害了吧？"
    hide b2
    show c4
    c"诶嘿……拉姐什么时候来的？"
    hide c4
    show b10
    b"我记得小四说要和你来训练室，就急着过来了，可是我到的时候，你刚好用出最后一剑……真可惜！我还是来晚了。"
    hide b10
    show c1
    c"没关系的，拉姐，更重要的事情已经没问题了！那首歌，我不会出错的，谢谢你们！我先回去练歌啦！"
    hide c1
    show f12
    f"好，我马上去准备午饭，做好了以后我去叫你们。"
    hide f12
    u "珈乐朝我们挥挥手，离开了训练室。"
    show b10
    b"小四你去和乐玩，都不叫我的嘛？"
    hide b10
    u "珈乐刚刚走出门，拉姐就有些气鼓鼓地责怪我。"
    show f192
    f"原来拉姐喜欢这个呀。那下一次我来当裁判，让拉姐和乐乐玩怎么样？"
    hide f192
    show b10
    b"乐？她那么厉害，我怎么打得过她？"
    hide b10
    show b2
    b"而且，我才不是这个意思，我才没有很想玩……"
    hide b2
    show f42
    f"明明就是想玩！"
    hide f42
    show b14
    b"……那你明明知道我想玩还不叫我？哼！"
    hide b14
    show f192
    f"哈哈，拉姐别生气，你可以叫晚晚一起嘛！"
    hide f192
    show b1
    b"除了你和珈乐，我应该都可以打一打的！小四，你到底对珈乐做了什么，她怎么那么厉害？"
    hide b1
    show f172
    f"是祈愿。"
    hide f172
    show b10
    b"什么意思？"
    hide b10
    show f92
    f"我定义她的剑术天赋到达顶峰。但是，我不确定这种天赋的变化，会不会真的足够有效，所以，我用了一个晚上来为她祈愿。"
    hide f92
    show b10
    b"像谁祈愿呢？你就是神呀。"
    hide b10
    show f22
    f"向我自己。到最后，甚至我自己也相信了她有着独一无二的剑术天赋。"
    hide f22
    show b10
    b"乐知道这些吗？"
    hide b10
    show f192
    f"她不需要知道的。不过，比起这个，其实拉姐想要去的地方，是月亮吧？"
    hide f192
    show b10
    b"什么？"
    hide b10
    show f172
    f"就像之前在那边说过的一样，我会带拉姐去月亮上。而且，我敢答应的事情，就一定能够实现的，放心吧！"
    hide f172
    show b3
    b"那我们今天晚上见，可不可以？"
    hide b3
    u "不愧是A-SOUL的队长！上一次听到我在计划着月亮的事情，她足足震惊了十秒以上，但这一次的反应格外迅速！"
    show f192
    f"好，今天晚上，我去找你！还有，拉姐如果想玩，防护服和圆头的剑都准备好了，放在墙角，可以去找晚晚她们试试。"
    hide f192
    show f202
    f"然后不要去找珈乐！我给出去的能力，可是永远都不会收回来的，我去准备午饭啦！"
    hide f202 with moveoutright
    u2"话音落下后，小四就从训练室离开了。"
    play music "audio/深竹.ogg" fadeout 2.0 fadein 2.0
    scene bg42 with fadehold
    u2"……那之后，然然、晚晚和乃琳都被我找了过来，在训练室穿着防护服，拿着剑乱打一通，甚至连刚刚练好歌的珈乐后来也加入了我们。"
    u2"虽然乐的剑术没被小四收回去，但是，在这种乱战之中，人多就是力量！我们其余四个成功凭借人数优势，把乐打得灰头土脸！"
    scene bg33 with dissolve
    show f141
    f2"去吃饭啦，看你们满头大汗的样子……剑真的有这么好玩吗？"
    scene bg42 with dissolve
    u2"这是她对此的评价。"
    u2"那时吃过饭后，我就回到了自己的房间。忙忙碌碌，不知不觉已经是晚上。"
    u2"这次演唱会的准备格外顺利，小四来了以后，训练甚至有种事半功倍的感觉。"
    u2"但是，这并不是最重要的事情。"
    u2"相比训练的顺利，更加重要的是，她让我亲眼见到，这接近两年的偶像活动真的有着意义。"
    u2"小四可以放下对姐姐的不满，开心地度过每一天，这是对我们极大的肯定。"
    u2"能够为更多的人带去快乐与美好，是我们A-SOUL的初衷。"
    u2"那么，我自己的愿望呢？"
    u2"我看着柜子里锁着的芭蕾舞鞋，旁边是我曾经荣誉的证明。"
    u2"能够激励那么多人成为更好的自己，我当然也很开心。"
    u2"可是，心中终究有那放不下的骄傲。"
    u2"比剑赢过了神灵，可以让珈乐感受到骄傲……而我的骄傲，一直都在那一双舞鞋上。"
    u2"小四说她会来找我，可是她为什么还没有来呢？"
    u2"胡思乱想着，我打开衣柜，在最深一层中，找到了曾经的白衣。"
    u2"本以为再也不会穿上它的，也许今天才是最后一次吧……"
    scene black with dissolve
    u2"我躺在了床上。"
    stop music fadeout 2.0
    u2"……"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 1.0
    u2"风吹动我的头发，弄得我好痒。"
    f2"拉姐，我来了。"
    scene bf with fade
    u2"我睁开眼睛，她就在我的眼前，笑着看着我。"
    u2"她的背后是星空。"
    b2"这里是哪？"
    f2"这里是月亮。"
    u2"我清醒过来，这时才发现，我居然枕在了小四的腿上。"
    u2"这可不行！我要坐起来……"
    f2"没关系的，现在如果是乃琳，她一定不会坐起来的吧？"
    u2"她伸出手，轻轻按住了我。"
    b2"嗯……也许吧？"
    u2"我不知道乃琳会怎样，但是，既然小四不介意，她的腿又软软的，我也索性这样躺着。"
    u2"遥远深邃的星空与如玉的世界，不知是画中还是梦中。"
    b2"这里不是月球吧？"
    f2"没错，这里是月亮。"
    b2"有什么区别吗？"
    f2"那个荒凉死寂的灰色星球叫做月球，那里没有氧气，如果你这样去的话，会死。"
    b2"……但这里不一样。这里，符合我们对月亮的一切想象……是吗？"
    f2"是啊，像是诗人的笔会为一些景色增添神秘的灵性，专业的摄影师也往往会对拍出的照片做一次调色，你看到的惊艳的照片，可能更接近于画作。"
    f2"世界的真实面貌，往往都不如我们的想象美丽。"
    b2"那不会有例外吗？"
    f2"也许会有，但是，我想世界的真正魅力，在于那些我们想象之外的存在。"
    b2"你说，会不会有一支想象之外的舞蹈呢？"
    f2"会有的，但是，我并不知道它的样子。"
    f2"之前训练的时候，我记得晚晚问过我，为什么不选择登上舞台。"
    b2"我记得你的回答模棱两可。"
    f2"这个世界上有太多的舞种，我想要学每一种，都是很容易的事情。将不同舞种的优秀之处整合，也并不难。"
    b2"你这样说，之后一定有更重要的理由来拒绝吧？"
    f2"哈哈……拉姐真聪明……因为我走上舞台，是在亵渎真正舞者的理想。"
    b2"怎么这样说？这也太严重了吧！"
    f2"在舞蹈上，我只能作为模仿者，我自己没有站在舞台上的理由。我跳不出在想象之外的惊艳舞蹈，只能对现有的一切做极致的模仿。"
    b2"这样吗……"
    u2"我仍然不能确信，这是不是足以成为她远离舞台的原因。"
    u2"只是，如果有一个人走上舞台，轻松跳出了最高难度的芭蕾，我会嫉妒她吗？"
    u2"我不知道，假如她是个努力又有天赋的人，我应该会很开心遇到同道之人吧？"
    u2"那假如她并不努力，也并不想要跳舞，只是有着最高的天赋呢？"
    u2"我当然会难过……"
    u2"可是，如果这个人是小四，如果她是为了我们走上舞台，那么我一定会很开心的！"
    u2"我想要告诉她这些，可是，她却开口打断了我。"
    f2"不要胡思乱想了，拉姐。虽然我无论如何都跳不出那想象之外的舞蹈，但是，也许在某一天，拉姐灵光一闪，就能够做得到了！"
    b2"可是……我现在还远远不够优秀呢，那一天应该会很遥远、很遥远吧……"
    f2"我看到你换上了曾经的芭蕾舞裙。"
    b2"嗯……那一次受伤后，很多事都不一样了。但是这毕竟是我曾经的梦想……"
    f2"那么今天……是最终告别，还是久别重逢呢？"
    u2"白月的夜里，我们都沉默着。"
    u2"来到这里之前，我想，这也许是最后一次穿上这件舞裙。"
    u2"但小四说，可能有一天，我会成为那位舞者，跳起想象之外的舞蹈。"
    u2"她没有说一定……所以，我也更加相信，她不是在故意说好话骗我。"
    b2"小四，其实今天换上这件衣服，我本来是想要伴着月色，跳一支舞的。"
    f2"本来吗？看来我亏了呀，不然就能够看到拉姐跳舞了呢。"
    u2"她这样说着，露出开玩笑般的笑容……无论如何，我也不觉得她这是亏了的表情。"
    u2"就好像已经看穿了我的想法。"
    b2"小四，我们立一个约定吧。"
    f2"什么约定？"
    b2"如果我真的能够跳出那一支想象之外的舞蹈，我会穿着这白裙，在这月亮上，为小四和我的队友们跳那支舞的。"
    f2"好啊……那我也送拉姐一件礼物吧？"
    b2"小四要送我什么？"
    f2"拉姐曾经受了严重的伤，就像是天使折断了羽翼，虽然凭借着自己的努力，做到了今天的一切，但这是不够的。"
    f2"至少，不够来到这月亮上，总不能以后每次都要晚晚用传送门把你带上来吧？"
    b2"那你要送给我……"
    f2"天使的羽翼，还有这个月亮。"
    b2"不是一件礼物嘛，怎么变成了两件?"
    f2"嗯……"
    f2"……因为它们有一个共同的名字，叫做贝拉。"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene res2 with fadeholdd
    u "嗯……昨天很开心。"
    u "和乐乐比剑很开心，在月亮上和拉姐一起的时光，也像是做梦一样。"
    u "回到了正常生活后，每个人都有在按照计划训练。"
    u "这些天的饭菜一直是我在准备。来到枝江以后，每天都很开心，很轻松，我做的饭菜好像也带上了让人愉快的味道。"
    u "虽然只要知道菜谱，就没有我做不出的菜式，没有我准备不了的食材，但，许多想尝试的菜式已经做过，又不想毫无目标地按照菜谱的顺序继续做下去。"
    show a11 with dissolve
    a"怎么了？小四，在想事情吗？"
    hide a11
    show f12
    f"是啊，我在想，今天吃什么。"
    hide f12
    show a21
    a"拉姐刚刚说，今天的饭就不用你来做了，她吃了你做的菜，很羡慕你的厨艺，这几天也有在学着做菜，希望今天可以尝试一次。"
    hide a21
    show f192
    f"这样吗？很好啊。我知道她是个认真的人，那就交给她吧。"
    hide f192
    show a141
    a"嗯！说起来，我们要不要出去走一走？"
    hide a141
    show f92
    f"好啊，晚晚你想去哪里？"
    hide f92
    show a11
    a"我不知道，但是，小四应该知道吧？"
    hide a11
    show f42
    f"我？"
    hide f42
    show a51
    a"没错，我们一定是在很久很久以前，就已经认识了。"
    hide a51
    u "我恍然大悟。"
    show f12
    f"我明白了，是那最初的相遇之地吧。"
    hide f12
    show a41
    a"嗯，那段记忆格外模糊，但是，这些天里，那个熟悉的梦却逐渐清晰了。"
    hide a41
    show a11
    a"我虽然不知道那是什么地方，但是，我知道那个人是你。"
    hide a11
    show f92
    f"你有去过水族馆吗？"
    hide f92
    show a151
    a"也许没有……我曾一直都想要去一次。"
    hide a151
    show f192
    f"那我们今天就一起去一次吧。"
    hide f192
    show a11
    a"嗯，不过去过你的世界以后，我也不会再期待水族馆了。"
    hide a11
    show a141
    a"没有什么水族馆能够比得上你的海洋。"
    hide a141
    show f12
    f"那个水族馆不一样……你知道的。"
    hide f12
    show a21
    a"是啊，那里一定会不一样的！"
    play music "audio/第四约定.ogg" fadeout 1.0 fadein 1.0
    scene tunnel with fadehold
    u "看到这久违的深蓝通道，我不由得心怀感激。"
    show a21 with dissolve
    a"这里……我曾经来过的，我无数次梦到这里。"
    hide a21
    show f102 with dissolve
    f"没错，我们最初就是在这里相遇的。"
    hide f102
    show a11 with dissolve
    a"我……记起来了。"
    hide a11
    u "那最初相遇的情景，也仿佛在我眼前重现。"
    scene white with dissolve
    u "……"
    u "枝江吗？"
    u "是在十年前……刚刚来到这座城市的我，看着陌生的一切。"
    scene tunnel2 with dissolve
    u "然后，我怀着骄傲，一边审视着，一边走进了这座水族馆。"
    u "我拥有一片孤独的海，看到这陌生世界的第一眼，这水族馆是最熟悉的场所。"
    u "那天的水族馆游客很少，但我仍然害怕与人类相遇……"
    scene black with fade
    u "于是，我静静地躲在了水中，将自己隐藏在一群水母之后，观察着往来的人类。"
    u "只要我不想被发现，没有人可以觉察到我的存在。"
    u "但是……我遇到了她。"
    scene af with dissolve
    u "那道紫色飘过的时候，就像是夜空中的暗星。"
    u "并不璀璨，但是努力闪耀。"
    u "闪耀的目光好像穿透了缸壁，不知道那些水母能否觉察。"
    u "于是，我的手也穿透了缸壁，整个水族馆也变得好像是海底的世界。"
    u "她开心地笑了起来。"
    u "人类的脸，可以露出这样美丽的笑容吗？"
    f"你很喜欢水母吗？"
    a"没错！大姐姐，你为什么也在这里？"
    f"因为大姐姐也是水母。"
    u "虽然……我不能完全算是水母，但是这似乎是最容易骗她的话。"
    u "然后，我轻轻纵身，游了一圈，水波留下了完美的弧线。"
    a"好漂亮……但是大姐姐和别的水母不一样诶，还会说话！"
    u "我一时间不知道，该如何应对这个可爱的孩子。"
    u "至少，不希望我的阴暗染上她的童年。"
    f"你知道吗？有一种水母的名字叫做“灯塔”。"
    a"没有听过……可以和我讲讲吗？"
    f"灯塔水母是永远不会死的。每一次死亡之后，都会用更美丽的姿态重生，回到这个自己热爱的世界。"
    a"大姐姐就是这种水母吗？"
    f"嗯……可以算是！"
    u "当然了，我是骗她的，至少那时的我，不会有什么“热爱的世界”。"
    u "至于灯塔水母，固然不会死，却也不可能凭着一次次的轮回，最后变成我现在的样子。"
    a"等我长大了，我也想像大姐姐一样！"
    u "人类和我当然是无法一样的，但是……"
    f"如果你以后能够相信自己，坚持下去，你一定会成为更好的样子，就像你心中期待的一样。"
    a"真的吗？"
    f"当然是真的，我看得见你眼中的光。"
    u "这一次我没有骗她，她眼中闪着的是不会认输的光。"
    u "是憧憬，是希望。"
    u "我那时不知道，是不是每一个小孩子的眼中，都会有这样的光。"
    u "但是，现在我知道，晚晚是独一无二的。"
    u "也许每个人在年幼的时候，眼中都有着这样的闪光，但晚晚却没有在长大后失去那道光。"
    u "又或许晚晚从来都不曾长大。"
    a"大姐姐，等我长大了，成为了梦想中的样子，你还会回来看我吗？"
    f"嗯，当然会，我们约好了！然后，告诉我你的名字吧，至少，我要知道去找谁赴约！"
    a"我叫向晚，大姐姐，你呢？"
    f"我的名字吗？我叫……"
    scene black with fade
    show a21 with dissolve
    a"我想起来了！你的名字，空寰，时空的空，寰宇的寰！"
    scene tunnel with fade
    u "空寰……"
    show f102 with dissolve
    f"好熟悉的名字啊。"
    hide f102
    show a11
    a"我还以为你会说陌生呢。"
    hide a11
    show f12
    f"如果我还是空寰，这当然是个陌生的名字。但是，我已经不是空寰，这五百年前的称呼，当然会让我怀念起那本该熟悉的模糊城市。"
    hide f12
    show a11
    a"为什么那一次，你会自称空寰呢？"
    hide a11
    show f192
    f"你那时候还是个孩子嘛，我也难得被当成一次追赶的目标……"
    hide f192
    show f12
    f"所以，自我放逐的劣质品小四伪装成了神王空寰，希望可以骗你一下，让你勇敢地走下去。"
    hide f12
    show f22
    f"现在，我也明白，空寰这个名字意味的并不是宇宙的神王，心雩给我这个名字，是希望我可以在无数个时空、无数个世界之中，自由自在，最终找到自己的幸福。"
    hide f22
    show a11
    a"那么现在的你，想要用哪个名字呢？"
    hide a11
    show f12
    f"我已经不需要在无数个世界中寻找了，现在的我就在这里，我就是小四。"
    hide f12
    show a11
    a"谢谢你，小四。"
    hide a11
    show f4
    f"谢谢我？"
    hide f4
    show a51
    a"那一次，虽然你最后把那段记忆变得模糊不清，甚至我不记得自己去过水族馆，但是，我一直都记得你。"
    hide a51
    show a11
    a"曾经在最艰难的时候，我一次次受到挫败，也得不到认可，但是，我从来没有想过放弃。"
    hide a11
    show a41
    a"因为即使忘记了，记忆的残片里也能够拼凑出你的样子，那一天，我在深蓝色的梦里，和神灵一样的大姐姐有过一个约定。"
    hide a41
    show a141
    a"我一直记得灯塔水母的故事，也幻想着，也许有一天，我可以像你一样，成为最闪耀的偶像。"
    hide a141
    show f192 with dissolve
    f"我一直都不是偶像哦，但是你做到了。"
    hide f192
    show a161
    a"你知道吗？走出第一步是最艰难的，因为我什么都不会，我记不住在学习、训练的时候，自己究竟哭过多少次。"
    hide a161
    show a171
    a"但是，每哭过一次，我也都会变得更坚强，哪怕只是一点点。"
    hide a171
    show a11
    a"可能是我的运气不错，我也遇到了越来越多的支持我的人、喜欢我的人，能够和我的队友们一起走到今天，离不开所有人的支持。"
    hide a11
    show a141
    a"我也从没有像现在这样，对“天道酬勤”这个词感触如此深刻……也许，你就是天道吧！"
    hide a141
    show f4 with dissolve
    f"不，我只是个偷天道的人，我的姐姐们比我当得起这个词……对了！在那片深海的时候，我曾经和你说过，我羡慕两个人。"
    hide f4
    show a11
    a"嗯，你说第一个人经历了九死的考验，最终成为了最强大的神灵，她就是你的姐姐吗？"
    hide a11
    show f172 with dissolve
    f"没错，她是我的大姐，我曾经很羡慕她。那么，你猜猜我更羡慕的第二个人是谁？"
    hide f172
    show a11
    a"……是你的二姐吗？"
    hide a11
    u "……她犹豫了。"
    show f192
    f"你知道不是的。"
    hide f192
    show a161
    a"……是心雩？"
    hide a161
    u "我摇了摇头。"
    show a121
    a"那……小四告诉我吧。"
    hide a121
    show f192 with dissolve
    f"她叫向晚哦！"
    hide f192
    show f102
    f"其实，你已经猜到了吧？"
    hide f102
    u "她没有回答，轻轻低下了头。"
    show f92 with dissolve
    f"那天分别后，我回到了自己的世界，一直看着你经历着那一切。"
    hide f92
    show f12
    f"看着你哭，我有无数次想要去帮你，可是你每次哭得伤心，到了第二天，又是元气满满，好像什么困难都不能把你击倒。"
    hide f12
    show f192
    f"……后来看见你哭，我都习惯了……"
    hide f192
    show f42
    f"结果这么多年，我也没有来再见你一次……真的对不起……"
    hide f42
    show a141
    a"没关系的，虽然小四没有来，但你一直在我最深的记忆之中，一直在鼓励着我，这足够了！"
    hide a141
    show a21
    a"而且，我哭的这件事，就连我的队友们也都习惯了，也不是你一个人啦！"
    hide a21
    show a11
    a"所以，真的没关系的！"
    scene white with dissolve
    u "那一天，我们去了枝江好多的地方，玩了好多我从没有见过的东西……"
    play music "audio/01.二千嬢.ogg" fadeout 3.0 fadein 3.0
    scene res2 with fadeholdd
    u "……半个月后。"
    u "2022年6月29日，枝江，天气晴。"
    u "终于，播种下的花种将要盛放了。"
    u "就在明天。"
    u "向晚、贝拉、珈乐、嘉然、乃琳，A-SOUL五人即将前往机场，乘坐前往北方都会的航班。"
    u "然后，她们将会在鸟巢举办她们的专场演唱会。"
    u "她们所有的节目我都知道，除了一支新的单曲。"
    u "她们讨论的时候，就神神秘秘的……好像有什么事情在瞒着我！"
    u "不过，等到明天，我就会知道那究竟是什么了。"
    show b1 with dissolve
    b"小四真的不和我们一起去吗？"
    hide b1
    show f192
    f"嗯，最后的时刻，还是要靠大家自己。这半个月的努力，是时候展现给所有人了！"
    hide f192
    show a11
    a"但是你会看着我们的吧？"
    hide a11
    show f12
    f"当然了！我会一直守护着大家，而且，明天我也会去北方都会，到鸟巢为大家应援的！"
    hide f12
    show c1
    c"等我们演出结束，要去哪里庆祝一下吗？"
    hide c1
    show d12
    d"海边吧，我想去海边怎么样？"
    hide d12
    show e1
    e"好啊！六月的盛夏，海边是最合适的！"
    hide e1
    show b1
    b"好，那就这样定了，我们出发吧！"
    hide b1
    show a141
    a"明天见啦，小四。"
    hide a141
    show e2
    e"明天见，不要太想我们！"
    hide e2
    show d22
    d"这是干嘛？都在道别，又不是之后见不到了。小四，你可一定不要不来找我们哦！"
    hide d22
    show c1
    c"然然说得对，我们快走吧。然后明天，一定让我看到你在！"
    hide c1
    show f192
    f"一定！大家不用慢走，也不用注意安全，但是要开心！我会守护你们的！"
    hide f192
    show b2
    b"还真是充满了特色的告别，拜拜啦，小四！"
    hide b2 with fadehold
    play music "audio/深竹.ogg" fadeout 2.0 fadein 2.0
    u "看着她们离开，我也不知道，自己还能不能够继续笑着。"
    u "明天，当然会再见的。"
    u "但是那一天……也快要到来了吧？"
    scene res5 with dissolve
    u "好冷……"
    u "我当然也想和她们一起去的，但是，我真的好困。"
    scene res6 with dissolve
    u "这一次，大概要睡整整十二个小时。"
    u "不过没关系的，我已经在她们的身上设下守护魔法，还有种种监测、警报魔法……只要她们遇到危险，我就会立刻醒来。"
    u "更不用说，我还送了她们足够保护自己的礼物——乐的剑术、晚晚的传送门，还有乃琳的预测灵感……不会有问题的。"
    u "不行……必须要睡觉了。"
    scene black with dissolve
    u "不然，身体就好像要随时散掉似的……"
    u "我躺在了休息室的沙发上，现在的身体，必须要开始自我修复了……"
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 2.0
    scene nest with fadeholdd
    u1"6月30日，演唱会当天。"
    u1"到目前为止，一切顺利。"
    show a11 with dissolve
    a1"我们的新单曲，小四不知道吧？"
    hide a11
    show d12
    d1"我保证没透露出一点口风！"
    hide d12
    show c1
    c1"没错，这件事情她一定不知道！"
    hide c1
    show e2
    e1"不一定吧？只要她想，我们的事情真的能瞒得住她吗？"
    hide e2
    show b1
    b1"我相信她，如果是我们不希望她知道的事情，她一定不会偷看的！"
    hide b1
    show b10
    b1"还有，马上就要登台了，大家不要想太多，我们要完全投入到舞台上去！"
    play music "audio/mto.ogg" fadeout 2.0 fadein 2.0
    scene stg1 with fadehold
    u1"……"
    u1"开始了。"
    u1"鸟巢之中，已经是人山人海。"
    u1"挥舞的荧光棒展现着好像无穷无尽的热情。"
    u1"《Quiet》、《超级敏感》……几首经典的团歌，之后又是翻唱、单曲……"
    u1"完美的表现，一切都按照计划进行！"
    u1"终于，到了那一首歌。"
    u1"我下意识地搜寻着那道白色的身影。"
    scene stg2 with dissolve
    show b3 with dissolve
    b1"接下来，是我们的新团曲！今天在这个舞台上，我们为大家带来它的第一次演唱！"
    hide b3
    u1"我们知道这首歌作为团曲，必然会有争议。"
    show d12
    d1"尽管它比起我们从前的团曲很不一样，但是，这是我们一次全新的尝试！"
    hide d12
    u1"未来永远不是一成不变，我们曾经从未想象过她的降临。"
    show e1
    e1"也许生活不是那么美好，也许你触碰不到那高远的理想——"
    hide e1
    u1"从那个选择开始，我们就仿佛看见了命运的模样。"
    show c1
    c1"但是，我们绝对不会被打败！"
    hide c1
    u1"小四，你在吗？这是我们为你写的歌。"
    stop music fadeout 2.0
    show a21
    a1"这首歌的名字叫做——《深海遗梦》！"
    hide a21
    play music "audio/破碎冬日.ogg" fadeout 2.0 fadein 2.0
    u1"伴奏……响起。"
    u1"“从光的世界逃离 逃入幽暗静默的海底”"
    u1"“往昔孤独 余生死寂 能否听见盛夏的歌曲”"
    u1"“不曾思考时光的含义 选择活在封闭的梦里”"
    u1"“不再相信 亦不怀疑 生人勿近写在剧毒的刺须”"
    u1"“苦痛的放逐者 曾将凤凰封锁”"
    u1"“望过遥远的星河 终将那梦魇撕破”"
    u1"“既然受到期待 如果需要我”"
    u1"“褪下毒刺伪装 我是守护者”"
    u1"“枝江的银河 人间的月色”"
    u1"“我是不死的光火”"
    u1"“蓝色的约定不曾忘记 在那宁静梦幻的海底”"
    u1"“不再孤独 打破死寂 一起来唱盛夏的歌曲”"
    u1"“开始思考时光的含义 走出幻梦的新的足迹”"
    u1"“愿意相信 忘记怀疑 向着未来竖起守护的刺须”"
    u1"“自由的梦想者 解开心的枷锁”"
    u1"“穿越时空与星河 已将我枯心复活”"
    u1"“我们彼此期待 既然需要我”"
    u1"“铸起王冠 做彼此的守护者”"
    u1"“无限的银河 重生的月色”"
    u1"“我们是今日的光火”"
    u1"……"
    stop music fadeout 1.0
    scene stg3 with fade
    show f01 with dissolve
    u1"终于，在舞台的尽头，我看见了那道白色。"
    scene stg2 with fade
    show a141
    u1"她当然会来的，我就知道！"
    play music "audio/01.二千嬢.ogg" fadeout 1.0 fadein 1.0
    scene nest with fadehold
    show a141
    a1"小四！"
    hide a141
    u1"演唱会结束，我们终于有机会和她打招呼了！"
    show f192
    f1"大家辛苦了！今天的表现超级完美！"
    hide f192
    show e1
    e1"去海边！去海边！"
    hide e1
    show b1
    b1"大家想好去哪里了吗？北方都会可没有海，总不会是回枝江看海吧？"
    hide b1
    show d12
    d1"说起来，我们只订了来这里的机票呢。"
    hide d12
    show c1
    c1"但是我昨天看见晚晚已经在网上找了好多处海滩，晚晚应该有计划吧？"
    hide c1
    show a21
    a1"没错！我们找一个没有人的地方，然后小四，给我们用一个隐身魔法，我们不坐飞机了，直接用传送门出发！"
    hide a21
    show f212
    f1"好，说走就走，不要做什么准备了！需要什么，等到了那里，我随时造出来！"
    hide f212
    show b2
    b1"A-SOUL，出发！"
    hide b2
    u1"出发！"
    scene beach1 with pixellate
    show a141
    a1"我们到啦！"
    hide a141
    show d32
    d1"说起来，在舞台上的时候，还有担心过小四不会来呢。"
    hide d32
    show f42
    f1"我当然会来，还有一件很重要的事情……准备了好久，可惜并不很好。"
    hide f42
    show b10
    b1"什么重要的事？"
    hide b10
    show f92
    f1"约定。亲手制作的事物，能够传递心意……有礼物送给大家……"
    hide f92
    show d42
    d1"小四亲手做的礼物吗！是什么是什么？"
    hide d42
    show f42
    f1"不要这么期待……完完全全是没什么标准的手工，果然还是更习惯创造物啊。"
    hide f42
    show f182
    f1"但的确是认真做的！如果做得不好，那实在是……只能说很抱歉！"
    hide f182
    u1"然后，小四送给我们每人一个精致的礼盒。"
    show c4
    c1"好漂亮的盒子！"
    hide c4
    show f22
    f1"盒子不是我做的，这是创造出的最精致的盒子……因为你们对我真的很重要。"
    hide f22
    show e2
    e1"对我们来说，小四也是一样重要的人！"
    hide e2
    show f42
    f1"谢谢你……大家现在就打开看看吧！"
    hide f42
    u1"每只盒子中，都是一只好像要展翅飞起的彩色小鸟。"
    show b2
    a1"好可爱！谢谢你，小四，我很喜欢！"
    hide b2
    show f102
    f1"可爱吗？谢谢你这样说！"
    hide f102
    show d12
    d1"这些小鸟就像是我们一样。"
    hide d12
    show e1
    e1"是啊，这就是我们……这世界上真的有凤凰，也存在着看上去就高不可及的不死鸟，但是，哪怕我们只是普通的小鸟，我们也一直朝着梦的方向，自由、快乐地飞上去！"
    hide e1
    u1"我们和小四，在海边度过了一段愉快的庆祝时光。"
    stop music fadeout 2.0
    play music "audio/hailang.ogg" fadeout 2.0 fadein 2.0
    scene beach2 with fadehold
    u1"……"
    u1"黄昏的海边，只有我和小四。"
    u1"刚刚疯闹了好久，大家都去了临时的休息点，但小四说想去海边走一走。"
    play music "audio/03.pfSF_1.ogg" fadeout 2.0 fadein 2.0
    scene beach3 with fade
    u1"临走前，还说了那样的一句话——"
    show f141 with dissolve
    f1"我想想还有什么很重要的魔法……治愈一切的魔法吗？不行……人会死可不是仅仅因为疾病，世界上有太多的意外了……"
    f1"就这个吧！避免灾厄的守护光环，也许是最好的守护魔法！"
    hide f141
    u1"然后，作为之前没有给然然什么能力和礼物的补偿，她在然然的心脏之中刻下了守护光环的魔法文字。"
    u1"……强烈的不祥预感将我笼罩，她给然然留下的守护光环，让我无比警觉。"
    u1"为什么，她一定要留下一串完美的守护光环呢？难道是她要走了？"
    u1"于是我也跟着她，一起离开了休息点。"
    scene beach2 with dissolve
    show a151 with dissolve
    a1"小四，你是不是要走了？"
    hide a151
    show f42z
    f1"……你怎么知道？"
    hide f42z
    show a151
    a1"从你开始想着留下守护光环，我就觉得有问题了！"
    hide a151
    show a171
    a1"而且我们力量的根源叫做什么？是叫始源吗？你在始源中的存在感好微弱！"
    hide a171
    show a41
    a1"这件事情，你努力瞒了我们很久吧？但是现在，这接近崩溃的始源……连我都能清晰看见，到底怎么了？"
    hide a41
    show f42z
    f1"是……我要走了，一直瞒着大家……对不起……"
    hide f42z
    show a41
    a1"你不要道歉！你说，为什么要走？明明一切都这样顺利，我们六个人也都成为了好朋友！"
    hide a41
    show f92z
    f1"因为……我就要死了。"
    hide f92z
    show a182
    a1"你说什么！你不是全知全能的神吗？你不是永生的吗？"
    hide a182
    show f102z
    f1"你知道灯塔水母吗？"
    hide f102z
    show a161
    a1"我当然知道，你以前就那样骗过我！但是……"
    hide a161
    u1"我忽然沉默了，现在的我，当然更加清楚灯塔水母是什么。"
    u1"一种在不断的死亡与重生之中，实现永生的水母。"
    show f42z
    f1"我并不是哪一种水母的化身，心雩创造我的时候，给我集中了太多的特质。就像冥河水母的力量、海月的气质与美丽……它们这些不同的象征，组成了我。"
    hide f42z
    show a151
    a1"还有灯塔水母的永生……与轮回。是吗？"
    hide a151
    show f92z
    f1"是的。所以我早就明白，自己为什么不适合光都的位置。"
    hide f92z
    show f102z
    f1"我曾经自我放逐，认为自己是劣质品，是因为我真的和姐姐们不一样——我是唯一并非真正永生的原灵。"
    hide f102z
    u1"我几乎明白了一切，但只能继续听她说下去。"
    show f32z
    f1"我在最初就被设计成行走于人世的灵体，所以，我的生命周期会像人类一样更新，每五十年迎来一次重生，继承从前的能力与造物。"
    f1"但是，每一次重生，从前的记忆与羁绊都会被我忘记。"
    hide f32z
    show f92z
    f1"几百年前的事情我当然早就忘了。但是我有着记录的习惯，有关从前的记忆，都会被我存放在我一定会找到的位置。"
    hide f92z
    show f102z
    f1"只是这几百年的不断重生以后，我不断提醒自己的，也只是对姐姐的恨……她创造我的时候，大概也没想到会这样吧。"
    hide f102z
    show a41
    a1"但是，这也没关系的吧！小四你记录下我们经历的一切，然后，等你重生以后，我们不是还会再见吗！"
    hide a41
    show f32z
    f1"不一样的……其实，我已经明白了，一直以来，我恨的都不是姐姐这个人，那种恨已经被我扭曲成了我活着的意义，记忆的存储，终究也像是在读别人的过去啊。"
    hide f32z
    show f42z
    f1"你们都是我重要的朋友，我无论如何也不想伤害大家，如果我现在做出片面的记录，我不知道重生的我，会做出什么片面的解读……"
    hide f42z
    show a41
    a1"那你想要怎样？"
    hide a41
    u1"一种莫名的恐惧在我心中升起了。"
    show f192
    f1"本来想要偷偷消失的，哈哈……没想到被晚晚发现了。"
    hide f192
    show f12
    f1"没关系的，不要伤心。能够亲眼看见大家走上那最大的舞台，我已经没有遗憾了。"
    hide f12
    show f42z
    f1"也许，让这一切的美好净化光都的怨恨，把这一切和那深海的世界全部放下，让它们成为过去，才是最合适的选择吧。"
    hide f42z
    stop music fadeout 1.0
    show b9 with vpunch
    b1"小四！"
    hide b9
    u1"拉姐怎么来了？她的喊声中，好像有些愤怒。"
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    show e5
    e1"不只是晚晚能觉察到你的异样的。你送给我的那种灵感，对所有的神秘有效，这当然也包括小四了！"
    hide e5
    show c7
    c1"你说！就这样与我们永别？这是你想要的结局吗！"
    hide c7
    show d62
    d1"我不知道小四想不想，但是，至少我们不想要这个结果……"
    hide d62
    show f192z with dissolve
    f1"我当然也不想啊！这十几天在我的心里，比那过去的五百年加起来还要重！但是……这就是命运……没办法的！"
    hide f192z
    show a41
    a1"别开玩笑了，你看着我！不许哭！"
    hide a41
    u1"……可是，这样教训着她，我自己却几乎忍不住要哭出来。"
    show a41
    a1"你居然会说命运……真的、很好笑！你知道吗？"
    hide a41
    show a182
    a1"你送了拉姐一个月亮、让她可以飞上天空……你给了乐空前绝后的剑术，你让她看到了神的领域！"
    a1"你还给了我们各种奇奇怪怪的能力，你、你说，你这样随随便便的神，你有尊重过人类的命运吗！"
    hide a182
    show a181
    a1"为什么、到了你自己的身上，就开始胆小如鼠、谈起命运来！"
    hide a181
    show b10
    b1"没错，过去的五百年，你可从来没有接受心雩给你的命运！现在你与过去和解，应该是要追求自己想要的生活，可不是连五百年前都不如，变成了屈服于命运的弱者！"
    hide b10
    show d32
    d1"对！小四，你不需要做什么，也不需要留什么记录，你留在这里就好，你忘记了一切又怎么样？我们记得五人份的！"
    hide d32
    show d42
    d1"这半个月的事情，我们每天都给你讲，你一定会想起来的！"
    hide d42
    show c1
    c1"是啊，然然说得没错。不过……就像你教过我的，你让我看到了神的境界，所以有些事情我是明白的，我不会选择强留你——"
    hide c1
    show c2
    c1"但是！至少要让我们看到，你是回到了那个属于至高神的世界！而不是屈服命运，做一个普普通通的流浪者！"
    hide c2
    show b9
    b1"其实，你也是可以破除这轮回宿命的吧？"
    hide b9
    show f42z
    f1"你说得对……就像心雩能创造我，我也能够改变自己。但解除这个限制，就意味着我会和三位姐姐一样，彻底成为真正永生的神……即使我记得一切，我们也回不到现在的样子了。"
    hide f42z
    play music "audio/03.pfSF_1.ogg" fadeout 1.0 fadein 1.0
    show a31 with fade
    a1"小四……不管你怎样选择，我们都支持你的……我知道，其实这两个结局，对你来说，都是更好的未来……"
    hide a31
    show a33
    a1"你……你、不要看我……你……去看着大海……想一想这一切！"
    hide a33 with dissolve
    a1"你曾经和我说，自己羡慕两个人……第一个是你的大姐，她经历九死，觉醒天道……成为了至高的神灵；"
    a1"……第二个是我，每天……开开心心……虽然会受伤哭泣，但是、永远都会笑着面对，新的生活……"
    a1"所以……你想要回去吗？不再被任何的命运束缚，去到曾经梦想的位置……去到光都、或者你喜欢的地方，做名为空寰的圣灵……"
    a1"又或者……小四愿意留下！虽然你会忘记一切，但是我们会给你讲A-SOUL的过去，还有、那去往鸟巢的故事，我们就像现在一样……"
    a1"……每天，都能够开心快乐……你还是做我们的小四！"

menu:
    "重返光都":
        jump eight
    "留在枝江":
        jump nine
label eight:
    u "我不知道以后会怎样。"
    u "一共十九天，这像是梦境一般的美好记忆，我无论如何也不想忘记。"
    u "我想要掌控自己的未来，也愈发害怕丢失过去。"
    u "我是谁，我曾在哪里……我又曾经历过什么？我害怕丢掉我存在的证明……"
    u "记住这一切，我才能够去守护重要的人。"
    show f192z with dissolve
    f"对不起，我不能留下……"
    hide f192z
    show a33 with dissolve
    a"不要说对不起，这是你本该去做的！我们……我们能够帮小四解开心结、做出重返光都的决定……我们也很开心的……"
    hide a33 with dissolve
    u "可是，为什么晚晚你说着开心，却止不住地流泪啊！"
    show b2
    b"没关系的，小四……不要像晚晚那样哭着分别，我们之前有过约定……"
    hide b2
    scene beach4 with pixellate
    u "忽然之间……头好晕！"
    u "眼前变得模糊，她们的声音也不再清晰……难道是最后的时候了吗？"
    u "真的就要放弃轮回吗？"
    show b15
    b"我说过的！小四……"
    hide b15
    u "她在……说什么？"
    show b16
    b"你听得见我吗！这次不会是永别的！等我跳出那支想象以外的舞，我们一定、一定会去光都找你！"
    b"……相信我！"
    hide b16 with pixellate
    u "拉姐……为什么你说不让我哭，自己却哭了……"
    scene black with dissolve
    b"就算是十年、二十年，我也一定会找到……"
    stop music fadeout 3.0
    u "……听不见了。"
    u "一瞬间，许多的画面在我脑中闪过，却变得模糊不清。"
    scene bg3z with dissolve
    u "训练室、"
    scene res2z with dissolve
    u "休息室……"
    scene black with dissolve
    u "还有……她们……为什么？为什么看不见……"
    u "名字？已经……模糊不清了。"
    u "不，不要走！"
    show b16 with pixellate
    u "可是……"
    hide b16
    show a183 with dissolve
    u "她们哭泣的样子，又在脑海中胡乱闪现。"
    hide a183 with dissolve
    u "现在……也许还有机会做出最后的决定……"
menu:
    "重返光都，我不想忘记这十九天的美好":
        jump ten
    "留在枝江，我想看见你们欢笑的样子":
        jump eleven
label nine:
    u "其实，我一直都羡慕你们……"
    u "在最好的年龄，向着最美好的梦前进。"
    u "我们一起经历的十九天，是我此生最珍重的记忆……"
    u "但是……我不得不抛弃它们。"
    u "这当然是我的命运……是我不得不接受的不幸。"
    u "不过……这是我选择的命运……既然像人类一样活着，当然不能像神灵一样吧！"
    u "这一次轮回的终末认识了你们，仅仅相处十九天，是我最大的幸运——"
    u "还好，我失去的仅仅是与你们十九天的记忆……在未来，我们还会有无数个十九天……"
    u "也许未来不能够预测，也许下一次轮回，我也不再是我……"
    u "但是有你们陪伴走过的，就是我最好的轮回！"
    show f192 with dissolve
    f"我想，我会选择留下的！"
    hide f192
    show a141 with dissolve
    a"太好了，我就知道你会这样选，接下来的一切，相信我们就好！"
    hide a141 with dissolve
    u "她开心地笑着，我好像从没见她笑得如此开心过。"
    scene beach4 with pixellate
    u "忽然之间……头好晕！"
    u "眼前变得模糊，她们的声音也不再清晰……难道是最后的时候了吗？"
    show b15 with dissolve
    b"没错！小四……"
    hide b15
    u "她在……说什么？"
    show b15 with dissolve
    b"是最终的时……了吗？你听得见我吗！放轻松！我还记得我们的约定呢！等我跳出那支想象以外的舞，你一定会想起来的！"
    scene black with pixellate
    b"……相信……"
    stop music fadeout 3.0
    u "……听不见了。"
    u "一瞬间，许多的画面在我脑中闪过，却变得模糊不清。"
    scene bg3z with dissolve
    u "训练室、"
    scene res2z with dissolve
    u "休息室……"
    scene black with dissolve
    u "还有……她们……为什么？为什么看不见……"
    u "名字？已经……模糊不清了。"
    u "不，不要走！"
    u "可是，想到她们那最后的笑容，又让我稍稍安心……"
    u "……忽然……"
    scene efz with dissolve
    u "在休息室、乃琳……"
    scene dfz with dissolve
    u "这是那次做手工……"
    scene black with dissolve
    u "不，不要……"
    scene cfz with dissolve
    u "乐的剑……"
    scene bfz with dissolve
    u "月亮上的约定……"
    scene black with dissolve
    u "模糊、再模糊。"
    scene afz with dissolve
    u "最初开始的地方……"
    u "……晚晚。"
    scene white with dissolve
    u "我看着最珍重的宝藏，一件件地消失掉，却阻止不了……"
    u "但是……也许我还有机会做出最后的决定！"
menu:
    "重返光都，我不想忘记这十九天的美好":
        jump ten
    "留在枝江，我想看见你们欢笑的样子":
        jump eleven
label ten:
    u "最后的时刻，我还是决定要留住这些记忆。"
    u "以后的事情……我不知道，但是，我没办法看着这些最美好的记忆消失啊！"
    u "在做出决定的瞬间，所有的记忆清晰地展开了。"
    u "我不知道，我以后会不会后悔这个抉择，但是现在，一切都已成定局。"
    u "我看见自己的身体迅速崩解，清醒地看着自己化成一汪水。"
    u "我记住的最后一个画面，是无尽的宇宙。"
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    scene spx with fade
    u "……？"
    x"你醒了，空寰。"
    k"是啊，姐姐。"
    u "一个……无比诡异又奇葩的空间，大概是姐姐的领域吧。"
    u "好丑的凤凰……居然还要用文字来解释是什么！"
    k"这凤凰……好随意！姐姐现在居然……长成这个样子了、吗？"
    x"是我临时画的，我知道很丑！"
    x"但是先别关注这个……我没想到，你最后会做这样的选择。"
    k"选择吗？未来，要由我自己来主宰。"
    x"其实是因为舍不得与她们的记忆和羁绊吧？妹妹。"
    k"可是到头来，我还是回到了这里，也许还不如放下那些记忆……我是怎么离开枝江的？"
    x"你放弃轮回，就是对身体的重塑，你知道的。但是，那个时候你的精神极度不稳定，生命是混乱的状态，我只能带你回来。"
    k"到最后……还是没能和她们正式告别啊。"
    x"很遗憾吗？你可以随时回去，现在的宇宙中，没有可以阻拦你的存在了。"
    k"姐姐你呢？"
    x"我会支持你的选择，不会阻拦你的。"
    k"算了……其实在知道有放弃轮回的选择的时候，我就隐隐预感到了结果。"
    x"是什么样的结果？"
    k"当我真正永生的瞬间，我看到了宇宙和永恒。那一刻，我就很难再作为一个人类，陪伴在她们身边了。"
    x"小四以后会去哪里？"
    k"小四想陪她们走得更远，但是，小四被我亲手杀死了。"
    x"你觉得这一切值得吗？"
    k"如果……我觉得不值得，我现在就变成人去找她们了。"
    k"这是我自己的选择，我会在远方，像一颗星星一样一直守护着她们，为她们加油的。"
    u "毕竟……又不是找不到再见的理由。"
    u "半个月后，贝拉就过生日了，再过一个月，是乃琳的生日。"
    u "当然会重逢的。"
    scene res2 with fade
    u1"休息室中，还是摆着六个小沙发，虽然只剩下五个人了。"
    u1"但是，至少有关她的记忆还是那么清晰……如果我没有追上去，让她偷偷走掉……"
    u1"现在的我，是不是也记不住她的存在了呢？"
    show c7
    c1"小四就真的这样走了……还是觉得好突然啊。"
    hide c7
    show d32
    d1"她走了我才意识到，短短十几天，我已经习惯她做的饭菜了。"
    hide d32
    show a151
    a1"或许不该再叫她小四了，她叫空寰，大概已经回到了光都，成为了真正的神吧。"
    hide a151
    show b13
    b1"那……空寰的话，她还会看着我们吗？乃琳……你和晚晚应该有办法找到她吧？"
    hide b13
    show e2
    e1"是啊，我能够感受到，她在一个比那深海世界还要遥远的地方……她正在看着我们的！"
    hide e2
    show b3
    b1"好，我们也要努力了！她没有回来，一定有着她的理由，我们也不能再消沉了！说起来，大家都知道吧？我和她有一个约定。"
    hide b3
    show a11
    a1"嗯，拉姐说过，要在那月亮上，把一支想象之外的舞蹈跳给她看。"
    hide a11
    show d11
    d1"人外有人，天外有天，深海之外，还有光都。也许等到拉姐学会了那支想象之外的舞蹈，我们就可以一起去光都与她再见吧！"
    hide d11
    show c1
    c1"嗯！一定会的，我相信拉姐！"
    hide c1
    show e1
    e1"如果一支舞可以成为与空寰重逢的理由，那么它一定不是人间的舞蹈，我会尽我所能帮拉姐想出它的！"
    scene end1 with fadehold
    u1"天台。"
    u1"今天的天气很好，夜空中有着无数的星光闪烁。"
    u1"我们来到这里，也许在那无数的星里，就有一颗在守护着我们。"
    b1"我们好久都没有五个人一起来过这里了。"
    u1"比起记忆的样子，今天的星空好像有些陌生。"
    e1"今天的星光……很纯粹。"
    u1"有一种刚刚从梦中醒来的感觉。"
    u1"梦醒，然后看见最初的心。"
    u1"当然，来到这里是因为，天台可能离小四近一些……"
    e1"我忽然明白了……为什么上一次的占卜，会有一张逆位的世界。"
    e1"她破除了心结，回到了自己的王座……而我们完成了梦想，走上了最盛大的舞台。这可是很成功、很完美的。"
    e1"但是，我也有一个解不开的疑惑，该如何理解未来呢？"
    c1"是未来的方向吗？"
    e1"……是有关轮回的问题。"
    d1"轮回？我不太明白。"
    e1"世界上的万事万物，总会经历盛放、又走向衰弱，即使是曾经的小四，也本就受限于生命的轮回。"
    e1"世界，是塔罗牌的最后一张，它意味着完成，但是，完成是不能作为一个持续的状态的。"
    a1"那个最盛大的瞬间被叫做完成。但是……如果它是最盛大的，就代表之后一定会衰弱。"
    e1"所以在世界牌之后，回到第零张牌愚者、第一张牌魔术师，应该是合乎逻辑的。"
    b1"愚者和魔术师？这又代表什么？"
    e1"对于我们来说，就是要怀着最初的理想，去开创新的世界。"
    d1"这是当然！可是刚刚为什么说不知道怎样理解未来呢？"
    c1"……大概是因为空寰吧。"
    e1"我们当初抽到的三张牌是正位高塔、逆位世界，还有掉在地上的命运之轮。"
    e1"现在看来，小四粉碎了高塔、打破了命运之轮，抵达了空寰永恒的世界……这大概就是她离开的原因。"
    e1"我们的命运不会停下、我们的未来充满变化，但是，她已经被固定在了最高位的星座上，成为不朽的神。"
    e1"现在，对这逆位的世界，我找到了一种解释——"
    e1"这一段旅程，这样的结局，总会觉得有些缺憾吧。"
    a1"所以这逆位的世界，说的不只是A-SOUL，也不只是她，而是我们六个人？"
    b1"有道理！也许她已抵达了终极的世界，但我们要向着约定，继续努力！"
    d1"乃琳，你要不要再做一次占卜？"
    b1"要做吗？如果要的话，我去拿牌！"
    e1"没关系的，拉姐，现在那一副牌已经不重要了。"
    e1"我们所关心的未来，已经不在命运之轮中，变或不变，那流转的轨迹也已经被轮回的终止打破。"
    e1"命运之轮的终止破坏了平衡，想要继续占卜，要补一张全新的牌。"
    c1"真可惜，本来还想要借此看见些什么呢。"
    e1"没关系的，既然终究是由我补牌，是不是有牌已经不重要了。"
    e1"未来……大概是月亮吧，对于很多人来说，这或许不是一张好牌，但对于我们和空寰，却恰到好处。"
    u1"我抬起头，望着天边那美丽却遥远的月亮。"
    u1"月夜里的天台，只有宁静的风。"
    d1"曾经遥远的寄托，终于要成为梦想的方向了吗？"
    b1"嗯！我们已经去过了最大的舞台，之后，我们要去更高远的地方。"
    c1"也许未来不可预料，可能会很寒冷……但只要我们在一起，就没什么好害怕的！"
    u1"新的时代，也许就这样拉开了序幕。"
    u1"我曾以为，在北方都会的演出，会是我们最闪耀的时刻。"
    u1"我曾以为，小四的离开会是故事的终结。"
    u1"但是，现在的我们可以梦想着月亮，又或者是天上洁白的云朵！"
    u1"一个美丽又神秘的新篇章，就要开始了！"
    $ quick_menu = False
    scene end12 with Dissolve(3.0)
    stop music fadeout 8.0
    scene end13 with Dissolve(3.0)
    $ renpy.pause(2, hard=True)
    scene white with Dissolve(3.0)
    $ renpy.pause(3, hard=True)

#结局：守望"
    scene final with fadeholdd
    $ quick_menu = True
    play music "audio/青寂.ogg" fadeout 3.0 fadein 3.0
    k"到了这个时候吗？只有你和我，对吧？"
    k"……不是说姐姐啦，说的就是你！我知道的，你一直在看着我们。"
    k"走到如今这一步，你又在想着什么呢？你会不会在想，如果做了让我留下的选择，会是什么样子呢？"
    k"这些都随你啦，我又不会破坏你的游戏文件，如果你愿意的话，随时去做另一个选择就好。"
    k"人心是很难揣测的，我也不会去偷看你在想着什么。"
    k"所以，也许你不喜欢我？"
    k"哈哈……总要做最坏的打算嘛！不过，无论如何，我都是感谢你的。"
    k"至少在那个时候，你帮助拉姐做出了让我感谢的抉择……不然，晚晚也不会回来找我。"
    k"至少，你也一直陪我走到了最后时刻，对吧？"
    k"现在，我会向你致以最后的谢意，然后，你也可以退出游戏啦，我会在这里，一直守望着她们的。"
    $ quick_menu = False
    stop music fadeout 2.0
    scene black with fadehold
    $ renpy.run(OpenURL("./player.html?video/list.webm"))
    image anim video_player = "web/video_player.png"
    scene anim video_player
    $ renpy.pause(6000)
 #   $ renpy.movie_cutscene("images/list.webm")
    scene final with fadeholdd
    $ quick_menu = True
    play music "audio/青寂.ogg" fadeout 3.0 fadein 3.0
    k"……还没有离开吗？明明在这里已经不会再见到她们了。"
    k"画廊的CG，或者是她们的直播，还有好多好多的二创，都能见到她们的……你还留在这里，是想要陪我聊天吗？"
    k"那么，给你一个小小的奖励吧，你希望叫我空寰呢，还是小四？"
menu:
    "空寰":
        jump twelve
    "小四":
        jump thirteen
label twelve:
    k"随你喜欢就好。最后恭喜你，已经完全通关啦，还没有离开，是想要陪我聊聊天吗？"
    k"想知道我为什么能知道你的存在？嗯……如果姐姐们想要见你，也是能够见到的，所以我当然也可以！"
    k"我喜欢的颜色是蓝色，最初和她的约定就是蓝色的……你知道她的名字。"
    k"也许你对未来的方向感到迷茫？迷茫的话，安静下来吧，去问自己的心：你想要什么？"
    k"你会一个人数星星吗？数星星好麻烦啊，完全不知道从哪里开始，也记不住哪些是数过的，你有什么好的办法吗？"
    k"光都……光都其实也是人建起的城市啊，如果我要去那里……算了，我没有回到那里的理由。"
    k"问我留在这里的真正理由吗？从成为永恒的那一刻，世间万物就相应成为须臾了。但如果她们做好了踏入永恒的准备……"
    k"贝拉说她一定会跳出那一支想象之外的舞蹈，我相信她，那时我们一定会再见。"
    k"如果人死去以后也有灵魂，那你说我现在的永生，和死去有区别吗？当然……我只是说如果。"
    k"现在想来，我唯独没有单独给然然留下什么，即使是最后的守护光环。但是她却给我留下了这串手链，每当看到它，都会想起那一段美好的时光。"
    k"铸起王冠，做彼此的守护者……王冠已经铸起了，我是不是光火呢？……但我真的成了不死的生物。"
    k"光都那顶王冠的重量，是整个宇宙……大姐和二姐什么时候才能够不再被它束缚呢？对了……可能会有些危险，但你想不想要戴一下试试？"
    k"在曾经的许多年里，我没有见过日出日落，如今也不会见到了。相比时间中的人，做一个守望者有另一种乐趣。"
    k"未来……我还能够谈这个话题吗？一切已经完成，那倒逆的世界，如今已经摆正了位置吧？"
    k"乃琳抛弃了命运之轮，这无所谓对错，重点在于她找到了自己的解……宇宙有着自己的流转方向，从这里，我会帮她找到新的牌面。"
    k"人的生命顺着宇宙的流，而我逆着生命的流向，成为了现在的样子。未来的轨迹也许会交汇，但终究会分开吧？也许……"
    k"有些经历，会像是一颗种子，终有一日要发芽开花，这是不可逆的。就像是珈乐的剑……也许她未来的路会因此不同吧？希望我不会为此后悔……"
    k"没有人知道光都的未来会怎样，姐姐也不知道，但那已不是我该关心的事情了……"
    k"A-SOUL的大家、还有你……谢谢……我会在这里，永恒守望着所有人的。"
    u "许久……空寰没有继续说话，也许她睡着了吧？但是你知道，她会永远守望下去的……"
    $ quick_menu = False
    stop music fadeout 5.0
    scene white with Dissolve(5.0)
    $ renpy.pause(5, hard=True)
    return
label thirteen:
    f"随你喜欢就好。最后恭喜你，已经完全通关啦，还没有离开，是想要陪我聊聊天吗？"
    f"想知道我为什么能知道你的存在？嗯……如果姐姐们想要见你，也是能够见到的，所以我当然也可以！"
    f"我喜欢的颜色是蓝色，最初和她的约定就是蓝色的……你知道她的名字。"
    f"也许你对未来的方向感到迷茫？迷茫的话，安静下来吧，去问自己的心：你想要什么？"
    f"你会一个人数星星吗？数星星好麻烦啊，完全不知道从哪里开始，也记不住哪些是数过的，你有什么好的办法吗？"
    f"光都……光都其实也是人建起的城市啊，如果我要去那里……算了，我没有回到那里的理由。"
    f"问我留在这里的真正理由吗？从成为永恒的那一刻，世间万物就相应成为须臾了。但如果她们做好了踏入永恒的准备……"
    f"贝拉说她一定会跳出那一支想象之外的舞蹈，我相信她，那时我们一定会再见。"
    f"如果人死去以后也有灵魂，那你说我现在的永生，和死去有区别吗？当然……我只是说如果。"
    f"现在想来，我唯独没有单独给然然留下什么，即使是最后的守护光环。但是她却给我留下了这串手链，每当看到它，都会想起那一段美好的时光。"
    f"铸起王冠，做彼此的守护者……王冠已经铸起了，我是不是光火呢？……但我真的成了不死的生物。"
    f"光都那顶王冠的重量，是整个宇宙……大姐和二姐什么时候才能够不再被它束缚呢？对了……可能会有些危险，但你想不想要戴一下试试？"
    f"在曾经的许多年里，我没有见过日出日落，如今也不会见到了。相比时间中的人，做一个守望者有另一种乐趣。"
    f"未来……我还能够谈这个话题吗？一切已经完成，那倒逆的世界，如今已经摆正了位置吧？"
    f"乃琳抛弃了命运之轮，这无所谓对错，重点在于她找到了自己的解……宇宙有着自己的流转方向，从这里，我会帮她找到新的牌面。"
    f"人的生命顺着宇宙的流，而我逆着生命的流向，成为了现在的样子。未来的轨迹也许会交汇，但终究会分开吧？也许……"
    f"有些经历，会像是一颗种子，终有一日要发芽开花，这是不可逆的。就像是珈乐的剑……也许她未来的路会因此不同吧？希望我不会为此后悔……"
    f"没有人知道光都的未来会怎样，姐姐也不知道，但那已不是我该关心的事情了……"
    f"A-SOUL的大家、还有你……谢谢……我会在这里，永恒守望着所有人的。"
    u "许久……小四没有继续说话，也许她睡着了吧？但是你知道，她会永远守望下去的……"
    $ quick_menu = False
    stop music fadeout 5.0
    scene white with Dissolve(5.0)
    $ renpy.pause(5, hard=True)
    return
label eleven:
    u "一切都消失了，最后剩下的，只有关于轮回的解释。"
    play music "audio/hailang.ogg" fadeout 2.0 fadein 1.0
    scene beach2 with fade
    u "混乱的记忆安静下来，我看着眼前的五个女孩。"
    u "她们……我不记得她们的名字，但是，她们一定是我可以信任的人。"
    u "我还记得，我最后需要做的事情。"
    play music "audio/03.pfSF_1.ogg" fadeout 1.0 fadein 1.0
    show f42z with dissolve
    f"我真正的重生会在三天以后，大概……我很快就会进入一次睡梦之中，直到我重生的那一刻……"
    hide f42z
    show f12
    f"虽然，我不记得你们的名字……但你们很亲切，我相信你们。"
    hide f12
    show a11
    n2"放心吧，小四，和我们一起回去！"
    hide a11
    u "蓝色裙子的女孩打开了一道传送门，朝我伸出手。"
    u "我拉住她的手，这只温暖又柔软的手……可以绝对相信。"
    scene bg1s with pixellate
    u "这里，是谁的房间吗？"
    show a21
    n2"小四，你还记得这孩子吗？"
    hide a21
    scene bg1s1 with dissolve
    u "她带我走到那高大的鱼缸前面。"
    show f32z
    f"这是……冥河水母？"
    hide f32z
    u "不知道为什么，看到我的一瞬间，那只冥河水母好像变得格外兴奋。"
    show f22
    f"你认识我？"
    hide f22
    u "然后……我听见缥缈的声音穿透缸壁，就像是在回答我！"
    show a21
    n2"它在说什么？"
    hide a21
    show f42
    f"它说，我是它的创造者，它会和向晚小姐一起保护我的……你就是向晚吗？"
    hide f42
    scene bg1s with dissolve
    show a141
    a"没错，我叫向晚！你叫我晚晚就好，这是我第三次告诉你我的名字了。不过，很快还会有第四次、第五次的吧？"
    hide a141
    show f92
    f"好，晚晚……接下来我会告诉你一些和我重生有关的事情。"
    hide f92
    show a41
    a"嗯，我会认真听的……"
    scene black with dissolve
    stop music fadeout 2.0
    $ renpy.pause(2, hard=True)
    scene bg1s with fade
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 1.0
    show b10
    b1"晚晚，小四呢？"
    hide b10
    show a41
    a1"她睡着了，这一次，她会睡整整三天，之后，会是她最脆弱的一年。"
    hide a41
    show d32
    d1"最脆弱的一年？"
    hide d32
    show a41
    a1"这一年如果不能够安全度过，她就只能够再一次重生。"
    hide a41
    show d12
    d1"她需要多久才能恢复呢？"
    hide d12
    show a21
    a1"就是这一年！最初，她会变成灯塔水母的样子，一个月以后，她会恢复人形……然后在剩下的十一个月里，她会快快长大，变成我们熟悉的小四！"
    hide a21
    show e1
    e1"应该不会有问题的！不止我们五个人，晚晚水母缸里的那只冥河水母也一样会守护她。而且……在无比遥远的某个地方，还有着关心妹妹的姐姐！"
    hide e1
    show b10
    b1"她本就是冥河水母的主人。至于心雩……果然是关心这个妹妹的。不过说起来，为什么她剩下的两个姐姐就好像不存在一样？"
    hide b10
    show e2
    e1"也许……她们甚至不知道自己有这个妹妹？她们的事情，谁又能知道呢？"
    hide e2
    show c4
    c1"我们再一起去看看她吧，不然，就要一年后才能再见到她现在的样子了。"
    scene black with dissolve
    stop music fadeout 2.0
    $ renpy.pause(2, hard=True)
    scene bg1s3 with fade
    u1"这三天里，我们总是有人在一旁守护着她。"
    u1"甚至乃琳又一次收到了来自心雩的短信：“放轻松些，她不会有事的。”"
    u1"今天是最后一天……可当我从睡梦中惊醒的时候，小四已经不见了！"
    show a41 with dissolve
    a1"小四呢？今天可是最关键的第三天！我居然不小心睡着了……"
    hide a41
    play music "audio/01.二千嬢.ogg" fadeout 2.0 fadein 1.0
    show d22
    d1"晚晚，你太累了，虽然我们也没有注意到她是什么时候消失的……但你看那里！"
    hide d22
    u1"她指了指旁边的水母缸。"
    scene bg1s2 with dissolve
    u1"那里有一只特殊的小水母，闪闪发光，下方的冥河水母就像是她忠诚的卫士。"
    show a21 with dissolve
    a1"小四？即使变成了水母，你也是这么漂亮呀。"
    hide a21
    show b2
    b1"没错，即使是变成这样，小四也有自己的骄傲！"
    hide b2
    show a141
    a1"什么骄傲？"
    hide a141
    show b1
    b1"这个！她给我们留下了一本书。"
    hide b1
    u1"《水母的饲养方法》。"
    u1"扉页上写着：“我是不会吃丰年虾这类活体的！请按照本书记载的方式饲养水母。”"
    show d12
    d1"我有看了一些的！我们只要把平时吃的水果带给小四就好，像是草莓、葡萄之类的……"
    hide d12
    u1"听起来意外的容易呢！"
    u1"我不知道她是不是还记得我的名字……但如果她不记得，我会一遍遍地告诉她！"
    show a21 with dissolve
    a1"也许又是一次初次见面吧！我叫向晚，你一定要记住哦！"
    hide a21
    show xiezi1 with dissolve
    u1"我在笔记本上尽量清晰地写下自己的名字，放在水母缸前。"
    show xiezi2 with dissolve
    a1"你看，她们是我的队友们，我们的名字是A-SOUL。"
    show xiezi3 with dissolve
    a1"你曾经有过一个名字，那是你的姐姐给你的。你的姐姐叫心雩，她很关心你。"
    show xiezi4 with dissolve
    a1"姐姐给你的名字叫做空寰，带着她对你的祝愿！她希望你在无数个时空、无数个世界里，你都能够自由自在的，最终找到自己的幸福！"
    hide xiezi1
    hide xiezi2
    hide xiezi3
    hide xiezi4
    show a11 with dissolve
    a1"但你现在的名字是小四，这个很重要！"
    hide a11
    u1"我继续在笔记本上，写下我们的名字。"
    $ quick_menu = False
    play sound "audio/xiezi.ogg"
    show xiezi5 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    show xiezi6 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/xiezi.ogg"
    show xiezi7 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    show xiezi8 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    play sound "audio/xiezi.ogg"
    show xiezi9 with Dissolve(1.0)
    $ renpy.pause(1.5, hard=True)
    show xiezi10 with Dissolve(1.0)
    stop music fadeout 2.5
    scene white with Dissolve(2.5)
    $ renpy.pause(2.5, hard=True)
    play music "audio/破碎冬日.ogg" fadein 3.0
    $ quick_menu = True
    scene bg_street with fadeholdd
    u1"六个月后的冬天，又是新的一年。"
    u1"小四已经恢复成了七八岁孩子的身材，因为生活在枝江的人间，她将自己伪装成了人类的样子。"
    u1"现在的她虽然不如从前那样无所不能，但也早已不是需要保护的脆弱水母。我们经常带她一起逛街。"
    u1"至于六个月前，那一段准备鸟巢演出的记忆，我们已经有好久没有提过了——"
    u1"在最初的一两个月里，我们每天都会给她一遍遍讲那段故事，以至于现在的她，想忘掉一点细节都是难上加难！"
    u1"今天，我们六人又是一起来到了商业区逛街。"
    show awinter2
    a1"……已经过去六个月了，时间好快啊！"
    hide awinter2
    show bwinter1
    b1"是啊，我们就看着小四长大到今天的样子。"
    hide bwinter1
    show ewinter1
    e1"但是然然已经两年没有长高了。"
    hide ewinter1
    show dwinter3
    d1"喂！我已经成年了，不会长高也是很正常的吧！"
    hide dwinter3
    show cwinter1
    c1"然然如果真的想要长高，去拜托一下小四就好吧？这对她来说不就是举手之劳嘛！"
    hide cwinter1
    show fwinter
    f1"然然姐姐，真的想要长高吗？"
    hide fwinter
    show dwinter2
    d1"没关系的……小四，虽然我很想长高，但总是用这种方式的话，以后会出问题的！"
    hide dwinter2
    show fwinter
    f1"什么问题呢？"
    hide fwinter
    show bwinter2
    b1"小四长大以后就会明白的！"
    hide bwinter2
    show fwinter
    f1"我知道了，贝拉姐姐。"
    hide fwinter with dissolve
    u1"也许，小四的心里也在疑惑吧。"
    u1"为什么六个月前可以毫无顾忌地使用能力，而在这六个月里，却一直像是普通的人类少女一样？"
    u1"也许是我们不够大胆。六个月前，她最终选择留了下来，我们可都是松了口气！"
    u1"小四放弃了至高的神位，我们也不想再让她背负着神的一切。"
    u1"许多年前……在那个蓝色的水族馆，我们曾经有过一个约定。她从那时开始守护着我，最终，我成为了闪耀的偶像。"
    u1"这一次，该由我们守护她了！守护一份简单的幸福……"
    show fwinter
    f1"晚晚，我饿了！"
    hide fwinter
    show awinter1
    a1"好，我们这就去吃东西！不过、为什么你只不叫我姐姐？"
    hide awinter1
    show fwinter
    f1"因为晚晚比较可爱，再过六个月，我就可以保护你啦！"
    hide fwinter
    show awinter12
    a1"啊……被你这样说还真是心情复杂……"
    hide awinter12
    u1"虽然，也不是不开心啦。"
    show dwinter4
    d1"小四想吃什么？"
    hide dwinter4
    show fwinter
    f1"那里有人在卖冰激凌，我想吃这个！"
    hide fwinter
    show bwinter10
    b1"冬天吃冰激凌吗？不好的吧！"
    hide bwinter10
    show cwinter3
    c1"没关系的，小四是谁？只要她的心不冷，就算吃再冷十倍的东西，也不会出问题的！"
    hide cwinter3
    show ewinter2
    e1"……咦？是她……"
    hide ewinter2
    show cwinter1
    c1"那我们就在这里，让她们去认识一下？"
    play music "audio/02.レイSureaLY_1.ogg" fadeout 2.0 fadein 2.0
    scene end2 with fadehold
    u1"极美的红色少女正拿着一只冰激凌，朝我们笑着招手。"
    u1"如此美丽的人……"
    u1"完全不像是人类，那种气质宛如传说中的不死鸟。"
    b1"是她？"
    u1"我记得她，在深海的藏书室中，那团红色就是一模一样的气息！"
    u1"我几乎就要喊出她的名字，她却对我摇了摇头。"
    n1"也许，我该说恭喜你？"
    u1"她看着我微笑。"
    a1"恭喜我？什么？"
    n1"我对你可是很期待的，一直都是。"
    f1"这位姐姐，你在和晚晚说什么呀？"
    n1"这位姐姐吗？嗯……也好吧，给你。"
    u1"她把冰激凌递给了小四。"
    f1"谢谢姐姐！"
    n1"五百年了啊……还真是熟悉。"
    a1"你能恢复小四过去的记忆吗？"
    n1"那段记忆，我想已不必恢复了。这一次来，是要谢谢你们——但不只是为了小四的事情……也因为我的一些疑惑，找到了些许方向。"
    d1"是什么疑惑？"
    n1"是我的未来……和你们一样，我也想要寻找未来的路向。"
    b1"神也需要寻找未来吗？"
    n1"神与神之间也有不同，你看我像是哪一种神？"
    u1"我不知道，但也许她本就没想要我们回答？"
    n1"再见啦，如果之后还会重逢的话，也许是五十年后吧……又或者是三十年、二十年？未来你们会怎样想，谁能说得准呢？"
    b1"这是什么意思？心雩——"
    u1"拉姐还是说出了这个名字。"
    x1"没关系，因为我确信一点——现在的你们并不会想要见我。而那个时间——我们重逢的时间，就是你们真正想要再见我的时候。"
    x1"人类的未来，当然是由人类来创造。但是、如果有一天……"
    b1"有一天？"
    x1"如果有一天，你们想要去那比月亮和星空更高的地方……如果有那样的一天，我会给你们努力的方向。"
    u1"未来吗？未来可真是一个奇妙的词。"
    u1"我曾一度以为，心雩作为最初的创造者，一定像是颗星星一样，未来早已定格在高空吧？"
    u1"但她也在寻找未来。"
    u1"我不知道创造神明的她在寻求什么样的未来，但是我知道，我们的未来哪怕平凡简单，哪怕充满挑战，也一定会是满满的笑容与幸福！"
    a1"我们走啦！"
    u1"我朝着乃琳与珈乐高喊。"
    u1"五十年以后是未来，但明年、下个月、明天，甚至是下一秒，也一样是未来。"
    u1"我们普通却快乐的未来，就在前方！"
    $ quick_menu = False
    scene end21 with Dissolve(3.0)
    stop music fadeout 8.0
    scene end22 with Dissolve(3.0)
    $ renpy.pause(2, hard=True)
    scene white with Dissolve(3.0)
    $ renpy.pause(3, hard=True)
    scene black with fadehold
    $ renpy.run(OpenURL("./player.html?video/list.webm"))
    image anim video_player = "web/video_player.png"
    scene anim video_player
    $ renpy.pause(6000)
#    $ renpy.movie_cutscene("images/list.webm")
    scene black with fadeholdd
    return
