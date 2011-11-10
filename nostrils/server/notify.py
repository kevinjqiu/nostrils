from pynotify import Notification

def send_notification(title, body):
    """The public interface for notification.

    A level of indirection is introduced so we
    can allow different implementations for notification,
    e.g., Notify OSD, Growl (gntp), screen, etc.
    """
    Notification(title, body).show()
