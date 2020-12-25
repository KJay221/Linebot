from transitions.extensions import GraphMachine

from utils import send_text_message, send_flex_message, send_image_message

import flex_message
import other_function

index=""
index_chart_range=""

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_begin(self, event):
        text = event.message.text
        if text.lower() == "start" or text == "返回功能選單":
            return True
        else:
            return False

    def on_enter_begin(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"begin",flex_message.begin)

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text == "fsm圖"

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        link = other_function.show_fsm_link()
        send_image_message(reply_token,link)

    def is_going_to_start(self, event):
        text = event.message.text
        if text == "開始使用" or text == "回主選單":
            return True
        else:
            return False

    def on_enter_start(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"start",flex_message.start)

    def is_going_to_index(self, event):
        text = event.message.text
        if text == "指數查詢" or text == "回指數選擇":
            return True
        else:
            return False

    def on_enter_index(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"指數查詢",flex_message.index)

    def is_going_to_USA_index(self, event):
        text = event.message.text
        return text == "美股指數"

    def on_enter_USA_index(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"美股指數",flex_message.index_USA)
    
    def is_going_to_index_search(self, event):
        global index
        text = event.message.text
        if text == "道瓊工業指數" or text == "標普500指數" or text == "那斯達克指數":
            index = text
            return True
        elif text == "返回查詢":
            return True
        else:
            return False
            
    def on_enter_index_search(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"指數查詢",flex_message.index_search)
    
    def is_going_to_index_chart(self, event):
        global index_chart_range
        text = event.message.text
        if text == "當日價格" or text == "五日價格" or text == "近一個月價格" or text == "近一年價格":
            index_chart_range = text
            return True
        else:
            return False

    def on_enter_index_chart(self, event):
        global index_chart_range, index
        reply_token = event.reply_token
        flex_message.index_chart["body"]["contents"][1]["text"] = index_chart_range
        flex_message.index_chart["body"]["contents"][0]["text"] = index
        other_function.get_index_chart(index, index_chart_range)
        send_flex_message(reply_token,"指數圖表",flex_message.index_chart)
    
    def is_going_to_TW_index(self, event):
        text = event.message.text
        if text.lower() == "台股指數" or text.lower() == "返回查詢":
            return True
        else:
            return False

    def on_enter_TW_index(self, event):
        reply_token = event.reply_token
        send_flex_message(reply_token,"index_TW",flex_message.index_TW)
    
    def is_going_to_TW_now(self, event):
        text = event.message.text
        return text.lower() == "即時資訊"

    def on_enter_TW_now(self, event):
        reply_token = event.reply_token
        other_function.change_TW_now()
        send_flex_message(reply_token,"index_TW_now",flex_message.index_TW_now)

    def is_going_to_TW_history(self, event):
        text = event.message.text
        return text.lower() == "歷史績效"

    def on_enter_TW_history(self, event):
        reply_token = event.reply_token
        other_function.change_TW_history()
        send_flex_message(reply_token,"index_TW_history",flex_message.index_TW_history)
    
    
    
    
    
    
    def is_going_to_search(self, event):
        text = event.message.text
        return text.lower() == "台股查詢"