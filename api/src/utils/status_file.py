import os


class Status_job:

    def __init__(self) -> None:
        self.status_file = 'status.txt'


    def create_status(self):
        try:
            with open(self.status_file, 'r') as file:
                file.read()

        except FileNotFoundError:
            with open(self.status_file, 'w') as file:
                file.write(str('0'))

    def set_status(self, status: str):
        self.create_status()

        with open(self.status_file, 'w') as file:
            file.write(str(status))

    def check_status(self):
        self.create_status()
        
        with open(self.status_file, 'r') as file:
            cancelled = file.read()
            
            if cancelled == "1":
                print('Cancelando...')
                return True
            
            else:
                print('Continue!')
                return
