from urllib.robotparser import RobotFileParser
import ssl

# 解决 SSL 报错
ssl._create_default_https_context = ssl._create_unverified_context

rp = RobotFileParser()

rp.set_url('http://www.rxshc.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.rxshc.com/'))
print(rp.can_fetch('*', "http://www.rxshc.com/wp-admin/"))