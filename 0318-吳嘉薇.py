def dead():
	print("nick")
	quit()


def start():
	print("你是個很有愛心的高中生,參加了慈善的動物基金協會計畫。\n某日,基金協會老師邀請你到南下參加照顧動物四日的活動。")
	x = input("請問你決定拒絕老師還是答應參加?\n(1)答應老師\n(2)拒絕老師")
	if x =="1":
		print("走吧")
		day2()
	elif x =="2":
	    print("拒絕老師")
	    print("遊戲結束")


def day2():
	print("到了目的地,你看到的不是可愛動物,而是科學家們用來實驗的的動物變成的不明生物。\n覺得很奇怪的問老師,老師卻陰險的說這些都是我們在政府的批准下秘密實行的動物實驗")
	b = input("當你覺得事情不對時請問你選擇馬上逃離還是靜觀其變?\n(1)馬上逃離\n(2)拿起手機拍攝")
	if b =="1":
		print("逃了很久 才發現找不到出口")
		day3()
	elif b =="2":
		print("被老師拿走手機,還好逃走了差點被被殺")
		day3()


def day3():
    print("出口找不到了陷入了絕望,看了看四周,發現了地上有保命的武器")
    c = input("你想選擇什麼保命武器?\n(1)斧頭\n(2)平底鍋\n(3)球棒")
    if c =="1":
        print("攻擊,輔助")
        day4()
    elif c =="2":
        print("使人擊暈,煮個菜,擋子彈")
        day4()
    elif c =="3":  
        print("輕便好帶")
        day4()


def day4():
    print("你聽到了老師及神秘人士的對話,說這次的動物實驗只是個開頭,這次他們需要的是人類")
    print("老師說:這就是為什麼我帶我的學生來的目的")
    d = input("請問我該怎麼辦?\n(1)阻止他們\n(2)躲起來\n(3)未完待續")
    if d =="1":
        print("自投羅網")
    elif d =="2":
        print("餓死")
    elif d =="3":
        print("期待") 

     


start()