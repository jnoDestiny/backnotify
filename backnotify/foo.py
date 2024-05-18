from celery import PeriodicTask
from datetime import timedelta
from functools import partial
from win10toast import ToastNotifier
from typing import Callable


class PeriodicNotification(PeriodicTask):
    def __init__(self, notification_handler: Callable, period: timedelta):
        super().__init__()
        self._period: timedelta = period
        self._notification_handler: Callable = notification_handler

    def run(self):
        self._notification_handler()


def main():
    notifier = ToastNotifier()
    notification_routine = partial(notifier.show_toast, "Straighten your back!", "You can't allow yourself to sit crooked", duration=10, threaded=True)
    notification_scheduler = PeriodicNotification(notification_routine, timedelta(seconds=20))


if __name__ == "__main__":
    main()
