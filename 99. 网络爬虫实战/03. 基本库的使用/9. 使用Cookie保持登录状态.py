import  requests

header = {
    'Cookie': '_zap=9f7f296b-660e-4ca5-a8d9-a939e564be2f; d_c0="AIACFBPHEwyPTrP9ZdEwO8KoRYikOxBolt0=|1500265684"; q_c1=1c6edd5c2e8f496f88435478b96366ce|1507891329000|1499346935000; _ga=GA1.2.266351145.1500265686; __DAYU_PP=uEaRb2BfmReaRymYmYUF2fb7a8578192; z_c0="2|1:0|10:1526055645|4:z_c0|92:Mi4xYXJzSUFBQUFBQUFBZ0FJVUU4Y1REQ1lBQUFCZ0FsVk4zUkRqV3dDci1OZ1ZjZEFvdlNmMUhvVTFTOUhrSWlzNFpB|f8641ffa3da1bae017b7c11dd4a0fbb09d0c4275c2a67f17c970e4a37fe62c21"; __utma=51854390.266351145.1500265686.1526055911.1526055911.1; __utmz=51854390.1526055911.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19552832/top-answers; __utmv=51854390.100-1|2=registration_date=20130308=1^3=entry_date=20130308=1; q_c1=1c6edd5c2e8f496f88435478b96366ce|1528710318000|1499346935000; _xsrf=8dbac32e-ae58-404b-9325-c9068d189df2; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

r = requests.get('https://www.zhihu.com', headers=header)

print(r.text)