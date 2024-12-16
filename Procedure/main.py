import subprocess


class Procedure:
    def start_mysql(self):
        try:
            subprocess.Popen("docker start test-mysql", shell=True, stdout=subprocess.PIPE)
            print("MySQL Started")
        except Exception as ex:
            print("There is some error while starting the mysql")
            raise ex
    def stop_mysql(self):
        try:
            subprocess.Popen("docker stop test-mysql", shell=True, stdout=subprocess.PIPE)
            print("MySQL Stopped")
        except Exception as ex:
            print("There is some error while stopping the mysql")

    def __init__(self):
        print("Procedure started")
        self.start_mysql()
