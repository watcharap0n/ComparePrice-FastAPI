from linebot.models import FlexSendMessage


def compare_price_flex(docno, docdate, duedate, remark, endpoint):
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
                                "text": f"{docdate}",
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
                        "text": f"มีการขอราคาจาก บริษัท คอนเจริญ จำกัด",
                        "size": "sm",
                        "color": "#666666",
                        "wrap": True,
                        "contents": []
                    },
                    {
                        "type": "text",
                        "text": f"อ้างอิงเอกสารเลขที่: {docno}",
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
                                "text": f"เสนอราคาภายในวันที่: {duedate}",
                                "size": "sm",
                                "color": "#666666",
                                "wrap": True,
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": f"Remark: {remark}",
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
                                    "uri": f"{endpoint}"
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
