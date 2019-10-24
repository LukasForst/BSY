#!/usr/bin/python3.6

import http.server
import json
import argparse

PORT_NUMBER = 80
LOGFILE = "log.json"


class MyHandler(http.server.BaseHTTPRequestHandler):
    def _GET(self):
        f = open("exploit", "rb")
        self.send_response(200)
        self.send_header('Content-type', "Application/octet-stream")
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    # Handler for the GET requests
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            dict_msg = eval(post_data.decode("utf-8"))
            dict_msg["ip"] = self.client_address[0]

            with open(LOGFILE, "a", encoding="utf-8") as file:
               file.write(json.dumps(dict_msg))
        except Exception as e:
            print("Error parsing incoming json data: ")
            print(e)

        # Doesn't do anything with posted data
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("OK".encode())
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, default=80,
                        help="port on which to listen")
    parser.add_argument('-l', '--log-path', dest='log_path', type=str,
                        default="log.json",
                        help="path to log file where json log will be produced")
    args = parser.parse_args()

    PORT_NUMBER = args.port
    LOGFILE = args.log_path

    try:
        server = http.server.HTTPServer(('', PORT_NUMBER), MyHandler)
        print('Started httpserver on port ', PORT_NUMBER)
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()


