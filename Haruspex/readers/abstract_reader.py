class AbstractReader:
    def get_new_user(self):
        raise NotImplemented()

    def get_next_snapshot(self):
        raise NotImplemented()
