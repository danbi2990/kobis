# import sublime
import os
import json


class JsonFile:
    def __init__(self, fpath, encoding='utf-8'):
        self.encoding = encoding
        self.fpath = fpath

    def load(self, default=[]):
        self.fdir = os.path.dirname(self.fpath)
        print(self.fdir)
        if not os.path.isdir(self.fdir):
            os.makedirs(self.fdir)
        if os.path.exists(self.fpath):
            with open(self.fpath, mode='r', encoding=self.encoding) as f:
                # content = f.read()
                try:
                    data = json.load(f)
                except:
                    # sublime.message_dialog('%s is bad!' % self.fpath)
                    raise
                if not data:
                    data = default
        else:
            with open(self.fpath, mode='w', encoding=self.encoding, newline='\n') as f:
                data = default
                f.write(json.dumps(data, indent=2, ensure_ascii=False))
        return data

    def save(self, data, indent=4):
        self.fdir = os.path.dirname(self.fpath)
        if not os.path.isdir(self.fdir):
            os.makedirs(self.fdir)
        with open(self.fpath, mode='w', encoding=self.encoding, newline='\n') as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))

    def remove(self):
        if os.path.exists(self.fpath):
            os.remove(self.fpath)
