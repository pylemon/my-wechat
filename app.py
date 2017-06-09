#!/usr/bin/env python
# coding=utf-8
import logging

from tornado import web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import options, define
from tornado.options import parse_command_line
from tornado.options import parse_config_file

import config

config.init()


class Application(web.Application):
    def __init__(self):
        from handlers import handlers
        settings = dict(
            debug=options.debug,
            autoescape=None
        )
        super(Application, self).__init__(handlers, **settings)


def main():
    if options.debug:
        define('settings', '%s/wechat.conf' % config.PROJDIR)
    else:
        define('settings', '')
    parse_command_line()
    debug = options.debug

    if options.settings:
        parse_config_file(options.settings)
    if not debug:
        options.debug = False

    if options.debug:
        logging.info('Starting server at port %s in debug mode' % options.port)
    else:
        logging.info('Starting server at port %s' % options.port)

    server = HTTPServer(Application(), xheaders=True)
    server.listen(int(options.port))
    IOLoop.instance().start()


if __name__ == '__main__':
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting application")
