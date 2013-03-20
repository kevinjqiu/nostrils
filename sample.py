from pyinotify import WatchManager
from pyinotify import Notifier
from pyinotify import ALL_EVENTS

wm = WatchManager()

def cb(s):
    print s

def process_event(event, *args, **kwargs):
    print event

wm.add_watch('.', mask=ALL_EVENTS)
notifier = Notifier(wm, default_proc_fun=process_event)
notifier.loop(callback=cb)
