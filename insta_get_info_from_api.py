import telebot,requests,threading
# مرحبا اخوتي البوت متاح للرفع على الانترنت
# ويعمل مع عدد كبير في وقت واحد بدون اي مشاكل
# المطور بارون قناتنا  @adowat
#يمكنك تعديل الرسائل لتناسبك
took="التوكن هنا فقط";bot = telebot.TeleBot(took)
@bot.message_handler(func=lambda m :True) # ردودك
def rm(m):
    def get_thinfo(usr):
        form={}
        try:
            url=f"https://www.instagram.com/{usr}/?__a=1"
            dwtl=requests.get(url).json()
            fullnam_e=dwtl['graphql']['user']['full_name']
            if fullnam_e=="":
                fullnam_e="لايوجد"
            bot.send_message(m.chat.id,"الاسم :"+str(fullnam_e))
            usernam_e=dwtl['graphql']['user']['username']
            if usernam_e=="":
                usernam_e="لايوجد"
            bot.send_message(m.chat.id,"اليوزر :"+str(usernam_e))

            userbi_o=dwtl['graphql']['user']['biography']
            if userbi_o=="":
                userbi_o="لايوجد"
            bot.send_message(m.chat.id,"البايو :"+str(userbi_o))

            account_pravte=dwtl['graphql']['user']['blocked_by_viewer'] #حساب خاص او لا 
            if account_pravte=="":
                account_pravte="لايوجد"
            elif account_pravte=="True":
                account_pravte="خاص"
            else:
                account_pravte="عام"
            bot.send_message(m.chat.id,"نوع الحساب :"+str(account_pravte))
            followers=dwtl['graphql']['user']['edge_followed_by']['count'] # عدد متابعين الحساب
            if followers=="":
                followers="لايوجد"
            bot.send_message(m.chat.id,"عدد متابعينه :"+str(followers))
            following=dwtl['graphql']['user']['edge_follow']['count'] # عدد الذين يتابعهم
            if following=="":
                following="لايوجد"
            bot.send_message(m.chat.id,"عدد الي يتابعهم :"+str(following))

            facebook_id=dwtl['graphql']['user']['fbid']
            if facebook_id=="":
                facebook_id="لايوجد"
            bot.send_message(m.chat.id," ايدي الفيسبوك :"+str(facebook_id))

            

            reels=dwtl['graphql']['user']['highlight_reel_count'] # عدد مقاطع الريلز
            if reels=="":
                reels="لايوجد"
            bot.send_message(m.chat.id,"مقاطع الريلز:"+str(reels))

            id_ac=dwtl['graphql']['user']['id'] #  ايدي الحساب المطلوب
            if id_ac=="":
                id_ac="لايوجد"
            bot.send_message(m.chat.id,"ايدي الانستا :"+str(id_ac))

            pic_url=dwtl['graphql']['user']['profile_pic_url_hd'] #  رابط الصورة
            if pic_url=="":
                pic_url="لايوجد"
            bot.send_message(m.chat.id,"الصورة:"+str(pic_url))
        except:
            form="s"
            bot.send_message(m.chat.id,"user name is viald")
    T = threading.Thread(target=get_thinfo, args=(m.text,))
    T.daemon = True
    T.start()
bot.infinity_polling()
#@adowat