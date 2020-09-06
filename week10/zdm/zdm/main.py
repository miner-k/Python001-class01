from scrapy import cmdline

# cmdline.execute(['scrapy','crawl','qipaoshui'])
# # cmdline.execute(['scrapy','crawl','zdmcomment'])

import schedule
import time

# def scarpy_job():
#     cmdline.execute(['scrapy','crawl','qipaoshui'])

# name = "longsongpong"
# schedule.every().day.at("21:11").do(job) #每天的23:00执行一次任务
#
# while True:
#     schedule.run_pending()
#     time.sleep(20)

 # CREATE TABLE IF NOT EXISTS comment_2020_09_02 (id INT UNSIGNED AUTO_INCREMENT, crate_time  timestamp not null default current_timestamp,product_name VARCHAR(200) NOT NULL,comment_count VARCHAR(10) NOT NULL,product_id VARCHAR(11) NOT NULL,comment_text TEXT ,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;

cmdline.execute(['scrapy','crawl','qipaoshui'])