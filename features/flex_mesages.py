from linebot.models import FlexSendMessage


def compare_price_flex():
    flex_msg = FlexSendMessage(
        alt_text='Compare Price!',
        contents={
            "type": "bubble",
            "direction": "ltr",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "text",
                                "text": "15-7-2021",
                                "size": "sm",
                                "color": "#666666",
                                "align": "end",
                                "wrap": True,
                                "contents": []
                            }
                        ]
                    },
                    {
                        "type": "text",
                        "text": "เรียน ร้านค้าวัสดุดี",
                        "weight": "bold",
                        "size": "md",
                        "margin": "xs",
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": "มีการขอราคาจาก บริษัท คอนเจริญ จำกัด ท่านสามารถเสนอราคาได้ที่เมนูด้านล่าง",
                        "size": "sm",
                        "color": "#666666",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "margin": "lg",
                        "contents": [
                            {
                                "type": "text",
                                "text": "เงื่อนไข :",
                                "size": "sm",
                                "color": "#AAAAAA",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "1. เสนอราคาภายในวันที่ 20/02/2021",
                                "size": "sm",
                                "color": "#666666",
                                "wrap": True,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "2. ส่งสินค้าภายใน 5 วัน",
                                "size": "sm",
                                "color": "#666666",
                                "margin": "xs",
                                "contents": []
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "เสนอราคา",
                                    "uri": "https://linecorp.com"
                                },
                                "height": "sm",
                                "style": "secondary"
                            }
                        ]
                    }
                ]
            }
        }
    )
    return flex_msg
