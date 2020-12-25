start = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/YDm0JTf.jpg",
    "size": "full",
    "aspectRatio": "20:16",
    "aspectMode": "cover"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "主選單",
        "weight": "bold",
        "size": "xl",
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "投資一定有風險，理財投資有賺有賠，申購前應詳閱公開說明書",
            "wrap": True,
            "align": "center"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "指數查詢",
          "text": "指數查詢"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台股查詢",
          "text": "台股查詢"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回功能選單",
          "text": "返回功能選單"
        }
      }
    ],
    "flex": 0
  }
}

index = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/wphWKKn.jpg",
    "size": "full",
    "aspectRatio": "20:14",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "指數查詢",
        "weight": "bold",
        "size": "xl",
        "wrap": True,
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "每買必跌，每賣必漲",
            "align": "center"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "台股指數",
          "text": "台股指數"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "美股指數",
          "text": "美股指數"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "回主選單",
          "text": "回主選單"
        },
        "color": "#00cf37"
      }
    ],
    "flex": 0
  }
}

index_USA = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/z2OsH0P.png",
    "size": "full",
    "aspectRatio": "20:14",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "美股指數",
        "weight": "bold",
        "size": "xl",
        "wrap": True,
        "align": "center"
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "text",
            "text": "Let's Make America Great Again",
            "align": "center"
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "道瓊工業指數",
          "text": "道瓊工業指數"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "標普500指數",
          "text": "標普500指數"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "那斯達克指數",
          "text": "那斯達克指數"
        }
      }
    ],
    "flex": 0
  }
}

index_search = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "價格查詢",
        "weight": "bold",
        "size": "xl",
        "wrap": True,
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "當日價格",
          "text": "當日價格"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "五日價格",
          "text": "五日價格"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "近一個月價格",
          "text": "近一個月價格"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "近一年價格",
          "text": "近一年價格"
        }
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "回指數選擇",
          "text": "回指數選擇"
        },
        "color": "#00cf37"
      },
    ]
  }
}

index_chart = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "那斯達克指數",
        "weight": "bold",
        "size": "xl",
        "align": "center"
      },
      {
        "type": "text",
        "text": "當日價格",
        "align": "center",
        "margin": "md",
        "size": "lg"
      },
      {
        "type": "image",
        "url": "https://app.quotemedia.com/quotetools/getChart?webmasterId=500&chcon=off&chfrmon=off&chbgch=ffffff&chbg=ffffff&chgrd=cccccc&chbdr=cccccc&chxyc=666666&chln=00578e&chdon=off&chfill=eeeeee&chfill2=0071BB&symbol=DJI&chscale=1d&chton=off&chwid=435&chhig=261&chtype=Mountain&chlowwh=10&chfnts=10&svg=true&lang=en&locale=en",
        "size": "full",
        "offsetTop": "none",
        "offsetBottom": "none",
        "offsetStart": "none",
        "offsetEnd": "none",
        "margin": "none",
        "aspectRatio": "20:15"
      },
      {
        "type": "separator"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回查詢",
          "text": "返回查詢"
        },
        "color": "#00cf37"
      },
      {
        "type": "button",
        "style": "primary",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "回主選單",
          "text": "回主選單"
        },
        "color": "#00cf37"
      }
    ],
    "flex": 0
  }
}

index_TW = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/CFKrUNe.jpg",
    "size": "full",
    "aspectRatio": "20:10",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "台股大盤指數",
        "weight": "bold",
        "size": "xl",
        "align": "center"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "即時資訊",
          "text": "即時資訊"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "歷史績效",
          "text": "歷史績效"
        }
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "回指數選擇",
          "text": "回指數選擇"
        },
        "height": "sm",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}

index_TW_now = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "台股大盤指數",
        "size": "xl"
      },
      {
        "type": "text",
        "text": "即時資訊",
        "margin": "xs"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "成交：",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "100",
            "size": "xl",
            "color": "#111111"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "漲跌：",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "100",
            "size": "xl",
            "color": "#111111"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "幅度：",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "100",
            "size": "xl",
            "color": "#111111"
          }
        ],
        "margin": "xxl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "separator"
      },
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回查詢",
          "text": "返回查詢"
        },
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "回主選單",
          "text": "回主選單"
        },
        "height": "sm",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}

index_TW_history = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "台股大盤指數",
        "size": "xl"
      },
      {
        "type": "text",
        "text": "歷史績效",
        "margin": "xs"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "1月：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "3月：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "6月：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "1年：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "3年：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "text",
            "text": "5年：",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "100",
            "size": "lg",
            "color": "#ff0000"
          }
        ],
        "margin": "xxl"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "返回查詢",
          "text": "返回查詢"
        },
        "style": "primary"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "回主選單",
          "text": "回主選單"
        },
        "height": "sm",
        "style": "primary"
      }
    ],
    "flex": 0
  }
}

begin = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://i.imgur.com/byOhSGS.jpg",
    "size": "full",
    "aspectRatio": "20:15",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    }
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "功能選擇",
        "weight": "bold",
        "size": "xl",
        "align": "center",
        "action": {
          "type": "uri",
          "uri": "https://github.com/KJay221/Linebot"
        }
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "text": "開始使用",
          "label": "開始使用"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "message",
          "label": "fsm圖",
          "text": "fsm圖"
        }
      },
      {
        "type": "separator"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "介紹與說明",
          "text": "介紹與說明"
        }
      }
    ],
    "flex": 0
  }
}