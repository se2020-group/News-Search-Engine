from scrapy import cmdline
import time
import multiprocessing
import logging
from local_settings import settings

command = 'scrapy crawl %s' % settings['name']
loop = True
if settings['name'] == 'tencentstaticlink':
    command += ' -a syear=%d -a smonth=%d -a sday=%d -a eyear=%d -a emonth=%d -a eday=%d' % (settings['syear'],
                                                                                             settings['smonth'],
                                                                                             settings['sday'],
                                                                                             settings['eyear'],
                                                                                             settings['emonth'],
                                                                                             settings['eday'])
    loop = False

if settings['name'] == 'tencentdetail':
    delay = 1
elif settings['name'] == 'tencentdynamiclink1':
    delay = 1
elif settings['name'] == 'tencentdynamiclink2':
    delay = 5


class run:
    def task(self):
        cmdline.execute(command.split())

    def main_run(self):
        if loop:
            while True:
                pp = multiprocessing.Process(target=self.task)
                logging.info('pp run ')
                pp.start()
                pp.join()
                time.sleep(delay)
        else:
            self.task()


if __name__ == '__main__':
    obj = run()
    obj.main_run()
