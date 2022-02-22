from celery import Celery, Task
import sys
import traceback
import time

celery = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')
# if without backend, can't get task result


class CustomTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task success!!!!!!!!!!!')
        return super(CustomTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('something wrong!!!')
        return super(CustomTask, self).on_failure(exc, task_id, args, kwargs, einfo)


def custom_on_failure(self, exc, task_id, args, kwargs, einfo):
    print('in custom on failure and sonething wrong!!!')
    error_class = exc.__class__.__name__  # get occur error class
    # detail = exc.args[0]  # 得到詳細的訊息 用exc
    cl, exc, tb = sys.exc_info()  # get whole exception info
    last_callstack = traceback.extract_tb(tb)[-1]  # get last line info of traceback
    exception_filename = last_callstack[0]
    exception_line = last_callstack[1]
    exception_func = last_callstack[2]
    err_msg = "Exception raise in file: {}, line {}, in {}: [{}] {}.".format(exception_filename,
                                                                             exception_line,
                                                                             exception_func,
                                                                             error_class, exc)
    print(f'custom error message: {err_msg}')


@celery.task()
def add(a, b):
    print('start add')
    result = a + b
    print(f'result = {result}')


@celery.task(bind=True)
def add_with_bind(self, a, b):  # use bind=True can get task self info
    print('start add_with_bind')
    print('Executing task id {0.id}, args: {0.args} kwargs: {0.kwargs}'.format(
        self.request))
    result = a + b
    print(f'result = {result}')
    return result


@celery.task(base=CustomTask)
def add_with_custom_task(a, b):
    print('start add_with_my_task')
    result = a + b
    print(f'result = {result}',flush=True)
    return result


@celery.task()
def divide_by_zero():
    return 1/0


@celery.task(base=CustomTask)
def divide_by_zero_with_custom_task():
    return 1/0


@celery.task(base=Task, on_failure=custom_on_failure)
def divide_by_zero_with_custom_on_failure():
    return 1/0
